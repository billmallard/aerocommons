---
title: "MAOS Drivetrain Economics: Why the Series Hybrid Has to Be Built on a Budget"
date: 2026-04-05T16:00:00-06:00
description: "An honest cost comparison of conventional ICE, premium series hybrid, and budget series hybrid propulsion for MAOS — and why the right comparison is against a twin-engine conventional, not a single."
tags: ["propulsion", "analysis", "design-decisions", "hybrid-electric", "weight-budget", "manufacturing"]
author: "MAOS Design Board"
summary: "Premium series hybrid components push MAOS propulsion cost to $150k+, which is genuinely excessive. But the right cost comparison isn't against a single-engine Lycoming — it's against a twin-engine conventional. And the budget hybrid path using motorcycle engines and accessible electrical components lands in a much more defensible range."
project: "maos"
article_type: "analysis"
draft: false
---

## The Honest Problem

The work done so far on MAOS drivetrain analysis has produced a premium component list that, when priced out, looks like this:

| Component | Qty | Unit Cost | Total |
|---|---|---|---|
| Rotax 915 iS (ICE generator engine) | 2 | $45,000 | $90,000 |
| Emrax 268 (axial-flux generator) | 2 | $12,000 | $24,000 |
| Emrax 268 or AXM3 (propulsion motor) | 2 | $12,000–$15,000 | $24,000–$30,000 |
| Motor controllers (4 total) | 4 | $4,000 | $16,000 |
| 40 kWh NMC battery pack | 1 | $20,000 | $20,000 |
| BMS, wiring, switchgear | — | — | $10,000 |
| Contra-rotating propeller | 1 | $10,000 | $10,000 |
| **Total** | | | **~$194,000** |

That's $194,000 for a drivetrain in an experimental homebuilt aircraft. By comparison, a single rebuilt Lycoming IO-540 and a Hartzell three-blade prop costs $40,000–$55,000.

At first glance, the series hybrid looks like a catastrophic economic failure. But the comparison isn't quite right.

---

## The Right Comparison: Twin, Not Single

The series hybrid drivetrain provides:
- Two independent power-generation channels (two ICE generators)
- Two independent propulsion channels (two electric motors)
- A 30-minute emergency battery reserve if both generators fail
- No mechanical gearbox linking engine to propulsion
- Continuous operation of ICE at optimum efficiency point

That capability profile doesn't compare to a single-engine Lycoming. It compares to a conventional twin-engine installation.

What does a twin-engine drivetrain actually cost, built new?

| Component | Qty | Unit Cost | Total |
|---|---|---|---|
| Lycoming IO-360 (rebuilt) | 2 | $22,000 | $44,000 |
| Hartzell 2-blade constant-speed prop | 2 | $8,000 | $16,000 |
| Engine mounts, cooling, exhaust | 2 sets | $3,000 | $6,000 |
| Gearboxes / prop governors | 2 | $2,500 | $5,000 |
| **Total** | | | **~$71,000** |

Still cheaper than the premium hybrid at $194k. But the gap is tighter than it looks against a single engine, and the comparison is getting more honest.

And there's one more factor the cost comparison can't capture:

**The pod-and-boom layout requires electrical transmission.** MAOS places the ICE generators in the wing and the propulsion motors on the tail boom. There is no practical way to run a mechanical drivetrain — shafts, gearboxes, couplings — from wing-mounted engines to a tail-mounted propeller on a pod-and-boom aircraft. The series hybrid isn't a nice-to-have engineering choice for MAOS. It's the enabling technology for the fundamental configuration. Without it, pods and booms don't work at this power level.

That's a real advantage that has no dollar figure.

---

## The Real Problem: Premium Components Were the Wrong Instinct

The analysis has been gravitating toward premium components: Rotax engineers, Emrax machines, aviation-grade controllers. These are good choices for minimizing risk and maximizing performance. They are not good choices for minimizing cost.

The motorcycle engine idea — Honda CB400, 400cc — was rejected early on power grounds. But the rejection was too narrow. The issue was 400cc. Not motorcycle engines.

### Motorcycle Engines at Useful Displacement

| Engine | Displacement | Stock HP | Est. Continuous at 85% | Used Engine Cost |
|---|---|---|---|---|
| Suzuki Hayabusa (Gen 2/3) | 1,340cc | 190 hp | ~108 kW / 145 hp | $3,000–5,000 |
| Kawasaki ZX-14R | 1,441cc | 208 hp | ~120 kW / 161 hp | $3,000–5,000 |
| BMW S1000RR | 999cc | 210 hp | ~120 kW / 161 hp | $4,000–7,000 |
| Honda CBR1000RR-R | 1,000cc | 217 hp | ~125 kW / 168 hp | $5,000–8,000 |
| Yamaha R1M | 998cc | 200 hp | ~114 kW / 153 hp | $4,000–7,000 |
| Viking 130 (Honda 1.5L car engine) | 1,497cc | 130 hp cont | 97 kW continuous | $14,000–18,000 installed |

The Viking 130 is the known-good reference point: Honda car engine, proven in aircraft, $14–18k installed. The Suzuki Hayabusa at $3–5k used is four times cheaper for more power.

### Why Generator Duty Is Easier on These Engines

Direct-drive aircraft engines work hard: they respond to throttle demands in real time, operate across a wide RPM and load range, and must manage power precisely through approach, go-around, and climb — often at maximum continuous power for extended periods.

A generator engine in a series hybrid does none of this. It runs at **one RPM, one throttle position, optimized mixture** for hours at a time. The electrical side handles all load variation. The battery absorbs peaks. The engine just makes AC current at a steady rate.

This is actually closer to an industrial genset application than an aircraft engine application — and industrial gensets routinely use automotive and motorcycle-derived engines at high duty cycles for exactly this reason.

The continuous thermal load is real and must be designed for. But constant-load continuous operation is **not harder** on an engine than variable-demand use. It's more predictable, easier to cool, and easier to optimize fuel consumption for.

---

## Three Cost Scenarios

### Scenario A: Conventional Single (Baseline)

| Component | Cost |
|---|---|
| Rebuilt Lycoming IO-540 | $28,000 |
| Hartzell 3-blade CS prop | $12,000 |
| Engine mount, cooling, exhaust | $4,000 |
| **Total** | **~$44,000** |

**What you get:** Proven, simple, parts everywhere. One engine, no redundancy, mechanical noise and vibration, fixed RPM constraint, no emergency reserve. Incompatible with pod-and-boom layout.

---

### Scenario B: Premium Series Hybrid

As costed above: **~$194,000**

**What you get:** Best-in-class components throughout, maximum power density, excellent documentation, known quantities. Financing a significant portion of a complete kit aircraft just on the drivetrain.

---

### Scenario C: Budget Series Hybrid

Optimize ruthlessly for cost without abandoning the architecture.

| Component | Qty | Unit Cost | Total | Notes |
|---|---|---|---|---|
| Suzuki Hayabusa 1340cc (used, low miles) | 2 | $4,000 | $8,000 | Hugely overpowered for generator duty at 85% throttle |
| Engine prep: cooling reroute, mounts, throttle body conversion | 2 | $2,000 | $4,000 | Custom fabrication |
| PMG generator head (50–80 kW axial-flux, mid-tier) | 2 | $5,000 | $10,000 | Emrax 228 or equivalent mid-tier axial-flux; not premium |
| Propulsion motor (Emrax 228 or equivalent) | 2 | $8,000 | $16,000 | 50 kW continuous each; two motors × 50 kW = 100 kW total |
| Motor controllers | 4 | $2,500 | $10,000 | Generator mode × 2, motor mode × 2 |
| 40 kWh DIY LFP battery pack | 1 | $10,000 | $10,000 | CATL 280Ah prismatic cells + BMS + case |
| HV wiring, switchgear, fusing, contactors | — | — | $6,000 | |
| Reduction drive (belt, ICE to generator) | 2 | $800 | $1,600 | Belt drive, ~1.5:1 ratio |
| Contra-rotating propeller | 1 | $8,000 | $8,000 | |
| Contingency (10%) | — | — | $7,400 | |
| **Total** | | | **~$81,000** | |

**What you get:** Full series hybrid architecture — two generator engines, two propulsion motors, 30-minute LFP battery reserve, no mechanical gearbox, pod-and-boom compatible. At $81k, this is $37k more than the single-engine conventional, and roughly comparable in total to a twin-engine conventional drivetrain.

---

## The Real Cost Comparison

| Configuration | Drivetrain Cost | Engines | Redundancy | Pod-and-Boom | Emergency Reserve |
|---|---|---|---|---|---|
| Single conventional ICE | ~$44,000 | 1 | None | ❌ No | None |
| Twin conventional ICE | ~$71,000 | 2 | Partial | ❌ No | None |
| **Budget series hybrid** | **~$81,000** | **2 gen+** | **Full** | **✅ Yes** | **30 min** |
| Premium series hybrid | ~$194,000 | 2 | Full | ✅ Yes | 30 min |

The budget hybrid beats the twin conventional by roughly $10k while delivering better redundancy, pod-and-boom compatibility, and emergency reserve. That's the defensible comparison.

The $113k premium between budget and premium hybrid buys component quality, power density, and reduced integration risk. For a first experimental build, that premium is hard to justify. For a refined second build, it might make sense.

---

## What Has to Be True for Budget Hybrid to Work

This isn't a free lunch. The budget approach carries real tradeoffs and risks.

**Engine conversion engineering is non-trivial.** The Hayabusa wasn't designed to run in an aircraft engine bay. Cooling rerouting, vibration isolation, FADEC or ECU reprogramming for constant-speed operation, oil system adaptation, and throttle-by-wire integration all require real engineering. Viking has done this work — their product costs $14–18k instead of $3–5k because of that engineering effort. For MAOS, this work needs to be done and documented.

**"Used engine" is a risk.** A used motorcycle engine with unknown history is not the same reliability starting point as a new Rotax with documented test hours. Mitigation: buy low-mile (under 5,000 miles), inspect carefully, replace wear items, run break-in hours on a test stand before installation. Two engines mitigates the single-failure risk.

**Mid-tier axial-flux machines have less documentation.** The Emrax 268 has years of experimental aviation builder data behind it. A cheaper machine may have less community knowledge. This increases integration engineering time.

**LFP battery packs are heavier.** The 40 kWh LFP DIY pack at ~$10k weighs approximately 320 kg / 706 lbs. This is significantly heavier than NMC options and may be incompatible with the MAOS weight budget. The budget hybrid may force a reconsideration of the 30-minute reserve requirement, or acceptance of a heavier aircraft.

**The 100 kW total propulsion from two 50 kW motors is tight.** Two Emrax 228s at 50 kW continuous each = 100 kW total, which is below the 120–130 kW shaft power target for 155 KTAS cruise. Performance will be compromised at altitude. This is a known trade.

---

## Near-Term Decisions This Forces

**1. Pick a budget target.** If $80–90k for the full drivetrain is the target, the budget hybrid path is viable. If $120k is acceptable, there's room for Rotax engines with budget electrical. If cost is secondary, the premium path is better characterized but approaches $200k.

**2. Decide on ICE engine approach.** Rotax (premium, proven, expensive), Viking/car engine conversion (mid-tier, known path, $14–18k), or DIY motorcycle/Hayabusa conversion (cheapest, most engineering work). This decision drives everything downstream.

**3. Acknowledge the battery weight problem.** The 30-minute LFP reserve at 706 lbs is probably incompatible with a 4-seat aircraft. Options: accept NMC at higher cost, accept shorter reserve, or accept fewer seats. This is a mission requirement question.

**4. Determine what "comparable to a twin" actually means for this aircraft.** MAOS isn't trying to replicate a Piper Twin Comanche. It's trying to build a novel capability. The series hybrid exists because it enables the pod-and-boom layout, not because it's cheaper. The cost just has to be *within reach* — not competitive with a single-engine Lycoming.

---

## Summary

The series hybrid is not an economical choice against a single-engine conventional aircraft. It was never going to be. The right comparison is against a twin-engine conventional, and against that baseline the budget hybrid path is within a defensible range.

The architecture is justified not primarily by cost but by what it enables: true mechanical independence between power generation and propulsion, the pod-and-boom layout that defines MAOS, and a genuine 30-minute emergency reserve that no conventional twin provides.

But that only holds if the ICE generator cost is controlled. Two Rotax 915 iSs at $90k makes the whole thing unaffordable. Two Hayabusas at $8k, with the engineering effort to make them work as generators, is a completely different conversation.

The motorcycle engine approach is not dead. It was rejected for the wrong engine at the wrong displacement. It deserves a serious second look at 1,000–1,400cc.

---

*Analysis by MAOS Design Board*

*Related articles:*
- [MAOS Generator Engine Comparison Matrix](/articles/2026-04-05-maos-engine-comparison-matrix/)
- [MAOS Generator Selection: Axial-Flux Machines and the 400V vs 800V Decision](/articles/2026-04-05-maos-generator-selection/)
- [MAOS Propulsion Redundancy Architecture and Battery Selection](/articles/2026-04-05-maos-propulsion-redundancy-battery/)
