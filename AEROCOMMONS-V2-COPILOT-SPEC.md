# AeroCommons v2 — Copilot Implementation Spec

## Context for the AI assistant reading this

You are helping implement a redesigned version of **AeroCommons** 
(`github.com/billmallard/aerocommons`), a Hugo static site deployed 
on Cloudflare Pages. The site auto-deploys on every push to the main branch.

The current site is a single-page landing for one project (MAOS aircraft). 
**v2 transforms it into an open-source GA hub** hosting multiple independent 
projects, each with its own GitHub repository. MAOS remains the flagship project. 
A second project (Beech 215 Prop Controller) is being added immediately.

Read this entire document before touching any files. Implementation order matters.

---

## Branding — do not change these

Match the existing site exactly on all of the following. Do not introduce 
new fonts, colors, or spacing conventions.

```css
/* Exact brand tokens — already defined in the existing Hugo theme */
--orange:        #E8611A;
--orange-light:  #F27733;
--navy:          #0E1B2E;
--navy-mid:      #162440;
--slate:         #2E4266;
--text-primary:  #0E1B2E;
--text-muted:    #4A5D7A;
--surface:       #F5F7FA;
```

**Typography:**
- Headlines / labels: `'Barlow Condensed'`, weights 700–800, uppercase
- Body: `'Barlow'`, weights 400–500
- Both fonts are already loaded via Google Fonts in the existing `<head>`

**Do not** introduce Inter, Roboto, system-ui, or any other font family.  
**Do not** change the sticky nav, nav logo mark, or nav link styles.  
**Do not** change the existing footer layout — only extend it.

---

## Repository structure — current state

```
aerocommons/
├── content/
│   ├── _index.md          ← current homepage (MAOS landing)
│   └── articles/
│       └── *.md           ← existing MAOS articles
├── data/                  ← likely empty or minimal
├── layouts/
│   ├── _default/
│   ├── index.html         ← main homepage template
│   └── partials/
│       ├── nav.html
│       └── footer.html
├── static/
├── themes/ (or assets/)
└── hugo.toml (or config.toml)
```

Confirm the actual structure before editing by running:
```bash
find . -type f -name "*.html" | head -40
find . -type f -name "*.toml" -o -name "*.yaml" | head -10
```

---

## What we are building — v2 scope

### New site sections (in homepage order)

1. **Announcement banner** — thin top bar: "AeroCommons is evolving…"
2. **Nav** — add "Projects" link; keep all existing links; add "Submit a Project" CTA button
3. **Hero** — replace MAOS-specific hero with hub-level mission statement. Keep visual style.
4. **Mission band** — single-line orange band: the open-source GA mission in one sentence
5. **Projects section** — card grid of all projects + a "Submit your project" dashed card
6. **Articles section** — existing articles, now tagged by project, shown in editorial grid
7. **Get Involved section** — four entry points (Build, Analyze, Expert Review, Submit Project)
8. **Non-profit / Support section** — honest pre-501(c)(3) framing + support tiers
9. **Footer** — extend with project links column; keep existing structure

### What stays exactly the same

- All existing MAOS content sections (Aircraft, Propulsion, Ground Ops, AI Dev, Manufacturing, The Commons) remain on the homepage **below** the new sections, or are migrated to a `/projects/maos/` page (see Phase 2 below).
- The `/articles/` listing page — extend taxonomy only, don't restyle.
- All existing article `.md` files — add front matter fields only, don't touch body content.

---

## Phase 1 — Data layer and taxonomy (do this first)

### 1A. Create the projects data file

Create `/data/projects.yaml`:

```yaml
projects:
  - id: maos
    title: "MAOS"
    subtitle: "Mobile Aviation Operating System"
    status: "active"           # active | new | paused | complete
    status_label: "Active Development"
    description: >
      A 4-seat experimental aircraft with series hybrid propulsion, 
      AI-assisted design board, and full open-source documentation. 
      155 KTAS cruise, 1,000 nm range, IFR capable.
    tags: ["Hybrid Electric", "4-Seat", "IFR", "AI Design", "FAA EAB"]
    repo: "https://github.com/billmallard/aerocommons"
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
    tags: ["ESP32", "Bonanza", "Avionics", "Prop Control", "Arduino"]
    repo: "https://github.com/billmallard/Beech215PropController"
    phase: "Design Phase"
    location: "Fort Worth, TX"
    stack: "ESP32 · Arduino / C++ · KiCad"
    weight: 2
```

### 1B. Update article front matter taxonomy

All existing article `.md` files in `/content/articles/` need two new front matter fields:

```yaml
---
title: "Your existing title"
date: 2025-01-15          # existing
draft: false              # existing
# ADD THESE TWO:
project: "maos"           # slug matching projects.yaml id — "maos" | "beech215" | "community"
article_type: "design"    # design | build-log | analysis | methodology | announcement
---
```

Tag all current articles `project: "maos"` unless the content is cross-project, 
in which case use `project: "community"`.

### 1C. Update hugo.toml / config.toml

Add the new taxonomy:

```toml
[taxonomies]
  tag = "tags"
  project = "project"
  article_type = "article_type"
```

If taxonomies already exist in the config, add `project` and `article_type` to 
the existing block — don't duplicate the `[taxonomies]` header.

---

## Phase 2 — Homepage template changes

### 2A. Top announcement banner

Add above the `<nav>` in `layouts/partials/nav.html` or directly in `layouts/index.html`:

```html
{{ if .Site.Params.show_announcement }}
<div class="announcement-banner">
  <p>
    AeroCommons is evolving into an open-source GA hub. 
    <a href="/articles/aerocommons-v2-announcement/">Read the announcement →</a>
  </p>
</div>
{{ end }}
```

Add to `hugo.toml`:
```toml
[params]
  show_announcement = true
```

CSS for the banner (add to existing stylesheet):
```css
.announcement-banner {
  background: rgba(232, 97, 26, 0.10);
  border-bottom: 1px solid rgba(232, 97, 26, 0.22);
  padding: 10px 2rem;
  text-align: center;
}
.announcement-banner p {
  font-size: 13px;
  font-weight: 500;
  color: #B84A0E;
}
.announcement-banner a {
  color: var(--orange);
  text-decoration: underline;
}
```

### 2B. Nav — add Projects link and CTA

In `layouts/partials/nav.html`, add `Projects` to the nav links list 
and add a CTA button at the end:

```html
<li><a href="/#projects">Projects</a></li>
<!-- existing links stay -->
<li><a href="/submit/" class="nav-cta">Submit a Project</a></li>
```

CSS for nav CTA:
```css
.nav-cta {
  background: var(--orange) !important;
  color: var(--white) !important;
  padding: 7px 18px;
  border-radius: 4px;
  font-weight: 600 !important;
  font-size: 13px !important;
  letter-spacing: 0.04em;
  transition: background 0.15s;
}
.nav-cta:hover { background: var(--orange-light) !important; }
```

### 2C. Replace / extend the hero section

The existing hero is MAOS-specific. Replace its headline and subhead only — 
keep all existing CSS classes and visual structure:

- **Eyebrow:** `Open Source General Aviation`
- **H1:** `Where GA Builders Build Together`
- **Subhead:** `AeroCommons is a non-profit community of experimental aircraft 
  builders, engineers, and pilots advancing open-source general aviation — 
  one published design at a time.`
- **Primary CTA:** `Explore Projects` → `/#projects`
- **Secondary CTA:** `View on GitHub` → keep existing link

Stat cards below the hero — replace MAOS-specific stats with hub stats:

| Stat | Label |
|------|-------|
| 2 | Active Projects |
| 100% | Open Source |
| FAA | EAB Compliant |
| 0 | Vendor Lock-In |

### 2D. Mission band (new section, insert after hero)

```html
<div class="mission-band">
  <div class="mission-band-inner">
    <p>
      <strong>Our mission:</strong> Make aviation engineering knowledge freely accessible. 
      Every design file, every simulation, every lesson learned — published and 
      open for the community to build on.
    </p>
  </div>
</div>
```

```css
.mission-band {
  background: var(--orange);
  padding: 22px 2rem;
}
.mission-band-inner {
  max-width: 1100px;
  margin: 0 auto;
}
.mission-band p {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 20px;
  font-weight: 600;
  color: #ffffff;
  letter-spacing: 0.01em;
  line-height: 1.3;
}
```

### 2E. Projects section (new, insert after mission band)

This section is data-driven from `/data/projects.yaml`:

```html
<section class="projects-section" id="projects">
  <div class="section-inner">
    <div class="section-label">Open Projects</div>
    <h2 class="section-title">What We're Building</h2>
    <p class="section-subtitle">
      Each project lives in its own GitHub repository with full documentation, 
      design files, and build logs — free for the EAB community to use, fork, and improve.
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
          <div class="project-meta">
            <span>{{ .phase }}</span>
          </div>
          <a href="{{ .repo }}" target="_blank" class="project-link">
            View on GitHub ↗
          </a>
        </div>
      </div>
      {{ end }}

      <!-- Submit card — always last -->
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
  overflow: hidden;
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
  border-top: 1px solid rgba(14,27,46,0.10);
  display: flex; align-items: center; justify-content: space-between;
}
.project-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 22px; font-weight: 800;
  text-transform: uppercase; color: var(--navy);
  margin-bottom: 4px;
}
.project-subtitle {
  font-size: 12px; font-weight: 600;
  letter-spacing: 0.06em; text-transform: uppercase;
  color: #7A8FA8; margin-bottom: 10px;
}
.project-desc { font-size: 14px; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px; }
.project-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 4px; }
.tag {
  background: rgba(232,97,26,0.08);
  color: #B84A0E;
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.06em; text-transform: uppercase;
  padding: 3px 9px; border-radius: 3px;
}
.project-link {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase;
  color: var(--orange); text-decoration: none;
}
.project-meta { font-size: 12px; color: #7A8FA8; }
.project-status {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  padding: 4px 10px; border-radius: 3px;
}
.status-active { background: rgba(22,120,60,0.10); color: #165a2a; }
.status-new    { background: rgba(232,97,26,0.10); color: var(--orange); }
.status-paused { background: rgba(14,27,46,0.07); color: var(--slate); }

.project-card-submit {
  border: 2px dashed rgba(14,27,46,0.20);
  background: transparent;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center;
  padding: 48px 24px;
  min-height: 260px;
  border-radius: 8px;
  transition: border-color 0.2s, background 0.2s;
  text-decoration: none;
}
.project-card-submit:hover {
  border-color: var(--orange);
  background: rgba(232,97,26,0.05);
}
.submit-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 20px; font-weight: 800;
  text-transform: uppercase; color: var(--navy);
  margin-bottom: 8px;
}
.submit-desc { font-size: 13px; color: var(--text-muted); line-height: 1.5; }
```

### 2F. Articles section (update existing or add new partial)

The articles listing on the homepage should now show a project badge on each card. 
In whatever partial renders article cards on the homepage, add:

```html
{{ with .Params.project }}
<span class="article-project-badge badge-{{ . }}">{{ . | upper }}</span>
{{ end }}
```

CSS:
```css
.article-project-badge {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.12em; text-transform: uppercase;
  padding: 3px 10px; border-radius: 3px;
  display: inline-block; margin-bottom: 8px;
}
.badge-maos    { background: var(--orange); color: #ffffff; }
.badge-beech215 { background: #165a2a; color: #ffffff; }
.badge-community { background: var(--navy); color: #ffffff; }
```

### 2G. Get Involved section (new)

Insert before the existing "Get Involved" / contact section, 
or replace it with this expanded version:

```html
<section class="involved-section" id="involved">
  <div class="section-inner">
    <div class="section-label" style="color: var(--orange);">Community</div>
    <h2 class="section-title" style="color: #ffffff;">Get Involved</h2>
    <p class="section-subtitle">
      Open projects need real hands. We're looking for builders, testers, 
      subject-matter experts, and engineers who want to work on something real.
    </p>
    <div class="involved-grid">

      <div class="involved-card">
        <div class="involved-title">Build a Prototype</div>
        <p class="involved-desc">
          MAOS subsystems are designed to be built and tested independently — 
          ECS controllers, FBW servos, motor thermal rigs. Pick a system.
        </p>
        <a href="https://github.com/billmallard/aerocommons/issues" 
           class="involved-link" target="_blank">See open tasks →</a>
      </div>

      <div class="involved-card">
        <div class="involved-title">Run Analysis</div>
        <p class="involved-desc">
          OpenFOAM, AVL, VSPAero — all containerized and documented. 
          Help close open decision gates with real simulation data.
        </p>
        <a href="https://github.com/billmallard/aerocommons" 
           class="involved-link" target="_blank">View decision gates →</a>
      </div>

      <div class="involved-card">
        <div class="involved-title">Expert Review</div>
        <p class="involved-desc">
          Retired military, airline, or experimental aviation background? 
          Board meeting notes and design proposals are public and open for critique.
        </p>
        <a href="/articles/" class="involved-link">Read the board notes →</a>
      </div>

      <div class="involved-card">
        <div class="involved-title">Submit Your Project</div>
        <p class="involved-desc">
          Have an open-source GA project that deserves a home? 
          Stand-alone GitHub repo required. Let's talk.
        </p>
        <a href="mailto:contact@aerocommons.org" class="involved-link">
          contact@aerocommons.org →</a>
      </div>

    </div>
  </div>
</section>
```

CSS:
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
  border-radius: 8px;
  padding: 26px 22px;
  transition: background 0.2s, border-color 0.2s;
}
.involved-card:hover {
  background: rgba(232,97,26,0.12);
  border-color: rgba(232,97,26,0.4);
}
.involved-title {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 18px; font-weight: 700;
  text-transform: uppercase;
  color: #ffffff; margin-bottom: 8px;
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

### 2H. Support / Non-profit section (new)

Insert between the Get Involved section and the existing "The Commons" section, 
or place it just above the footer:

```html
<section class="nonprofit-section" id="support">
  <div class="section-inner nonprofit-inner">
    <div class="nonprofit-text">
      <div class="section-label">Non-Profit Formation</div>
      <h2 class="section-title">This Work Needs a Durable Home</h2>
      <p>
        AeroCommons is forming as a 501(c)(3) non-profit to ensure this work 
        stays open, independent, and community-governed — permanently. 
        No corporate interests. No paywalls. No IP lock-in.
      </p>
      <p>
        Early supporters help fund hosting, tooling, and the overhead of 
        formal non-profit status. Everything else stays volunteer-driven.
      </p>
      <a href="mailto:contact@aerocommons.org" class="btn-primary" 
         style="margin-top: 1.5rem; display: inline-flex;">
        Support the Mission
      </a>
    </div>
    <div class="nonprofit-tiers">
      <!-- Tier cards — static HTML for now, 
           replace with a payment integration (Stripe / Open Collective) later -->
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

CSS:
```css
.nonprofit-section { background: var(--surface); padding: 72px 2rem; border-top: 1px solid rgba(14,27,46,0.10); }
.nonprofit-inner {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 4rem; align-items: start;
}
.nonprofit-text p { font-size: 16px; color: var(--text-muted); line-height: 1.7; margin-bottom: 12px; }
.nonprofit-tiers { display: flex; flex-direction: column; gap: 12px; }
.tier-card {
  background: #ffffff;
  border: 1px solid rgba(14,27,46,0.10);
  border-radius: 6px;
  padding: 16px 18px;
  display: flex; align-items: center; gap: 14px;
}
.tier-card.tier-featured {
  border-color: var(--orange);
  background: rgba(232,97,26,0.05);
}
.tier-amount {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 24px; font-weight: 800;
  color: var(--orange); min-width: 80px;
}
.tier-title { font-weight: 700; font-size: 14px; color: var(--navy); margin-bottom: 2px; }
.tier-desc { font-size: 12px; color: var(--text-muted); }
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

## Phase 3 — New pages

### 3A. `/content/submit.md` — Project submission page

Create this file:

```markdown
---
title: "Submit a Project"
description: "Propose an open-source GA project for AeroCommons."
layout: "simple"
---

## Submit an Open-Source GA Project

AeroCommons hosts open-source general aviation projects. If you have a project 
that belongs here, we'd like to hear about it.

**Requirements:**
- Active public GitHub repository
- FAA Experimental Amateur-Built scope, or directly supporting EAB builders
- Documentation published alongside design files
- Willing to maintain the repo and respond to community questions

**To submit:** Email [contact@aerocommons.org](mailto:contact@aerocommons.org) 
with your GitHub repo link and a brief description of the project. 
We'll review and respond within two weeks.

---

*AeroCommons is a non-profit community. We don't charge for hosting or 
take ownership of submitted projects — they remain yours under your chosen license.*
```

### 3B. `/content/about.md` — Organization page

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

- Aviation engineering knowledge should be freely available to anyone who wants to learn and build.
- The FAA Experimental Amateur-Built program is one of the most important 
  innovation frameworks in all of engineering.
- Open-source methodology — published design files, decision records, 
  and analysis outputs — makes better aircraft, not just cheaper ones.
- Every homebuilder who publishes their work makes the next builder's 
  job easier.

### Projects

See the [Projects](#projects) section on the homepage for current active projects.

### Articles

All technical articles are published at [/articles/](/articles/).
```

---

## Phase 4 — Footer update

In `layouts/partials/footer.html`, add a Projects column alongside existing links:

```html
<div class="footer-col">
  <h4>Projects</h4>
  <ul>
    {{ range sort .Site.Data.projects.projects "weight" }}
    <li><a href="{{ .repo }}" target="_blank">{{ .title }}</a></li>
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

Also update the footer copyright line:
```html
<p>© {{ now.Year }} AeroCommons · 
   <a href="/about/">Non-Profit (501(c)(3) pending)</a> · 
   Open Source · FAA Experimental Amateur-Built</p>
```

---

## Phase 5 — Articles listing page taxonomy filter

On the `/layouts/articles/list.html` page (or equivalent), add project filter tabs:

```html
<div class="article-filters">
  <a href="/articles/" class="filter-btn {{ if not .Params.project }}active{{ end }}">
    All
  </a>
  {{ range .Site.Data.projects.projects }}
  <a href="/project/{{ .id }}/" class="filter-btn">{{ .title }}</a>
  {{ end }}
  <a href="/project/community/" class="filter-btn">Community</a>
</div>
```

This relies on Hugo's taxonomy system. Since we added `project` as a taxonomy 
in Phase 1C, Hugo will automatically generate `/project/maos/`, `/project/beech215/`, 
and `/project/community/` listing pages — no additional template needed unless 
you want custom styling.

CSS for filter tabs:
```css
.article-filters {
  display: flex; gap: 8px; flex-wrap: wrap;
  margin-bottom: 2rem;
}
.filter-btn {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: 13px; font-weight: 700;
  letter-spacing: 0.10em; text-transform: uppercase;
  padding: 6px 16px; border-radius: 4px;
  border: 1px solid rgba(14,27,46,0.20);
  color: var(--text-muted);
  text-decoration: none;
  transition: background 0.15s, color 0.15s, border-color 0.15s;
}
.filter-btn:hover, .filter-btn.active {
  background: var(--orange);
  color: #ffffff;
  border-color: var(--orange);
}
```

---

## Implementation order — follow this sequence

1. `hugo.toml` — add taxonomy entries and `show_announcement` param
2. `/data/projects.yaml` — create the data file
3. Update all article front matter — add `project:` and `article_type:` fields
4. Update nav partial — add Projects link and CTA
5. Homepage template — banner, hero text, mission band, projects section
6. Homepage template — involved section, nonprofit section
7. Footer partial — add columns
8. Articles listing page — add filter tabs
9. Create `/content/submit.md` and `/content/about.md`
10. Test locally with `hugo server -D`, verify all sections render
11. Push to main branch — Cloudflare Pages auto-deploys

---

## Things to confirm before starting

- [ ] What is the Hugo config filename — `hugo.toml`, `config.toml`, or `config/_default/`?
- [ ] Where are CSS/SCSS files — `assets/css/`, `themes/*/css/`, or `static/css/`?
- [ ] Does the existing theme use Hugo Pipes for asset bundling, or are CSS files in `/static/`?
- [ ] Are there existing taxonomy definitions in the config that need to be extended rather than created fresh?
- [ ] What Hugo version is specified in `netlify.toml`, `cloudflare.toml`, or the repo readme?

Run `hugo version` to confirm the installed version before editing templates.

---

## Notes for future phases (not in this scope)

- **Per-project pages** at `/projects/maos/` and `/projects/beech215/` — migrate 
  the existing MAOS homepage sections there, keep a summary card on the main homepage
- **Payment integration** — Open Collective is the fastest path to accepting 
  donations before 501(c)(3) is finalized; no merchant account required
- **Discord integration** — link to community Discord from Get Involved section 
  once the server is set up
- **Project submission workflow** — GitHub issue template as a structured intake form
