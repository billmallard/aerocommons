---
title: "Fly-By-Wire for Homebuilt Aircraft: Why Pod-and-Boom Changes the Game"
date: 2026-03-26T14:00:00-05:00
description: "Board review of FBW control architecture for MAOS: why distributed actuation is cleaner in a pod-and-boom design, and what it takes to do it safely."
tags: ["design-decisions", "systems", "safety", "aerodynamics", "board-meeting"]
author: "AeroCommons Design Board"
session: "BOARD-FBW-REVIEW-001"
draft: false
---

## The Question

Can a homebuilder implement fly-by-wire (FBW) primary flight controls in an experimental aircraft? And more specifically: does the MAOS pod-and-boom architecture make this easier or harder than a conventional design?

We took this question to the full design review board — five specialized agents covering aerodynamics, structures, propulsion, systems, and safety. Here's what we found.

---

## The Short Answer

**True full-authority FBW doesn't exist as a COTS product for homebuilders yet, but useful subsets of it do** — and for a pod-and-boom aircraft like MAOS, the migration path is genuinely cleaner than for conventional designs.

**Phase 1 (available today):** Garmin G3X + ESP-X gives you envelope protection and automatic leveling through existing autopilot servos. This is stability augmentation, not true FBW, but it delivers the most critical safety benefit: loss-of-control-in-flight (LOC-I) prevention. It's a free software update if you're already building a G3X panel.

**Phase 2 (experimental):** ArduPilot is open-source autopilot software that runs full FBW on Pixhawk hardware. It's been used in manned experimental aircraft by builders willing to do their own integration work. The limitation: it's UAV software adapted to manned use, with no formal support structure.

**Phase 3 (not yet COTS):** True FBW with proper redundancy and failure monitoring for manned IFR flight doesn't have an off-the-shelf solution today. But the technology is becoming robust and cheap enough that industry observers expect FBW homebuilts to arrive as UAV technology commercializes.

---

## Why Pod-and-Boom is Different

Here's where the MAOS architecture shows a real advantage.

On a conventional aircraft, routing mechanical controls is annoying but manageable — cables and pushrods through a fuselage you can access during construction. On a pod-and-boom aircraft, routing mechanical controls through a structural tail boom to reach the elevator and rudder is a **genuine engineering headache:**
- Pulleys at the boom entry point
- Tension management across temperature extremes
- Access for inspection and maintenance
- The boom structure has to accommodate all of it

A wire harness routed alongside the electrical bundle you're already running for propulsion? **Trivial by comparison.**

The MAOS boom is practically begging for distributed FBW.

---

## What Actually Exists: Volz Servos

**Volz Servos** makes actuators specifically for this application — their DA-30 and DA-58 product lines have been used to implement full FBW on manned experimental aircraft, with dual-redundant designs. On the Vertical Aerospace VX4 piloted eVTOL, Volz DA-30-HT and DA-58-D actuators control all flight surfaces with CAN bus interfaces.

More relevant to homebuilders: Volz makes an **OPV (Optionally Piloted Vehicle) variant** with an electromagnetic clutch. When the pilot applies enough force, the clutch disengages and the output shaft moves freely, giving the pilot manual authority. That's an elegant manned-aircraft failure mode solution **built into the actuator itself** — if the servo jams, you can muscle through it.

---

## The Design Decisions This Opens Up

### The Sidestick Becomes a Pure Sensor

With no mechanical run to the surfaces, the stick in the cockpit just measures what the pilot's hand is doing — force, position, or both — and sends that as a command signal. A Hall-effect stick has no friction, no wear, no cable stretch, and weighs almost nothing. This also means the co-pilot position can have an identical stick wired in parallel at essentially zero additional structural cost.

### Servo Sizing is Straightforward

The critical number is **hinge moment** — the aerodynamic force trying to move the surface, which you need to overcome. For a four-seat aircraft at MAOS speeds, elevator hinge moments run roughly **15–30 Nm** at Vne (assuming aerodynamically balanced surfaces). The Volz DA-26-D provides **12 Nm continuous and 18 Nm peak per channel**, with dual channels — meaning two independent electrical windings in one housing. Mount two of them on the elevator (one per side of the horn) and you have well-characterized redundancy at roughly 300 grams per unit.

**Critical caveat:** This assumes aerodynamically balanced control surfaces. Unbalanced surfaces could require 10× more torque. You must calculate actual hinge moments for your specific geometry before selecting actuators.

### CAN Bus is the Right Interface

Volz implements CAN bus protocol in their aviation actuators, which means you're sending digital command/status packets over a two-wire bus rather than individual PWM signals. An ESP32-S3 (or similar microcontroller) already speaks CAN. The whole flight control electrical interface reduces to a **twisted pair running the length of the boom** alongside the power wiring you're already routing.

---

## The Electrical Architecture

Any system that you cannot afford to lose in flight needs its own power domain, completely galvanically isolated from everything else. For FBW, that means the flight control computers and actuators must be able to keep operating even if the main HV bus, both DC-DC converters, and the primary avionics bus all fail simultaneously.

Certified aircraft solve this with an **essential bus** or **standby bus** that has its own dedicated battery, diode-isolated from the main electrical system. The bus can accept charging from the main system during normal operations, but if the main system fails, the standby battery takes over automatically with no switching required.

### Three Power Domains

Your electrical architecture needs at least three domains:

1. **400V HV bus** — propulsion only (15 kWh flight-critical battery)
2. **28V primary avionics bus** — derived from the HV bus via DC-DC converter; powers EFIS, comms, nav, autopilot computers, engine monitoring; backed by a small dedicated LiFePO4 (~4-6 Ah, standard practice)
3. **Standby/essential bus** — completely independent of the HV bus; powers flight control actuators, FBW computer, one AHRS, one radio, GPS; has its own small dedicated battery

The critical insight: **the FBW load is tiny.** Garmin GSA 28 autopilot servos draw roughly 1-3A each under load at 14-28V. Even three axes of actuation plus a flight control computer is maybe **20-30W continuous.** A 6 Ah LiFePO4 at 24V gives you roughly **7-8 hours** of standby flight control authority. That battery weighs about **3-4 lbs.** This is not a significant weight or cost problem.

### Weight Comparison

Our structures team ran the numbers:

- **FBW system:** ~12 lb total (5 servos, standby battery, wiring, sensors, mounts)
- **Mechanical system:** ~20 lb (pushrods, cables, pulleys, bellcranks, pedals, column)
- **Net savings: ~8 lb in favor of FBW**

---

## The Centerline Thrust Advantage

MAOS has something almost no conventional FBW aircraft has at this scale: **coaxial counter-rotating motors on centerline.** This eliminates several failure modes that conventional twin-engine aircraft must design around:

### What You Get

1. **Engine-out yaw doesn't exist.** On a conventional twin, losing one engine creates a massive yaw moment from asymmetric thrust. With centerline thrust, one motor degrades and both are still on centerline — the aircraft just has less total thrust. That's a manageable power problem, not a directional control emergency.

2. **P-factor and gyroscopic precession cancel.** Counter-rotating props produce equal and opposite gyroscopic moments. A single-engine aircraft fights P-factor, slipstream, gyroscopic precession, and torque all pushing the same direction. MAOS has none of that.

3. **Torque reaction is zeroed.** Full power application doesn't yaw or roll the aircraft. This matters particularly on go-around from a slow approach.

### What You Don't Get

**Differential thrust is not a flight control mechanism.** With coaxial motors on centerline, there's effectively zero moment arm for lateral forces. Speeding up one motor and slowing the other doesn't push the nose sideways — both thrust vectors are coincident on the centerline.

You do get differential **reaction torque** (one rotor's torque isn't fully canceled), but this is small and sluggish. Each propeller exerts ~510 Nm of torque reaction. A 10% torque difference yields ~51 Nm net roll moment, producing a roll acceleration of ~2.9 deg/s². That's not viable as primary flight control — it's too small and too slow due to propeller inertia.

**Implication:** Rudder can be sized for crosswind and spin recovery only (not engine-out), potentially allowing a smaller vertical tail and lower drag.

---

## The Safety Reality Check

Here's where the conversation gets serious.

Our safety team reviewed the FBW proposal and identified **10 critical gaps** that must be closed before you can safely put FBW primary controls in a manned aircraft:

1. **No FCC redundancy** — single flight control computer is a catastrophic single point of failure
2. **No sensor redundancy** — sidestick, AHRS, air data each single-channel
3. **Single CAN bus** — bus fault loses all actuator communication
4. **Clutch reliability unknown** — no failure-rate data or life testing for the OPV clutch
5. **Force-fighting synchronization unproven** — dual servos on the same horn need position-sync logic that hasn't been tested
6. **No EMI/lightning protection** — no shielding or surge suppression plan
7. **No software development rigor** — no flight-critical coding standards (e.g., MISRA C) or verification plan
8. **Pilot-strength assumptions** — no validation of required clutch-disengagement force (must be ≤40 lb per FAA guidance)
9. **Failure detection/annunciation** — how does the pilot know a servo has jammed or the FCC has failed?
10. **Single standby battery** — battery failure eliminates all FBW power

### What Failure Modes Look Like

**Mechanical controls** fail through break, jam, or wear — each is a single-point failure that can be catastrophic if not redundant.

**FBW controls** introduce new failure modes: loss of electrical power, flight-control-computer failure, sensor errors, software bugs, CAN-bus faults, and EMI susceptibility. The proposed mitigations (standby bus, dual-channel servos, OPV clutch) address **some** but not **all** of these.

**The OPV clutch is a cool idea, but:**
- Clutch fails to disengage (electrical/mechanical) → surface locked → **CATASTROPHIC**
- Clutch disengages inadvertently → loss of servo authority → **CONTROLLED** (if pilot can muscle through)
- Disengagement force exceeds pilot strength → **CATASTROPHIC**

You need prototype testing to validate clutch disengagement force, reliability data (MTBF) from Volz for aviation environments, and a fail-safe design (power-off state must be known).

---

## The Phased Migration Path

Here's the sensible approach:

### Phase 1 (First Flight): Mechanical Controls + ESP-X

- Conventional pushrods/cables to all surfaces
- Garmin G3X + ESP-X as stability augmentation
- Zero additional development risk
- Delivers envelope protection and LOC-I prevention
- **Everyone agrees this is the right first-flight configuration**

### Phase 2 (After Envelope Expansion): Electric Actuators on Secondary Surfaces

- Replace mechanical runs with electric actuators on **secondary surfaces first** (trim, flaps)
- Retain mechanical primary controls as backup
- Validate electrical integration, CAN bus, and FBW computer with non-critical surfaces

### Phase 3 (Optional, Later): Full FBW with Mechanical Reversion

- Full FBW with ArduPilot or custom ESP32-based flight control law implementation
- Mechanical controls retained as reversionary mode (via OPV clutch)
- **Do not proceed to Phase 3 until:**
  - Complete FMEA documented
  - Redundancy architecture eliminates all single points of failure
  - Prototype testing validates clutch performance and force requirements
  - Software development plan meets flight-critical standards
  - EMI/lightning protection plan defined

---

## What This Means for Homebuilders

If you're building a conventional tractor aircraft, mechanical controls are annoying but manageable. The FBW migration path exists, but you're fighting a legacy structure that was designed around cables and pushrods.

If you're building a pod-and-boom aircraft — especially one with centerline thrust — **the FBW migration path is genuinely cleaner.** The boom wants wiring, not pushrods. The centerline thrust eliminates engine-out yaw. The weight penalty is negative (FBW is lighter). The electrical architecture is straightforward.

**But don't underestimate the engineering work required for full FBW.** Phase 1 (ESP-X) is a free win. Phase 2 (electric actuators on secondary surfaces) is a reasonable experimental step. Phase 3 (full-authority FBW primary controls) is a **significant systems engineering problem** that requires redundancy, testing, and flight-critical software standards.

The technology is getting there. The pod-and-boom architecture is ready for it. But as of 2026, you're still building the proof-of-concept.

---

## The Board's Recommendation

**For MAOS v1.0:**
- Build Phase 1 (mechanical controls + Garmin ESP-X)
- This is safe, proven, and gives you envelope protection
- It's the low-risk path that still delivers the most critical FBW benefit: LOC-I prevention

**For MAOS v1.1 (or a future variant):**
- Treat full FBW as an upgrade path, not a first-flight feature
- Complete the redundancy design, FMEA, and prototype testing before committing
- Add **DG-013: FBW implementation strategy** as an open decision gate with explicit resolution criteria

**Bottom line:** The pod-and-boom architecture makes FBW **easier**, not harder. But "easier" doesn't mean "trivial." Do the engineering work. Test the assumptions. Build Phase 1 first.

---

## Further Reading

- **Volz Servos:** [volz-servos.com](https://volz-servos.com) (DA-30, DA-58, OPV variants)
- **Garmin ESP-X:** [garmin.com](https://www.garmin.com) (Electronic Stability Protection for G3X)
- **ArduPilot:** [ardupilot.org](https://ardupilot.org) (Open-source autopilot for fixed-wing, helicopter, multirotor)
- **FAA AC 20-27:** Certification and Operation of Amateur-Built Aircraft

---

**MAOS Design Review Board**  
CHAIRMAN, AERO, STRUCTURES, PROPULSION, SYSTEMS, SAFETY  
2026-03-26
