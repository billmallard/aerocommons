---
title: "The Silent Killer: Why Electric Motor Cooling Is Mission-Critical in Aircraft"
date: 2026-03-26T00:08:00-06:00
description: "Permanent magnet demagnetization is silent, invisible, and permanent — and it's completely preventable if you design the cooling system correctly."
tags: ["propulsion", "systems", "design-decisions", "analysis"]
author: "AeroCommons Design Board"
draft: false
---

In traditional aircraft engines, overheating gives you warning. The oil pressure gauge drops. The cylinder head temperature climbs. The engine starts running rough. You have *minutes* to diagnose and land before catastrophic failure.

In an electric motor, the most dangerous failure mode is completely silent.

The motor keeps running. The gauges look normal. But deep inside the rotor, the permanent magnets are quietly, irreversibly losing their strength. By the time you notice reduced performance, the damage is done. Permanent.

This is **demagnetization** — and it's why electric aircraft motor cooling deserves the same engineering respect as your electrical system architecture.

---

## What Are We Actually Cooling?

Electric motors generate heat from three main sources:

1. **Resistive losses** in the copper windings (I²R heating)
2. **Eddy current losses** in the stator laminations
3. **Mechanical losses** from bearings and air friction

In a high-performance aircraft motor like the Beyond Aviation AXM3 (155 kW continuous), even at 95% efficiency, you're rejecting **~8 kW of waste heat** at cruise power.

That's 8,000 watts. Continuously. For hours.

In an internal combustion engine, about 30% of waste heat exits through the cooling system, 30-40% through the exhaust, and the rest radiates away. The cooling system is just one of several thermal pathways.

**In an electric motor, the cooling system is the *only* thermal exit.** Every watt of waste heat must leave through the coolant. There's no exhaust. There's no backup.

If the cooling system fails, the motor has nowhere to shed heat.

---

## The Magnet Problem

Modern high-performance electric motors use **neodymium-iron-boron (NdFeB) permanent magnets** in the rotor. These magnets are phenomenally strong — which is why they enable such high power density.

But they have a weakness: **temperature**.

### Curie Temperature vs. Operating Temperature

The **Curie temperature** is the point at which a magnet completely loses its ferromagnetic properties — the atomic magnetic domains randomize, and the material stops being magnetic.

For NdFeB magnets, the Curie temperature is around **310-400°C** depending on the grade.

So that's fine, right? We just need to keep the motor below 300°C and we're good?

**No.**

Long before you hit the Curie temperature, the magnets start to **partially demagnetize** — and this damage is **irreversible**.

### Maximum Operating Temperatures by Grade

Different grades of NdFeB magnets have different maximum operating temperatures — the temperature above which you start losing magnetism permanently:

| Grade | Max Operating Temp | Curie Temp | Typical Use |
|-------|-------------------|------------|-------------|
| N (standard) | 80°C | 310-340°C | Consumer electronics, low-duty motors |
| M/H | 100-120°C | 340°C | Industrial motors, moderate duty |
| SH | 150°C | 340°C | High-performance automotive |
| UH | 180°C | 350°C | Aerospace, high-temp industrial |
| EH | 200°C | 350°C | Aerospace, extreme environments |
| AH/TH | 230°C | 350-370°C | Military, extreme aerospace |

Notice the gap between *max operating temperature* and *Curie temperature*. That gap is where **partial, progressive, irreversible demagnetization** happens.

If you run a standard N-grade magnet at 100°C for extended periods, it will slowly lose strength. After 100 hours, it might be down to 95% of rated strength. After 500 hours, maybe 90%. After 1,000 hours, 85%.

**And you won't know until you need full power and it's not there.**

---

## Why Aviation Makes This Worse

Electric aircraft motors face thermal stresses that automotive motors don't:

### 1. **Continuous High-Power Operation**

A Tesla motor runs at high power for 10-15 seconds during acceleration, then cruises at 20-30% power. Cooling system design is optimized for short bursts.

An aircraft motor runs at **70-80% continuous power for 2-3 hours** during cruise. There's no coasting. There's no regenerative braking to give the motor a thermal break.

If your cooling system is undersized by even 10%, the motor temperature will climb slowly but steadily over a multi-hour flight.

### 2. **Altitude Effects**

At 17,500 feet, the air density is about 50% of sea level. Your radiator's cooling capacity drops proportionally.

If your cooling system has a safety margin at sea level but none at altitude, you'll discover this the hard way during a long cruise climb on a hot day.

### 3. **Ambient Temperature Variation**

Ground operations on a 100°F Arizona ramp. Cruise at -20°F at 15,000 feet. Descent back into hot air. Your cooling system has to handle this thermal cycling without allowing the rotor magnets to spike above their rated temperature at any point in the flight.

### 4. **The Rotor-Stator Temperature Gradient**

Here's the really insidious part: **you can't directly measure rotor temperature in most motors**.

You can measure:
- Coolant inlet temperature
- Coolant outlet temperature  
- Stator winding temperature (if the motor has embedded thermocouples)

But the rotor is spinning. It's hard to get a sensor on it. And the rotor magnets are typically **20-40°C hotter than the coolant outlet temperature** during high-power operation.

So if your coolant outlet is reading 90°C and you think you're fine because your motor is rated to 120°C, **your rotor magnets might actually be at 130°C** — already into the demagnetization zone.

---

## The Failure Mode That Keeps Me Up at Night

Imagine this scenario:

You're cruising at 15,000 feet on a hot summer day. Your coolant outlet temperature gauge reads 85°C — within limits. The motor sounds fine. No vibration. No alarms.

But 1,000 feet below you, a single coolant pump bearing is starting to fail. The flow rate is dropping by 5%. You don't notice — the flow sensor, if you even have one, is still showing "normal" because 95% flow looks almost the same as 100% flow.

The rotor temperature climbs from 110°C to 120°C. Still below the alarm threshold. The motor keeps running.

Over the next 30 minutes, the SH-grade magnets (rated to 150°C) are experiencing 120°C continuously. At that temperature, they're losing about 0.5% of their magnetism per hour.

It's not catastrophic. It's not even noticeable. But it's **permanent**.

Three hundred flight hours later, your motors are delivering 90% of rated torque. You don't notice in cruise because you're rarely at full power. But on a hot day at a high-density altitude airport, when you need full power for takeoff, the motors can't deliver. You abort the takeoff.

You send the motor in for inspection. The technician says: "The windings are fine. The bearings are fine. But the magnets are weak. This motor has been run too hot. There's nothing we can do. You need a new rotor assembly."

**That's a $15,000 repair.**

And the worst part? You had no idea it was happening.

---

## How to Design Around This

The MAOS cooling philosophy is built around one principle: **never let demagnetization happen, because you can't undo it**.

### 1. **Conservative Temperature Targets**

- **Target:** 85°C coolant outlet at continuous cruise power
- **Warning:** 90°C (reduce power, investigate)
- **Auto-derate:** 95°C (controller automatically reduces motor current to prevent further heating)
- **Shutdown:** 105°C (only if auto-derate fails)

These targets assume a 30°C gradient between coolant outlet and rotor magnets, meaning:
- 85°C coolant = ~115°C rotor magnets (safe margin below 150°C for SH-grade)
- 95°C coolant = ~125°C rotor magnets (still safe, but investigating)

### 2. **Dual Redundant Coolant Pumps**

Each motor has **two coolant pumps** in the same loop — primary and backup, with automatic switchover on flow loss.

This is not weight creep. This is not over-engineering.

A coolant pump weighs ~2 lbs and costs $300. A replacement rotor assembly weighs 20 lbs and costs $15,000. And if you lose cooling during flight, you're not just risking the motor — you're risking the aircraft.

**The second pump is not optional.**

### 3. **Flow Monitoring, Not Just Temperature**

Temperature tells you when something is already wrong. Flow rate tells you when something is *about to be* wrong.

If coolant flow drops from 10 L/min to 8 L/min, your temperature might only rise 5°C — not enough to trigger an alarm. But over a 2-hour flight, that 5°C difference is the boundary between safe operation and progressive demagnetization.

Monitor flow rate. Set alarms. Treat flow loss as seriously as you would oil pressure loss in a piston engine.

### 4. **Design for Altitude Cooling**

Size your radiator for **worst-case altitude, not sea level**.

If you need 8 kW of cooling at 17,500 feet with 50% air density, your radiator needs to be twice the size of one that would work at sea level.

Yes, this adds weight. Yes, this adds drag. But the alternative is motors that work great on the test stand and fail at altitude.

### 5. **Magnet Grade Selection**

For MAOS, we're specifying **SH-grade or better** NdFeB magnets (150°C max operating temperature).

Standard N-grade (80°C max) is not viable for continuous aviation duty. Even M/H grade (120°C max) is marginal.

The cost difference between N-grade and SH-grade magnets is about 30-40%. For a motor that costs $10,000, that's an extra $3,000-4,000.

**Worth every penny.**

### 6. **Thermal Soak Testing**

Benchtop motor testing must include **continuous high-power thermal soak runs** — 2+ hours at 70-80% rated power with coolant temperature stabilized.

Peak power testing tells you if the motor works. Thermal soak testing tells you if the motor *survives*.

If your motor can't hold 85°C coolant outlet temperature for 3 hours straight at cruise power on the test bench, it won't survive a cross-country flight.

---

## What About SmCo Magnets?

**Samarium-cobalt (SmCo) magnets** have much better thermal stability than NdFeB:
- Curie temperature: 700-800°C
- Max operating temperature: up to 310°C
- Much more resistant to demagnetization

So why doesn't everyone use them?

**Lower magnetic strength.** SmCo has about 70-80% the magnetic flux density of NdFeB. That means a motor with SmCo magnets is heavier and larger for the same power output.

For aerospace, where weight is everything, the trade-off usually favors NdFeB with aggressive cooling over SmCo with relaxed cooling.

But SmCo is a valid choice for applications where thermal margin is more important than weight — for example, motors mounted in hot engine bays or near exhaust systems.

---

## Detection: Can You Tell If Demagnetization Is Happening?

Yes, but it's not easy.

### Indirect Indicators:
- **Torque ripple increase** — demagnetization is rarely uniform, so one pole weakens before others
- **Efficiency drop** — weaker magnets mean more current needed for the same torque
- **Back-EMF reduction** — if you can measure the motor's generated voltage during spin-down, a drop indicates weaker magnets

### Direct Measurement:
- **Flux linkage testing** — measure the magnetic flux through the stator coils with the rotor stationary
- **Gauss meter testing** — physically measure magnet strength (requires motor disassembly)

The problem: **all of these methods require either specialized test equipment or motor disassembly**.

There is no cockpit gauge that says "your magnets are at 92% strength."

**Prevention is the only practical strategy.**

---

## The Lesson for Builders

If you're designing or building an electric aircraft, **take motor cooling as seriously as electrical system design**.

It's not enough to slap a radiator on and call it good. You need:
- Conservative temperature targets with margin for altitude and aging
- Redundant pumps (or at least a pump failure detection system)
- Flow monitoring, not just temperature monitoring
- High-temperature magnet grades matched to your duty cycle
- Validation testing under sustained cruise power conditions

Electric propulsion has enormous promise — higher efficiency, lower noise, simpler maintenance, fewer moving parts.

But **"simpler" doesn't mean "easier"**. The failure modes are different. The design priorities are different. The testing requirements are different.

Demagnetization is silent. It's invisible. It's permanent.

And it's completely preventable if you design the cooling system correctly the first time.

---

## What We're Doing on MAOS

Our motor cooling design targets:
- **85°C coolant outlet** continuous (30°C margin to rotor demagnetization threshold)
- **Dual redundant pumps** per motor loop with auto-switchover
- **Flow + temperature monitoring** with graduated warnings (90°C alert, 95°C auto-derate)
- **SH-grade NdFeB magnets** minimum (150°C max operating temp)
- **Radiator sized for 17,500 ft** with sea-level margin
- **3-hour benchtop thermal soak** validation before first flight

We're treating the cooling system as **flight-critical** — not an accessory, but a primary system on par with the electrical bus and the flight control surfaces.

Because in an electric aircraft, if you lose cooling, you lose propulsion. Maybe not immediately. Maybe not catastrophically. But silently, progressively, permanently.

And we'd rather overdesign the cooling system than underdesign the mission.

---

**Want to follow along?** We publish our design decisions, technical analyses, and lessons learned as we go. Check out the MAOS project documentation or join the discussion.

**Next in this series:** Electrical bus cross-tie architecture — why one wire can make the difference between a manageable failure and a forced landing.
