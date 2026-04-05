---
title: "MAOS Propulsion Architecture Decision: 1G+1B+2M"
date: 2026-04-05T18:00:00-06:00
description: "MAOS selects the 1G+1B+2M series hybrid architecture: one ICE generator engine, one battery pack, two independent electric propulsion motors. Power budget, failure mode analysis, and component direction."
tags: ["propulsion", "design-decisions", "hybrid-electric", "electric-aviation", "analysis", "systems"]
author: "MAOS Design Board"
summary: "After analyzing conventional twin, premium hybrid, and budget hybrid alternatives, MAOS selects 1G+1B+2M: a single ICE generator engine, one battery pack, and two independent contra-rotating electric motors. The architecture provides three independent degradation layers before total propulsion loss, fits the experimental builder budget, and enables the pod-and-boom configuration."
project: "maos"
article_type: "design"
draft: false
---

## Decision

**MAOS propulsion architecture: 1G + 1B + 2M**

- **1G** — One ICE generator engine, ~160–200 hp, running at constant speed and load
- **1B** — One battery pack, ~40 kWh, sized for 30-minute emergency reserve
- **2M** — Two independent electric propulsion motors, contra-rotating, on the tail boom

This decision closes the propulsion architecture question. The reasoning follows.

---

## Power Flow

```
[ICE Engine — constant speed]
         |
   [Generator / AFPM]
         |
   [400V DC Bus]
      |       |
 [Battery]  [Load]
  contactor
      |
   [400V DC Bus continued]
         |
   +-----------+
   |           |
[Ctrl 1]   [Ctrl 2]
   |           |
[Motor 1]  [Motor 2]
   |           |
[Fwd Prop] [Aft Prop]
 (contra-rotating, coaxial)
```

The battery connects to the bus in **parallel**, not in series. It is a reservoir, not a gateway. Generator power flows to the motors whether or not the battery is engaged. This matters enormously for the failure analysis.

---

## Why Not 2G?

Two generator engines provide better redundancy — one engine failure becomes a managed abnormal rather than an emergency. The analysis showed this is the right answer for a demanding IFR aircraft flown regularly over inhospitable terrain.

It is not the right answer for MAOS Phase 1.

**Two Rotax 915 iS engines cost ~$90,000 before a single electrical component is purchased.** The entire drivetrain at premium component prices reaches $190,000+. For an experimental homebuilt, that is not a viable budget. The architecture exists to enable a novel aircraft, not to replace a certified twin at twice the price.

The 30-minute battery reserve after ICE failure is acceptable for the intended mission. It is a genuine emergency with a clear, procedurally manageable resolution — not certain doom. After landing, the beer is well-earned.

The 2G architecture remains the right long-term development path. If MAOS proves out the design and a second aircraft is built, upgrading to 2G changes the ICE engine, mountings, and generator — the bus, motors, battery, and airframe are unchanged.

---

## Power Budget

Assumptions: MTOW 2,600 lbs, 155 KTAS cruise, L/D 14 at cruise, drivetrain efficiency 0.84 (generator × controller × motor).

| Operating Condition | Shaft Power at Prop | ICE Required | Battery Contribution |
|---|---|---|---|
| Cruise (155 KTAS) | 80 kW / 108 hp | **96 kW / 128 hp** | None — ICE has 32 hp margin, recharging |
| Climb 700 fpm @ 120 KIAS | 101 kW / 135 hp | **120 kW / 161 hp** | ~1 kW — effectively zero |
| Climb 1,000 fpm @ 120 KIAS | 119 kW / 160 hp | **141 kW / 189 hp** | 18 kW electrical — negligible vs. 40 kWh reserve |
| Climb 1,200 fpm @ 120 KIAS | 131 kW / 175 hp | **155 kW / 208 hp** | 30 kW electrical — minor |

**Key finding:** A 160 hp ICE handles 700 fpm climb solo and comfortably covers cruise with margin to spare. Battery contribution to climb is small relative to the reserve capacity — at 1,000 fpm, 24 kWh usable sustains the battery boost draw for over an hour. In practice, climb typically lasts 15–25 minutes. The battery barely notices it.

At cruise, the 32 hp of surplus generator capacity goes into recharging the battery. The battery arrives at cruise altitude near-full and stays there.

---

## Graceful Degradation — The Full Failure Ladder

Because the battery is a parallel tap, not a series component, failure of any single element produces a degraded-but-flyable outcome in most cases:

| Failure Event | Operational Mode | Capability | Action |
|---|---|---|---|
| **Normal** | Full hybrid | All power available, battery buffer active | None |
| **Battery failure / isolation** | Generator-direct | Cruise power, stable voltage, no peaks, no emergency reserve | Land soon — precautionary |
| **ICE / Generator failure** | Battery-only | 30 min at 60 kW emergency power | Declare emergency, nearest suitable runway |
| **Single motor failure** | One motor | ~60% thrust, degraded climb, reduced cruise speed | Emergency — land with power at nearest suitable airport |
| **Battery fail + single motor** | Generator → one motor | Reduced thrust, no reserve | Land as soon as practical |
| **ICE fail + single motor** | Battery → one motor | 30 min, reduced thrust | Emergency — 30 min is still 30 min |
| **Both motors fail** | None | Glide | Emergency descent |
| **ICE fail + both motors fail** | None | Glide | Emergency descent |

Two simultaneous independent failures are required before the aircraft becomes a glider. That is a reasonable safety profile for an experimental aircraft operated under IFR.

### The Battery Bypass in Detail

When the battery contactor opens — whether due to battery fault detection, manual isolation, or BMS protection — the generator continues to power the motors directly. This works because:

1. The ICE runs at **constant RPM** for generator duty, producing stable, well-regulated DC output
2. The motor controllers have a wide input voltage acceptance range (typ. ±20% of bus voltage)
3. Voltage sag under load is manageable when the generator is properly sized — at cruise the generator has 32 hp of margin, more than enough to hold bus voltage under motor load

What changes without the battery: rapid load transients (sudden throttle demands, turbulence response) are no longer smoothed by the battery's capacitance. The motor controllers manage this by limiting ramp rates in generator-direct mode — response is slightly slower but perfectly adequate for normal flight.

This is not a workaround. It is a designed operating mode.

---

## Component Direction

### ICE Generator Engine

**Primary candidate: Rotax 916 iS (160 hp / 118 kW)**

At constant-speed generator duty:
- 128 hp needed for cruise — 32 hp margin available for battery charging
- 700 fpm climb handled solo
- 1,000 fpm climb requires modest battery supplement
- Known reliability, experimental builder support network, liquid-cooled (waste heat available for ECS)
- Cost: ~$50,000 new

**Budget candidate: Large-displacement motorcycle engine (Hayabusa / ZX-14R class, turbocharged)**

- 1,340–1,441cc, 190–208 hp stock, ~$3,000–5,000 used
- Generator duty (constant RPM, constant load) is less demanding than motorcycle use
- Requires engineering: cooling reroute, FADEC/ECU conversion, mount design
- Proven precedent: Viking Aircraft Engines (Honda car engine → aircraft, $14–18k installed)
- Requires a dedicated bench test and development program

The motorcycle engine path is not off the table. It is the right economic answer *if* the engineering work is treated as a real project and not an assumption. The Rotax is the right answer if budget allows and build schedule is the priority.

### Battery Pack

**Target: 40 kWh, NMC chemistry**

- LFP: Too heavy at 706 lbs for 40 kWh. Possible if power level or reserve time is reduced.
- NMC 811: ~441 lbs for 40 kWh. Challenging but viable.
- NCA: ~410 lbs. Better.
- Silicon-anode NMC (Amprius): ~353 lbs. Best available today, limited supply.
- Donut Lab solid-state: ~220–275 lbs if specs hold. Monitor for production availability.

**Planning basis: NMC 811, 40 kWh, ~441 lbs.** Design the battery bay to accept this weight. If lighter chemistry becomes available before build, the same bay works.

The battery weight is the most significant open variable in the MAOS weight budget. At 441 lbs it consumes roughly 35% of the 1,200 lb useful load target. This forces one of:
- Accepting a 3-seat + fuel mission rather than 4-seat
- Reducing emergency reserve (shorter battery time at same power)
- Reducing emergency power level (longer time, lower power)
- Waiting for better battery chemistry

This is an open design question. It is not a reason to abandon the architecture.

### Propulsion Motors

**Candidate: Emrax 228 × 2 (50 kW continuous each)**

- Two motors × 50 kW continuous = 100 kW combined
- This is below the 120–130 kW cruise target
- Gap closed by battery contribution and/or accepting slightly reduced cruise speed
- Weight: 12.3 kg / 27 lbs each = 24.6 kg / 54 lbs both motors combined
- Cost: ~$8,000 each / $16,000 total
- Maximum voltage: 700V — compatible with both 400V and 800V bus options

**Better candidate if available: Beyond Aviation AXM3 × 2**

- ~100 kW continuous each (estimated)
- ~15 kg each / 30 kg total — significantly lighter than Emrax
- Used in Samson Sky Skybrid — real-world aviation validation
- Voltage not publicly confirmed — Samson Sky's 800V choice suggests 800V-native design
- Availability and pricing require direct Evolito engagement

**Action item:** Contact Evolito before finalizing motor selection and bus voltage. The answer may determine whether MAOS operates at 400V or 800V.

---

## What This Architecture Is and Is Not

**It is:**
- A single-engine aircraft with exceptional emergency reserve
- A genuine series hybrid with full battery buffer (unlike Samson Sky's generator-direct Skybrid)
- A design that enables the pod-and-boom configuration through electrical power transmission
- Accessible to an experimental builder at a defensible budget
- Upgradeable to 2G without changing the airframe, bus, motors, or battery

**It is not:**
- A multi-engine aircraft in the regulatory sense
- A match for the redundancy profile of a certified twin
- The final word on the 400V vs. 800V decision
- Ready to close on ICE engine selection (Rotax vs. motorcycle engine path requires a decision)

---

## Cost Summary (Rotax Path)

| Component | Qty | Est. Cost | Total |
|---|---|---|---|
| Rotax 916 iS | 1 | $50,000 | $50,000 |
| Generator (Emrax 268, AFPM) | 1 | $12,000 | $12,000 |
| Motor controllers (generator mode) | 1 | $4,000 | $4,000 |
| Propulsion motors (Emrax 228) | 2 | $8,000 | $16,000 |
| Motor controllers (motor mode) | 2 | $4,000 | $8,000 |
| 40 kWh battery pack (NMC) | 1 | $20,000 | $20,000 |
| BMS, wiring, switchgear, protection | — | — | $8,000 |
| Contra-rotating propeller | 1 | $8,000 | $8,000 |
| Reduction drive, coupling, mount | 1 | $3,000 | $3,000 |
| Contingency (10%) | — | — | $12,900 |
| **Total** | | | **~$142,000** |

## Cost Summary (Motorcycle Engine Path)

| Component | Qty | Est. Cost | Total |
|---|---|---|---|
| Hayabusa / ZX-14R (used, low miles) | 1 | $4,500 | $4,500 |
| Engine conversion (cooling, ECU, mount) | — | — | $4,000 |
| Generator (Emrax 228 or equivalent) | 1 | $8,000 | $8,000 |
| Motor controllers (generator mode) | 1 | $2,500 | $2,500 |
| Propulsion motors (Emrax 228) | 2 | $8,000 | $16,000 |
| Motor controllers (motor mode) | 2 | $2,500 | $5,000 |
| 40 kWh battery pack (NMC) | 1 | $20,000 | $20,000 |
| BMS, wiring, switchgear, protection | — | — | $8,000 |
| Contra-rotating propeller | 1 | $8,000 | $8,000 |
| Reduction drive, coupling, mount | 1 | $2,000 | $2,000 |
| Contingency (10%) | — | — | $7,800 |
| **Total** | | | **~$86,000** |

---

## Open Items Before Architecture Is Fully Closed

1. **Bus voltage** — 400V or 800V. Hold pending Evolito AXM3 inquiry.
2. **ICE engine path** — Rotax 916 iS vs. motorcycle engine conversion. Cost vs. schedule vs. risk tradeoff.
3. **Battery weight** — 441 lbs at NMC 811 needs to clear the weight budget before committing to 40 kWh.
4. **Motor selection** — Emrax 228 (available now) vs. AXM3 (pending Evolito response).

---

*Decision recorded by MAOS Design Board — 2026-04-05*

*Related articles:*
- [MAOS Drivetrain Economics](/articles/2026-04-05-maos-drivetrain-economics/)
- [MAOS Propulsion Redundancy Architecture and Battery Selection](/articles/2026-04-05-maos-propulsion-redundancy-battery/)
- [MAOS Generator Selection: Axial-Flux Machines and the 400V vs 800V Decision](/articles/2026-04-05-maos-generator-selection/)
- [MAOS Generator Engine Comparison Matrix](/articles/2026-04-05-maos-engine-comparison-matrix/)
