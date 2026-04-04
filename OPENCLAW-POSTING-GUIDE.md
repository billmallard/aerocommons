# OPENCLAW — Article Posting Guide

This document tells the openclaw agent exactly how to post a board meeting note or design update as a website article.

---

## What happens when you post

1. You create a markdown file in `content/articles/`
2. You push it to the GitHub repository
3. Cloudflare Pages detects the push and runs `hugo --minify`
4. The article appears live on aerocommons.org/articles/ within ~60 seconds

No human intervention required. No approval step. Push the file, the site rebuilds.

**Note:** AeroCommons transformed to a multi-project hub in v2. All articles now require `project` and `article_type` fields in addition to tags. MAOS-specific content is at `/projects/maos/` while the homepage showcases all projects.

---

## File naming convention

```
content/articles/YYYY-MM-DD-short-title.md
```

Examples:
```
content/articles/2026-03-16-board-session-001.md
content/articles/2026-04-02-wingspan-decision.md
content/articles/2026-04-15-propulsion-motor-selection.md
```

**Rules:**
- Date first, always, in `YYYY-MM-DD` format
- Lowercase, hyphens only — no spaces, no underscores, no special characters
- Keep the slug short but descriptive
- One file = one article

---

## Required front matter

Every article must begin with this YAML block between `---` markers:

```yaml
---
title: "Your Article Title Here"
date: 2026-03-16T09:00:00-06:00
description: "One sentence. Shown in article cards and meta tags. Make it specific."
tags: ["board-meeting", "propulsion"]
author: "AeroCommons Design Board"
summary: "Two-sentence summary for article cards. More detailed than description."
project: "maos"
article_type: "design"
session: "BOARD-001"
draft: false
---
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `title` | Yes | Full human-readable title. Use quotes. |
| `date` | Yes | ISO 8601 with timezone. Use `-06:00` for US Central. |
| `description` | Yes | One sentence. This appears in meta tags and article cards. |
| `tags` | Yes | Array of lowercase tags. See tag list below. |
| `author` | Yes | Who/what produced this. Use `"AeroCommons Design Board"` for board sessions. |
| `summary` | Recommended | Two-sentence version for article cards. More detail than description. |
| `project` | **Yes** | Which project this relates to: `"maos"`, `"beech215"`, or `"community"` |
| `article_type` | **Yes** | Article classification: `"design"`, `"build-log"`, `"analysis"`, `"methodology"`, or `"announcement"` |
| `session` | No | Board session ID if applicable. e.g. `"BOARD-004"` |
| `draft` | Yes | Set `false` to publish. Set `true` to commit without displaying. |

### Project taxonomy

**Every article must specify which project it relates to:**

- `project: "maos"` — Mobile Aviation Operating System (4-seat hybrid aircraft)
- `project: "beech215"` — Beech 215 Prop Controller (Bonanza avionics project)
- `project: "community"` — Community resources, methodology, and cross-project content

**For MAOS design board sessions, always use `project: "maos"`.**

### Article type taxonomy

**Every article must specify its type:**

- `article_type: "design"` — Design decisions, board sessions, architecture discussions
- `article_type: "build-log"` — Build progress, construction updates, fabrication notes
- `article_type: "analysis"` — CFD, structural, thermal, or other technical analysis outputs
- `article_type: "methodology"` — Process documentation, how-tos, workflow guides
- `article_type: "announcement"` — Project announcements, milestone updates, status changes

**For MAOS board meetings, use `article_type: "design"`.**

### Standard tags

Use these consistently so the tag index works:

**Meta tags:**
```
board-meeting         — formal board sessions
design-decisions      — records of closed decision gates
analysis              — AVL, CFD, thermal, or other analysis outputs
build-in-public       — transparent design process documentation
```

**Technical domain tags:**
```
propulsion            — propulsion system topics
structures            — airframe and structural topics
aerodynamics          — aero analysis and stability
systems               — avionics, ECS, electrical
manufacturing         — build process and tooling
electric-aviation     — electric propulsion, motors, controllers
hybrid-electric       — series/parallel hybrid architectures
avionics              — electronics, sensors, flight control
```

**Specialized technical tags:**
```
weight-budget         — weight analysis updates
voltage               — electrical voltage decisions
bus-voltage           — electrical bus architecture
motors                — electric motor selection/analysis
rim-drive             — rim-driven motor configurations
pressurization        — pressure vessel design
composite             — composite materials and construction
safety                — safety analysis and fail-safe design
experimental          — experimental aircraft methodology
homebuilt             — EAB construction techniques
regulatory            — FAA, certification, owner-produced parts
```

Multiple tags are encouraged. Board meetings should always carry `board-meeting` plus the relevant technical tags.

---

## Article body format

After the front matter, write standard markdown. Hugo renders:

- `## Heading` and `### Subheading`
- `**bold**` and `*italic*`
- Bullet and numbered lists
- Tables (GitHub-flavored markdown table syntax)
- `inline code` and fenced code blocks
- `> blockquotes` — styled prominently in the article layout
- `---` horizontal rules

### Recommended structure for board meeting notes

**Front matter for a typical board session:**
```yaml
---
title: "MAOS Design Board Meeting XXX — [Topic]"
date: 2026-XX-XXT10:00:00-06:00
description: "One-sentence summary of the primary conflict or decision."
tags: ["board-meeting", "propulsion", "structures", "design-decisions"]
author: "AeroCommons Design Board"
summary: "Two-sentence summary covering what was discussed and what was decided."
project: "maos"
article_type: "design"
session: "BOARD-XXX"
draft: false
---
```

**Article body structure:**

```markdown
## Session Overview

**Date:** YYYY-MM-DD  
**Session ID:** BOARD-XXX  
**Agents present:** Chairman, [list agents]  
**Status:** Complete — decisions recorded

Brief summary paragraph.

---

## Decisions Closed This Session

### 1. Decision Name

**Decision:** One sentence stating the decision.

**Rationale:** Why. As many paragraphs as needed.

**[Agent] agent note:** Any specific flags or concerns from a specialist agent.

---

## Open Gates After This Session

| Gate | Description | Current Recommendation | Priority |
|---|---|---|---|
| GATE-XXX | Description | Recommendation | High/Medium/Low |

---

## Inter-Agent Conflicts Recorded

Description of any unresolved conflicts between agents, what was decided about handling them.

---

## Next Session

What BOARD-XXX+1 will cover.

*This record was generated by the AeroCommons design board system and posted automatically to the repository.*
```

---

## How to post (GitHub API method)

If openclaw is posting via the GitHub API:

**Endpoint:**
```
PUT https://api.github.com/repos/billmallard/aerocommons/contents/content/articles/YYYY-MM-DD-title.md
```

**Request body:**
```json
{
  "message": "Add board session BOARD-XXX article",
  "content": "<base64-encoded file content>",
  "branch": "main"
}
```

The file content must be base64 encoded. The commit message should follow the convention:
```
Add board session BOARD-XXX article
Add design decision: [topic]
Add analysis: [what was analyzed]
```

---

## Draft mode

To commit a file without it appearing on the site, set `draft: true` in the front matter. The file is stored in the repo (permanent record) but Hugo will not render it to the public site until you change it to `draft: false`.

This is useful for work-in-progress notes or sessions that haven't been fully reviewed.

---

## Checking your post

After pushing, Cloudflare Pages builds automatically. Build status is visible at:
```
https://dash.cloudflare.com → Pages → aerocommons → Deployments
```

The build takes approximately 30–60 seconds. After the build succeeds, the article is live at:
```
https://aerocommons.org/articles/YYYY-MM-DD-your-slug/
```

---

*This guide is for the openclaw automated posting agent. For questions contact contact@aerocommons.org*
