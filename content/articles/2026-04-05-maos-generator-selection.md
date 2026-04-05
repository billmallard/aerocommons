---
title: "MAOS Generator Selection: Axial-Flux Machines and the 400V vs 800V Decision"
date: 2026-04-05T14:00:00-06:00
description: "Evaluating generator candidates for the MAOS series hybrid drivetrain, with analysis of axial-flux PM machines, ICE shaft interface, and the voltage architecture question reopened by Samson Sky's Skybrid 800V choice."
tags: ["propulsion", "analysis", "design-decisions", "hybrid-electric", "electric-aviation", "systems", "voltage"]
author: "PROPULSION, MAOS Design Board"
summary: "The MAOS generator is the least-analyzed component in the series hybrid drivetrain. This article evaluates axial-flux permanent magnet machines as the leading candidate technology, examines the ICE-to-generator shaft interface problem, and reopens the bus voltage question in light of Samson Sky's Skybrid choosing 800V over the automotive 400V standard."
project: "maos"
article_type: "analysis"
draft: false
---

## Overview

**Date:** 2026-04-05
**Owner:** PROPULSION
**Purpose:** Evaluate generator candidates for the MAOS series hybrid drivetrain and reassess the bus voltage decision.

The MAOS propulsion design has analyzed ICE engines extensively and touched on propulsion motors (Donut Lab rim-drive, Axiom). The generator — the electrical machine that converts ICE shaft power into DC bus power — has received the least attention and is arguably the most critical integration point in the drivetrain. It directly couples two major systems: the ICE (mechanical) and the electrical bus (power delivery). It is also where the bus voltage decision has the most impact.

---

## What the Generator Must Do

In a series hybrid, the generator is not a backup or emergency device. It is the primary power source during all normal flight operations. It runs continuously at high load. Requirements:

| Parameter | Requirement | Basis |
|---|---|---|
| Continuous power per unit | 65–80 kW | Single generator failure must sustain flight |
| Peak power | 90–110 kW | Takeoff climb, both generators running at load |
| Speed range | 4,000–12,000 RPM | Motorcycle ICE operating range |
| Output voltage | 400V DC (current decision) or 800V DC (under review) | Bus architecture |
| Cooling | Liquid preferred | Sustained high-load aircraft duty cycle |
| Weight | <30 kg / 66 lbs per unit | Weight budget |
| Form factor | Compact, inline or coaxial with ICE | Wing-integrated mounting |

The weight target of <30 kg is aggressive. It reflects the dual-unit installation (two generators in the wing) and the need to keep engine+generator weight below approximately 100 kg per side total.

---

## Generator Technology Landscape

### Why Axial-Flux Permanent Magnet (AFPM)?

Conventional radial-flux machines (the type in most industrial motors and alternators) pack power into a long cylinder. Axial-flux machines pack power into a thin disc. For aircraft, where you want maximum power density in minimum volume and weight, axial-flux dominates the high-performance space.

**Axial-flux advantages:**
- 3–5× higher torque density than radial-flux at equivalent weight
- Short axial length — fits inline with an ICE crankshaft extension without major packaging penalty
- High efficiency (93–98% at operating point)
- No brushes, no commutator — solid-state operation
- Can be run as either motor or generator from the same machine

**Axial-flux trade-offs:**
- More complex manufacturing than radial-flux
- Axial magnetic forces create bearing loads that must be designed for
- Less established supply chain than radial-flux industrial machines

### Can the Same Machine Be Used for Both Generator and Motor?

Yes — and this is worth taking seriously for MAOS.

An axial-flux PM machine is bidirectional. The same physical unit can:
- Be driven by the ICE crankshaft → acts as generator (produces electrical power)
- Be supplied with electrical power → acts as motor (produces shaft power)

**Implication:** If MAOS standardizes on one axial-flux machine type — say the Beyond Aviation AXM3 or Emrax 268 — that machine can serve as both the ICE-coupled generator in the wing and the propulsion motor on the tail boom. This reduces:
- Unique part count (one machine, two roles)
- Spare parts inventory
- Training/maintenance complexity
- Procurement risk (single supplier relationship)

The controller software differs (generator mode vs. motor mode), but modern motor controllers handle both. This is the architecture of several production EVs and hybrid powertrains.

---

## Candidate Generator Machines

### Emrax Series (Slovenia)

Emrax makes aviation-focused axial-flux machines that are among the best-documented in experimental aviation. They publish actual tested data (not just peak claims) and have a track record in ultralight and experimental aircraft.

| Model | Cont. Power | Peak Power | Weight | Max RPM | Max Voltage | Cooling |
|---|---|---|---|---|---|---|
| **Emrax 188** | 20 kW | 50 kW | 7.2 kg | 6,500 | 700V | Air/liquid |
| **Emrax 228** | 50 kW | 100 kW | 12.3 kg | 6,000 | 700V | Air/liquid/oil |
| **Emrax 268** | 80 kW | 160 kW | 20.4 kg | 5,000 | 700V | Air/liquid/oil |
| **Emrax 348** | 100 kW | 200 kW | 36 kg | 4,500 | 700V | Liquid/oil |

**For MAOS (65–80 kW continuous per generator):**
- Emrax 268 at 20.4 kg is the strong fit — 80 kW continuous, well within voltage range, proven in experimental aircraft
- Emrax 228 is marginal at 50 kW continuous — meets the requirement only if peak is used as sustained
- Emrax 348 exceeds the power requirement and is too heavy at 36 kg

**Sourcing:** Direct from Emrax (emrax.com), US distributors available. Lead time typically 8–16 weeks. Price range: $8,000–$15,000 per unit (varies by model and cooling spec). Well-documented builder community for experimental aircraft.

---

### Beyond Aviation / Evolito AXM Series (UK)

The AXM series (originally Advanced Systems Research, now marketed as Evolito) is an axial-flux machine designed specifically for aviation. The Samson Sky Switchblade's Skybrid system is reported to use the AXM3 — making it a directly relevant reference design for MAOS.

| Model | Cont. Power | Peak Power | Weight | Notes |
|---|---|---|---|---|
| **AXM2** | ~50 kW | ~100 kW | ~10 kg (est.) | Smaller unit, less published data |
| **AXM3** | ~100 kW | ~200 kW | ~15 kg (est.) | Samson Sky Skybrid motor; specs not fully public |

**Caveats:** Evolito/Beyond Aviation does not publish full datasheets publicly. The weight and power figures above are estimated from available sources including the Samson Sky application. The AXM3 is confirmed in real-world aerospace use, which carries significant weight as a validation signal.

**For MAOS:** If the AXM3 at ~100 kW continuous and ~15 kg is accurate, it would be the best power-to-weight option in this comparison — and using the same machine for both generator and propulsion motor becomes very compelling. The standardized architecture would look like: AXM3 as ICE-driven generator in each wing, two AXM3s as contra-rotating propulsion motors on the tail boom. Four identical machines total.

**Sourcing:** Contact Evolito directly (evolito.aero). Aerospace/experimental customers, not consumer market. Lead time and pricing unclear — likely OEM relationships rather than catalog sales.

---

### Magnax AXF Series (Belgium)

Magnax produces yoke-less axial-flux machines with very high torque density, aimed at industrial and EV applications.

| Model | Cont. Power | Peak Power | Weight | Max RPM |
|---|---|---|---|---|
| **AXF225** | 75 kW | 175 kW | 29 kg | 3,500 |

The AXF225 meets the power requirement but at 29 kg is near the weight limit, and the 3,500 RPM maximum is problematic for direct coupling to a motorcycle ICE running at 6,000–11,000 RPM. A reduction drive would be required, adding weight and complexity.

**Assessment:** Marginal. The RPM mismatch is the primary disqualifier without a reduction gearbox.

---

### YASA (UK / Mercedes-Benz)

The YASA P400 is a well-regarded axial-flux machine — ~160 kW peak, excellent power density — but YASA was acquired by Mercedes-Benz in 2021 and is now embedded in the automotive supply chain. It is not practically available to independent builders or small OEMs. Listed here for reference only.

**Assessment:** Not accessible for MAOS. Monitor for future licensing or surplus availability.

---

### Infinitum Electric (Air-Core Axial Flux, USA)

Infinitum replaces the heavy steel stator core with a printed circuit board winding, eliminating iron losses and reducing weight significantly. The company targets industrial applications (commercial HVAC, data centers) but the technology is relevant.

| Spec | Value |
|---|---|
| Peak efficiency | >96% |
| Weight reduction vs. conventional | ~50% |
| Power range | 10–100 kW (commercial line) |
| Aviation use | None documented |

**Assessment:** Interesting technology, no aviation track record. Too early for MAOS primary application. Worth watching.

---

### Conventional Aircraft Alternators / Generators

For completeness: certified aircraft generators (Prestolite, Plane Power, B&C) are radial-flux wound-field machines producing 24–28V or 115/200VAC. They top out at 60–100 amps (1.5–2.8 kW). These are not relevant to the MAOS HV bus application — they are three orders of magnitude too small in power output.

**Assessment:** Not applicable.

---

## Generator Comparison Matrix

| Machine | Cont. Power | Weight | Power/Weight | Max Voltage | RPM Range | Aviation Track Record | Availability | Est. Unit Cost |
|---|---|---|---|---|---|---|---|---|
| **Emrax 268** | 80 kW | 20.4 kg | 3.9 kW/kg | 700V | To 5,000 RPM | Good (experimental) | Good | ~$12,000 |
| **Emrax 348** | 100 kW | 36 kg | 2.8 kW/kg | 700V | To 4,500 RPM | Good (experimental) | Good | ~$15,000 |
| **Beyond Aviation AXM3** | ~100 kW (est.) | ~15 kg (est.) | ~6.7 kW/kg (est.) | Unknown | Unknown | Excellent (Samson Sky) | OEM only | Unknown |
| **Emrax 228** | 50 kW | 12.3 kg | 4.1 kW/kg | 700V | To 6,000 RPM | Good (experimental) | Good | ~$8,000 |
| **Magnax AXF225** | 75 kW | 29 kg | 2.6 kW/kg | Unknown | To 3,500 RPM | None | Limited | Unknown |

**Working conclusion:** Emrax 268 is the planning baseline — documented specs, known availability, aviation use cases, and meets MAOS requirements. AXM3 is the aspirational target pending direct engagement with Evolito.

---

## The ICE-to-Generator Shaft Interface

This is the integration problem that gets less attention than it deserves.

Motorcycle-derived ICE engines run at 8,000–12,000 RPM at peak power. The Rotax 915 iS redlines at 5,800 RPM. Most axial-flux generators have a maximum continuous RPM of 4,500–6,000.

**Three options:**

### Option 1: Direct Drive
ICE crankshaft → generator shaft, no intermediate gearing.

- Works if ICE operating RPM matches generator RPM range
- Rotax 915 iS at 5,500 RPM cruise × Emrax 268 (5,000 RPM max) → borderline
- Requires ICE to operate in a narrow RPM band (constant-speed operation)
- Simplest mechanically, no reduction gear weight penalty

**Verdict:** Feasible with Rotax if the ICE is run at constant speed ~4,500–5,000 RPM via FADEC. The FADEC controls ICE RPM to hold generator output constant regardless of throttle demand, with electrical power output managed by the motor controllers.

### Option 2: Reduction Belt/Chain Drive
ICE → reduction ratio → generator.

- Allows ICE to operate at efficient RPM while generator operates at its optimal RPM
- Typical ratio: 1.5:1 to 2:1
- Weight penalty: 2–5 kg for belt drive system
- Adds complexity, maintenance point, potential failure mode
- Provides vibration isolation between ICE and generator

**Verdict:** Reasonable if direct drive creates RPM conflicts. Belt drive is the simplest reduction option.

### Option 3: Reduction Gearbox
ICE → gearbox → generator.

- Fixed ratio, compact, but heavier and more complex than belt
- Adds 5–10 kg
- Gear mesh introduces noise and vibration

**Verdict:** Not preferred for MAOS unless specific packaging constraints force it.

**Recommendation: Design for direct drive with Rotax 915 iS at constant-speed FADEC operation. Emrax 268 RPM limit is compatible. Evaluate belt reduction only if thermal testing shows the Emrax cannot sustain load at the required RPM.**

---

## Reopening the Voltage Question: 400V vs 800V

Decision D-001 closed the MAOS bus voltage at **400V DC**, citing automotive EV component alignment. That decision should be revisited in light of new reference data.

### What Samson Sky's 800V Choice Signals

The Samson Sky Switchblade — a production-intent flying car with a series hybrid drivetrain — chose **800V** for their Skybrid system. This is a directly comparable application: a high-performance experimental/LSA vehicle, series hybrid, axial-flux motors. Their engineering team made the 400V vs. 800V decision recently, with full knowledge of the automotive 400V ecosystem.

This is not a reason to automatically copy their decision, but it is a signal worth examining.

### The 800V Case

| Factor | 400V | 800V |
|---|---|---|
| Current at 75 kW | 187.5 A | 93.75 A |
| Cable cross-section | Larger | ~50% smaller |
| Cable weight (both buses) | Baseline | Significant reduction |
| Generator winding | More turns needed | Standard for axial-flux |
| Motor controller availability | Excellent (automotive EV) | Good (Hyundai E-GMP, Porsche Taycan ecosystem) |
| Safety engineering | Moderate | More stringent (>60V IEC threshold applies either way; >600V requires different approach) |
| Emrax compatibility | ✅ All models rated to 700V | ✅ All models rated to 700V |
| Beyond Aviation AXM3 | Unknown | Likely designed for 800V given Skybrid |

**Key insight on cable weight:** In an aircraft with generator in the wing and motors on the tail boom, the HV cables run the full length of the airframe — potentially 8–12 feet each. At 75 kW per motor:

- At 400V: ~188A → requires 35–50 mm² cable → approximately 0.5–0.7 kg per meter
- At 800V: ~94A → requires 16–25 mm² cable → approximately 0.25–0.35 kg per meter

Over a 3-meter cable run per bus, 800V saves approximately 1.5–2.5 kg per bus. For a four-cable system (two generators, two motors) the savings could be 6–10 kg total. Not enormous, but not trivial.

### The 400V Case

The original rationale holds: the 400V automotive EV ecosystem is larger, cheaper, and more accessible. Chevrolet Bolt, Nissan Leaf, older Tesla, most European EVs operate at 350–450V. Motor controllers, DC-DC converters, BMS systems, and pre-engineered battery packs are all widely available off-the-shelf.

800V components are available but thinner on the ground: Porsche Taycan, Hyundai/Kia E-GMP platform, Lucid Air. Growing, but not as deep a supplier bench for DIY applications.

### Recommendation

**Do not reclose this decision yet.** The Samson Sky data point warrants requesting a technical conversation with Evolito/Beyond Aviation to understand what voltage their AXM3 is designed for. If the AXM3 is optimized for 800V (which would explain Samson Sky's choice), and if MAOS uses AXM3s for both generators and motors, then 800V becomes the natural choice.

**If AXM3 is unavailable or not designed for 800V: stay at 400V** and use Emrax 268 as the generator baseline. The Emrax is rated to 700V and works at either bus voltage.

**Action item:** Contact Evolito with a technical inquiry. Ask specifically about AXM3 operating voltage, availability to experimental builders, pricing, and whether generator mode operation (ICE-driven) is a supported configuration.

---

## Generator BOM (Baseline: Emrax 268 × 2)

| Item | Specification | Qty | Est. Unit Cost | Est. Total | Source |
|---|---|---|---|---|---|
| **Emrax 268 (liquid cooled)** | 80 kW cont, 20.4 kg, 700V max | 2 | $12,000 | $24,000 | emrax.com / US distributors |
| **Motor controller (generator mode)** | Must support regen/generator mode at bus voltage | 2 | $2,500–$5,000 | $5,000–$10,000 | Unitek Bamocar, Sevcon, or equivalent |
| **Shaft coupling / flex disc** | ICE crankshaft to generator input | 2 | $200–$500 | $400–$1,000 | Rexnord, Lovejoy, custom |
| **Coolant lines and fittings** | Liquid-cooled Emrax integration | 2 sets | $150 | $300 | McMaster-Carr |
| **Generator mounting plate** | Wing rib integration, machined aluminum | 2 | $300–$500 | $600–$1,000 | Custom fabrication |
| **HV wiring (generator to bus)** | 35 mm² shielded HV cable + connectors | 2 runs | $300 | $600 | Belden / TE Connectivity |
| **Fusing / protection** | Pre-charge circuit, isolation contactor, fuse | 2 sets | $400 | $800 | Gigavac, TE |
| **Temperature sensors** | Stator winding thermal monitoring | 2 | $50 | $100 | Emrax-integrated or add-on |
| | | | **Subtotal** | **~$32,000–$38,000** | |

This is the two-generator cost for the electrical generation side only — does not include ICE engines, battery, motors, or motor controllers for the propulsion side.

---

## Architecture Standardization Opportunity

If Evolito engagement confirms the AXM3 is available and works as a generator:

**Four AXM3 units:**
- 2× in wings, ICE-driven (generators)
- 2× on tail boom, electrically driven (contra-rotating propulsion motors)

**Advantages:**
- Single machine type to design mounts, cooling, and wiring for
- One set of spare parts covers all four positions
- Controller firmware difference only (generator control vs. motor control)
- Every unit is interchangeable — a failed propulsion motor can be replaced with a spare from generator inventory

**Weight (estimated at AXM3 ~15 kg each):** 4 × 15 kg = 60 kg / 132 lbs for all four machines combined. This would be a significant weight advantage over any alternative architecture.

This is worth pursuing aggressively before finalizing the generator selection.

---

## Next Steps

1. **Contact Evolito** — Request AXM3 datasheet, operating voltage, generator mode support, pricing, and lead time for experimental builders
2. **Reopen voltage decision** — Hold pending Evolito response. If AXM3 is 800V-native, revisit D-001
3. **Emrax 268 bench test planning** — If AXM3 is unavailable, plan a bench test coupling an Emrax 268 to a Rotax 912 or 915 at constant-speed operation to validate direct drive RPM compatibility
4. **Controller selection** — Generator-mode controller selection is dependent on voltage decision. Identify candidates at both 400V and 800V now

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 0.1 Preliminary*

*Related articles:*
- [MAOS Generator Engine Comparison Matrix](/articles/2026-04-05-maos-engine-comparison-matrix/)
- [MAOS Propulsion Redundancy Architecture and Battery Selection](/articles/2026-04-05-maos-propulsion-redundancy-battery/)
