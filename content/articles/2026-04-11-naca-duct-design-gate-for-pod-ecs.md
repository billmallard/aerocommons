---
title: "NACA Duct Design Gate for Pod ECS: Test Matrix, Instrumentation, and Go/No-Go Criteria"
date: 2026-04-11T12:20:00-06:00
description: "Companion engineering guide for MAOS pod inlet and outlet decisions: pressure-recovery targets, boundary-layer checks, instrumentation plan, and design-gate acceptance criteria for pressurization and electric A/C."
tags: ["aerodynamics", "ecs", "pressurization", "testing", "naca-duct", "maos"]
author: "AeroCommons"
project: "maos"
article_type: "analysis"
draft: false
---

This is the companion to [Do NACA Ducts Work? What the Original Data Actually Says](/articles/2026-04-11-do-naca-ducts-work/).

That article answers the historical question. This one answers the build question:

- What should we measure?
- How should we test candidate pod inlet/outlet concepts?
- What acceptance criteria should trigger go/no-go decisions?

If a decision gate is not measurable, it is not a real gate.

---

## 1) System Context for MAOS Pod ECS

From current ECS requirements:

- Pressurization and climate loops are pod-contained
- Pod-external ECS connections are electrical only
- Pressurization loop ingests ambient air through a filtered pod inlet
- Outflow valve regulates cabin pressure on aft bulkhead
- Ground hot-day cooling and off-design operations are key mission drivers

That means inlet/outlet geometry is not just aerodynamic styling. It is a first-order systems integration decision affecting:

- Compressor inlet pressure margin
- Condenser heat rejection margin
- Cabin pressure-control stability
- Serviceability and repeatability across repeated assembly cycles

---

## 2) Candidate Geometry Set (Minimum)

Run at least four concepts in parallel during concept screening:

1. Flush submerged inlet (classic NACA-style)
2. Submerged inlet with boundary-layer management feature (deflector/fence variant)
3. Semi-flush scoop (small external protrusion)
4. Modest external scoop optimized for recovery, not aesthetics

For outlets, at minimum evaluate:

1. Flush or near-flush side outlet near controlled pressure region
2. Aft-facing low-profile outlet geometry
3. Dedicated outflow valve region with shielding from local separated flow

Do not let one concept dominate before data arrives.

---

## 3) Metrics to Track

Track both aerodynamic and systems-level metrics. NACA-era values alone are insufficient.

### 3.1 Inlet Aerodynamic Metrics

- Total pressure recovery: $\pi_r = P_{t,in}/P_{t,\infty}$
- Static pressure at compressor inlet
- Distortion index at compressor face (simple circumferential variation is acceptable for early phases)
- Duct pressure loss coefficient

### 3.2 ECS Functional Metrics

- Pressurization compressor electrical power versus delivered mass flow
- Cabin climb rate and pressure-control stability
- Condenser approach temperature and net heat rejection
- Ground hot-day cabin cooldown time

### 3.3 Robustness Metrics

- Sensitivity of recovery to AoA, yaw, and dynamic pressure
- Sensitivity to crosswind and propwash-equivalent flow skew
- Repeatability across reinstall/reseal cycles

If performance is good only at one point, treat that as a red flag.

---

## 4) Test Matrix (Minimum Viable)

Use this as a baseline matrix; expand as needed.

| Test ID | Scenario | Why it matters | Pass/Fail focus |
| :-- | :-- | :-- | :-- |
| T1 | Ground idle, hot day | Condenser sizing driver | Cooling margin and compressor power |
| T2 | Low-speed climb, high AoA | Boundary-layer and incidence stress | Inlet recovery stability |
| T3 | Cruise nominal | Design-point validation | Recovery and drag balance |
| T4 | Cruise off-design yaw | Crosswind and sideslip sensitivity | Distortion and control stability |
| T5 | Descent / low power | Outlet backflow risk | Cabin pressure control behavior |
| T6 | Repeated assembly cycle check | Modularity reality | Seal consistency and repeatability |

When resources are limited, prioritize T1, T2, and T6 first because they are most likely to expose hidden integration risk.

---

## 5) Instrumentation Plan (Prototype Level)

You do not need a giant lab to get useful data. You do need disciplined instrumentation.

### 5.1 Pressure Measurement

- Free-stream reference total/static (or calibrated surrogate station)
- Inlet lip pressure taps
- Duct static taps at 2-3 stations
- Compressor-face total pressure rake (even a simple multi-point rake helps)
- Cabin pressure and outflow valve region static pressure

### 5.2 Temperature and Thermal

- Ambient air temperature near inlet
- Condenser inlet/outlet air temperature
- Refrigerant high-side and low-side temperature/pressure
- Cabin air temperature at multiple points

### 5.3 Flow and Electrical

- Pressurization compressor speed and power draw
- Condenser fan speed and power draw
- Climate compressor speed and power draw
- Estimated mass flow (or calibrated surrogate from pressure/temperature map)

### 5.4 Vehicle State

- Airspeed proxy, AoA proxy, yaw proxy
- Test-point annotation for configuration state (doors, seals, fan modes, valve positions)

Log at a fixed cadence with synchronized timestamps. If datasets cannot be aligned, root-cause analysis becomes guesswork.

---

## 6) Data Reduction and Comparison Method

For each concept, reduce to the same comparison outputs:

1. Recovery versus flow demand map
2. Recovery versus AoA/yaw map
3. Compressor power versus delivered function (pressurization or cooling)
4. Worst-case margin table for each mission segment
5. Integration penalties (weight, complexity, maintenance access)

Then choose on system value, not on a single best number.

A concept that is 1 percent worse in cruise recovery but dramatically better in assembly repeatability or off-design stability may be the correct aircraft choice.

---

## 7) Proposed Go/No-Go Criteria

These are template criteria and should be tuned once baseline data arrives.

### 7.1 Pressurization Inlet Gate

- Demonstrates stable recovery across required AoA/yaw envelope without compressor instability indicators
- Maintains adequate inlet pressure margin at worst-case low-speed/high-demand condition
- No unacceptable sensitivity to realistic seal/assembly variation

### 7.2 Condenser Inlet Gate

- Meets ground hot-day cooling requirement with acceptable electrical power and duty cycle
- No thermal runaway trend in sustained low-ram conditions
- Acceptable debris/water ingestion behavior for expected operations

### 7.3 Outlet/Outflow Gate

- Pressure-control loop remains stable throughout mission transitions
- No repeatable backflow instability in tested yaw/crosswind conditions
- Service and inspection access acceptable for recurring maintenance

If any of these fail, geometry is not frozen.

---

## 8) Common Program Risks and Mitigations

### Risk: Optimizing for drag before validating pressure margin

Mitigation: Run systems-level acceptance criteria first, then optimize drag inside passing concept set.

### Risk: Overtrusting CFD without boundary-condition realism

Mitigation: Use CFD for down-select, but require physical pressure/thermal test correlation before gate closure.

### Risk: Ignoring outlet behavior until late integration

Mitigation: Include outlet stability tests from first integrated ECS prototype phase.

### Risk: Single-point success mistaken for envelope success

Mitigation: Enforce multi-condition pass matrix as gate policy.

---

## 9) Why This Matters for Open-Source Aviation

Open-source aviation cannot rely on aesthetic consensus or inherited geometry rules. It has to rely on transparent evidence.

Publishing the full test matrix, instrumentation assumptions, and gate criteria does three useful things:

- Makes design debates reproducible
- Allows external contributors to challenge assumptions with data, not opinion
- Prevents future builders from repeating expensive dead ends

That is the real value of this gate: it is reusable engineering process, not just one inlet decision.

---

## 10) Working Conclusion

For MAOS-like pod ECS architecture, "Do NACA ducts work?" is the wrong final question.

The right final question is:

- Which inlet/outlet concept delivers the most robust systems performance across real mission conditions at acceptable drag, weight, and maintenance complexity?

That answer comes from gate-tested data.

Until then, all geometry choices are provisional.
