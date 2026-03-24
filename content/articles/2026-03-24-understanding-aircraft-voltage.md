---
title: "Understanding Electric Aircraft Voltage: Why 400V and What's the Deal with IGBTs vs SiC?"
date: 2026-03-24T14:36:00-06:00
description: "Plain-language guide to voltage choices in electric aviation, why aircraft aren't grounded like cars, and what IGBT vs SiC means for homebuilders."
tags: ["electric-aviation", "systems", "education", "voltage", "build-in-public"]
author: "Bill Mallard / MAOS Design Team"
draft: false
---

We just decided to use a 400-volt electrical system for the MAOS aircraft. If you're not an electrical engineer, that number might not mean much to you. Is 400 volts a lot? Is it safe? Why not 270 volts, or 800, or just use a car battery at 12 volts?

Then I found research about what's actually flying, and it opened up a whole new set of questions. The only type-certified electric aircraft in the world (Pipistrel Velis Electro) uses 345 volts and specifically chose "IGBT" power electronics over "SiC" because "the aircraft isn't grounded like a car."

What does *that* mean?

Let's break it down in plain language. No equations. No jargon left unexplained.

---

## What Is Voltage, and Why Does It Matter?

Think of electricity like water in a pipe.

- **Voltage** is the *pressure* pushing the water through the pipe
- **Current** (measured in amps) is *how much water* is flowing
- **Power** (measured in watts or kilowatts) is what you actually get done = voltage × current

If you want to deliver 100 kilowatts of power, you have two choices:

**Option A: High voltage, low current**
- 400 volts × 250 amps = 100 kW
- Thin wires (less current = less heat)
- Lighter, cheaper, easier to manage

**Option B: Low voltage, high current**
- 100 volts × 1,000 amps = 100 kW
- Thick heavy wires (high current = lots of heat)
- Heavier, more expensive, harder to manage

This is why your house uses 120 volts (or 240 volts) instead of 12 volts like your car battery. High voltage = efficient power delivery.

But there's a trade-off: **high voltage is more dangerous** and requires more careful insulation design.

---

## What Are Electric Aircraft Actually Using?

Here's what we found when we researched flight-proven electric aircraft:

### Light Aircraft (Our Class)
**Pipistrel Velis Electro** (the only type-certified electric aircraft)
- Voltage: **345 volts**
- Power: 57.6 kW (77 horsepower)
- What it is: Two-seat trainer, fully certified by EASA (European aviation authority)
- **Baseline:** This is the *only* electric aircraft that has gone through full certification. Everything else is experimental or in development.

**MAOS** (what we're building)
- Voltage: **400 volts**
- Power: 155 kW (208 horsepower) from dual motors
- What it is: Four-seat experimental aircraft, series hybrid (gas engines drive generators, electric motors drive props)

### Medium Power
**Bye Aerospace eFlyer 2**
- Voltage: **600 volts**
- Power: 90 kW (121 horsepower)

### Heavy / High-Performance
**magniX** (powers Eviation Alice, Harbour Air eBeaver)
- Voltage: **800 volts** — described by the company as "the highest voltage ever flown in an aircraft"
- Power: 350-650 kW (469-871 horsepower) depending on model

**Beta Technologies ALIA** (eVTOL cargo drone)
- Voltage: Estimated **800+ volts** (not publicly disclosed)
- Power: 426+ kW (572+ horsepower)

**Joby Aviation S4** (air taxi eVTOL)
- Voltage: Estimated **800+ volts** (company is secretive about specs)
- Power: Six distributed motors, ~200 kWh battery

---

## Why Three Voltage Tiers?

The pattern is clear: electric aviation has settled into the same voltage tiers as the automotive industry.

| Aircraft Class | Voltage | Why? |
|----------------|---------|------|
| **Light trainers** | 345-400V | Proven safe, manageable current, automotive EV components available |
| **Medium power** | 600V | Transition zone, less common |
| **Heavy / eVTOL** | 800V | State-of-the-art, requires custom engineering, pioneering territory |

This mirrors what happened in cars:
- Mass-market EVs (Tesla Model 3, Nissan Leaf): **~400 volts**
- High-performance EVs (Porsche Taycan, Lucid Air): **800 volts**

**We chose 400 volts because:**
1. It's proven by the only certified electric aircraft (Pipistrel at 345V)
2. It's a modest step up (55 volts higher) for our higher power needs
3. We're not pioneering unproven voltage territory
4. Massive component ecosystem from the automotive EV industry

---

## How Does MAOS Compare to Pipistrel?

Let's put the numbers side by side:

| | Pipistrel Velis | MAOS |
|---|-----------------|------|
| **Voltage** | 345V | 400V (16% higher) |
| **Total power** | 57.6 kW | 155 kW (2.7× more) |
| **Motors** | 1 | 2 (redundancy) |
| **Power per motor** | 57.6 kW | 77.5 kW (35% more per motor) |
| **Current flow** | ~167 amps | ~375 amps |

**What this means:**
- We're not jumping from 345V to 800V (that would be pioneering)
- We're going from 345V to 400V (modest, proven step)
- Our power increase (2.7×) comes mostly from *adding a second motor* for redundancy, not from pushing each motor way beyond what's been proven
- Each of our motors is only 35% more powerful than Pipistrel's certified motor

This is conservative engineering. We're scaling up proven technology, not inventing new territory.

---

## Why Aircraft Voltage Is Different from Cars: The Grounding Problem

Here's where it gets interesting. When we looked at why Pipistrel chose 345 volts and specific power electronics, we found this quote:

> "The aircraft isn't grounded like a car, so keeping currents manageable and EMI low is critical."

What does "grounded" mean, and why does it matter?

### Cars Are Grounded
When you drive a car:
- The car body (chassis) is connected to the battery's negative terminal
- The tires touch the road (which eventually connects to literal ground through moisture/conductivity)
- If an electrical fault happens (wire touches the chassis), current can flow through the car body to ground safely
- This is why jumper cables have one clamp on the battery and one on "any metal part" — the whole chassis is part of the electrical circuit

### Aircraft Are NOT Grounded
When you fly an aircraft:
- The aircraft is surrounded by *air* (an insulator — electricity can't flow through it)
- Rubber tires prevent any connection to ground even when parked
- The aircraft is **electrically isolated** — floating in space with no path for current to flow to ground
- If an electrical fault happens, there's nowhere for the current to go except *through the aircraft structure* or *through a person touching the wrong thing*

**This changes everything about electrical safety in aircraft.**

---

## What Happens at Altitude?

The problem gets worse as you climb:

### Air Density Drops
- At sea level: air is relatively dense (acts as okay insulation)
- At 17,500 feet (our cruise altitude): air density is ~55% of sea level
- **Thinner air = worse insulator**
- High voltage can "jump" across gaps more easily (called "corona discharge" or "arcing")

### EMI Becomes Critical
**EMI = Electromagnetic Interference** — unwanted electrical noise that can mess with radios, GPS, autopilots, and other electronics.

In a car:
- EMI is annoying (might interfere with your radio)
- The metal chassis acts as a shield
- You can ground noisy components to the chassis

In an aircraft:
- EMI can interfere with **navigation, communication, and flight-critical systems**
- The aircraft structure is not a good ground reference (it's floating)
- You have to design the electronics to produce less EMI in the first place

**This is why Pipistrel made different choices than a car manufacturer would.**

---

## IGBTs vs SiC: What's the Difference?

These are two types of *power switching devices* — the electronic components that control how electricity flows from the battery to the motor.

Think of them like extremely fast, high-power light switches. To make an electric motor spin, you need to switch the power on and off thousands of times per second in precise patterns. These switches do that job.

### IGBT (Insulated-Gate Bipolar Transistor)
**Technology:** Mature, developed in the 1980s, widely used in trains, industrial machinery, and electric vehicles

**Characteristics:**
- Switches relatively slowly (~20 kHz typical)
- Generates more heat (less efficient)
- Produces **lower EMI** (slower switching = less electrical noise)
- Well understood, proven reliability
- Cheaper

**Think of it like:** A heavy-duty mechanical relay — robust, reliable, but not the fastest

### SiC (Silicon Carbide MOSFET)
**Technology:** Newer, higher-performance, used in modern performance EVs (Porsche Taycan, Tesla Model 3 after 2021)

**Characteristics:**
- Switches very fast (~100+ kHz capable)
- More efficient (less heat = less cooling needed = weight savings)
- Produces **higher EMI** (fast switching = more electrical noise)
- Still maturing in aviation applications
- More expensive

**Think of it like:** A high-speed electronic switch — faster and more efficient, but generates more electrical noise

---

## Why Pipistrel Chose IGBTs for Their Certified Aircraft

From the engineering team's explanation:

**"The aircraft isn't grounded, so keeping currents manageable and EMI low is critical."**

Translation:
1. **No ground reference** means EMI can't be dissipated to ground like in a car — it radiates into the aircraft structure and can interfere with avionics
2. **Slower switching (IGBTs)** produces less EMI than fast switching (SiC)
3. **Lower EMI** = less risk of interfering with radios, GPS, autopilot
4. At 345 volts, the efficiency loss from IGBTs vs SiC is acceptable — they can cool the electronics adequately

**They traded efficiency for electrical quietness and proven reliability.**

This is **conservative engineering** — choosing the less cutting-edge technology that has decades of proven track record in safety-critical applications.

---

## What About 800V Aircraft? Why Do They Use That Voltage?

The magniX systems (powering the Eviation Alice and other aircraft) operate at 800 volts. According to the company, this is **"the highest voltage ever flown in an aircraft."**

Why so high?

**Power density.** When you need 500-650 kW (671-871 horsepower), staying at 400 volts means:
- 400V × 1,625 amps = 650 kW
- **1,625 amps is a LOT of current**
- Wiring becomes extremely heavy
- Cooling becomes a major challenge

At 800 volts:
- 800V × 813 amps = 650 kW
- Half the current = much lighter wiring
- More manageable heat dissipation

**But it comes with serious engineering challenges:**

### 1. Corona Effects
At 800 volts and altitude, electrical fields can be strong enough to ionize the thin air around conductors, creating **corona discharge** — a glowing purple haze around wires that:
- Wastes power
- Erodes insulation
- Produces ozone (which further erodes insulation)
- Generates EMI

**Solution:** Careful conductor spacing, special insulation materials, extensive creepage/clearance analysis

### 2. Custom Connectors Required
From the magniX case study:
> "They went through a dedicated connector development program with their supplier to handle 800V at altitude."

Standard automotive EV connectors (rated for 400-600V at sea level) are not adequate for 800V at 17,500 feet where air density is 55% of sea level.

**Solution:** Custom-engineered connectors, rigorous altitude testing

### 3. Insulation Breakdown
High voltage at low air density increases risk of **dielectric breakdown** — when insulation fails and electricity jumps across a gap.

**Solution:** Increased creepage distances (surface path length) and clearance distances (air gap) throughout the system

---

## So Why Did We Choose 400V for MAOS?

Here's our logic:

### 1. We're in the Light Aircraft Class
- Our power requirement: 155 kW (208 HP)
- Pipistrel (certified): 57.6 kW (77 HP) at 345V
- We need 2.7× more power, achieved by doubling motors + modest per-motor increase
- 400V is appropriate for this power class

### 2. Proven Technology
- Pipistrel proves ~400V works and is certifiable
- We're only 55 volts higher than the certified baseline
- Not pioneering unproven voltage territory like 800V aircraft

### 3. Component Availability
- Massive automotive EV ecosystem at 400V (Tesla, GM, Ford, VW all use ~400V)
- Inverters, motor controllers, contactors, connectors all readily available
- No custom connector development required
- Lower cost, faster procurement

### 4. Manageable EMI and Insulation Challenges
- 400V stays below the threshold where corona effects become major concerns
- Can use conservative power electronics (IGBT or SiC — we have choices)
- Standard automotive HV safety practices apply
- Pipistrel demonstrates that automotive-derived components work in this voltage range

### 5. Future-Proofing
- Room to grow electrical loads in v1.1 (pressurization, electric heat, etc.)
- But not so high that we're in pioneering territory
- Can use emerging electric aircraft charging infrastructure (CCS standard up to 1,000V)

---

## What Current Is Actually Flowing at 400V?

Let's make this concrete with our actual numbers:

**MAOS at cruise:**
- Power required: ~120-130 kW (motors running at ~80% power)
- Voltage: 400V
- Current: 130,000 watts ÷ 400 volts = **325 amps**

**MAOS at max continuous:**
- Power: 155 kW (motors at 100%)
- Voltage: 400V
- Current: 155,000 watts ÷ 400 volts = **388 amps**

**For comparison, if we used 270V (the other option we considered):**
- Same 155 kW power
- 270V
- Current: 155,000 ÷ 270 = **574 amps**

**What this means:**
- 400V: 388 amps — manageable with automotive-grade wiring
- 270V: 574 amps — would require heavier wiring (more weight, more heat)

The ~200 amp reduction by going to 400V saves us about **10 pounds** in wiring weight.

---

## Safety: Is 400V Dangerous?

Short answer: **Yes, but it's manageable with proper training and procedures.**

### The Reality Check
- Your house: 120V (or 240V) can kill you
- Car battery: 12V — generally safe to touch
- Electric car: 400V — **lethal if mishandled**
- MAOS: 400V — same danger level as any EV

### How We Make It Safe

**1. Color Coding**
- All high-voltage wiring: **bright orange** (industry standard)
- Immediately obvious which components are dangerous
- Follows SAE J1673 automotive HV standards

**2. Service Disconnect**
- Big obvious switch that isolates the entire HV system
- **Lockout/tagout procedures** — physical lock on the disconnect when working on the system
- Only one person has the key

**3. Insulation Monitoring**
- Electronic system that constantly checks insulation integrity
- Detects ground faults before they become dangerous
- Shuts down system if insulation degrades

**4. Dual-Redundant Contactors**
- Contactors = heavy-duty high-voltage relays
- Two in series on main power paths
- If one fails closed, the other can still disconnect power

**5. Training**
- Builder (me) will complete high-voltage electrical safety training
- Same training automotive EV technicians take
- Arc flash protection equipment, proper test procedures

**6. It's an Experimental Aircraft**
- I'm the builder, maintainer, and pilot
- I'm the only one who will work on the HV system
- No mechanics, no passengers touching HV components

**This is no different than building a Tesla powertrain into a kit car** — homebuilders have been doing high-voltage conversions for years. It requires respect and proper procedures, but it's well within experimental aircraft builder capability.

---

## What's Next?

Now that voltage is decided, we can:

1. **Specify generator heads** — Beyond Motors AXM2 with 400V output winding
2. **Source motor controllers** — Evaluate Cascadia Motion, Tesla aftermarket, others at 400V
3. **Design wiring harness** — Now that we know current levels (388 amps max)
4. **Develop HV safety procedures** — Lockout/tagout, insulation testing, arc flash protection
5. **Choose IGBT vs SiC** — Based on EMI testing with actual motor controllers

The voltage decision unlocks all downstream electrical design work.

---

## Lessons Learned

**1. Always look at what's actually flying.**
Theory is great, but Pipistrel's certified aircraft at 345V told us more than any textbook.

**2. Aircraft electrical design is different from automotive.**
The lack of grounding and altitude effects create unique challenges. Don't just copy a car.

**3. Conservative scaling is smart.**
Going from 345V to 400V with dual motors is safer than jumping to 800V with a single massive motor.

**4. Voltage tiers exist for good reasons.**
Light/medium/heavy aircraft use different voltages because the engineering challenges scale non-linearly.

**5. Component ecosystems matter.**
400V gives us access to thousands of automotive EV parts. 800V would force us to pioneer custom solutions.

---

## Questions?

This is complex stuff, and I'm learning as I go. If anything is unclear or you have questions, let me know. I'll update this article as we learn more.

The whole point of building this aircraft in public is to share what we learn — the good decisions, the mistakes, and everything in between.

Next up: engine selection (Honda 400cc vs Kawasaki I4 turbo — that's a whole other article).

---

*MAOS is an experimental aircraft project. Nothing in this article constitutes professional engineering advice. High-voltage electrical systems can be lethal. Always consult qualified professionals and follow proper safety procedures.*

---

**Further Reading:**
- [Design Decision D-001: 400V Electrical System](../2026-03-24-voltage-decision-400vdc/)
- Pipistrel Velis Electro technical specifications
- magniX high-voltage aviation powertrains
- SAE J1673: High Voltage Safety Standards
