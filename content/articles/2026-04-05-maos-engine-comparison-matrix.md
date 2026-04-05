---
title: "MAOS Generator Engine Comparison Matrix"
date: 2026-04-05T10:00:00-06:00
description: "Systematic evaluation of 13 ICE engines for the MAOS generator drive application, covering both single and twin-engine variants."
tags: ["propulsion", "analysis", "design-decisions", "weight-budget", "hybrid-electric", "electric-aviation"]
author: "PROPULSION, MAOS Design Board"
summary: "The PROPULSION agent evaluated 13 ICE engines against eight criteria for the MAOS generator drive application. Rotax 915 iS and 916 iS lead for the twin variant; Flygas GAS 418S is the highest power-to-weight option pending cost and availability confirmation."
project: "maos"
article_type: "analysis"
draft: false
---

## Overview

**Version:** 0.1 Preliminary
**Date:** 2026-04-03
**Owner:** PROPULSION
**Purpose:** Evaluate ICE generator engine options for MAOS, covering both SINGLE (one engine, 75 kW generator) and TWIN (two engines, 150 kW total) variants.

---

## Selection Criteria

For the MAOS generator application, each engine is evaluated against eight criteria:

1. **Continuous power:** 75 kW (100 hp) minimum for generator head drive
2. **Weight:** Lighter is better — target < 65 kg / 143 lbs per engine
3. **Power-to-weight:** > 1.5 hp/kg preferred
4. **Cooling:** Liquid-cooled (required for waste heat harvesting)
5. **Reliability:** Proven in aviation or high-duty applications
6. **Fuel:** Mogas capable — 100LL avgas not required
7. **Cost:** Reasonable for experimental aircraft budget
8. **Availability:** Lead time < 6 months, vendor responsive

---

## Engine Comparison Matrix

| Engine | Displacement | Power (hp/kW) | Weight (kg) | HP/kg | Cooling | Fuel | Aviation Use | Cost Est. | Status |
|--------|-------------|---------------|-------------|-------|---------|------|--------------|-----------|--------|
| **Flygas GAS 418S** | 1,800 cc | 180 hp / 132 kW @ 5,800 RPM | < 85 kg | 2.2 | Liquid | 98 octane / mogas | UAV, experimental | €20k–30k (est) | ✅ Viable |
| **UL Power UL520iS** | 3,120 cc | 200 hp / 147 kW @ 5,800 RPM | ~118 kg | 1.7 | Liquid (heads) / Air (cylinders) | Mogas | Dark Aero 1, certified kits | $45k–55k | ✅ Viable |
| **Kawasaki I4 Turbo** | ~1,000 cc | 148 hp / 110 kW cont | 130–140 kg installed | 1.1–1.14 | Liquid | Mogas + FADEC | Experimental, aviation derivatives | $15k–25k (est) | ✅ Viable |
| **Rotax 912 iS** | 1,352 cc | 100 hp / 73.5 kW @ 5,800 RPM | 72 kg | 1.39 | Liquid (heads) / Air (cylinders) | Mogas (91 octane min) | Widely used LSA/experimental | $28k–32k | ✅ Viable |
| **Rotax 915 iS** | 1,352 cc | 141 hp / 103.5 kW @ 5,800 RPM | 83 kg | 1.70 | Liquid (heads) / Air (cylinders) | Mogas (91 octane min) | LSA/experimental, certified | $42k–48k | ✅ Viable |
| **Rotax 916 iS** | 1,352 cc | 160 hp / 118 kW @ 5,800 RPM | ~85 kg | 1.88 | Liquid (heads) / Air (cylinders) | Mogas (91 octane min) | New (2023+), certified | $50k+ | ✅ Viable |
| **Viking 130** | 1,500 cc | 130 hp / 97 kW cont | 108 kg dry | 1.20 | Liquid | Mogas | Experimental, Honda-based | $14k–18k | ✅ Viable |
| **Aeromomentum AM13** | 1,300 cc | 100 hp / 73.5 kW @ 5,500 RPM | 68 kg | 1.47 | Liquid | Mogas (Suzuki base) | Experimental | $12k–16k | ✅ Viable |
| **Aeromomentum AM15** | 1,500 cc | 115 hp / 84.5 kW @ 5,500 RPM | 75 kg | 1.53 | Liquid | Mogas (Suzuki base) | Experimental | $14k–18k | ✅ Viable |
| **Hirth F-30** | 1,494 cc | 85 hp / 62 kW @ 6,500 RPM | 62 kg | 1.37 | Liquid | Mogas | Ultralight, experimental | €12k–16k | ⚠️ Marginal |
| **Honda CB650 (modified)** | 2,596 cc | 67 hp / 50 kW (stock) | 140–160 kg installed | 0.42–0.48 | Liquid | Mogas | None — motorcycle base | $7k–12k + mods | ⚠️ Marginal |
| **Honda CB500 (modified)** | 942 cc | 47 hp / 35 kW (stock) | 130–150 kg installed | 0.31–0.36 | Liquid | Mogas | None — motorcycle base | $5k–10k + mods | ⚠️ Marginal |
| **Hirth F-23** | 1,006 cc | 50 hp / 37 kW @ 6,500 RPM | 45 kg | 1.11 | Liquid | Mogas | Ultralight, experimental | €8k–12k | ❌ Disqualified |

---

## Analysis by Category

### Top Candidates

**Flygas GAS 418S** — 180 hp, 2.2 hp/kg, liquid-cooled, aviation-designed

The highest power-to-weight ratio in the matrix. Supercharged for altitude performance. Designed for aviation (UAV/experimental), not adapted from a ground vehicle. Primary unknowns are US availability and exact pricing.

**Rotax 916 iS** — 160 hp, 1.88 hp/kg, turbocharged, certified

The premium choice. Proven reliability, extensive experimental support network, certified basis, excellent altitude performance. Most expensive at $50k+. Best fit for the SINGLE variant where only one engine is required.

**Rotax 915 iS** — 141 hp, 1.70 hp/kg, turbocharged, certified

Strong balance of power, cost, and reliability. Proven in LSA and experimental fleets. Exceeds the 75 kW continuous target with meaningful margin. Solid choice for both variants.

**UL Power UL520iS** — 200 hp, 1.7 hp/kg (Dark Aero's engine)

Used in the Dark Aero 1. Heavier (118 kg) and expensive ($45–55k) — arguably overspecified for a 75 kW generator drive. Primary value may be in cooling system design and installation technique precedent from the Dark Aero build.

**Rotax 912 iS** — 100 hp, 1.39 hp/kg

The most widely-used experimental engine. Proven, well-supported, lowest cost among certified options. Barely meets the 75 kW target — no margin. Conservative choice; adequate but not preferable.

**Viking 130** — 130 hp, 1.20 hp/kg, Honda-based conversion

Proven in the experimental market. Reasonable cost ($14–18k). At 108 kg dry it exceeds the PROPULSION-SLA weight target and requires negotiation with the weight budget. Good budget-conscious option.

**Kawasaki I4 Turbo** — 148 hp, 1.1–1.14 hp/kg

Meets power requirements. FADEC included. However, at 130–140 kg installed, this is the heaviest option in the viable category. This engine was the original Kawasaki candidate that generated the STRUCTURES weight objection in Board Meeting 001 — the weight penalty is confirmed significant.

### Marginal Candidates

**Aeromomentum AM15** — 115 hp, 1.53 hp/kg — Meets power, but limited aviation track record. Budget option.

**Aeromomentum AM13** — 100 hp, 1.47 hp/kg — Marginally meets power target. Lightweight and low cost, but less proven.

**Hirth F-30** — 85 hp, 1.37 hp/kg — Underpowered at 62 kW vs. 75 kW target. Very light (62 kg). Not viable for MAOS generator drive.

**Honda CB500/CB650 (modified)** — Both severely underpowered and produce poor power-to-weight when installed weight is accounted for. No aviation pedigree. Not suitable.

### Disqualified

**Hirth F-23** — 37 kW continuous, 50% below the minimum requirement. No path to 75 kW in this platform.

---

## Recommendation Matrix

### SINGLE Variant — 1× Engine, 75 kW Generator

| Priority | Engine | Rationale |
|----------|--------|-----------|
| Best Overall | Rotax 916 iS | Premium, proven, certified, excellent support |
| Best Value | Rotax 915 iS | Proven, certified, balance of cost/performance |
| High Performance | Flygas GAS 418S | Highest power-to-weight — pending cost/availability |
| Budget | Viking 130 | Proven experimental, meets power, over weight target |
| Conservative | Rotax 912 iS | Widest support base, barely adequate power |

### TWIN Variant — 2× Engines, 150 kW Total

| Priority | Engine | Rationale |
|----------|--------|-----------|
| Best Overall | Rotax 915 iS (2×) | Proven, certified, good power-to-weight |
| High Performance | Flygas GAS 418S (2×) | Excellent power-to-weight — cost unknown |
| Best Value | Viking 130 (2×) | Lower cost, proven experimental, over weight SLA |
| Budget | Aeromomentum AM15 (2×) | Meets power, low cost, less proven |

---

## Weight Budget Impact

Engines within the PROPULSION-SLA target of 65 kg / 143 lbs per engine:

| Engine | Weight (kg) | Weight (lbs) | vs. SLA Target |
|--------|-------------|--------------|---------------|
| Flygas GAS 418S | < 85 kg | < 187 lbs | Over — requires SLA negotiation |
| Rotax 916 iS | ~85 kg | ~187 lbs | Over — requires SLA negotiation |
| Rotax 915 iS | 83 kg | 183 lbs | Over — requires SLA negotiation |
| Rotax 912 iS | 72 kg | 159 lbs | Over — minor |
| Aeromomentum AM13 | 68 kg | 150 lbs | Over — minor |
| Aeromomentum AM15 | 75 kg | 165 lbs | Over — minor |
| Hirth F-30 | 62 kg | 137 lbs | ✅ Under — but underpowered |
| Viking 130 | 108 kg | 238 lbs | Over — significant |
| Kawasaki I4 Turbo | 130–140 kg | 286–308 lbs | Over — disqualifying |

> Note: The original Honda motorcycle engine architecture that triggered the power/weight conflict in Board Meeting 001 is confirmed inadequate. The Kawasaki alternative that was the competing option is among the heaviest viable candidates. The Rotax family represents the practical center of the trade space.

---

## Next Steps

1. **Contact vendors for quotes:** Flygas (US availability, pricing, lead time), Rotax distributors (915 iS and 916 iS), Viking Aircraft Engines
2. **Investigate Flygas supercharger kits:** Flygas offers supercharger/intercooler kits for Rotax 912/914 — evaluate as an alternative path to high-altitude performance at lower cost
3. **Validate generator interface:** Confirm 75 kW continuous against Beyond Motors AXM2 generator head specifications and RPM requirements for reduction gear selection
4. **Variant selection dependency:** Engine selection and variant selection (SINGLE vs. TWIN) are coupled decisions — both must close before detailed structural design can begin

---

*Analysis by PROPULSION, MAOS Design Board*
*Version 0.1 Preliminary — updated as vendor quotes and analysis progress*

*MAOS Project — Mobile Aviation Operating System*
*Four-seat experimental aircraft, FAA Amateur-Built category*
