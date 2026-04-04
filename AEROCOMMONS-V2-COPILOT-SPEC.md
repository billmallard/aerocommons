# AeroCommons v2 — Copilot Implementation Spec (Revised)

## Context for the AI assistant reading this

You are helping implement a redesigned version of **AeroCommons**
(`github.com/billmallard/aerocommons`), a Hugo static site deployed
on Cloudflare Pages. The site auto-deploys on every push to the main branch.

**The core problem:** The current homepage is 100% MAOS aircraft content.
AeroCommons is becoming a multi-project open-source GA hub. MAOS needs to
move to its own project page at `/projects/maos/`, and the homepage needs to
become a hub landing page.

**Read this entire document before touching any files.**
Implementation order matters — doing phases out of order will break the site.

---

## Branding — do not change these

Match the existing site exactly. Do not introduce new fonts, colors, or
spacing conventions.

```css
--orange:       #E8611A;
--orange-light: #F27733;
--navy:         #0E1B2E;
--navy-mid:     #162440;
--slate:        #2E4266;
--text-primary: #0E1B2E;
--text-muted:   #4A5D7A;
--surface:      #F5F7FA;
```

**Typography:**
- Headlines / labels: `'Barlow Condensed'`, weights 700–800, uppercase
- Body: `'Barlow'`, weights 400–500
- Both loaded via Google Fonts in existing `<head>` — do not re-add them

**Do not** introduce Inter, Roboto, system-ui, or any other font.
**Do not** change the nav logo mark, nav link hover styles, or footer layout.

---

## Confirm project structure before starting

Run these commands and review the output before editing any file:

```bash
# Confirm Hugo config filename
ls *.toml *.yaml 2>/dev/null || ls config/

# Confirm actual layout files
find layouts/ -type f -name "*.html" | sort

# Confirm content structure
find content/ -type f | sort

# Confirm where CSS lives
find . -name "*.css" -not -path "*/node_modules/*" | sort
find assets/ -name "*.scss" 2>/dev/null | sort

# Confirm Hugo version
hugo version
```

Answer these questions before proceeding:
- [ ] Config file name and location?
- [ ] Where is the homepage template? (`layouts/index.html` or `layouts/_default/baseof.html`?)
- [ ] Where is CSS? (`static/css/`, `assets/css/`, or inside a theme folder?)
- [ ] Is there an existing `layouts/partials/nav.html` and `layouts/partials/footer.html`?
- [ ] Are there any existing taxonomy definitions in the config?

---

## Overview of all changes

| Phase | What | Result |
|-------|------|--------|
| 0 | Create MAOS project page | All current MAOS content lives at `/projects/maos/` |
| 1 | Data layer + taxonomy | `projects.yaml`, updated front matter, config taxonomy |
| 2 | New hub homepage | 9-section hub landing page replaces MAOS homepage |
| 3 | Nav update | Hub-level nav replaces MAOS-specific nav |
| 4 | Articles update | Project badges, filter tabs on listing page |
| 5 | New static pages | `/submit/`, `/about/` |
| 6 | Footer update | Add Projects and Organization columns |

---

## Phase 0 — Migrate MAOS content to its own project page

**This must happen before anything else.** The current homepage template
contains all MAOS content. We need to move it to a new project page layout
and content file before the homepage can become the hub landing page.

### 0A. Create the MAOS project content file

Create `/content/projects/maos/_index.md`:

```markdown
---
title: "MAOS — Mobile Aviation Operating System"
description: "A 4-seat series-hybrid experimental aircraft engineered for the EAA homebuilder community."
layout: "project"
project_id: "maos"
---
```

This file is intentionally minimal — the content renders from the layout template,
exactly as the current homepage does.

### 0B. Create the project page layout template

Create `/layouts/projects/list.html` (Hugo uses `list.html` for `_index.md` pages):

This template should contain **all the MAOS-specific sections** currently in
`layouts/index.html`. Specifically, copy these sections verbatim from
`layouts/index.html` into the new template:

1. The MAOS hero section (headline: "The aircraft you **build yourself.**")
2. The three-pillar intro section (Inherently Safe / One Builder / Open from Day One)
3. **The Platform** section (Pod-and-Boom Fuselage, Wing, ECS)
4. **Target Specifications** table
5. **Propulsion Architecture** section (Dual ICE Generators, HV Bus, Rim-Drive Motors, Custom FADEC)
6. **Ground Operations** section (Road Transport, Crane System, Wing Attach, Preflight, Recovery)
7. **AI Development Methodology** section (Agent roles, Decision Gates, Living Documentation, etc.)
8. **Manufacturing Philosophy** section (Cut / Form / Print / Source)
9. **The Commons** section (repo contents list)
10. **Get Involved** section (contact email, GitHub star link)

Wrap the template with base layout inheritance:

```html
{{ define "main" }}

  {{/* MAOS project nav — internal anchor links for this page only */}}
  <div class="project-subnav">
    <div class="project-subnav-inner">
      <a href="/projects/maos/">
        <span class="project-subnav-badge">MAOS</span>
      </a>
      <a href="#aircraft">The Aircraft</a>
      <a href="#ground">Ground Ops</a>
      <a href="#ai">AI Development</a>
      <a href="#manufacturing">Manufacturing</a>
    </div>
  </div>

  {{/* === PASTE ALL MAOS SECTIONS HERE === */}}
  {{/* Copy sections verbatim from current layouts/index.html */}}
  {{/* Replace {{ define "main" }} wrapper if present */}}

{{ end }}
```

CSS for the project subnav (add to existing stylesheet):

```css
.project-subnav {
  background: var(--navy-mid);
  border-bottom: 1px solid rgba(255,255,255,0.08);
  padding: 0 2rem;
  position: sticky; top: 60px; z-index: 90;
}
.project-subnav-inner {
  max-width: 1100px; margin: 0 auto;
  display: flex; align-items: center; gap: 2rem;
  height: 44px;
}
.project-subnav a {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px; font-weight: 600;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: rgba(255,255,255,0.55);
  text-decoration: none;
  transition: color 0.15s;
}
.project-subnav a:hover { color: rgba(255,255,255,0.9); }
.project-subnav-badge {
  background: var(--orange);
  color: #ffffff;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 12px; font-weight: 700;
  letter-spacing: 0.10em; text-transform: uppercase;
  padding: 3px 10px; border-radius: 3px;
}
```

### 0C. Update the main nav for the MAOS project page

The top-level nav currently shows MAOS-specific anchor links
(`The Aircraft`, `Ground Ops`, `AI Development`, `Manufacturing`).
On the MAOS project page, these still make sense as a secondary subnav
(which we just added above). In the main nav, they should only be visible
when the visitor is on the MAOS project page — or removed entirely from
the global nav and replaced with hub-level links (handled in Phase 3).

For now, the simplest safe approach: keep the existing nav untouched.
Phase 3 will replace it once the new hub homepage is confirmed working.

### 0D. Verify MAOS page before proceeding

Run `hugo server -D` and confirm:
- `http://localhost:1313/projects/maos/` renders all MAOS content correctly
- All internal anchor links (`#aircraft`, `#ground`, `#ai`, `#manufacturing`) work
- No content is missing compared to the current live homepage

**Do not proceed to Phase 1 until this page looks correct.**

---

## Phase 1 — Data layer and taxonomy

### 1A. Create `/data/projects.yaml`

```yaml
projects:
  - id: maos
    title: "MAOS"
    subtitle: "Mobile Aviation Operating System"
    status: "active"
    status_label: "Active Development"
    description: >
      A 4-seat experimental aircraft with series hybrid propulsion,
      AI-assisted design board, and full open-source documentation.
      155 KTAS cruise, 1,000 nm range, IFR capable.
    tags: ["Hybrid Electric", "4-Seat", "IFR", "AI Design", "FAA EAB"]
    repo: "https://github.com/billmallard/aerocommons"
    project_url: "/projects/maos/"
    phase: "Phase 1 — Preliminary Design"
    location: "Fort Worth, TX"
    stack: "OpenVSP · AVL · OpenFOAM · ESP32"
    weight: 1

  - id: beech215
    title: "Beech 215"
    subtitle: "Open Prop Controller"
    status: "new"
    status_label: "New Project"
    description: >
      An open-source replacement for the Airborne Electronics 350A electric
      propeller controller on early-model Beechcraft Bonanza aircraft.
      Built on ESP32. No vendor dependency.
    tags: ["ESP32", "Bonanza", "Avionics", "Prop Control"]
    repo: "https://github.com/billmallard/Beech215PropController"
    project_url: "/projects/beech215/"
    phase: "Design Phase"
    location: "Fort Worth, TX"
    stack: "ESP32 · Arduino / C++ · KiCad"
    weight: 2
```

### 1B. Update article front matter

All existing `.md` files in `/content/articles/` need two new fields.
Add them to every article's front matter block — do not touch body content:

```yaml
project: "maos"        # "maos" | "beech215" | "community"
article_type: "design" # "design" | "build-log" | "analysis" | "methodology" | "announcement"
```

Tag all current articles `project: "maos"` unless the article is
cross-project, in which case use `project: "community"`.

### 1C. Update hugo.toml / config.toml

Add to the taxonomies block. If `[taxonomies]` already exists, add
the two new lines inside it — do not create a duplicate `[taxonomies]` header.

```toml
[taxonomies]
  tag = "tags"
  project = "project"
  article_type = "article_type"

[params]
  show_announcement = true
```

---

## Phase 2 — New hub homepage

The current `layouts/index.html` will be **replaced** with the new hub
homepage. Before replacing it, confirm the MAOS project page from Phase 0
is rendering all content correctly — that content is no longer needed here.

The new `layouts/index.html` should contain these sections in order:

### Section 1 — Announcement banner

```html
{{ if .Site.Params.show_announcement }}
<div class="announcement-banner">
  <p>
    AeroCommons is evolving into an open-source GA hub. MAOS is now at
    <a href="/projects/maos/">/projects/maos/</a> —
    <a href="/articles/aerocommons-v2-announcement/">read the announcement →</a>
  </p>
</div>
{{ end }}
```

```css
.announcement-banner {
  background: rgba(232,97,26,0.10);
  border-bottom: 1px solid rgba(232,97,26,0.22);
  padding: 10px 2rem;
  text-align: center;
}
.announcement-banner p {
  font-size: 13px; font-weight: 500; color: #B84A0E;
}
.announcement-banner a { color: var(--orange); text-decoration: underline; }
```

### Section 2 — Hero (hub-level)

Replace the MAOS-specific hero headline and stats. Keep all existing hero
CSS classes, background treatment, and visual structure — only change the text content.

**Eyebrow text:** `Open Source General Aviation`

**H1:** `Where GA Builders Build Together`

**Subhead:**
> AeroCommons is a non-profit community of experimental aircraft builders,
> engineers, and pilots advancing open-source general aviation —
> one published design at a time.

**Primary CTA:** `Explore Projects` → `/#projects`

**Secondary CTA:** `View on GitHub` → `https://github.com/billmallard/aerocommons`

**Hero stat cards** — replace the 6 MAOS-specific stats with these 4:

| Number | Label |
|--------|-------|
| 2 | Active Projects |
| 100% | Open Source |
| FAA | EAB Compliant |
| 0 | Vendor Lock-In |

### Section 3 — Mission band

```html
<div class="mission-band">
  <div class="mission-band-inner">
    <p>
      <strong>Our mission:</strong> Make aviation engineering knowledge freely
      accessible. Every design file, every simulation, every lesson learned —
      published and open for the community to build on.
    </p>
  </div>
</div>
```

```css
.mission-band { background: var(--orange); padding: 22px 2rem; }
.mission-band-inner { max-width: 1100px; margin: 0 auto; }
.mission-band p {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 20px; font-weight: 600;
  color: #ffffff; line-height: 1.3;
}
```

### Section 4 — Projects grid

Data-driven from `/data/projects.yaml`. This section **replaces** all the
MAOS platform/propulsion/etc. content that used to appear here.

```html
<section class="projects-section" id="projects">
  <div class="section-inner">
    <div class="section-label">Open Projects</div>
    <h2 class="section-title">What We're Building</h2>
    <p class="section-subtitle">
      Each project lives in its own GitHub repository with full documentation,
      design files, and build logs — free for the EAB community to use,
      fork, and improve.
    </p>

    <div class="projects-grid">
      {{ range sort .Site.Data.projects.projects "weight" }}
      <div class="project-card">
        <div class="project-card-header">
          <span class="project-status status-{{ .status }}">{{ .status_label }}</span>
        </div>
        <div class="project-body">
          <div class="project-title">{{ .title }}</div>
          <div class="project-subtitle">{{ .subtitle }}</div>
          <p class="project-desc">{{ .description }}</p>
          <div class="project-tags">
            {{ range .tags }}
            <span class="tag">{{ . }}</span>
            {{ end }}
          </div>
        </div>
        <div class="project-footer">
          <span class="project-meta">{{ .phase }}</span>
          <div style="display:flex; gap: 12px;">
            <a href="{{ .project_url }}" class="project-link">Details →</a>
            <a href="{{ .repo }}" target="_blank" class="project-link">GitHub ↗</a>
          </div>
        </div>
      </div>
      {{ end }}

      <a href="/submit/" class="project-card-submit">
        <div class="submit-title">Submit Your Project</div>
        <p class="submit-desc">
          Have an open-source GA project? Stand-alone GitHub repo required.
        </p>
      </a>
    </div>
  </div>
</section>
```

CSS for project cards:

```css
.projects-section { background: var(--surface); padding: 72px 2rem; }
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}
.project-card {
  background: #ffffff;
  border: 1px solid rgba(14,27,46,0.10);
  border-radius: 8px;
  display: flex; flex-direction: column;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.project-card:hover {
  border-color: var(--orange);
  box-shadow: 0 4px 24px rgba(232,97,26,0.10);
}
.project-card-header { padding: 20px 24px 0; display: flex; justify-content: flex-end; }
.project-body { padding: 12px 24px 20px; flex: 1; }
.project-footer {
  padding: 14px 24px;
  border-top: 1px solid rgba(14,27,46,0.08);
  display: flex; align-items: center; justify-content: space-between;
}
.project-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 22px; font-weight: 800;
  text-transform: uppercase; color: var(--navy); margin-bottom: 4px;
}
.project-subtitle {
  font-size: 12px; font-weight: 600;
  letter-spacing: 0.06em; text-transform: uppercase;
  color: #7A8FA8; margin-bottom: 10px;
}
.project-desc { font-size: 14px; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px; }
.project-tags { display: flex; flex-wrap: wrap; gap: 6px; }
.tag {
  background: rgba(232,97,26,0.08); color: #B84A0E;
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.06em; text-transform: uppercase;
  padding: 3px 9px; border-radius: 3px;
}
.project-status {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  padding: 4px 10px; border-radius: 3px;
}
.status-active { background: rgba(22,120,60,0.10); color: #165a2a; }
.status-new    { background: rgba(232,97,26,0.10); color: var(--orange); }
.project-link {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--orange); text-decoration: none;
}
.project-meta { font-size: 12px; color: #7A8FA8; }
.project-card-submit {
  border: 2px dashed rgba(14,27,46,0.18);
  background: transparent;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 48px 24px;
  min-height: 200px; border-radius: 8px;
  text-decoration: none;
  transition: border-color 0.2s, background 0.2s;
}
.project-card-submit:hover {
  border-color: var(--orange);
  background: rgba(232,97,26,0.04);
}
.submit-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 20px; font-weight: 800;
  text-transform: uppercase; color: var(--navy); margin-bottom: 8px;
}
.submit-desc { font-size: 13px; color: var(--text-muted); line-height: 1.5; }
```

### Section 5 — Articles (homepage preview)

Show the 3 most recent articles with project badges.
This section can reuse whatever partial currently renders articles on the
homepage — extend it to show the project badge, don't replace it.

In the article card partial, add before the article title:

```html
{{ with .Params.project }}
<span class="article-project-badge badge-{{ . }}">{{ . | upper }}</span>
{{ end }}
```

```css
.article-project-badge {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  padding: 3px 10px; border-radius: 3px;
  display: inline-block; margin-bottom: 8px;
}
.badge-maos     { background: var(--orange); color: #ffffff; }
.badge-beech215 { background: #165a2a; color: #ffffff; }
.badge-community { background: var(--navy); color: #ffffff; }
```

Add a "View all articles" link below the articles preview:

```html
<div style="margin-top: 2rem; text-align: center;">
  <a href="/articles/" class="btn-outline-navy">View All Articles</a>
</div>
```

### Section 6 — Get Involved

This replaces the existing "This aircraft gets built by a community" contact
section. Keep the same visual weight and dark-navy background treatment.

```html
<section class="involved-section" id="involved">
  <div class="section-inner">
    <div class="section-label" style="color: var(--orange);">Community</div>
    <h2 class="section-title" style="color: #ffffff;">Get Involved</h2>
    <p class="section-subtitle" style="color: rgba(255,255,255,0.65);">
      Open projects need real hands — builders, analysts, domain experts,
      and engineers who want to work on something real.
    </p>
    <div class="involved-grid">

      <div class="involved-card">
        <div class="involved-title">Build a Prototype</div>
        <p class="involved-desc">MAOS subsystems are designed to be built
        and tested independently — ECS controllers, FBW servos, motor
        thermal rigs. Pick a system, pick a city.</p>
        <a href="https://github.com/billmallard/aerocommons/issues"
           target="_blank" class="involved-link">See open tasks →</a>
      </div>

      <div class="involved-card">
        <div class="involved-title">Run Analysis</div>
        <p class="involved-desc">OpenFOAM, AVL, VSPAero — all
        containerized and documented. Help close open decision gates
        with real simulation data.</p>
        <a href="https://github.com/billmallard/aerocommons"
           target="_blank" class="involved-link">View decision gates →</a>
      </div>

      <div class="involved-card">
        <div class="involved-title">Expert Review</div>
        <p class="involved-desc">Retired military, airline, or
        experimental aviation background? Board meeting notes and design
        proposals are public and open for expert critique.</p>
        <a href="/articles/" class="involved-link">Read the board notes →</a>
      </div>

      <div class="involved-card">
        <div class="involved-title">Submit Your Project</div>
        <p class="involved-desc">Have an open-source GA project that
        deserves a home? AeroCommons is becoming the hub for EAB
        open-source work.</p>
        <a href="mailto:contact@aerocommons.org"
           class="involved-link">contact@aerocommons.org →</a>
      </div>

    </div>
  </div>
</section>
```

```css
.involved-section { background: var(--navy); color: #ffffff; padding: 72px 2rem; }
.involved-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
  gap: 1rem;
}
.involved-card {
  background: rgba(255,255,255,0.055);
  border: 1px solid rgba(255,255,255,0.10);
  border-radius: 8px; padding: 26px 22px;
  transition: background 0.2s, border-color 0.2s;
}
.involved-card:hover {
  background: rgba(232,97,26,0.12);
  border-color: rgba(232,97,26,0.40);
}
.involved-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 18px; font-weight: 700;
  text-transform: uppercase; color: #ffffff; margin-bottom: 8px;
}
.involved-desc { font-size: 13px; line-height: 1.6; color: rgba(255,255,255,0.55); }
.involved-link {
  display: inline-block; margin-top: 14px;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--orange); text-decoration: none;
}
```

### Section 7 — Non-profit / Support

```html
<section class="nonprofit-section" id="support">
  <div class="section-inner nonprofit-inner">

    <div class="nonprofit-text">
      <div class="section-label">Non-Profit Formation</div>
      <h2 class="section-title">This Work Needs a Durable Home</h2>
      <p>AeroCommons is forming as a 501(c)(3) non-profit to ensure
      this work stays open, independent, and community-governed —
      permanently. No corporate interests. No paywalls. No IP lock-in.</p>
      <p>Early supporters help fund hosting, tooling, and the admin
      overhead of formal non-profit status. Everything else stays
      volunteer-driven.</p>
      <a href="mailto:contact@aerocommons.org"
         class="btn-primary" style="margin-top:1.5rem; display:inline-flex;">
        Support the Mission
      </a>
    </div>

    <div class="nonprofit-tiers">
      <div class="tier-card">
        <div class="tier-amount">$5/mo</div>
        <div>
          <div class="tier-title">Contributor</div>
          <div class="tier-desc">Keep the lights on. Listed in contributors.</div>
        </div>
      </div>
      <div class="tier-card tier-featured">
        <div class="tier-amount">$25/mo</div>
        <div>
          <div class="tier-title">Builder Sponsor</div>
          <div class="tier-desc">Prototype task board access. Discord invite.</div>
        </div>
        <span class="tier-badge">Popular</span>
      </div>
      <div class="tier-card">
        <div class="tier-amount">$100/mo</div>
        <div>
          <div class="tier-title">Partner Sponsor</div>
          <div class="tier-desc">Logo placement, early design board access.</div>
        </div>
      </div>
      <div class="tier-card">
        <div class="tier-amount">One-time</div>
        <div>
          <div class="tier-title">Single Donation</div>
          <div class="tier-desc">Any amount. Tax-deductible once 501(c)(3) approved.</div>
        </div>
      </div>
    </div>

  </div>
</section>
```

```css
.nonprofit-section {
  background: var(--surface); padding: 72px 2rem;
  border-top: 1px solid rgba(14,27,46,0.10);
}
.nonprofit-inner {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 4rem; align-items: start;
}
.nonprofit-text p {
  font-size: 16px; color: var(--text-muted);
  line-height: 1.7; margin-bottom: 12px;
}
.nonprofit-tiers { display: flex; flex-direction: column; gap: 12px; }
.tier-card {
  background: #ffffff;
  border: 1px solid rgba(14,27,46,0.10);
  border-radius: 6px; padding: 16px 18px;
  display: flex; align-items: center; gap: 14px;
}
.tier-card.tier-featured {
  border-color: var(--orange);
  background: rgba(232,97,26,0.05);
}
.tier-amount {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 22px; font-weight: 800;
  color: var(--orange); min-width: 80px;
}
.tier-title { font-weight: 700; font-size: 14px; color: var(--navy); margin-bottom: 2px; }
.tier-desc  { font-size: 12px; color: var(--text-muted); }
.tier-badge {
  margin-left: auto;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.10em; text-transform: uppercase;
  background: var(--orange); color: #ffffff;
  padding: 3px 10px; border-radius: 3px;
}
@media (max-width: 768px) {
  .nonprofit-inner { grid-template-columns: 1fr; gap: 2rem; }
}
```

---

## Phase 3 — Update global nav

Replace the MAOS-specific anchor links in the top nav with hub-level links.

**Current nav links (remove):**
- `The Aircraft` → `#aircraft`
- `Ground Ops` → `#ground`
- `AI Development` → `#ai`
- `Manufacturing` → `#manufacturing`

**New nav links (replace with):**
- `Projects` → `/#projects`
- `Articles` → `/articles/` ← keep existing
- `About` → `/about/`
- `GitHub` → `https://github.com/billmallard/aerocommons` ← keep existing
- Add CTA button: `Submit a Project` → `/submit/`

```css
.nav-cta {
  background: var(--orange) !important;
  color: #ffffff !important;
  padding: 7px 18px;
  border-radius: 4px;
  font-weight: 600 !important;
  font-size: 13px !important;
  letter-spacing: 0.04em;
  transition: background 0.15s;
}
.nav-cta:hover { background: var(--orange-light) !important; }
```

---

## Phase 4 — Articles listing page

In `layouts/articles/list.html` (or equivalent), add project filter tabs
above the article grid. Hugo's taxonomy system will generate `/project/maos/`
etc. automatically once the taxonomy is registered (Phase 1C).

```html
<div class="article-filters">
  <a href="/articles/"
     class="filter-btn{{ if not .IsPage }} active{{ end }}">All</a>
  {{ range .Site.Data.projects.projects }}
  <a href="/project/{{ .id }}/" class="filter-btn">{{ .title }}</a>
  {{ end }}
  <a href="/project/community/" class="filter-btn">Community</a>
</div>
```

```css
.article-filters { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 2rem; }
.filter-btn {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px; font-weight: 700;
  letter-spacing: 0.10em; text-transform: uppercase;
  padding: 6px 16px; border-radius: 4px;
  border: 1px solid rgba(14,27,46,0.20);
  color: var(--text-muted); text-decoration: none;
  transition: background 0.15s, color 0.15s, border-color 0.15s;
}
.filter-btn:hover, .filter-btn.active {
  background: var(--orange); color: #ffffff; border-color: var(--orange);
}
```

---

## Phase 5 — New static pages

### `/content/submit.md`

```markdown
---
title: "Submit a Project"
description: "Propose an open-source GA project for AeroCommons."
layout: "simple"
---

## Submit an Open-Source GA Project

AeroCommons hosts open-source general aviation projects. If you have
a project that belongs here, we'd like to hear about it.

**Requirements:**
- Active public GitHub repository
- FAA Experimental Amateur-Built scope, or directly supporting EAB builders
- Documentation published alongside design files
- Willing to maintain the repo and respond to community questions

**To submit:** Email [contact@aerocommons.org](mailto:contact@aerocommons.org)
with your GitHub link and a brief description. We'll respond within two weeks.

*AeroCommons does not take ownership of submitted projects — they remain yours
under your chosen open-source license.*
```

### `/content/about.md`

```markdown
---
title: "About AeroCommons"
description: "Open-source general aviation engineering for the EAB community."
layout: "simple"
---

## About AeroCommons

AeroCommons is a non-profit community advancing open-source general aviation
engineering. We host independent open-source projects, publish technical articles,
and provide a home for builders who want to share their work with the EAB community.

**Status:** Non-profit formation in progress (501(c)(3) pending).
**Founded:** 2024, Fort Worth, Texas.
**Contact:** [contact@aerocommons.org](mailto:contact@aerocommons.org)

### What we believe

Open-source methodology — published design files, decision records, and analysis
outputs — makes better aircraft, not just cheaper ones. Every homebuilder who
publishes their work makes the next builder's job easier.

The FAA Experimental Amateur-Built program is one of the most important innovation
frameworks in all of engineering. We exist to support it.
```

---

## Phase 6 — Footer update

In `layouts/partials/footer.html`, add two columns alongside existing links.
Do not remove or reorder existing footer content — add only.

```html
{{/* Add these two columns to the existing footer link grid */}}
<div class="footer-col">
  <h4>Projects</h4>
  <ul>
    {{ range sort .Site.Data.projects.projects "weight" }}
    <li><a href="{{ .project_url }}">{{ .title }}</a></li>
    {{ end }}
    <li><a href="/submit/">Submit a Project</a></li>
  </ul>
</div>

<div class="footer-col">
  <h4>Organization</h4>
  <ul>
    <li><a href="/about/">About</a></li>
    <li><a href="/#support">Support Us</a></li>
    <li><a href="/submit/">Submit a Project</a></li>
    <li><a href="mailto:contact@aerocommons.org">Contact</a></li>
  </ul>
</div>
```

Update the copyright line:

```html
<p>© {{ now.Year }} AeroCommons ·
   <a href="/about/">Non-Profit (501(c)(3) pending)</a> ·
   Open Source · FAA Experimental Amateur-Built</p>
```

---

## Implementation order — strict sequence

Follow this order. Each phase should be tested locally before the next begins.

```
Phase 0  →  Create /projects/maos/ and verify it renders all current content
Phase 1  →  Data file, article front matter, hugo.toml taxonomy + params
Phase 2  →  Replace layouts/index.html with new hub homepage
Phase 3  →  Update global nav (partials/nav.html)
Phase 4  →  Update articles listing page
Phase 5  →  Create /content/submit.md and /content/about.md
Phase 6  →  Update footer partial
         →  hugo server -D full review
         →  git push → Cloudflare auto-deploy
```

**Between Phase 0 and Phase 2:** the site will have duplicate content
(MAOS content on both `/` and `/projects/maos/`). This is intentional and
temporary. The homepage duplication is resolved when Phase 2 replaces `index.html`.

---

## SEO / redirect note

Once v2 is live, the existing anchor links that external sites may have
bookmarked (`/#aircraft`, `/#ground`, `/#ai`, `/#manufacturing`) will
no longer resolve correctly on the homepage. Add these redirects in
`static/_redirects` (Cloudflare Pages format):

```
/#aircraft      /projects/maos/#aircraft       301
/#ground        /projects/maos/#ground         301
/#ai            /projects/maos/#ai             301
/#manufacturing /projects/maos/#manufacturing  301
```

Note: Hash fragment redirects are client-side only and cannot be handled
by server-side redirect rules. The practical solution is to keep the anchor
IDs present on the homepage temporarily (hidden sections or redirecting
JS), or accept that old bookmarks land on the new homepage. For an
experimental project site this is acceptable — just remove the old nav
links and let old anchors 404 gracefully.

---

## Notes for later phases (out of scope for this implementation)

- **Beech 215 project page** at `/projects/beech215/` — same layout as
  MAOS project page once enough content exists
- **Payment integration** — Open Collective is the fastest path to
  accepting donations before 501(c)(3) is finalized
- **Discord** — link from Get Involved section once server is established
- **GitHub issue template** as a structured project submission intake form