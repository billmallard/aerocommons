---
title: "Do NACA Ducts Work? What the Original Data Actually Says"
date: 2026-04-11T11:30:00-06:00
description: "A hard look at original NACA submerged-inlet research, where skepticism is justified, and what it means for pod inlets and outflow design in pressurization and electric A/C systems."
tags: ["aerodynamics", "systems", "pressurization", "ecs", "education"]
author: "AeroCommons"
project: "maos"
article_type: "analysis"
draft: false
---

Short answer: **yes, NACA ducts can work**. Longer answer: **they work well only inside a specific design envelope**. A lot of modern skepticism comes from using them outside that envelope and expecting scoop-like ram pressure.

If you read the original NACA work carefully, that skepticism is not anti-science. It is exactly what the data predicts.

This article targets a practical question builders ask all the time: **when should you use a NACA duct, when should you avoid one, and what should you test before committing to tooling?**

## Key Terms

- **NACA duct / submerged inlet**: A flush or recessed inlet intended to reduce external drag compared with protruding scoops while still providing useful internal airflow.
- **Pressure recovery (ram-recovery ratio)**: The ratio of total pressure at the inlet station to free-stream total pressure. Higher recovery usually means better pressure margin for downstream systems.
- **Boundary layer**: The slower-moving air near a surface. If an inlet ingests too much of it, recovery and flow quality can degrade.
- **Mass-flow coefficient / inlet-velocity ratio**: A measure of how much flow the inlet is being asked to pass relative to local external flow.
- **Incremental drag**: Drag added by the inlet installation compared with the same body without that inlet.
- **Flow distortion**: Non-uniform pressure or velocity at the downstream face of the inlet/duct, which can hurt compressor or system performance.
- **Off-design condition**: Any operating point away from nominal cruise, such as high angle of attack, yaw/sideslip, climb, descent, low-speed, or crosswind operation.

---

## What Was Actually Studied?

Most of what builders call a "NACA duct" comes from postwar NACA submerged-inlet work in the 1945-1951 period, not from one single magical test.

Key records:

- **NACA-ACR-5I20 (1945)**, "An Experimental Investigation of NACA Submerged-Duct Entrances"
- **NACA-RM-A8B16 (1948)**, high-subsonic tests with inlets forward of wing leading edge
- **NACA-RM-A8I29 (1948)**, ram-recovery characteristics versus location, boundary layer, Mach, AoA
- **NACA-RM-A7D14 (1947)**, full-scale Ryan FR-1 installation tuning
- **NACA-RM-A51H20 (1951)**, submerged inlet vs nose inlet in transonic free-fall tests
- **NACA-TN-2323 (1951)**, theoretical + tunnel + flow-visualization analysis

The important point is this: these studies do **not** claim "flush is always best." They repeatedly report condition-dependent performance.

---

## What the Original Data Says (And Doesn't Say)

Before diving into each report, define terms clearly:

- **Ram-recovery ratio**: total pressure at inlet station divided by free-stream total pressure
- **Mass-flow coefficient / inlet-velocity ratio**: how hard the inlet is being asked to work relative to local external flow
- **Incremental drag**: drag added by the inlet installation versus a baseline body

These are the quantities NACA used repeatedly. Most modern arguments about NACA ducts are actually arguments about one of these three metrics.

### 1) NACA itself states boundary-layer and placement limits

From NACA-ACR-5I20: desirable behavior appears when the inlet is in a region of **low incremental velocity and thin boundary layer**. It also states submerged entrances are most suitable for systems that require only **small internal diffusion**, and that where complete diffusion is required, **nose or wing-leading-edge inlets may be superior**.

That is already a built-in caveat.

### 2) Mass-flow demand can dominate recovery

From NACA-RM-A8B16: reported ram-recovery ratio changed from about **0.50 at zero flow** to **0.95 at mass-flow coefficient 1.00**. Mach and angle-of-attack effects were smaller in that particular configuration.

Translation: your inlet can look fine on one operating point and disappoint badly on another if demanded flow is off-design.

### 3) Location matters a lot

From NACA-RM-A8I29: inlets ahead of or near the wing leading edge had only slight high-Mach recovery decrease, but inlets aft of the wing max-thickness station showed **large** recovery decreases at high Mach.

So "a NACA duct" is not one thing. Local flowfield can make or break it.

### 4) Real installations needed lip/ramp tuning

From NACA-RM-A7D14 (Ryan FR-1): inner-lip flow stall caused high pressure losses in the original installation. Revised entrance lips and deflectors gave a **12% recovery increase** at design condition. Authors still concluded a larger redesign (ramp angle and lip camber) was needed for optimum performance.

This is a strong warning against copy-paste geometry.

### 5) Flush did not automatically beat other inlets

From NACA-RM-A51H20: in transonic tests, the nose-inlet model had lower external drag than the submerged-inlet model through the test range (though airplane-level delta could be small depending on area ratios).

Again: no universal supremacy.

### 6) The vortex mechanism is real, but not free

From NACA-TN-2323: divergent-ramp inlets generate a vortex pair and retard some ramp-floor boundary-layer growth, but there are vortex-associated losses and geometry-dependent tradeoffs.

The oft-repeated "the vortices save everything" story is incomplete.

---

## Why the Myth Persisted

There are at least four reasons NACA duct folklore became oversimplified:

1. Early reports were interpreted as broad endorsement instead of conditional guidance.
2. Builders copied geometry shape but ignored local boundary-layer thickness and approach flow quality.
3. Many applications cared most about drag aesthetics, not guaranteed pressure margin.
4. Bench success at one operating point got generalized to all mission conditions.

This is normal engineering-history drift. It is not bad intent. But it does create design risk when people quote a geometry without quoting the test envelope.

---

## Is There Room for Skepticism?

Yes, and it is evidence-based skepticism, not internet contrarianism.

The original literature supports skepticism whenever people claim one of these:

- "NACA ducts always have low drag and great pressure recovery"
- "If it is flush and looks right, it works"
- "One published geometry scales everywhere"
- "A NACA duct is the best choice for every cooling or pressurization inlet"

The data supports a narrower claim:

- Properly designed submerged inlets can provide useful recovery at low drag in favorable local flow with correct geometry and operating point.

That is much less universal than hobby lore suggests.

---

## Practical Implications for Pod Inlets and Outlets (Pressurization + A/C)

For MAOS-like pod architecture, the question is not "NACA yes/no?" The question is:

- What mass flow is needed in each mission segment?
- How much pressure recovery is needed?
- What is the local boundary layer at the chosen station?
- What happens at low speed, high AoA, crosswind, and ground operation?

### 1) Pressurization intake (high consequence)

The ECS requirements call for electric pressurization compressor feed and reliable operation through broad envelope conditions. That is a **reliability-first** intake problem, not a "minimum external bump" problem.

Design implication:

- Treat a pure flush NACA solution as a candidate, not a default.
- If compressor inlet pressure margin is tight, consider semi-flush or modestly proud geometry, or boundary-layer management features, to protect worst-case recovery.
- Validate at off-design points, especially low-speed/high-AoA/climb conditions where boundary layer and local incidence can drift.

### 2) Condenser/heat-rejection airflow (A/C)

Ground hot-day cooling is often the sizing case. On the ground, ram effects are weak, so inlet pressure recovery from external aerodynamics matters less than fan and exchanger design.

Design implication:

- For A/C condenser circuits, a low-drag submerged inlet may still be fine if fan authority is strong and duct losses are controlled.
- Do not assume cruise-optimized inlet geometry solves taxi/idle thermal performance.

### 3) Outflow and exhaust air (pressurization + ventilation)

NACA geometry is an inlet concept. Cabin outflow is a different physics problem.

Design implication:

- Use dedicated outflow-valve architecture and place outlets where external pressure field supports stable cabin pressure control.
- Avoid outlet placements that can ingest separated flow at high AoA or cause backflow in crosswind/propwash interactions.
- For pod systems, favor inspectable, serviceable, contamination-resistant outlet hardware over elegant flush shaping alone.

### 4) Modularity constraint (pod-and-boom)

Because ECS stays in the pod and avoids wing pneumatic interfaces, inlet/outlet decisions must support repeated assembly and predictable duct sealing.

Design implication:

- Slight aerodynamic penalty may be acceptable if it buys large gains in maintainability, repeatable sealing, and testability.

### 5) What to optimize for each function

Do not optimize all pod flow paths for the same objective.

- Pressurization intake objective: pressure margin and stable compressor feed
- Condenser inlet objective: net heat rejection at worst ambient, especially ground idle and taxi
- Cabin ventilation objective: occupant comfort and contaminant removal
- Outflow objective: controllable cabin pressure with no backflow surprises

Trying to solve all four with one "universal" inlet style usually creates compromises in the wrong place.

---

## Failure Modes That Deserve Explicit Skepticism

If you want to be rigorous, skepticism should be pointed at specific failure modes:

- **Boundary-layer ingestion creep** as AoA and Reynolds number change
- **Lip separation** in off-design incidence or yaw
- **Flow distortion** at compressor face, causing efficiency loss or surge margin erosion
- **Crosswind-induced reversal tendencies** for outlets during low-speed operations
- **Ground-operation thermal shortfall** where fan-only condenser flow cannot meet hot-day load

None of these are theoretical edge cases for a pod pressurization and ECS architecture. They are ordinary development issues that appear once you leave design-point cruise.

---

## Recommended Test Plan Before Freezing Geometry

If this becomes a design gate, the minimum credible workflow is:

1. Define mission-point airflow and pressure requirements (ground hot day, climb, cruise, descent).
2. Evaluate 2-4 inlet concepts (flush submerged, submerged+deflector, semi-flush scoop, modest external scoop).
3. Estimate local boundary-layer thickness at candidate locations (CFD or tuft/smoke + pressure taps on prototype).
4. Measure total-pressure recovery and duct loss on a representative mockup.
5. Re-test at off-design AoA/yaw and low dynamic pressure.
6. Select geometry based on system margin and reliability, not appearance.

This is exactly where historical NACA lessons are most useful: they tell us which variables matter so we test the right things.

For a full MAOS-oriented implementation guide, see the companion article:

- [/articles/2026-04-11-naca-duct-design-gate-for-pod-ecs/](/articles/2026-04-11-naca-duct-design-gate-for-pod-ecs/)

---

## Decision Rule (Practical)

If you need a one-page gate criterion:

1. If the system can tolerate moderate recovery variation and values clean exterior lines, test submerged first.
2. If the system has tight pressure margin or strong off-design sensitivity, include semi-flush or external scoop concepts from the start.
3. If outlet stability is mission-critical, decouple outlet design decisions from inlet style preferences.
4. Freeze geometry only after measured off-design performance, not after CAD review.

This keeps engineering decisions attached to measured risk, not tradition.

---

## Should This Be an AeroCommons Article?

Yes. This is strong article material because it connects three communities that usually talk past each other:

- Builders repeating received NACA wisdom
- Engineers focused on pressure-recovery and boundary-layer constraints
- Systems designers trying to make pressurization and electric A/C actually work in a pod architecture

It also fits AeroCommons mission: open-source engineering that turns folklore into testable decisions.

---

## Sources (Primary)

- NASA NTRS: NACA-ACR-5I20, "An Experimental Investigation of NACA Submerged-Duct Entrances" (1945)  
  https://ntrs.nasa.gov/citations/20050061115
- NASA NTRS: NACA-RM-A8B16, "An Experimental Investigation of NACA Submerged Inlets at High Subsonic Speeds I" (1948)  
  https://ntrs.nasa.gov/citations/19930093808
- NASA NTRS: NACA-RM-A8I29, "Ram-recovery Characteristics of NACA Submerged Inlets at High Subsonic Speeds" (1948)  
  https://ntrs.nasa.gov/citations/19930085451
- NASA NTRS: NACA-RM-A7D14, "Tests of Submerged Duct Installation on the Ryan FR-1 Airplane" (1947)  
  https://ntrs.nasa.gov/citations/20030063155
- NASA NTRS: NACA-RM-A51H20, "Drag and Pressure Recovery of a Submerged Inlet and a Nose Inlet" (1951)  
  https://ntrs.nasa.gov/citations/19930093734
- NASA NTRS: NACA-TN-2323, "Theoretical Investigation of Submerged Inlets at Low Speeds" (1951)  
  https://ntrs.nasa.gov/citations/19890067876
- NASA NTRS: "Summary of NACA submerged-inlet investigations" (1947 conference paper)  
  https://ntrs.nasa.gov/citations/19790079925
