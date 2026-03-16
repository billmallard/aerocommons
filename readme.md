# AeroCommons — MAOS Platform

**Mobile Aviation Operating System**
*An open-source experimental aircraft development project*

---

> **This is a design and development project, not a flying aircraft.**
> The MAOS does not yet exist as a physical airplane. What exists right now is a growing body of engineering design work, analysis, and documentation — all of it published here as it is produced. If you found this page, you are watching the project from the beginning.

---

## What Is This?

AeroCommons is building an experimental aircraft called the **MAOS — Mobile Aviation Operating System**.

The concept: a four-seat, IFR-equipped, series-hybrid experimental aircraft that a single builder can construct in a two-car garage, transport on a road-legal trailer, and deploy from a remote airstrip without hangar support. It targets a 20,000 ft ceiling, carries TKS ice protection, and uses a novel propulsion architecture — two motorcycle-derived generator engines driving contra-rotating electric motors — that provides meaningful redundancy at every stage of the power chain.

It is designed and built under **FAA Experimental Amateur-Built (E-AB)** rules, the same regulatory framework used by thousands of homebuilt aircraft flying today. This means the builder constructs more than 51% of the aircraft themselves, and the FAA issues a special airworthiness certificate on that basis.

The MAOS does not exist yet as metal and composite. The design work is underway. This repository is where that work lives.

---

## What Is GitHub? (A Note for Pilots)

If you arrived here from the EAA forums, a fly-in conversation, or a link someone sent you, and you have never used GitHub before — welcome. Here is what you need to know.

**GitHub is a platform for storing, versioning, and collaborating on files.** It was built by software developers, so the interface can feel foreign if your world is airplanes rather than code. But the underlying idea is simple and useful for a project like this:

- Every document, drawing, and design file we produce is stored here
- Every change to every file is recorded, with a timestamp and a description of what changed and why
- Anyone in the world can read the files, download them, and propose changes
- Discussions happen in the open, attached to specific documents or topics

Think of it as a combination of a **shared filing cabinet**, a **change log**, and a **community forum** — one where the entire history of every decision is preserved and searchable.

You do not need to understand software development to participate here. You need to be willing to read, ask questions, and share your experience.

---

## Where We Are Right Now

The following formal design documents have been completed and are in the repository:

| Document | Title | Status |
|---|---|---|
| DWG MAOS-GA-001 | General Arrangement — Artist's Concept | Complete |
| DWG MAOS-PM-002 | Project Briefing — Team & Propulsion Architecture | Complete |
| MAOS-TRL-DEV-001 Rev A | Trailer & Ground Support Development Plan | Complete |
| MAOS-ECS-DEV-001 Rev B | Environmental Control System Development Plan | Complete |

**Open design decisions** currently under active analysis include: final wingspan (which drives trailer length and wing loading), flap vs. flapless configuration, HV bus voltage, propulsion motor final selection, and pressurization system design.

The design is not frozen. This is the point in the project where decisions are still being made and where experienced input has the most value.

---

## The Aircraft — Key Concepts

**Airframe:** Pod-and-boom configuration. A cylindrical pressure pod carries the crew and systems. A tail boom carries the empennage and propulsion motors. High wing with V-struts. Fixed faired tricycle gear.

**Propulsion:** Series hybrid. Two Honda 400cc motorcycle-derived engines mounted in the wing run as pure electrical generators. Their output feeds a common high-voltage bus alongside a flight battery pack. Contra-rotating electric motors on the tail boom provide thrust. No single failure produces a total power loss.

**Wing:** Single-piece removable high wing. Generators are integrated into the wing structure. Wing removal and installation uses the trailer's built-in crane system — no hangar, no forklift, no external ground equipment.

**Trailer:** A purpose-built ground support system based on an enclosed aluminum gooseneck car hauler. An overhead crane beam runs the length of the trailer interior. The aircraft is transported, deployed, and recovered entirely from the trailer. Road legal within Texas highway envelope.

**ECS:** Full climate control from first flight (v1.0), with all structural provisions for pressurization built in so that pressurization (v1.1) is an installation upgrade rather than a redesign.

**Avionics:** IFR equipped. EFIS-based glass panel. All-weather capable including TKS fluid ice protection.

**Regulatory:** FAA Experimental Amateur-Built, 51% rule. The aircraft will carry an experimental airworthiness certificate.

---

## How This Project Is Being Designed

The MAOS uses a structured **AI-assisted design methodology** that we believe is genuinely novel for homebuilt aircraft development.

Rather than using AI as a search tool or writing assistant, the project runs a **multi-agent design board** — a set of specialized AI agents assigned to Aerodynamics, Structures, Propulsion, Systems, Manufacturing, and Safety, coordinated by a Chairman agent. These agents hold formal board sessions, surface conflicts between disciplines, and produce structured decision records.

Every open design question is tracked as an explicit **decision gate**. No decision is resolved informally. Every gate has a current recommendation, a rationale, and remains open for revision until it is formally closed.

All session transcripts, agent SKILL files, board agendas, decision records, and analysis outputs are published in this repository as they are produced. The methodology itself is open — any builder can fork it and apply it to their own project.

This is not a replacement for engineering judgment. The agents surface conflicts and structure analysis. The human makes decisions.

---

## Manufacturing Philosophy

The MAOS is designed to be built by **one person with basic tools**. Not a well-equipped professional shop. A two-car garage with hand tools, a drill press, and internet access.

Primary structure uses:
- **Aluminum sheet and extrusions** — cut to DXF files by SendCutSend, OSH Cut, or equivalent. Parts arrive flat and ready to assemble.
- **Foam-core fiberglass composite** — hot-wire cut foam cores, hand-laid fiberglass. No autoclave. No CNC.
- **3D printed tooling and formers** — FDM for jigs, fixtures, and non-structural components. Never primary structure.
- **COTS hardware** — McMaster-Carr, Aircraft Spruce, standard commercial sources for everything else.

All design files are published in open formats: STEP, STL, DXF. Primary CAD tools are FreeCAD and OpenVSP. No vendor lock-in.

---

## How to Follow This Project

**You do not need an account to read everything in this repository.** All documents, drawings, and files are publicly visible.

If you want to do more than read:

### ⭐ Star the repository
The star button is in the top-right corner of this page. Starring a repository on GitHub is the equivalent of bookmarking it and telling the platform you find it interesting. It helps the project be discovered by others, and it tells us the work is reaching people.

### 👁️ Watch the repository
The **Watch** button (also top-right) lets you subscribe to activity. You can choose to be notified when new documents are published, when discussions open, or when decisions are recorded. You can tune the notification level to whatever suits you — from everything to only major releases.

### 💬 Join the Discussions
The **Discussions** tab at the top of this page is where the community conversation happens. You can:
- Ask questions about the design
- Share experience from your own builds or flying that's relevant to a design decision
- Follow threads on specific topics (propulsion, trailer ops, avionics, etc.)
- Propose an idea or flag a concern

Discussions are indexed and searchable. A question you ask today may help a builder three years from now.

### 🐛 Open an Issue
If you spot a problem in a document — a calculation that doesn't look right, a specification that conflicts with another, or a decision that seems to be missing — open an **Issue**. The Issues tab is designed for exactly this. It creates a tracked record of the concern and ensures it gets addressed.

### 🍴 Fork the Repository
If you want your own copy of the design files to experiment with, propose major changes, or adapt for your own project, you can **Fork** the repository. This creates a complete copy under your own GitHub account. Any changes you make to your fork are yours — and if you want to propose those changes be incorporated into the main project, you submit a **Pull Request**.

---

## Who We Are Looking For

The MAOS is a serious engineering project aimed at building a real aircraft. The people who will make it successful are:

- **Experienced homebuilders** who have completed or are building EAA projects and can ground-check design assumptions against shop reality
- **Pilots** — particularly those with IFR, mountain, or backcountry experience who can speak to the operational requirements the design is meant to serve
- **Aerospace and mechanical engineers** who want to apply professional judgment to a project that actually matters to them
- **Makers and fabricators** with composite, aluminum, or electrical skills
- **Software and firmware developers** interested in the open-source FADEC and control systems

You do not have to be credentialed to contribute. You have to be serious, specific, and willing to be wrong.

---

## Principles

1. **Safety through design, not pilot skill.** The aircraft must be inherently stable and departure-resistant. A bad moment should not become a fatal one.
2. **If a determined amateur cannot build it, the design has failed.** Complexity is a bug, not a feature.
3. **Weight is always the enemy.** Every component justifies its existence in grams, not just function.
4. **Open from the first session.** Nothing is held back for a later announcement. The work is public as it happens.
5. **The 51% rule is the design rule.** The builder-fabricated portions are the capable, interesting, achievable portions — not a compliance exercise.

---

## Links

- **Website:** [aerocommons.org](https://aerocommons.org)
- **Contact:** [contact@aerocommons.org](mailto:contact@aerocommons.org)
- **Discussions:** [github.com/billmallard/aerocommons/discussions](https://github.com/billmallard/aerocommons/discussions)

---

*AeroCommons is an open-source experimental aircraft development project. The MAOS has not yet flown. All specifications are design targets subject to revision. Nothing in this repository constitutes airworthiness approval or certification of any kind. Build and fly at your own judgment and risk.*