---
title: "MAOS Propulsion Redundancy Architecture and Battery Selection"
date: 2026-04-05T16:00:00-06:00
description: "Defining what 'engine failure' means in a series hybrid, evaluating six redundancy architectures, and comparing battery chemistries for the 30-minute emergency reserve requirement."
tags: ["propulsion", "analysis", "design-decisions", "hybrid-electric", "electric-aviation", "safety", "weight-budget", "motors"]
author: "AeroCommons Design Board"
summary: "In a series hybrid, the motor is the new single point of failure — not the ICE. This article evaluates six redundancy architectures, sizes the 30-minute emergency battery reserve, and compares five battery chemistries by weight, safety, and sourcing. The analysis converges on a specific architecture recommendation."
project: "maos"
article_type: "analysis"
draft: false
---

## The Question That Won't Resolve Without Being Named

Is the MAOS a single-engine aircraft or a multi-engine aircraft?

In a conventional airplane, this is easy: count the propellers. One propeller, one engine, single-engine. Two propellers, two engines, twin.

In a series hybrid, that question falls apart. The ICE engines don't turn the propeller. The electric motors do. The ICE engines turn generators. The generators charge the bus. The bus powers the motors. You can have two ICE engines and one motor. You can have one ICE engine and two motors. You can add a battery that provides no thrust on its own but buys you thirty minutes of power if every other component fails.

What constitutes an "engine failure?" What provides safety?

This article answers those questions, evaluates six architectures, and uses the answers to size and select a battery.

---

## Section 1: Rethinking the Failure Tree

In a conventional twin, the failure tree is simple:

```
Engine 1 fails → Engine 2 continues → Fly on one engine → Land
Engine 2 fails → Engine 1 continues → Fly on one engine → Land
Both fail       → Glide → Emergency landing
```

In a series hybrid, the failure tree is different:

```
[ICE Gen 1] ──→ [Rectifier] ──→
                               [DC Bus] ──→ [Controller] ──→ [Motor] ──→ [Propeller]
[ICE Gen 2] ──→ [Rectifier] ──→              ↑
                                          [Battery]
```

Each box is a potential failure point. But they are not equal.

**The motor is the new critical single point of failure.**

In a conventional twin, losing one engine doesn't affect the other engine's propeller. The propellers are mechanically independent. In a series hybrid with one motor, losing that motor — regardless of how many ICE generators are running — produces complete propulsion loss. Immediately. No degraded performance. No asymmetric thrust to manage. No continued flight.

In a conventional twin, you fear the engine. In a series hybrid, you fear the motor.

This reframes the architecture problem entirely.

### What "Failure" Means in Each Component

| Component | Failure Mode | Propulsion Result | Recovery |
|-----------|-------------|-------------------|----------|
| ICE Gen 1 | Fuel, mechanical, electrical | Bus loses one supply; battery buffers | Fly on Gen 2 + battery |
| ICE Gen 2 | Same | Same | Fly on Gen 1 + battery |
| Both ICE Gens | Simultaneous failure, fuel | Bus has battery only | 30-min emergency battery reserve |
| Battery | Cell short, BMS fault | Buffer gone; generators must carry all loads | Reduced tolerance for load spikes |
| Motor Controller | Semiconductor failure | Motor stops | Depends on architecture |
| Motor | Winding, bearing | Motor stops | Depends on architecture |
| Propeller | Blade, hub | Thrust lost (may also damage motor if uncontrolled) | Depends on architecture |

The critical insight: **ICE generator failures are graceful. Motor failures are not.**

A two-generator aircraft that loses one generator is still flying, with a battery buffer and one generator running. That's a manageable emergency with a long solution window.

A single-motor aircraft that loses its motor — with both generators running perfectly, battery fully charged — is a glider. Immediately.

---

## Section 2: The Six Architectures

### Notation

- **G** = ICE-Generator unit (engine + generator + rectifier as one failure unit)
- **B** = Battery pack (independent energy storage)
- **M** = Motor + controller (one propulsion channel)
- **CR** = Contra-rotating (two coaxial propellers, two motors on same axis)

### Architecture 1: 2G + 1B + 1M

```
G1 ──┐
     ├──→ [DC Bus] ──→ M1 ──→ Prop
G2 ──┘         ↑
               B
```

**Single G failure:** G2 + B continue. Full power available unless battery limited. ✅
**Both G failure:** B alone → 30-min emergency power. ✅
**M1 failure:** Complete propulsion loss. Aircraft is a glider. ❌ **CRITICAL**
**B failure:** G1+G2 only. Narrow margin for load spikes. ⚠️

**Verdict:** The motor is the single point of failure. Two generators provide no protection against the worst failure mode. This architecture feels like a twin but isn't. Not recommended for IFR mountain operations.

---

### Architecture 2: 2G + 1B + 2M (Coaxial Contra-Rotating)

```
G1 ──┐
     ├──→ [DC Bus] ──→ M1 (fwd prop) ──┐
G2 ──┘         ↑                       ├→ [Coaxial shaft]
               B    ──→ M2 (aft prop) ──┘
```

**Single G failure:** G2 + B → Full power to both motors. ✅
**Both G failure:** B → Both motors at emergency power. ✅
**M1 failure:** M2 continues alone → ~50% thrust. Aircraft can still fly. ✅
**M2 failure:** M1 continues alone → ~50% thrust. ✅
**Both M failure:** Complete propulsion loss. Extremely unlikely (independent failure modes). ✅
**B failure:** G1+G2 share bus, reduced resilience. ⚠️

**Verdict:** This is the architecture. Two coaxial motors on the same axis provide propulsion redundancy with no asymmetric thrust problem — no multi-engine rating required, no dead-leg control issue. The failure modes are manageable at every single node.

**Penalty:** Second motor + controller weight. Roughly 15–25 kg (33–55 lbs) additional.

---

### Architecture 3: 2G + 2B (Split Bus) + 2M (Coaxial)

```
G1 ──→ [Bus A] ──→ M1 (fwd prop)
            ↑
            B1

G2 ──→ [Bus B] ──→ M2 (aft prop)
            ↑
            B2
[Bus Tie (normally open)]
```

**Single G failure:** Affected bus runs on its battery. Bus tie can connect buses if needed. ✅
**Single B failure:** Affected bus loses buffer; generator carries it. ✅
**Both G failure:** B1 + B2 each power their motor. Maximum isolation. ✅
**Single M failure:** Remaining motor on its bus. ✅

**Verdict:** Maximum redundancy. Every single node can fail without complete propulsion loss (except propeller). Avionics buses work exactly this way. The penalty is weight and system complexity — two battery packs with a managed bus tie, two independent motor controllers, and the control logic to manage cross-connect without cascade failure.

**This architecture is where 2G + 1B + 2M grows when you want one more layer of protection.**

---

### Architecture 4: 2G + 1B (Small Buffer) + 2M (Coaxial)

Same as Architecture 2 but with battery sized only as a transient buffer (not a 30-minute emergency reserve). Battery is ~5–10 kWh rather than 30 kWh. Weight savings significant.

**Both G failure:** Small buffer → 5–10 minutes only. Not enough to reach alternate or complete IFR approach. ❌ **under the stated 30-minute requirement**
**Single G failure:** Remaining G + buffer → OK. ✅

**Verdict:** Viable only if the operational profile doesn't require 30-minute battery reserve. Rejected based on Bill's stated requirement.

---

### Architecture 5: 1G + 1B + 2M (Coaxial)

```
G1 ──→ [DC Bus] ──→ M1 + M2
            ↑
            B
```

**G1 failure:** Battery only → 30-min emergency. ✅ (per requirement)
**M1 failure:** M2 continues at ~50% thrust. ✅
**B failure:** G1 alone, no buffer. Manageable. ⚠️

**Verdict:** True single-engine aircraft. One generator is a single point of failure for sustained flight. The battery covers the reserve requirement. Simpler, lighter than 2-generator options. Appropriate only if the mission profile accepts that a generator failure begins the clock on a 30-minute emergency.

---

### Architecture 6: 1G + 1B + 1M

**G failure:** Battery only → 30 min, then glider. ❌
**M failure:** Immediate glider. ❌

**Verdict:** Rejected. Compounding single points of failure.

---

### Architecture Comparison Matrix

| Architecture | Single G Fail | Both G Fail | Single M Fail | B Fail | Practical Weight Penalty | Recommendation |
|---|---|---|---|---|---|---|
| **2G + 1B + 1M** | Fly ✅ | Battery ✅ | Glider ❌ | Marginal ⚠️ | Baseline | ❌ Motor SPOF |
| **2G + 1B + 2M** | Fly ✅ | Battery ✅ | 50% thrust ✅ | Marginal ⚠️ | +15–25 kg | ✅ **Recommended baseline** |
| **2G + 2B + 2M** | Full ✅ | Split battery ✅ | 50% ✅ | Isolated ✅ | +25–40 kg | ✅ Maximum redundancy |
| **2G + Small B + 2M** | Fly ✅ | <10 min ❌ | 50% ✅ | Marginal ⚠️ | -Weight | ❌ Under reserve requirement |
| **1G + 1B + 2M** | Battery ✅ | N/A | 50% ✅ | Marginal ⚠️ | Minimum | ⚠️ Single ICE risk |
| **1G + 1B + 1M** | Battery ✅ | N/A | Glider ❌ | Marginal ⚠️ | Minimum | ❌ Rejected |

**Baseline recommendation: 2G + 1B + 2M (coaxial contra-rotating)**

This is the architecture that matches the original MAOS concept — two generator engines in the wing — with the addition of an explicit second motor on the tail boom axis. It provides:
- Graceful degradation at every node
- No asymmetric thrust complication
- True equipment redundancy equivalent to a conventional twin in practical terms
- 30-minute emergency reserve from the battery if both generators fail

---

## Section 3: The 30-Minute Battery — What Power Level?

"30 minutes of battery power" is meaningless without defining the scenario.

**Scenario: Both generators fail. Aircraft is at flight altitude in IMC.**

What does the pilot need to do?
1. Maintain controlled flight immediately — cannot lose speed or altitude control
2. Execute emergency descent from up to 20,000 ft
3. Navigate to an airport or VMC conditions
4. Execute an approach and landing

What power does this require?

| Flight Phase | Power Required | Rationale |
|---|---|---|
| Controlled descent (best glide + power) | 30–40 kW | Maintain airspeed, gentle descent rate |
| Maneuvering for approach | 40–60 kW | Speed control, configuration |
| Final approach and go-around capability | 50–75 kW | Full approach power, missed approach margin |
| **Conservative sizing basis** | **60 kW continuous** | Maintains full IFR approach capability throughout |

**Battery energy calculation for 30 minutes at 60 kW:**

```
Required shaft energy:   60 kW × 0.5 hr = 30 kWh
Motor efficiency:        92%
Controller efficiency:   97%
Battery discharge eff:   97%
                         ________________________
Battery energy needed:   30 / (0.92 × 0.97 × 0.97) = 34.5 kWh → round to 35 kWh
```

This is the battery sizing target: **35 kWh usable capacity.**

Add 10–15% for depth-of-discharge margin (don't cycle to 0% — kills cells quickly):

**Pack capacity required: ~40 kWh**

---

## Section 4: Battery Technology Comparison

### Cell-Level Chemistry Comparison

| Chemistry | Cell Specific Energy | Pack Specific Energy (est.) | Specific Power | Cycle Life | Temperature Range | Thermal Runaway Risk | Notes |
|---|---|---|---|---|---|---|---|
| **LFP** (LiFePO₄) | 150–180 Wh/kg | 110–140 Wh/kg | Moderate | 2,000–6,000 cycles | −20°C to +60°C (reduced below 0°C) | Very low — no oxygen release | Gold standard for safety. Heavy. |
| **NMC 622/811** | 200–270 Wh/kg | 160–210 Wh/kg | High | 800–2,000 cycles | −30°C to +55°C | Moderate | Mainstream EV chemistry. Best energy/weight balance. |
| **NCA** | 250–300 Wh/kg | 190–230 Wh/kg | High | 1,000–2,000 cycles | −30°C to +55°C | Moderate | Tesla's original chemistry. High energy density. Less common outside Tesla ecosystem. |
| **NMC w/ Silicon Anode** | 300–400 Wh/kg | 230–280 Wh/kg | High | 500–1,500 cycles | −20°C to +55°C | Moderate | Amprius, Enovix. Highest specific energy available. Short cycle life. Not widely available. |
| **Donut Lab (Solid-State)** | **400 Wh/kg (claimed)** | Unknown — no pack data published | Claimed very high (5-min charge) | 100,000 cycles (claimed) | −30°C to 100°C (claimed, 99% retention) | None claimed — all solid-state | See note below. Verified in Verge motorcycles. No voltage, capacity, dimensions, or pricing published. Specs are controversial. |
| **Li-S** (Lithium-Sulfur) | 400–600 Wh/kg (theoretical) | Not yet practical | Low | <500 cycles | Research phase | Low | Too early for this application. Watch for 2028+ products. |

### Weight for 40 kWh Pack

| Chemistry | Pack Specific Energy | Pack Weight for 40 kWh | Weight in lbs |
|---|---|---|---|
| LFP | 125 Wh/kg | **320 kg** | **706 lbs** |
| NMC 622 | 175 Wh/kg | **229 kg** | **505 lbs** |
| NMC 811 | 200 Wh/kg | **200 kg** | **441 lbs** |
| NCA | 215 Wh/kg | **186 kg** | **410 lbs** |
| Silicon-anode NMC | 250 Wh/kg | **160 kg** | **353 lbs** |
| Donut Lab (if 400 Wh/kg is pack-level) | 400 Wh/kg | **100 kg** | **220 lbs** |
| Donut Lab (if 400 Wh/kg is cell-level, ~80% pack efficiency) | 320 Wh/kg | **125 kg** | **275 lbs** |

The Donut Lab figures — if the specific energy claim holds at pack level — would reduce the 40 kWh emergency reserve to **220 lbs**, which is a fundamentally different weight conversation. Even the conservative cell-level interpretation lands at **275 lbs**, better than any conventional chemistry above. The catch: no pack-level specifications have been published, and no production availability, pricing, or independently verified test data exists at this time.

These numbers are significant. LFP at 706 lbs is likely incompatible with the MAOS weight budget. NMC 811 at 441 lbs is challenging but potentially viable if it displaces other weight — the battery IS the structural buffer, the emergency system, and part of the energy storage. Silicon-anode at 353 lbs is the most viable from a weight standpoint but the least mature of the commercially available options.

**This is the fundamental weight tension in MAOS propulsion design:** The 30-minute emergency reserve requirement, at the power level needed for an IFR approach, implies a battery in the 350–450 lb range regardless of chemistry — unless the power level assumption changes.

### What If the Emergency Power Requirement Is Reduced?

| Emergency Power | Battery kWh Needed | NMC 811 Weight | NCA Weight |
|---|---|---|---|
| 60 kW (full IFR approach) | 40 kWh | 441 lbs | 410 lbs |
| 40 kW (reduced speed descent) | 26 kWh | 287 lbs | 267 lbs |
| 25 kW (powered glide only) | 16 kWh | 176 lbs | 164 lbs |

At 25 kW (basically powered glide with minimal maneuvering), the battery weight drops to a much more manageable range. But this may not be sufficient for an IFR missed approach. This is a mission requirement question, not a technical one: **what does "get the plane on the ground" actually require if you're in IMC at 18,000 ft?**

### Specific Cell and Module Candidates

| Product | Format | Chemistry | Specific Energy | Availability | Notes |
|---|---|---|---|---|---|
| **CATL LFP 280Ah prismatic** | Prismatic cell | LFP | ~160 Wh/kg cell | Widely available (EV salvage, direct) | Standard cell in DIY/industrial energy storage. Excellent cycle life. Heavy. |
| **Samsung SDI 94 Ah prismatic** | Prismatic cell | NMC | ~215 Wh/kg cell | EV salvage | Used in BMW i3, various EVs. Reliable but older chemistry. |
| **Molicel P45B** | 21700 cylinder | NMC | ~260 Wh/kg cell | Available new | 4,500 mAh, 45A continuous. Excellent power density. Used in high-performance EV packs. |
| **Tesla 4680** | 46800 cylinder | NMC (tabless) | ~270 Wh/kg cell (claimed) | Limited aftermarket | High specific energy, tab-less design. Scarce outside Tesla ecosystem. |
| **Panasonic NCR21700A** | 21700 cylinder | NCA | ~260 Wh/kg cell | Available new | Used in Tesla Model 3. Proven at scale. |
| **Amprius 450 Wh/kg cells** | Pouch | Si-anode NMC | ~400–450 Wh/kg cell | Limited, aerospace customers | NASA evaluated. Best-in-class specific energy. Very expensive. Short cycle life currently. |
| **Donut Lab solid-state** | Custom ("clay-like") | All solid-state | 400 Wh/kg (claimed) | No production availability — pending | Verified in Verge motorcycles. No voltage, capacity, dimensions, or pricing published. See note. |
| **Lithionics 12V/24V/48V modules** | Module (LFP) | LFP | ~130 Wh/kg module | Direct (aviation market) | Aviation-focused supplier. Pre-built modules with BMS. Expensive but plug-and-play. |

> **Note on Donut Lab battery claims:** Donut Lab publishes 400 Wh/kg specific energy, 100,000-cycle life, 5-minute charge time, and −30°C to 100°C operating range with 99% capacity retention across that range — all in an all-solid-state cell with no thermal runaway risk. The Verge motorcycle application is real production use, which gives these claims more credibility than a press release alone. The controversy centers on the simultaneous combination of maximum energy density, maximum power (5-minute charge implies ~48C rate), and maximum cycle life — no conventional chemistry achieves all three at once. The 5-minute charge claim is the most physically difficult to reconcile; it can be set aside for the MAOS application since charge rate is irrelevant to the mission. The energy density and safety claims — if they hold — would be genuinely significant for MAOS. No pack-level specifications, pricing, lead time, or production availability have been published. **Design around NMC 811 as the planning baseline; treat Donut Lab as a potential upgrade that improves the weight budget if and when production availability is confirmed.**

### Format Considerations for Aviation

**Cylindrical cells (18650, 21700):** Used in Tesla, Molicel packs. High energy density at cell level, but pack-level efficiency lower because round cells don't pack perfectly. Very robust mechanically — individual cell failures are isolated. Excellent for vibration. Require many cells in parallel — BMS complexity increases.

**Prismatic cells (CATL, Samsung):** Flat aluminum-cased cells. Pack very efficiently, high pack-level density. Fewer cells = simpler BMS. Less vibration-tolerant than cylindrical — need good mounting/damping. Large format means a single cell failure has bigger impact.

**Pouch cells:** Highest specific energy at cell level. Swelling under charge/discharge — requires compression fixtures. Most vulnerable to physical damage. Not recommended for first aviation application without specific design for pouch behavior.

**Recommendation for MAOS Phase 1:** Prismatic NMC or cylindrical NMC (Molicel P45B or Samsung SDI). Avoid pouch for initial build. LFP if weight budget can tolerate it and safety is prioritized over performance.

---

## Section 5: The Architecture and Battery Decision Are One Decision

Here is where it comes together.

The 2G + 1B + 2M architecture requires a battery that can:
1. Provide 30-minute emergency reserve (40 kWh at 60 kW basis)
2. Buffer transient load spikes during generator transitions
3. Handle both motors simultaneously during emergency (not just one)

Weight implication with NMC 811: **~440 lbs** for the battery alone.

At that weight, the 2G + 1B + 2M architecture starts to look like:
- Two ICE generators: ~180–200 lbs (2× Rotax 915 iS equivalent)
- Two motors + controllers: ~60–80 lbs (2× AXM-series type motors)
- Battery: ~440 lbs (40 kWh NMC)
- **Propulsion system total: ~680–720 lbs**

On a target MTOW of ~2,500–3,000 lbs with 1,000–1,200 lb useful load, this is a significant fraction of empty weight. It is not impossible — the Tesla Model 3 Long Range battery pack is ~480 kg for 100 kWh — but it shapes everything downstream.

**Two levers to pull before accepting this weight:**

**Lever 1: Reduce emergency power assumption.** If "get the plane on the ground" means descending at 30–40 kW (not maintaining full IFR approach capability), the battery requirement drops to ~22–26 kWh and battery weight drops to ~260–310 lbs. This is a significant reduction but changes what you can do in an emergency.

**Lever 2: Accept silicon-anode NMC at higher cost.** Amprius-class cells at 400 Wh/kg bring 40 kWh into a ~220 lb package. This is the right answer if the technology is available at reasonable cost and demonstrated cycle life — neither of which is certain in 2026.

**An honest assessment:** At the target MTOW and useful load the design has been working toward, a 30-minute emergency reserve at full IFR power is a constraint that will significantly impact the mission. The designer needs to make a deliberate choice between:

- **Option A:** Full IFR emergency capability → heavy battery → reduced mission payload/range
- **Option B:** Partial emergency capability (powered descent, not full approach power) → lighter battery → better mission performance
- **Option C:** Two smaller batteries (Architecture 3) — each ~20 kWh — each powering one motor independently → same total energy but better failure isolation, potentially better chemistry options at smaller pack size

Architecture 3's split-battery approach actually offers a practical advantage here: two 20 kWh packs of NMC 811 weigh the same as one 40 kWh pack, but each pack independently powers one motor, meaning a battery failure only affects one propulsion channel rather than both.

---

## Summary and Next Steps

**Architecture decision:** 2G + 1B + 2M (coaxial contra-rotating) is the correct baseline. This can evolve to 2G + 2B + 2M if the weight budget supports it.

**Battery sizing:** Define the emergency power assumption first. 60 kW (full IFR approach) → 40 kWh. 40 kW (powered descent) → 26 kWh. This is a mission requirements question, not a technical one.

**Battery chemistry:** NMC 811 prismatic (CATL, Samsung) is the practical near-term choice. Molicel P45B cylindrical is viable for smaller format. LFP if weight budget is generous and safety is prioritized. Silicon-anode if availability and cost improve.

**The motor selection can't be finalized until the bus voltage and peak current are known** — the motor and controller are specified together. The two-motor architecture validates the Donut Labs and Axiom Motors approaches reviewed previously; both companies offer coaxial configurations or paired motor systems.

**Immediate action items:**
1. Decide the emergency power assumption — this is a builder decision, not an engineering one
2. Get a quote from CATL or a prismatic cell distributor for 280Ah LFP and NMC cells in 40 kWh quantity
3. Contact Molicel about cylindrical cell availability in aviation-scale quantities (50–200 cells)
4. Get weight and dimensions for the Rotax 916 iS to update the propulsion weight budget with real numbers
5. Revisit motor selection (Donut / Axiom) with two-motor architecture explicitly in mind

---

*Analysis by MAOS Design Board*
*MAOS Project — Mobile Aviation Operating System*
*AeroCommons / Fort Worth, Texas*
