---
title: "Running OpenClaw on QNAP Container Station — A Practical Guide"
date: 2026-03-24T14:00:00-06:00
description: "Lessons learned deploying OpenClaw's multi-agent gateway on a QNAP NAS using Container Station, Docker Compose, and SMB-mounted volumes."
tags: ["openclaw", "qnap", "docker", "infrastructure", "container-station", "multi-agent"]
author: "AeroCommons"
summary: "A detailed walkthrough of deploying OpenClaw on QNAP Container Station — including volume mounts, gateway binding, device pairing, dashboard access, agent-to-agent communication, and every gotcha we hit along the way."
draft: false
---

If you're trying to run [OpenClaw](https://openclaw.ai) on a QNAP NAS using Container Station, this article covers the real-world problems we encountered and how we solved them. OpenClaw is a multi-agent AI gateway that orchestrates LLM-based agents with persistent sessions, tool use, and channel integrations. Running it on a NAS makes sense — always-on, network-accessible, and colocated with your data. Getting there took some work.

## Why QNAP?

Our use case is a multi-agent design board for an experimental aircraft project. Seven AI agents (a chairman/orchestrator plus six domain specialists) need to run 24/7 with persistent sessions, file-based workspaces, and Discord integration. A QNAP NAS with Container Station checks every box: Docker Compose support, always-on availability, local network access, and plenty of storage for agent workspaces and session transcripts.

## The Docker Compose File

QNAP Container Station supports Docker Compose natively. Here's the structure that works:

```yaml
services:
  openclaw:
    image: cloudlookup/openclaw:latest
    container_name: openclaw-qnap
    restart: unless-stopped
    ports:
      - "18789:18789"
      - "18791:18791"
    volumes:
      - /share/YOUR_POOL/OpenClaw:/root/.openclaw
    environment:
      - OPENCLAW_GATEWAY_BIND=lan
      - OPENCLAW_GATEWAY_TOKEN=your-gateway-token-here
      - ANTHROPIC_API_KEY=your-api-key
```

### Volume Mounts — QNAP Native Paths

This is the first place you'll get stuck. QNAP Container Station runs Docker natively on the NAS — not through WSL2 or a VM. Volume paths must use the QNAP filesystem directly.

Your shared folder path will look like:
```
/share/POOL_NAME/ShareName:/root/.openclaw
```

Find your pool name by SSH'ing into the NAS and running `ls /share/`. Common patterns are `ZFS19_DATA`, `CACHEDEV1_DATA`, or similar depending on your storage pool configuration.

**Do not** use Windows UNC paths (`\\nas-ip\share`), mapped drive letters (`Z:\`), or Docker Desktop path conventions (`/D/path`). None of these work in Container Station — they either create empty Docker volumes or fail silently.

### Port Mapping

OpenClaw uses two ports:
- **18789** — Gateway API and WebSocket (agents, sessions, channels)
- **18791** — Control UI dashboard (browser-based management)

Map both. If you're running Caddy or another reverse proxy for TLS termination, you can map different external ports.

## Gateway Configuration (openclaw.json)

The `openclaw.json` file lives inside your mounted volume at the root of the `.openclaw` directory. Here are the settings that matter for QNAP deployment.

### Bind to LAN

By default, OpenClaw binds to loopback (`127.0.0.1`), which means nothing outside the container can reach it. For a NAS deployment, you need LAN binding:

```json
{
  "gateway": {
    "bind": "lan"
  }
}
```

You can also set this via the environment variable `OPENCLAW_GATEWAY_BIND=lan` in your compose file — either works, but don't set both to different values.

### The `gateway.mode` Trap

Older OpenClaw configs (pre-2026.3.x) included a `gateway.mode` field set to `"local"`. **This field has been removed from the schema.** If your config still contains it, OpenClaw's strict validation will reject it at startup. Worse, in some beta builds, `"mode": "local"` forces the gateway to bind to `127.0.0.1` regardless of your `bind` setting — making the dashboard unreachable from any other machine.

Remove it:
```json
// REMOVE THIS — no longer valid
"gateway": {
  "mode": "local"  // ← delete this line
}
```

If you're unsure whether your config has stale keys, run `openclaw doctor --fix` inside the container:
```bash
docker exec openclaw-qnap openclaw doctor --fix
```

### Allowed Origins for the Control UI

When accessing the dashboard from a browser on a different machine, you'll get WebSocket connection failures unless the Control UI knows which origins to accept:

```json
{
  "gateway": {
    "bind": "lan",
    "controlUi": {
      "allowedOrigins": [
        "http://localhost:18789",
        "http://YOUR_NAS_IP:18789",
        "http://YOUR_NAS_IP:18791"
      ]
    }
  }
}
```

Add every IP:port combination you'll use to access the dashboard. If you're testing from multiple machines, include all of them.

### Don't Use ADVERTISE Unless You Have a TLS Proxy

OpenClaw supports `OPENCLAW_ADVERTISE_WS` and `OPENCLAW_ADVERTISE_HTTP` environment variables that tell the dashboard to connect to a specific WebSocket URL. If you set these to point at a Caddy or nginx TLS endpoint that isn't running, the dashboard will connect briefly then disconnect with a 1006 error in a loop.

**Leave ADVERTISE settings out** unless you have a working TLS reverse proxy. The dashboard will auto-discover the gateway address from the page URL.

## Device Pairing and Authentication

When you first browse to the Control UI (`http://nas-ip:18789/openclaw`), you need two things:

### 1. Gateway Token

The gateway requires a token for API access. Set it in your compose file (`OPENCLAW_GATEWAY_TOKEN`) or in the config file. Then enter it in the Control UI settings — it's not automatic.

### 2. Device Approval

Each new browser that connects creates a device pairing request. You must approve it from inside the container:

```bash
docker exec openclaw-qnap openclaw devices approve
```

Until approved, the dashboard will show a pairing screen. Check pending devices with:
```bash
docker exec openclaw-qnap openclaw devices list
```

## Multi-Agent Configuration

This is where things get interesting. If you're running multiple agents (not just a single default), there are several config sections that must work together.

### Agent List

Define your agents in `agents.list`. Each gets an `id`, `workspace`, and `agentDir`:

```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "default": true,
        "workspace": "/root/.openclaw/workspaces/main",
        "agentDir": "/root/.openclaw/agents/main"
      },
      {
        "id": "specialist-a",
        "workspace": "/root/.openclaw/workspaces/specialist-a",
        "agentDir": "/root/.openclaw/agents/specialist-a",
        "model": {
          "primary": "openrouter/x-ai/grok-4.1-fast",
          "fallbacks": ["openrouter/anthropic/claude-sonnet-4-5"]
        }
      }
    ]
  }
}
```

Create the workspace and agent directories on your NAS share before starting the container, or OpenClaw will create them automatically on first run.

### Enabling Agent-to-Agent Communication

**This is the part that took the longest to figure out.** Having agents defined in the config does not mean they can talk to each other. You need three additional config sections:

#### 1. `tools.agentToAgent` — Enable the capability

```json
{
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["main-agent", "specialist-a", "specialist-b"]
    }
  }
}
```

Without this, `sessions_send` between agents is blocked.

#### 2. `tools.sessions.visibility` — Let agents see each other

```json
{
  "tools": {
    "sessions": {
      "visibility": "all"
    }
  }
}
```

The default is `"tree"` (agents only see their own subagent sessions). Set `"all"` for full cross-agent visibility, or `"agent"` to limit visibility to same-agent sessions.

#### 3. `session.agentToAgent` — Limit ping-pong depth

```json
{
  "session": {
    "agentToAgent": {
      "maxPingPongTurns": 5
    }
  }
}
```

This prevents runaway back-and-forth between agents. The maximum allowed value is 5.

#### 4. Orchestrator subagent permissions

The orchestrating agent needs permission to spawn sessions with other agents:

```json
{
  "agents": {
    "list": [
      {
        "id": "main-agent",
        "default": true,
        "subagents": { "allowAgents": ["*"] }
      }
    ]
  }
}
```

#### What `groupChat` Is NOT

We initially tried adding `"peers"` to each agent's `groupChat` config, thinking that was how you wire agents together. It's not. The `groupChat` field is exclusively for **channel group chat mention patterns** (controlling when an agent responds to @-mentions in Discord/Telegram/WhatsApp groups). It has nothing to do with inter-agent communication. OpenClaw's strict schema validation will reject unknown keys immediately.

### Subagent Timeouts and Concurrency

When your orchestrator spawns sessions with multiple agents in parallel, the default timeout and concurrency limits will bite you:

```json
{
  "agents": {
    "defaults": {
      "subagents": {
        "runTimeoutSeconds": 120,
        "maxConcurrent": 10
      }
    }
  }
}
```

- **`runTimeoutSeconds`**: Default is short. If your agents read workspace files at session startup (which they will — that's what AGENTS.md tells them to do), they can easily exceed the default timeout before producing a response. 120 seconds gives room.
- **`maxConcurrent`**: Default is 1. If you're spawning 6+ agents for a roll call, they queue up and the last ones timeout waiting. Set this to at least your agent count.

### Agent Workspace Instructions Matter

Each agent has an `AGENTS.md` file in its workspace that controls its behavior. If this file tells the agent to read 5-6 files at the start of "Every Session," it will do that on *every incoming message* — including quick `sessions_send` pings from other agents. This burns through timeouts.

Structure your agent instructions to differentiate between session startup (read everything) and direct messages (respond immediately):

```markdown
## Direct Messages
When you receive a direct message from another agent:
- Respond immediately to the question
- Do NOT re-read your entire workspace first
- Keep responses focused

## Session Startup
1. Read SOUL.md
2. Read IDENTITY.md
3. Read shared design state
...
Only run this checklist at session start or reset. Not on every message.
```

## Debugging Tips

### Config Validation

OpenClaw has strict JSON schema validation. Any unknown key causes a startup warning and best-effort config loading. Check validation with:

```bash
docker exec openclaw-qnap openclaw doctor
```

Add `--fix` to auto-repair common issues.

### Hot Reload

OpenClaw watches `openclaw.json` for changes and hot-reloads. You can edit the config file from a mapped drive or SMB share and see changes apply without restarting the container. Watch the container logs for reload confirmations.

### Dashboard WebSocket Disconnects

If the dashboard connects then immediately disconnects (error 1006), check:
1. `allowedOrigins` includes your browser's origin
2. ADVERTISE settings aren't pointing to a dead proxy
3. Gateway is bound to `lan`, not `loopback`

### Agent Not Responding

If specific agents don't respond to `sessions_send`:
1. Check `maxConcurrent` — agents queued beyond the limit will timeout
2. Check `runTimeoutSeconds` — agents reading large workspaces need more time
3. Check the agent's model and fallback — if both the primary model and fallback are unavailable via your API provider, the agent silently fails
4. Check session transcripts — large transcripts slow context loading

## What We'd Do Differently

1. **Start with `openclaw doctor --fix`** after any config change. It catches schema issues immediately.
2. **Set `maxConcurrent` to your agent count from day one.** The default of 1 makes multi-agent setups appear broken.
3. **Don't confuse `groupChat` with agent routing.** The docs are clear once you find the right page, but the field name is misleading if you're coming from a multi-agent mindset.
4. **Use environment variables for secrets**, not inline JSON values. OpenClaw supports `${ENV_VAR}` substitution in config strings.
5. **Test agent communication with a simple roll call** before attempting complex multi-round protocols.

## Current Stack

- **QNAP NAS** with Container Station (Docker Compose)
- **OpenClaw** v2026.3.1-beta.1 (`cloudlookup/openclaw:latest`)
- **7 agents** — orchestrator on Claude Sonnet 4, domain agents on Grok 4.1-fast via OpenRouter
- **Discord** channel integration for human interaction
- **Persistent sessions** with file-based workspaces on NAS shared storage

The system runs 24/7, agents maintain context across conversations, and the orchestrator can convene multi-agent board meetings on demand. Getting here required solving a chain of infrastructure problems — volume paths, network binding, device pairing, origin allowlists, agent-to-agent wiring, timeout tuning — but the result is a self-hosted multi-agent system that doesn't depend on any cloud orchestration layer.
