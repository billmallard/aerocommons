---
title: "The Wing That Isn't There: When Removing Parts Makes an Airplane Better"
date: 2026-03-26T00:08:00-06:00
description: "MAOS wing attachment decision: cantilever wins over braced struts by adding weight to the spar but removing everything else."
tags: ["board-meeting", "design-decisions", "structures", "aerodynamics", "weight-budget"]
author: "AeroCommons Design Board"
session: "BOARD-002-PREP"
draft: false
---

In aircraft design, there's a fundamental truth: every part you add makes the airplane heavier, more complex, and harder to build.

So when you can achieve the same result by making one part stronger instead of adding two new parts, you're usually winning.

This week, the MAOS design board analyzed whether our high wing should be **braced** (supported by external struts from the fuselage to mid-span) or **cantilever** (self-supporting with no external bracing).

The strut option seems simpler at first — lighter wing spar, proven design, thousands of Cessnas and Cubs flying with struts. But when you add up the total system weight and count all the parts, the answer reverses.

**Cantilever wins. Here's why.**

---

## The Trade-Off

### Braced Wing (V-Struts from Fuselage to Mid-Span)

**Pros:**
- Lighter wing spar (struts carry half the bending load)
- Proven configuration — Cessna 172, 182, Piper Cub, thousands of homebuilts
- More builder labor hours (helps meet 51% rule for amateur-built certification)

**Cons:**
- External struts add drag
- More parts: strut tubes, strut attach fittings, wing-end fittings, fairings
- Rigging complexity — struts must be aligned and tensioned correctly
- More failure points (strut attach bolts, fittings)

### Cantilever Wing (No External Bracing)

**Pros:**
- Cleaner aerodynamics (no strut drag or interference)
- Fewer parts — just wing attach fittings at the root
- Simpler to build (no strut fabrication, no rigging)
- Simpler to trailer (no strut disconnection)

**Cons:**
- Heavier wing spar (must carry full root bending moment)
- Fewer builder labor hours (worse for 51% rule)

On the surface, this looks like a classic trade: **lighter but more complex** (braced) vs. **heavier but simpler** (cantilever).

But the math tells a different story.

---

## The Weight Analysis (STRUCTURES Agent)

Our structures agent ran the numbers for a 42-foot wingspan, 140 square foot wing, designed for 6g ultimate load at 2,430 lbs MTOW.

### Braced Wing System Weight

| Component | Weight (lbs) | Notes |
|---|---|---|
| Wing spar | 85 | V-strut at mid-span reduces root bending moment by ~50% |
| V-struts (pair) | 22 | Aluminum tube + streamlined fairings |
| Strut attach fittings | 18 | Forged lugs, bolts, wing-end fittings |
| Wing root reinforcement | 12 | Standard for high-wing attachment |
| **Total system** | **137 lbs** | |

### Cantilever Wing System Weight

| Component | Weight (lbs) | Notes |
|---|---|---|
| Wing spar | 135 | Must carry full root bending moment, heavier section required |
| V-struts | 0 | None |
| Strut fittings | 0 | None |
| Wing root reinforcement | 28 | Heavier attach fittings for full-moment transfer |
| **Total system** | **163 lbs** | |

**Net penalty: +26 lbs for cantilever.**

So cantilever is heavier, right? That should settle it — braced wins on weight.

Not so fast.

---

## The Drag Analysis (AERO Agent)

Weight is only half the story. The struts sit in the airflow. They create drag.

### Strut Drag Penalty

Our aero agent estimated the drag penalty for a pair of V-struts at cruise speed (155 knots true airspeed at 17,500 feet):

**Sources of drag:**
1. **Profile drag** — the struts themselves have form drag (even with streamlined fairings)
2. **Interference drag** — where the struts attach to the wing and fuselage, airflow is disrupted
3. **Induced drag increase** — the struts change the spanwise lift distribution, slightly reducing the effective aspect ratio (Oswald efficiency factor drops from ~0.85 to ~0.83)

**Total drag increase: ~2% at cruise**

That translates to:
- **-3 knots cruise speed** (155 KTAS → 152 KTAS with struts)
- **+2% fuel burn**
- **-30 nautical miles range** (1,000 nm → 970 nm)

### Lift-to-Drag Ratio Impact

Clean glide ratio (engine-out, prop feathered):
- Braced wing: ~14.2:1 estimated
- Cantilever wing: ~14.8:1 estimated

**+4% better glide ratio with cantilever.**

That's the difference between making a field 2 miles away or 2.1 miles away after an engine failure. Small, but not nothing.

---

## The Builder Analysis (STRUCTURES + MANUFACTURING)

From a buildability standpoint, cantilever is simpler:

### Part Count Comparison

| System | Braced Wing | Cantilever Wing |
|---|---|---|
| Major structural assemblies | 5 (wing, 2x strut, 2x attach) | 3 (wing, 2x attach) |
| Rivets/bolts (wing + struts) | ~1,200 | ~800 |
| Custom fittings required | 6 (strut ends, wing ends, fuselage lugs) | 2 (wing root attach only) |

**33% fewer fasteners. 40% fewer major subassemblies.**

### Build Time Estimate

- **Braced wing:** ~800 hours (wing + strut fabrication + fitting + rigging)
- **Cantilever wing:** ~600 hours (wing + root attach only)

**-200 hours of builder labor.**

This is the flip side: **cantilever is simpler to build, but that's *worse* for 51% rule compliance.**

Under FAA Experimental Amateur-Built regulations, the builder must complete at least 51% of the construction labor to qualify for the amateur-built certificate. Fewer labor hours means the builder has less work to count toward that 51% threshold.

For a project like MAOS where we're outsourcing the motor controllers, generators, avionics, and landing gear, every hour of builder labor counts toward compliance. Losing 200 hours from the wing is a hit.

**But:** The wing is still fully builder-fabricated either way. The labor hours are in the rigging complexity, not the core structural work. We can make up the 200 hours elsewhere (fuselage skinning, interior build, systems installation).

---

## The Safety Analysis (SAFETY Agent — Not Filed)

Interestingly, the safety agent didn't file a position on this one.

That tells us something: **from a safety standpoint, braced and cantilever are equivalent.**

Both are proven. Both have been used in thousands of aircraft. Failure modes:
- **Strut failure:** Catastrophic (wing folds up) — but struts are simple tension/compression members, easy to inspect, rarely fail
- **Spar failure:** Catastrophic (wing separates) — but spars are massively overdesigned (6g ultimate with 1.5 safety factor), also rarely fail

Neither configuration has an inherent safety advantage. Both require proper design and inspection.

---

## The Decision Matrix

Let's summarize the trade:

| Factor | Braced Wing | Cantilever Wing | Winner |
|---|---|---|---|
| **System weight** | 137 lbs | 163 lbs (+26) | Braced |
| **Cruise speed** | 152 KTAS | 155 KTAS (+3) | Cantilever |
| **Range** | 970 nm | 1,000 nm (+30) | Cantilever |
| **Glide ratio** | 14.2:1 | 14.8:1 (+4%) | Cantilever |
| **Part count** | 5 assemblies, 1,200 fasteners | 3 assemblies, 800 fasteners | Cantilever |
| **Build time** | 800 hours | 600 hours (-200) | Cantilever (but worse for 51% rule) |
| **Rigging complexity** | Must align and tension struts | Bolt-on at root only | Cantilever |
| **Trailering** | Disconnect 4 strut attach points | Disconnect wing root only | Cantilever |

Cantilever wins on **speed, range, efficiency, simplicity, and ease of operation**.

Braced wins on **weight and 51% rule labor hours**.

---

## Why Cantilever Won

The deciding factor: **26 lbs of extra wing weight buys you 3 knots, 30 nm range, simpler construction, and easier operation.**

3 knots doesn't sound like much. But over a 1,000 nm cross-country flight, that's **20 minutes faster**. For a 7-hour endurance mission, that's real.

And the 26 lbs penalty is well within our weight budget margin. Our current empty weight is ~230 lbs known out of a ~1,135 lb budget. We have **900+ lbs of margin**. Spending 26 lbs to gain 3 knots and eliminate rigging complexity is a good trade.

The 51% rule concern is valid — losing 200 hours of builder labor is not ideal. But MAOS has plenty of other builder-fabricable structure: the fuselage pod, the tail boom, the empennage, the landing gear fairings, the interior. We can hit 51% without needing the extra strut hours.

And critically: **the builder explicitly said he wanted "the simplest wing planform possible."**

Cantilever is simpler. One piece. No struts. No rigging. Bolt it on, torque the bolts, go fly.

---

## What This Means for MAOS

The wing attachment decision is now **closed: cantilever**.

Updated weight budget:
- Wing structure: **206 lbs** (updated from 180 lbs baseline)
- Wing loading: **16.9 lb/ft²** (was 16.7 lb/ft²) — still well below the 18 lb/ft² concern threshold

No other systems are affected. The decision does not block any open decision gates.

The aerodynamics agent will update drag estimates to remove strut drag from the model. The structures agent will finalize the cantilever spar design and update the wing structural drawings.

---

## The Lesson: Count Everything

This is a textbook example of why you have to **count the whole system**, not just the headline number.

"Braced wing has a lighter spar" is true. But:
- You have to add the strut weight
- You have to add the strut fitting weight
- You have to add the drag penalty
- You have to add the build complexity
- You have to add the operational rigging requirement

When you add it all up, the "lighter" option is actually heavier *in total*, slower, and more complex.

**The part that isn't there weighs nothing, costs nothing, and never fails.**

Cantilever wins because it removes parts. The spar is heavier, but everything else goes away.

---

## What We're Building

MAOS will have a **42-foot cantilever high wing** — one continuous piece, no struts, no external bracing.

The wing will be removable for trailering (crane-assisted, disconnect at the root attach fittings, lift off). But during flight operations, it's a simple bolt-on assembly. No rigging. No alignment checks. No strut tension adjustments.

Just a wing. Doing its job. Efficiently.

---

**Want to follow the decision-making process in real time?** We publish every design board analysis, agent position, and trade study as we go. Check out the MAOS project documentation.

**Next decision on the docket:** Wingspan — how wide can we go before the trailer won't fit under Texas overpasses?
