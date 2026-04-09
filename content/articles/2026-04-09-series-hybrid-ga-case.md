---
title: "The Case for Series Hybrid Propulsion in General Aviation"
date: 2026-04-09T07:00:00-05:00
description: "Most GA pilots dismiss hybrid-electric aviation as limited-range experimentation. The series hybrid architecture is something different — and its redundancy, efficiency, and performance arguments deserve a serious look."
tags: ["propulsion", "hybrid-electric", "design-decisions", "analysis", "electric-aviation", "maos"]
author: "AeroCommons Design Board"
project: "maos"
article_type: "analysis"
draft: false
---

The word "hybrid" in aviation conjures something unpleasant: heavy battery packs, 45 minutes of endurance, regulatory uncertainty, and the vague implication that you're flying an appliance. That image comes from pure-electric aircraft and their compromises. A series hybrid powertrain is architecturally different from a pure-electric aircraft in ways that matter enormously — and conflating the two has kept most GA pilots from seriously evaluating an architecture that has real advantages over conventional piston propulsion.

---

## What a Series Hybrid Actually Is

In a series hybrid, the internal combustion engine never drives the propeller. It drives a generator. The generator feeds a DC electrical bus. The bus powers electric motors that turn the props. A battery pack connects to the same bus as a parallel reservoir — it is not a gateway between the engine and the motors.

There is no mechanical link between the ICE and the propeller. Every element between ignition and thrust is electrical.

This is not a new concept. Diesel-electric locomotives have used this exact architecture since the 1930s. The diesel engine runs at its optimal RPM regardless of train speed or load. The electric motors provide variable torque on demand without transmission losses. Modern diesel-electric freight locomotives are among the most reliable prime movers ever built — TBOs measured in decades, not years.

The GA application adds one element: a battery buffer. The battery smooths transient load demands, provides an emergency reserve if the ICE fails, and enables boost power during takeoff and climb by contributing while the ICE simultaneously runs at its rated output.

Power flow in the MAOS 1G+1B+2M architecture:

```
[ICE Engine — constant speed, constant load]
                 |
       [Generator — AFPM / wound field]
                 |
           [400V DC Bus]
           |           |
       [Battery]    [Load]
        contactor
           |
      [400V DC Bus]
                 |
         +-------+-------+
         |               |
    [Controller 1]  [Controller 2]
         |               |
    [Motor 1]        [Motor 2]
```

The battery is a parallel tap. If it fails or is isolated, the generator continues powering the motors directly. There is no single point of failure that silences the propeller.

---

## The Redundancy Argument

A conventional single-engine piston has one meaningful propulsion failure mode: the engine stops. Everything downstream — prop, reduction drive, FADEC — is mechanically joined. If the crankshaft stops turning, the aircraft becomes a glider.

In 1G+1B+2M, the failure matrix is qualitatively different:

| Failure Event | Operational Mode | Capability |
|---|---|---|
| Normal | Full hybrid | Full power, battery buffer active |
| Battery isolated | Generator-direct | Cruise power, stable voltage, no reserve |
| ICE / Generator failure | Battery-only | 30 min at emergency power |
| Single motor failure | One motor | ~60% thrust, reduced cruise |
| Battery fail + single motor | Generator → one motor | Reduced thrust, continue to destination |
| ICE fail + single motor | Battery → one motor | 30 min, reduced thrust |
| Both motors fail | None | Glide |
| ICE fail + both motors fail | None | Glide |

Two simultaneous independent failures are required before the aircraft becomes a glider. That is materially different from a conventional single, where one failure produces that outcome.

The comparison is not against a certified twin — it is against the actual aircraft most pilots building high-performance experimentals would otherwise fly: a single-engine IFR machine where engine failure ends in a field. Against that baseline, the architecture is a genuine step forward.

There is also a subtler reliability argument. Electric motors have different failure modes than piston engines — and categorically fewer of them. Bearing MTBF in industrial motors runs 10,000–20,000 hours. Windings in properly sized continuous-duty motors: 30,000–50,000 hours. There are no intake valves, carburetors, magnetos, or mixture controls. Failure modes are largely progressive rather than sudden, and they announce themselves through vibration and thermal monitoring before they cause a loss of thrust.

The ICE in a series hybrid runs at one power setting for generator duty. No throttle jockeying, no power changes, no enrichment during descent. Constant-speed, constant-load operation is demonstrably easier on an engine than variable-load flight. TBO for engines operated at constant conditions consistently exceeds equivalent flight-cycle TBOs.

---

## The Performance and Efficiency Argument

A piston engine in direct-drive application must be run at whatever power the flight regime demands — high for climb, low for cruise, full for takeoff. SFC varies significantly across that range. The efficient 65–75% power band is rarely where the flight profile actually wants the throttle.

In a series hybrid, the ICE output is decoupled from instantaneous thrust demand. During climb, the motors draw additional power from the battery while the ICE runs at its rated continuous output. During cruise, the ICE charges the battery while the motors consume exactly what the flight requires. The battery absorbs the difference in all directions.

The ICE can always run where it is most efficient. For a turboshaft, this is particularly significant — turbines have strong SFC characteristics at a specific power fraction, and in direct-drive application you'd rarely sustain that point. In generator duty, you set it and leave it.

Electric motors also provide essentially flat torque curves from zero RPM. There is no throttle lag. In turbulence, the motor controllers absorb load transients without the engine ever seeing them. Commanded power changes are near-instantaneous, which changes how the aircraft responds to gust loads and pilot inputs.

---

## Two Paths for MAOS

Series hybrid is MAOS's closed architecture decision. The open question is which ICE provides the best match for the intended mission. Two candidates define the two ends of the design space.

### Path 1: Rotax 915 iS Turbo

The Rotax 915 iS produces 141 hp (105 kW) at max continuous, maintains rated power to FL150 through its integral turbocharger, and runs on 100LL or Mogas.

In MAOS generator duty:

| Attribute | Value |
|---|---|
| Engine weight | ~176 lbs |
| Max continuous power | 141 hp / 105 kW |
| Fuel burn at 75% generator load | ~7 GPH |
| Fuel type | 100LL or Mogas |
| Acquisition cost | ~$35,000 new |
| TBO | 2,000 hours |
| Max altitude (rated power) | FL150 |
| Estimated MAOS cruise (retractable gear) | ~200 KTAS SL / ~230 KTAS TAS at FL150 |

The retractable gear performance projection deserves emphasis. MAOS with fixed gear is a 155 KTAS aircraft on this engine. With retractable gear, removing the dominant drag item — landing gear represents approximately 31% of total cruise drag in the fixed-gear baseline — the same Rotax pushes the same airframe to approximately 200 KTAS at sea level. For reference, the Pipistrel Panthera — a 4-seat retractable composite aircraft and the most directly comparable configuration — achieves ~199 KTAS, but does so on a Lycoming IO-540 producing approximately 235 hp. MAOS approaches the same cruise speed at 141 hp on a Rotax 915, a 40% reduction in horsepower. No production 4-seat aircraft powered by a Rotax has reached this speed class.

The Rotax path is the MAOS P1 design basis. It produces a capable, efficient aircraft at a weight and cost that a single builder can design, build, and operate. Five hours of fuel is 35 gallons — 210 lbs. The mission radius is genuine IFR cross-country territory.

### Path 2: Allison M250-C18 Turboshaft

The M250-C18 is the turboshaft variant of the Allison 250 series — the powerplant behind the Bell JetRanger, MD500, and dozens of other turbine helicopters across forty years of production. It produces 317 shp (236 kW), weighs 138 lbs dry, and burns Jet-A.

In the certified aircraft market, this engine costs several hundred thousand dollars. In the overhauled general aviation aftermarket — supported by decades of helicopter operations and one of the largest engine parts ecosystems in existence — it is available for **$15,000–$40,000 overhauled.** That is comparable to a mid-time piston engine. It is the most accessible turbine powerplant available to an experimental builder, by a wide margin.

In MAOS generator duty at 70% power:

| Attribute | Value |
|---|---|
| Engine weight | **138 lbs** |
| Max continuous power | 317 shp / 236 kW |
| Fuel burn at 70% generator load | ~22–24 GPH |
| Fuel type | Jet-A |
| Acquisition cost | $15,000–$40,000 overhauled |
| TBO | 3,500 hours |
| Max altitude (rated power) | FL250+ |
| Estimated MAOS cruise | ~250 KTAS |

The M250-C18 is actually *lighter* than the Rotax 915 at 138 lbs vs. 176 lbs. The turbine's weight advantage over the piston is real. The penalty is fuel consumption — the turbine burns 3–4× as much.

---

## The Fuel Weight Reality

Jet-A is cheaper per gallon than avgas. The turbine burns enough more of it to erase that advantage quickly. For the same mission:

**500 NM IFR mission with 45-minute reserves:**

| | Rotax 915 | M250-C18 | Delta |
|---|---|---|---|
| Time aloft | ~3.9 hrs | ~3.0 hrs | Turbine saves 55 min |
| Fuel burned | ~27 gal | ~72 gal | |
| Fuel weight | ~162 lbs | ~492 lbs | **+330 lbs turbine** |
| Fuel cost (est.) | ~$148 | ~$432 | |

**850 NM solo mission with 45-minute reserves:**

| | Rotax 915 | M250-C18 | Delta |
|---|---|---|---|
| Time aloft | ~6.1 hrs | ~4.5 hrs | Turbine saves 1.6 hrs |
| Fuel burned | ~43 gal | ~107 gal | |
| Fuel weight | ~258 lbs | ~731 lbs | **+473 lbs turbine** |

Carrying 330–475 lbs of additional fuel for the same destination has structural consequences that compound. Heavier fuel load requires stronger structure. Stronger structure adds empty weight. Higher MTOW requires more lift, which adds induced drag, which requires more thrust, which burns more fuel. The turbine requires a fundamentally larger aircraft to be designed properly — not as an upgrade to the Rotax-based MAOS, but as a different vehicle from the start.

---

## The Turbine Variant Is a Different Aircraft

The M250-C18 option is not a bolt-in engine upgrade. At 250 KTAS cruise, 317 shp available, and rated power to FL250+, a turbine-powered MAOS occupies the performance envelope of a cabin-class turboprop. At a fraction of a percent of the new acquisition cost of a TBM 960, it represents access to performance and reliability that has historically required a seven-figure budget.

The M250-C18's aftermarket availability is the enabling condition. No other turbine with comparable power output and weight is accessible at this price point to an experimental builder. It is a legitimate design opportunity that belongs on the roadmap.

Building it correctly means accepting the weight budget and structural implications that follow. The 400V DC bus, electric motors, battery architecture, and pod-and-boom airframe all translate from the Rotax P1. The ICE mounting, fuel system, and weight class are the primary changes. The sensible sequence is to validate the architecture on a lighter, more accessible piston-powered aircraft first, then apply that validated platform to the more demanding turbine variant.

---

## Why Series Hybrid, and Why Now

GA builders default to direct-drive pistons because that is what the community knows, what is supported, and what 70 years of homebuilding experience has optimized for. The historical argument against series hybrid was weight — battery packs were prohibitively heavy and electric motors were exotic.

Neither constraint holds in the same way today. Battery energy density has roughly doubled in a decade. High-performance aviation-grade electric motors are commercially available from multiple vendors at competitive prices. Motor controller technology from the EV industry has matured into products with automotive-level reliability and aviation-adapted variants. The tools to build a series hybrid experimental aircraft exist and are accessible.

Against the piston single-engine baseline most experimental builders are working from, the series hybrid architecture offers:

- A second layer of propulsion redundancy before loss of thrust
- An ICE that runs at its efficient operating point regardless of flight regime
- Longer engine life from constant-speed, constant-load operation
- Near-instant torque response with no throttle lag
- A clear upgrade path to turbine power on a proven platform

That is the case. The architecture is sound. The components are available. The economics are favorable for the piston path now, and unusually favorable for the turbine path for anyone willing to design the larger aircraft it requires.

---

*MAOS is developing around the 1G+1B+2M series hybrid architecture. Related documentation:*
- [MAOS Propulsion Architecture Decision: 1G+1B+2M](/articles/2026-04-05-maos-1g1b2m-architecture-decision/)
- [MAOS Generator Engine Comparison Matrix](/articles/2026-04-05-maos-engine-comparison-matrix/)
- [MAOS Drivetrain Economics](/articles/2026-04-05-maos-drivetrain-economics/)
