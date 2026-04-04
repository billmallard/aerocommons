---
title: "Single vs Twin: The Engine Architecture Decision That Defines an Aircraft"
date: 2026-03-25T12:45:00Z
description: "Deep dive into the single vs twin engine debate for MAOS hybrid-electric aircraft: weight analysis, safety philosophy, battery sizing, and what kind of redundancy you trust."
tags: ["design-decisions", "propulsion", "safety", "build-in-public", "hybrid-electric"]
author: "Bill Mallard / MAOS Design Team"
project: "maos"
article_type: "analysis"
draft: false
---

One of the most fundamental decisions in aircraft design is deceptively simple: one engine or two?

For a hybrid-electric aircraft like MAOS, this question becomes even more complex. We're not just choosing engines — we're choosing generators, battery sizing, cooling systems, electrical architecture, and ultimately, the entire safety philosophy of the aircraft.

We spent the last week running the numbers, debating failure modes, and wrestling with weight budgets. This is the story of that analysis.

---

## The Question

Should MAOS use:

**Option A:** Two smaller engines (twin Honda 400cc, ~75 kW each) with a small battery backup (~3-5 kWh)

**Option B:** One larger engine (single Kawasaki I4 turbo, 150 kW) with a large flight-critical battery (~10-15 kWh)

Both configurations drive the same electric motors through the same 400V electrical bus. The only difference is how we generate that power.

---

## The Case for Twins

**Redundancy is king.**

If one engine fails, the other keeps running. You have continued powered flight — not full power, but enough to maintain altitude or execute a controlled descent to any suitable airport.

This is the traditional aviation answer. Twin-engine aircraft have lower accident rates in engine-out scenarios. Pilots are trained for it. Regulations are built around it.

From a safety perspective, twins offer:
- **No single point of failure** — losing one generator doesn't ground the aircraft
- **Manageable failure modes** — engine-out is serious, but survivable and well-understood
- **Lower workload** — pilot has time to assess, plan, execute
- **Proven precedent** — decades of twin-engine GA aircraft data

---

## The Case Against Twins

**Complexity and weight.**

Two engines means:
- Two separate fuel systems (tanks, lines, pumps, filters)
- Two separate cooling loops (radiators, pumps, hoses, reservoirs)
- Two separate electrical generators
- Two separate mounting structures
- Twice the maintenance
- Twice the failure modes to monitor

Our structures team calculated the wing center-section integration weight:

| Item | Twin (lbs) | Single (lbs) | Delta |
|------|------------|--------------|-------|
| Engine mounts + hardware | 12 | 7 | -5 |
| Spar box reinforcements | 22 | 12 | -10 |
| Ribs + shear clips | 8 | 4 | -4 |
| Fairings + duct integration | 16 | 9 | -7 |
| **Total wing integration** | **58** | **32** | **-26 lbs** |

Add in the propulsion system itself:

| System | Twin | Single | Delta |
|--------|------|--------|-------|
| Engines | 240 lbs (120 ea) | 130-140 lbs | **-100 lbs** |
| Generators | 32 lbs | 30-40 lbs | -2 lbs |
| Fuel systems | 50 lbs (dual) | 25 lbs | **-25 lbs** |
| Cooling | 90-100 lbs (dual loops) | 50-60 lbs | **-40 lbs** |
| Battery | 40-60 lbs (3-5 kWh) | 100-130 lbs (10-15 kWh) | **+70 lbs** |
| Mounts/plumbing | 40 lbs | 20 lbs | **-20 lbs** |
| **Total propulsion** | **492-522 lbs** | **355-395 lbs** | **-100 to -127 lbs** |

Even accounting for the larger battery, **the single-engine configuration is 100+ pounds lighter.**

For an aircraft with a 2,430 lb max takeoff weight, that's a 4-5% reduction in empty weight. That translates directly to payload capacity, range, or performance margin.

---

## The Battery Question

Here's where it gets interesting.

In the twin configuration, the battery is a **backup buffer** — it gives you 10 minutes to deal with a double-engine failure and find a place to land. It's insurance, not primary.

In the single configuration, the battery becomes **flight-critical** — if the engine fails, you have *only* the battery to get you safely on the ground.

So how much battery do you need?

### Failure Scenario: Engine-Out at Cruise Altitude

Assume worst case: engine failure at 17,500 feet, 50+ miles from the nearest airport.

**Emergency descent profile:**
- Altitude loss: 17,500 ft → 1,000 ft pattern altitude = 16,500 ft
- Descent rate: 800-1,000 fpm (standard emergency descent)
- Time: ~18-22 minutes
- Power draw: 50-62 kW (one motor at reduced power + essential avionics)

**Approach and landing:**
- Missed approach contingency: 3 minutes
- Go-around if needed: 2 minutes  
- Second approach: 5 minutes
- **Total margin time: ~10 minutes**

**Total emergency duration: 30 minutes minimum**

At 60 kW average draw:
- 30 min × 60 kW = **30 kWh** required

But wait — batteries don't like being fully discharged, and you want margin for temperature variations, aging, and uncertainty.

A more realistic requirement:
- **Usable capacity:** 12-15 kWh
- **Installed capacity:** 15-18 kWh (accounting for 80% depth-of-discharge limit)

At 200-250 Wh/kg (current aviation-grade lithium-ion), that's:
- 15 kWh / 0.22 kWh/kg = **68-75 kg = 150-165 lbs**

That's heavier than our initial estimate, but it's the minimum defensible size for a flight-critical battery.

---

## The Safety Debate

Our safety team objected strongly to the single-engine configuration.

Here's their argument:

> **Twin-engine architecture has lower overall risk.**
>
> In a twin, engine failure is a *manageable* event with continued powered flight. In a single, engine failure becomes a *time-limited emergency* dependent on battery state-of-charge.
>
> Batteries can fail silently. A degraded cell, a bad BMS reading, a thermal fault — you don't know until you need it. An engine, by contrast, gives you warning: temperature, vibration, power loss, noise. Pilots are trained to recognize it.
>
> **The failure mode matrix shifts from MANAGEABLE to CONTROLLED-but-battery-critical.**

Their recommendation:

If we go with a single engine, we **must** add:
1. Ballistic Recovery System (BRS parachute) — 40 lbs, $20k
2. Dual redundant Battery Management Systems
3. Continuous state-of-charge display in the cockpit
4. Full FMEA (Failure Modes and Effects Analysis) for the battery system

With those mitigations, single-engine becomes *acceptable*, but not preferable.

---

## The Propulsion Team's Rebuttal

Our propulsion team countered:

> **The weight savings are too significant to ignore.**
>
> Even with a 150 lb flight-critical battery, we're still 50-100 lbs lighter than the twin configuration. That's not trivial — it's the difference between hitting our performance targets and falling short.
>
> Twin engines don't eliminate risk — they shift it. You still have twice the failure modes to monitor, twice the maintenance burden, twice the thermal management complexity.
>
> And let's talk about real-world GA safety: the Cirrus SR22 is a single-engine aircraft with a BRS, and it has one of the *lowest* fatal accident rates in its class. The parachute works.
>
> **Recommendation: Single Kawasaki I4 turbo + 15 kWh battery + BRS. Accept the paradigm shift.**

---

## The Builder's Dilemma

This is where it gets uncomfortable.

Both positions are defensible. Both teams did their homework. The numbers support both architectures.

**Twin = traditional, conservative, redundant.** Higher weight, higher complexity, but well-understood risk profile.

**Single = modern, efficient, lighter.** Lower weight, simpler systems, but requires new thinking about battery-critical failure modes.

There's no "right" answer in an absolute sense. There's only the answer that fits the mission, the builder's risk tolerance, and the regulatory environment.

---

## What We're Thinking

As of this writing, we're leaning toward **single-engine + large battery + BRS**, for three reasons:

1. **Weight budget pressure** — We're already tight on empty weight. 100 lbs matters.

2. **Simplicity** — One fuel system, one cooling loop, one engine to maintain. For an experimental homebuilt aircraft, that's a huge buildability and maintainability win.

3. **Technology trajectory** — Battery energy density is improving every year. In 5 years, that 150 lb battery could be 100 lbs. In 10 years, it could be 70 lbs. The architecture scales favorably with technology progress.

But this decision isn't closed yet. We're still working through:
- BRS integration weight and CG impact
- Battery thermal management in the wing center section
- FAA experimental certification implications
- Builder workload and training requirements

---

## Why This Matters Beyond MAOS

The single-vs-twin debate is fundamentally about **what kind of redundancy you trust**.

In traditional aviation, redundancy means *duplication* — two engines, two electrical systems, two hydraulic pumps.

In modern electric systems, redundancy increasingly means *energy storage* — one generator, one big battery, sophisticated monitoring.

This is the same philosophical shift happening in:
- Electric cars (no one demands twin motors for safety)
- Grid-scale energy systems (renewables + storage, not duplicate generators)
- Modern avionics (single integrated flight computers replacing mechanical backups)

Aviation is conservative by necessity — and rightly so. But at some point, "we've always done it this way" has to be challenged with data.

**The question isn't whether batteries *can* be flight-critical. The question is: under what conditions, with what safeguards, and for what missions?**

For MAOS — a four-seat hybrid-electric aircraft with a 17,500 ft service ceiling, designed for the experimental/homebuilt market — we think the answer is *yes, with a BRS and proper monitoring*.

But we'll let you know if the board changes our mind.

---

## What Happens Next

This analysis goes to the design review board for a final decision. The agenda item is:

**DG-005: Generator Configuration (Single 150 kW vs Twin 75 kW)**  
**DG-006: Battery Sizing (Emergency buffer vs Flight-critical)**

The board will hear positions from:
- PROPULSION (recommends single)
- STRUCTURES (recommends single, cites weight)
- SAFETY (recommends twin, cites risk)
- SYSTEMS (defers, either works electrically)
- MANUFACTURING (defers, either is buildable)
- AERO (no impact)

Then we'll make the call.

---

## The Lesson

Great engineering decisions are rarely obvious. If they were, there wouldn't be a debate.

The hard part isn't the math — the math is clear. The hard part is choosing *which risks you're willing to accept* and *which benefits you're willing to pay for*.

That's why we write it down. That's why we document the dissent. That's why we make the builder read the summary and acknowledge the trade-offs.

Because five years from now, when this aircraft is flying, someone's going to ask:

*"Why did you choose one engine?"*

And the answer needs to be better than *"It seemed lighter."*

---

**Want to follow along?** We publish our design decisions, meeting notes, and technical analyses as we go. Check out the MAOS project documentation or join the discussion.

**Next in this series:** How we're integrating a ballistic recovery system into a mid-wing aircraft without destroying the CG envelope.
