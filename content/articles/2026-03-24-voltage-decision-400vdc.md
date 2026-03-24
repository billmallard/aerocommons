---
title: "Design Decision D-001: 400V Electrical System"
date: 2026-03-24T13:26:00-06:00
description: "First closed decision for MAOS: 400VDC bus voltage validated by flight-proven aircraft and automotive EV ecosystem alignment."
tags: ["design-decisions", "systems", "propulsion", "voltage", "electric-aviation"]
author: "MAOS Design Board"
session: "D-001"
draft: false
---

## Decision Summary

**Decision Gate:** DG-004 Bus Voltage  
**Decision:** 400VDC electrical bus  
**Authority:** Builder (Direct Decision)  
**Date:** 2026-03-24  
**Status:** CLOSED

---

## The Decision

The MAOS aircraft will use a **400-volt DC electrical system** for the main propulsion bus.

This is the first design decision formally closed and documented in the MAOS project. After comprehensive technical analysis comparing 270V and 400V architectures, the builder selected 400V based on:

1. **Flight-proven validation** — Pipistrel Velis Electro (only type-certified electric aircraft) operates at 345V
2. **Component availability** — Massive automotive EV ecosystem at 400V (Tesla, VW, GM, Ford standard)
3. **Weight savings** — 400V reduces current from 556A to 375A for our 155 kW power requirement, saving ~10 lbs in wiring
4. **Future-proofing** — Headroom for v1.1 electrical loads without architectural redesign
5. **Industry alignment** — Light aircraft tier (345-400V) validated by certified and experimental aircraft worldwide

---

## Flight-Proven Context

Research into what electric aircraft are actually flying revealed clear voltage tiers:

### Light Aircraft (Our Class)
- **Pipistrel Velis Electro:** 345V, 57.6 kW, type-certified
- **MAOS:** 400V, 155 kW (dual 77.5 kW motors)

### Medium Power
- **Bye Aerospace eFlyer 2:** 600V, 90 kW

### Heavy / High-Performance
- **magniX (Eviation Alice):** 800V — "highest voltage ever flown in an aircraft"
- **Beta Technologies ALIA:** 800V+ estimated
- **Joby Aviation S4:** 800V+ estimated

**Key finding:** 400V sits squarely in the proven light aircraft tier. We're 55 volts above the only certified electric aircraft, not pioneering unproven territory like 800V systems that require custom connector development and advanced insulation engineering.

---

## Power Scaling vs Certified Baseline

| Parameter | Pipistrel Velis | MAOS | Ratio |
|-----------|----------------|------|-------|
| **Voltage** | 345V | 400V | 1.16× |
| **Total Power** | 57.6 kW | 155 kW | 2.69× |
| **Motors** | 1 | 2 | 2× |
| **Power Per Motor** | 57.6 kW | 77.5 kW | **1.35×** |
| **Current** | ~167A | ~388A | 2.32× |

**Conservative scaling:** Our 2.69× power increase comes primarily from using *two motors* for redundancy. Each motor is only 35% more powerful than Pipistrel's certified motor — not a giant leap into unproven territory.

---

## Technical Consensus

- **SYSTEMS:** Recommended 400V after determining generator heads are voltage-configurable (no conversion loss penalty)
- **PROPULSION:** Supported 400V; will specify Beyond Motors AXM2 generator heads with 400V output winding
- **No dissenting agents**

Original 270V recommendation was based on an assumed generator output voltage constraint. Technical review determined that constraint does not exist — generator heads can be wound for any voltage we specify.

---

## Why Not 270V?

270V was initially considered because it was assumed to optimize generator efficiency. Analysis revealed:

1. Generator voltage is **configurable** — no efficiency penalty for 400V vs 270V
2. 270V requires **higher current** (556A vs 375A at 155 kW) → heavier wiring
3. **Smaller component ecosystem** at 270V compared to automotive EV standard 400V
4. **Less future headroom** for electrical load growth in v1.1+

---

## Why Not 800V?

800V is state-of-the-art for high-power electric aircraft (magniX, Beta, Joby), but comes with significant challenges:

1. **Corona effects** at altitude require extensive creepage/clearance design
2. **Custom connectors required** — magniX went through dedicated connector development program
3. **Pioneering territory** — described as "highest voltage ever flown" 
4. **Not necessary for our power class** — 400V handles 155 kW comfortably

We're building a light aircraft, not an eVTOL. Use proven technology, not cutting-edge.

---

## Aircraft vs Automotive: The Grounding Challenge

An important lesson from Pipistrel's engineering team:

> "The aircraft isn't grounded like a car, so keeping currents manageable and EMI low is critical."

**What this means:**
- Cars: Metal chassis connected to battery negative, tires provide path to ground, electrical faults can dissipate
- Aircraft: Rubber tires, surrounded by insulating air, electrically isolated — no path to ground
- At altitude: Thinner air (55% density at 17,500 ft) = worse insulation, higher arc-over risk

**Implication:** Aircraft electrical systems require more careful EMI (electromagnetic interference) management than automotive systems, especially at altitude. 400V is proven safe; 800V requires pioneering insulation/EMI work.

---

## Action Items

| Responsible Agent | Task | Timeline |
|-------------------|------|----------|
| **PROPULSION** | Specify Beyond Motors AXM2 generator heads with 400V output winding | Before component procurement |
| **SYSTEMS** | Source 400V motor controllers (Cascadia Motion, Tesla aftermarket, Sevcon/Dana) | Preliminary design phase |
| **SYSTEMS** | Develop high-voltage safety procedures (lockout/tagout, insulation testing) | Before electrical integration |
| **SYSTEMS** | Design wiring harness for 400V per SAE J1673 automotive HV standards | Detailed design phase |
| **STRUCTURES** | Update weight budget: wiring harness 40 lbs → 30 lbs | Next revision |

---

## What This Unblocks

With voltage decided, the following work can now proceed:

- **Motor controller procurement** (long lead-time item)
- **Inverter specifications**
- **Wiring harness detailed design**
- **DG-008 (ECS condenser placement)** — depends on bus voltage
- **Battery buffer sizing** and BMS selection
- **Contactors and safety systems** selection

This was the critical-path blocker for all electrical component specifications.

---

## Safety Considerations

400V is lethal if mishandled, but manageable with proper procedures:

1. **Color coding:** All HV wiring bright orange (SAE J1673 standard)
2. **Service disconnect:** Physical lockout/tagout when working on HV systems
3. **Insulation monitoring:** Continuous ground fault detection
4. **Dual-redundant contactors:** Two in series on main power paths
5. **Builder HV training:** Same training automotive EV technicians receive

This is no different than thousands of homebuilt electric vehicle conversions — requires respect and proper procedures, but well within experimental builder capability.

---

## Historical Note

**This is the first closed decision in MAOS project history.**

The design board now has a functioning decision log. DG-004 moved from OPEN to CLOSED. Interface specifications updated (generator output voltage, motor controller input voltage now defined).

Process validated: technical analysis → builder review → documented decision → action items assigned.

---

## References

- [SYSTEMS Bus Voltage Analysis (270V vs 400V)](../proposals/SYSTEMS-bus-voltage-270v-vs-400v-analysis-2026-03-24.md)
- [Flight-Proven Voltage Survey](../proposals/SYSTEMS-flight-proven-voltage-survey-2026-03-24.md)
- MAOS-design-state.md (Decision Log Section 4, Decision D-001)

---

## Next Decisions

**DG-005: Engine Selection** (Honda 400cc vs Kawasaki I4 turbo vs others) remains open. Technical analysis complete, awaiting builder decision.

---

*Decision documented by CHAIRMAN, MAOS Design Review Board, 2026-03-24*
