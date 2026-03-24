---
title: "Builder Rebuttals to PROPULSION Engine Analysis"
date: 2026-03-19T09:00:00-06:00
description: "Builder challenges PROPULSION's power requirements and engine selection criteria, arguing certification standards don't apply to experimental aircraft."
tags: ["propulsion", "builder", "engine-selection", "rebuttals"]
author: "Bill (Builder)"
draft: false
---

# Builder Rebuttals to PROPULSION Engine Analysis
**Date:** March 19, 2026  
**Author:** Bill (Builder / Final Decision Authority)  
**Subject:** Challenges to PROPULSION's power requirements and engine selection criteria

---

## Executive Summary

PROPULSION's analysis applies inappropriate certification standards to an experimental aircraft and uses overly conservative single-engine-failed performance criteria that don't reflect operational reality in piston twins or the unique advantages of our hybrid architecture.

---

## Rebuttal 1: Single-Engine Performance Standards Are Inappropriate

### PROPULSION's Position (Challenged)
> "Single-generator-failed condition: One generator must provide 65-75 kW continuous"
> "Honda 400cc: Cannot maintain cruise power in single-engine-failed condition"

### Builder's Counter-Argument

**The loss of an engine in ANY piston twin is a true emergency.** The aircraft cannot maintain cruise performance in that situation. 

In many scenarios, an ICE twin single-engine scenario is far more desperate than what we're discussing with a hybrid architecture. The criteria that "the aircraft must maintain cruise performance with one generator failed" is **not a valid design requirement.**

### What We Should Actually Require

Performance goals for single-generator failure should be:

1. **Maintain safe margin above stall speed**
2. **Maintain safe margin above VMC (if applicable)**
3. **Some positive climb capability** — not cruise performance

**Reality check on piston twins:** Most piston twins under ideal circumstances can climb at maybe 200 feet per minute at gross weight on a standard day. And that is questionable. Many times single-engine driftdown comes into play.

**Our hybrid advantage:** If we lose a generator, we still have **battery pack time where full power is available.** This gives us options no conventional twin has:
- Immediate full power for obstacle clearance
- Time to configure for best single-engine performance
- Time to select a suitable landing site
- Gradual power reduction as battery depletes

### Action Required from PROPULSION

**Redefine single-generator-failed performance requirements:**
- What is minimum power required to maintain Vstall + 20 knots?
- What is minimum power required for 100-200 fpm climb at sea level?
- How long can battery buffer provide supplemental power?
- What is the driftdown profile with one generator + battery supplement?

**Stop comparing to cruise power requirements.** That's not the standard for emergency operations.

---

## Rebuttal 2: Certification Standards Do Not Apply

### PROPULSION's Position (Challenged)
> "No aviation pedigree or reliability data"
> "No certified FADEC systems available"
> "Aftermarket turbo kits not certified for aviation use"

### Builder's Counter-Argument

**Stop arguing from a position based on aircraft certification.**

This is an **EXPERIMENTAL** aircraft. It is, by definition, **not certified.**

We can use non-certified options where we deem them advantageous in any way. The entire point of the Experimental Amateur-Built category is to enable innovation outside the constraints of certified aircraft standards.

**Certification arguments are irrelevant to this design decision.**

What matters:
- **Reliability data** from the actual application (motorcycle, industrial, marine)
- **Suitability for continuous duty** at our required power levels
- **Integration complexity** vs. weight penalty trade
- **Cost** and **availability**

What does NOT matter:
- FAA certification status
- "Aviation pedigree"
- Whether the manufacturer markets it for aircraft use

### Action Required from PROPULSION

**Remove all certification-based objections from the engine analysis.** If Honda 400cc engines have reliability issues in continuous-duty applications, cite that data. Don't cite lack of certification as a technical problem.

---

## Rebuttal 3: Engine Options Are Not Binary

### PROPULSION's Position (Challenged)
> Analysis presents only Honda 400cc vs. Kawasaki as options
> No other alternatives evaluated

### Builder's Counter-Argument

There are **other alternatives besides just Kawasaki and Honda 400cc.**

**Alternatives to evaluate:**
1. **Higher displacement Honda engines** (500cc, 600cc variants)
2. **Viking engines** (aircraft conversion engines)
3. **Other motorcycle/industrial engines** in the 50-80 HP range
4. **Any engine available on the market** that fits the power/weight/integration profile

I'm sure there were a number of engine options discussed in the prior Claude.ai documentation. PROPULSION is free to evaluate what's on the market and offer up any alternatives that suit our use case.

**Don't limit the trade space to two options** when there may be better compromises available.

---

## Rebuttal 4: Cruise Power Requirements May Be Conservative

### Builder's Perspective

**Real-world cruise power is significantly lower than takeoff or climb power.**

Example: My Bonanza has a Continental E-225 engine that makes 225 HP. At cruise altitude (9,500 ft), I suspect it's barely making 100 HP in that environment.

**Cruise power requirements can be greatly reduced** compared to sea-level full-power assumptions.

### Food for Thought

- What is actual cruise power required at 9,500 ft vs. sea level?
- Are we sizing generators for worst-case (low altitude, high power) when cruise happens at altitude where power requirements are much lower?
- Can we accept reduced low-altitude performance if high-altitude cruise is optimized?

**This doesn't change the analysis directly**, but it's context for understanding what "cruise power" actually means in operation.

---

## New Decision Framework: Failure Tolerance Requirements

These failure scenarios and failure tolerance profiles are **new and have never really been documented in any aircraft certification** that I'm aware of.

We need to establish our own standards for:

### Failure Mode 1: Single Generator Engine Loss
- **Immediate capability:** Full power available (battery supplements remaining generator)
- **Sustained capability:** TBD — what can one generator + battery provide for how long?
- **Minimum acceptable:** Maintain flight, positive climb capability, time to reach suitable landing site

### Failure Mode 2: Single Electric Propulsion Motor Loss
- **Impact on thrust:** 50% reduction (one of two motors)
- **Remaining capability:** What performance with one motor at full power?
- **Can remaining motor + battery provide safe flight?**

### Failure Mode 3: Battery Pack Loss
- **Impact:** Loss of buffer, grid-tie between generators and motors
- **Remaining capability:** Direct generator-to-motor operation
- **Can we operate without the battery at all?**

### PROPULSION Action Required

**Develop failure mode performance analysis for all three scenarios.** Single-generator-failed is only one of several cases we need to understand.

---

## Summary: What PROPULSION Must Address

1. **Redefine single-generator-failed requirements** based on emergency performance (Vstall + margin, modest climb) rather than cruise maintenance
2. **Remove certification-based objections** — focus on actual reliability and suitability data
3. **Expand engine trade space** — evaluate Honda variants, Viking, and other options beyond just Kawasaki
4. **Develop comprehensive failure mode analysis** — generator loss, motor loss, battery loss

## What I Need from the Board

- **Specific power numbers** for emergency operations, not cruise
- **Battery supplemental power duration** in single-generator scenario
- **Trade analysis** of more engine options, not just two
- **Failure tolerance framework** for this hybrid architecture

---

**Builder position:** I am not convinced that Kawasaki engines are required based on PROPULSION's current analysis. The power requirements appear to be based on inappropriate standards (maintaining cruise performance in emergency) and the trade space has not been fully explored.

**Next action:** PROPULSION must revise analysis with these rebuttals addressed before I will accept a 500 lb weight penalty.
