---
title: "Could In-Wheel Hub Motors Power an Aircraft Propeller?"
date: 2026-03-25T12:46:00Z
description: "Evaluating automotive in-wheel hub motors (Donut Labs 17\") vs aviation motors for MAOS rim-drive propulsion. When can automotive tech cross over to aviation?"
tags: ["propulsion", "motors", "rim-drive", "build-in-public", "component-evaluation"]
author: "Bill Mallard / MAOS Design Team"
draft: false
---

We're designing a hybrid-electric aircraft with an unusual propulsion architecture: rim-driven contra-rotating propellers mounted on booms behind the wing.

Instead of a traditional hub motor with the prop bolted to a shaft, the motor *is* the rim — the propeller blades attach directly to the outer ring of the motor, which spins around a stationary center. Think of it like a giant wheel, but instead of spokes and a tire, it's spinning motor magnets and propeller blades.

It's lighter, more efficient, and eliminates gearboxes. But it requires a very specific type of motor: high torque, large diameter, direct drive.

We've been planning to use **Beyond Aviation AXM3 axial-flux motors** — proven in electric aviation, but expensive (~€10k each) and moderately heavy (27 kg / 60 lbs).

Then someone asked:

**"What about in-wheel hub motors from the automotive world?"**

---

## What Are In-Wheel Hub Motors?

Most electric cars use a central motor connected to the wheels through a drivetrain (gears, axles, differentials). But some experimental EVs put the motor *inside the wheel itself* — eliminating the drivetrain entirely.

This is called an **in-wheel hub motor** or **wheel motor**, and it's exactly the same concept we're using for rim-drive propellers.

A few companies make them:
- **Donut Labs** (automotive performance, e-motorcycles)
- **Elaphe** (commercial vehicles, buses)
- **Protean Electric** (passenger cars, now defunct)

We decided to look at **Donut Labs** specifically, because:
1. They publish detailed specs openly
2. They're still in business and taking orders
3. Their 17" motor is in the right power/torque range for MAOS

---

## The Specs: Donut vs Beyond Aviation

Our baseline is the **Beyond Aviation AXM3**, which we know works in electric aircraft:
- **Peak power:** 220 kW (295 HP)
- **Continuous power:** 155 kW (208 HP)
- **Weight:** 27 kg (60 lbs)
- **Cooling:** Water-cooled
- **Efficiency:** ~95%
- **Cost:** ~€10,000
- **Aviation pedigree:** Flight-proven in multiple experimental electric aircraft

Donut Labs makes five motor sizes. Here's how they compare:

| Motor | Peak Power | Cont. (est) | Torque | Weight | Diameter | Cost (est) | Aviation Viability |
|-------|------------|-------------|--------|--------|----------|------------|-------------------|
| **Beyond AXM3** | **220 kW** | **155 kW** | — | **27 kg** | ~250 mm | **€10k** | ✅ **Baseline** |
| Donut 17" Enclosed | 150 kW | ~120-135 kW | 1200 Nm | 21 kg | 432 mm | €8-12k? | 🟡 **Maybe** |
| Donut 17" Open | 150 kW | ~120-135 kW | 1200 Nm | 21 kg | 432 mm | €8-12k? | 🟡 **Maybe** |
| Donut 21" | 630 kW | ~450 kW | 4300 Nm | 40 kg | 533 mm | High | ❌ **Too big** |
| Donut 12" | 15 kW | 12 kW | 300 Nm | 8 kg | 305 mm | Low | ❌ **Too small** |
| Donut 5" (drone) | 3 kW | 2.5 kW | 20 Nm | 1.5 kg | 127 mm | Low | ❌ **Toy** |

The **17" variants** are the interesting ones — slightly lower peak power than the AXM3, but **22% lighter** (21 kg vs 27 kg) and potentially cheaper.

---

## What Makes the 17" Compelling

**1. Weight savings**

At 21 kg vs 27 kg per motor, that's a **12 lb savings per motor**, or **24 lbs total** for our twin-motor setup.

In an aircraft where every pound matters, that's significant — especially since propulsion system weight sits far aft on the booms, affecting CG.

**2. Direct-drive torque**

The Donut 17" produces **1200 Nm of torque** continuously. That's enough to drive a large-diameter, slow-turning propeller directly — no gearbox needed.

Our current design uses a 2:1 reduction gearbox between the motor and the propeller. If the Donut can drive the prop directly, we save:
- Gearbox weight: ~8-12 lbs per side
- Gearbox complexity: no oil changes, no gear noise, no efficiency loss (~2-3%)
- Gearbox cost: ~$2,000 per unit

**3. High efficiency**

Donut claims **>95% efficiency**, which matches the AXM3. At the power levels we're operating (80-120 kW continuous), every percentage point of efficiency matters for range and cooling.

**4. Potentially lower cost**

Donut's motors are designed for automotive production volumes, not boutique aviation. If they're serious about scaling, the 17" might be cheaper than the AXM3 — though we don't have confirmed pricing yet.

---

## What Makes the 17" Risky

**1. No aviation heritage**

The Beyond AXM3 has flown in multiple electric aircraft prototypes. It has logged hours in the air. It's been validated for vibration, thermal cycling, altitude, and electromagnetic interference.

The Donut 17" has been used in:
- The Verge TS electric motorcycle
- WattEV semi-truck prototypes
- Some automotive demo projects

That's great for ground vehicles, but aircraft impose different stresses:
- **Vibration:** Constant, high-frequency vibration from propellers and airframe
- **Gyroscopic loads:** A spinning propeller creates massive gyroscopic forces during pitch/yaw maneuvers
- **Temperature extremes:** -40°F at altitude, 120°F on the ramp in Arizona
- **Duty cycle:** Continuous high-power operation for 2-3 hours, not 15-minute bursts

We don't know if the Donut can handle this. It might be fine. It might fail spectacularly after 100 hours. **We have no data.**

**2. Cooling integration**

The Donut is designed to be mounted *inside a wheel*, where it gets airflow from wheel rotation and ambient cooling from the tire/rim.

Our rim-drive propeller sits in a boom *behind* the wing, where airflow is more complex. We'd need to design:
- Custom cooling ducts
- Water-cooling integration (if the Donut supports it — some versions are air-cooled only)
- Thermal monitoring and management

The AXM3 is explicitly designed for water-cooling and has mounting interfaces for aircraft installations. The Donut would require custom engineering.

**3. Mounting and integration**

The Donut is designed to mount like a wheel hub — bolted to a fixed axle, with the outer rim spinning.

Our rim-drive prop is the same concept, but the mechanical interface is different:
- Propeller blade attach points
- Structural loads (thrust, bending, gyroscopic)
- Sealing against water/debris ingress
- Electrical connections in a rotating assembly

The AXM3 has standard aviation mounting patterns. The Donut would need custom adapters, which adds weight and complexity back into the system.

**4. Certification and support**

Beyond Aviation sells motors specifically for experimental aircraft. They understand aviation regulations, provide technical support, and have a supply chain for aviation customers.

Donut Labs sells motors for automotive/industrial use. If we have a problem, will they support an aviation application? If we need a replacement, can we get one in days instead of months?

For a one-off experimental aircraft, this might not matter. For a kit aircraft sold to builders, it's a serious concern.

---

## So... Should We Use the Donut?

**Not yet. But maybe eventually.**

Here's our current thinking:

### Short-term: Stick with the AXM3
- Proven in aviation
- Known integration
- Supplier support
- We can finish the design and start building

### Medium-term: Test the Donut as an upgrade path
- Order a Donut 17" for benchtesting
- Validate thermal performance under aircraft-like duty cycles
- Design a mounting adapter and test structural loads
- Run vibration and EMI testing
- If it passes → retrofit into MAOS v1.1 as a weight-saving upgrade

### Long-term: Push for aviation-rated in-wheel motors
- Work with Donut (or competitors) to develop aviation-specific versions
- Get them into the supply chain for experimental aircraft builders
- Publish data so other projects can use them

The *potential* weight savings (24 lbs motors + 16-24 lbs gearbox elimination = **40-48 lbs total**) are too significant to ignore.

But we're not going to gamble the entire propulsion system on an unproven motor just to save weight. We'll de-risk it first.

---

## Why This Matters Beyond MAOS

The automotive world is *way* ahead of aviation in electric motor development, for one simple reason: **volume**.

Tesla alone has built over 5 million electric motors. The entire electric aviation industry has built maybe a few thousand.

That volume gap means:
- Automotive motors are cheaper (economies of scale)
- Automotive motors are more advanced (more R&D investment)
- Automotive motors are more reliable (millions of test hours)

But aviation has different requirements — higher power density, longer continuous duty cycles, harsher environments, stricter safety margins.

**The question is: How do we adapt automotive technology for aviation without compromising safety?**

Some possibilities:
- Use automotive motors with aviation-specific cooling/mounting systems
- Work with automotive suppliers to create "aviation-rated" versions of existing designs
- Develop hybrid solutions — automotive motors with aviation-grade controllers and sensors

The Donut Labs 17" is a test case for this approach. If it works, it opens the door for other automotive components to cross over into aviation.

If it doesn't, we learn what *doesn't* transfer and refine the requirements.

---

## What Happens Next

We're putting the Donut on the "shortlist for future testing" list, but not blocking current development on it.

The design will proceed with the Beyond AXM3 as the baseline motor. Once we have a flying prototype, we can afford to experiment with alternatives.

But we'll keep watching the automotive world. Because the next breakthrough in aviation motors might not come from an aviation company at all.

---

**Want more technical deep dives?** Follow the MAOS project for regular updates on our design decisions, component evaluations, and lessons learned. We publish everything — including the mistakes.

**Next up:** How we're designing a water-cooling system for wing-mounted generators in a homebuilt aircraft.
