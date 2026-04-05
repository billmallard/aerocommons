---
title: "MAOS-ECS Phase 1: Environmental Control System BOM"
date: 2026-04-05T14:00:00-06:00
description: "Component-level BOM, sourcing, and bench test plan for the MAOS Environmental Control System — air conditioning, heat, and pressurization."
tags: ["systems", "analysis", "pressurization", "design-decisions", "electric-aviation", "build-in-public"]
author: "AeroCommons Design Board"
summary: "First BOM article for the MAOS-ECS sub-project. Covers the three subsystems — refrigeration/AC, cabin heating, and pressurization — using 400V EV-market hardware where possible. Describes how they integrate and how to bench-test the system before the airframe exists."
project: "maos"
article_type: "analysis"
draft: false
---

## Project: MAOS-ECS

**Project ID:** MAOS-ECS
**System:** Environmental Control System — cabin air conditioning, heating, and pressurization
**Phase:** 1 — Component BOM and bench test architecture
**Date:** 2026-04-05
**Status:** Preliminary

---

## What This System Has to Do

The MAOS cabin is a pressurized composite cylinder approximately 48 inches in diameter. It needs to remain livable from sea level to a pressurized flight altitude of 20,000 ft, in ambient temperatures ranging from -40°F to 100°F on the ground.

Three subsystems in scope:

1. **Refrigeration / Air Conditioning** — remove heat from the cabin, dehumidify incoming air
2. **Cabin Heating** — warm the cabin in cold conditions, particularly at altitude
3. **Pressurization** — maintain cabin altitude at or below 8,000 ft up to 20,000 ft flight altitude (approximately 5 PSI differential)

These are not three separate systems. They share air handling infrastructure, share the 400V DC bus, and benefit from integration with the generator engine cooling circuit. Designing them together from the start is the right approach.

---

## Architecture Overview

```
[Generator Engine Coolant Loop]
        ↓ waste heat
[Cabin Heat Exchanger] ──────────────────────→ [Cabin Air Distribution]
        ↑                                               ↑
[EV Heat Pump Compressor] → [Refrigerant Circuit] ─────┘
        ↑
[400V DC Bus]

[Pressurization Centrifugal Blower]
        ↑
[400V DC Bus]
        ↓
[Cabin] → [Outflow Valve] → [Overboard]
```

**Key architectural decisions:**

**400V-native components throughout.** The MAOS HV bus is 400V DC. Modern EV market heat pump compressors run natively at 300–400V. Using them eliminates a DC-DC conversion stage with its associated weight, efficiency loss, and failure point.

**Engine waste heat as primary cabin heat source.** The two generator engines produce significant waste heat through their liquid cooling circuits. At cruise, this heat is essentially free. A simple coolant-to-air heat exchanger in the cabin supply duct provides heat without drawing from the battery or running the compressor in heat-pump mode. The heat pump supplements or replaces this when engines are at low power.

**Separate pressurization circuit.** Pressurization uses a dedicated centrifugal blower, not the AC compressor. These are different requirements — pressurization needs reliable, continuous, controllable airflow at modest pressure ratios; the refrigeration circuit moves refrigerant, not cabin air. Combining them adds complexity without meaningful benefit at this scale.

**Pod integrity preserved.** The MVS camera system (replacing side windows) has already removed four major penetrations from the pressure vessel. ECS duct penetrations will be minimized to two: a supply inlet and the outflow valve exhaust. All penetrations are circular and use double-lip seals.

---

## Subsystem 1: Refrigeration / Air Conditioning

### How It Works

A standard vapor-compression refrigeration cycle. Refrigerant is compressed (compressor) → condensed overboard (condenser, mounted in airstream) → expanded (expansion valve) → evaporated in the cabin supply duct (evaporator). Condensed water drains overboard.

In heat pump mode, the cycle reverses: the cabin evaporator becomes a condenser and heats incoming air. This supplements waste heat recovery at low engine power or on the ground.

### Component BOM — Refrigeration Circuit

| Component | Part / Source | Est. Cost | Notes |
|-----------|---------------|-----------|-------|
| **EV Heat Pump Compressor** | Hanon HSC34 electric scroll compressor (salvage from Hyundai Ioniq 5, Kia EV6, or Hyundai Tucson PHEV) | $150–400 (salvage) / $700–1,000 (new aftermarket) | 400V native, variable speed, brushless, ~3–5 kW input, sealed oil charge — the same unit in millions of EVs. PN varies by donor vehicle. Search: "HV electric AC compressor Ioniq 5" |
| **Condenser** | Microchannel aluminum condenser, 12"×10"×1" (custom or HVAC aftermarket) | $80–200 | Sized for 5,000 BTU/h rejection at 150 KTAS. Mounted in wing-root or belly fairing with ram air. Final dimensions TBD pending CFD of installation location. |
| **Evaporator** | Automotive HVAC evaporator core, ~8"×6"×2.5" | $40–100 | Installed in cabin air supply duct. Standard automotive part — size to duct cross-section. |
| **Electronic Expansion Valve (EEV)** | Fujikoki SEES or Sporlan SEI-0.5 | $60–120 | Electronically controlled for variable superheat. Required for heat pump reversibility. |
| **Reversing Valve (4-way)** | Standard HVAC reversing valve, 1/4" connections | $40–80 | Required only if using heat pump heating mode. Can omit for AC-only Phase 1. |
| **Receiver/Dryer** | Standard inline receiver-dryer, compatible with R-1234yf | $25–50 | |
| **Refrigerant** | HFO-1234yf (native to modern EV compressors) | $80–150 / lb (small qty) | ~1–2 lb charge. 1234yf has GWP of 4 vs. R134a at 1,360. Compressor warranty typically requires 1234yf. |
| **Compressor inverter** | Salvage EV compressor inverter from donor vehicle (or standalone EV compressor driver board) | $100–300 (salvage) | The Hanon compressor requires a 3-phase inverter to run. On many EVs this is a separate module. Some OEM inverters can be PWM-commanded via CAN; others need aftermarket driver. Research required on specific donor vehicle. |
| **High/Low pressure switches** | Saginomiya or Parker dual pressure switch | $30–60 | Safety cutout — prevents compressor operation outside limits. |
| **Refrigerant hose/fittings** | Parker or Gates barrier hose, A/C fittings | $80–150 | Use barrier hose rated for 1234yf. Length TBD pending layout. |
| **Subtotal — Refrigeration** | | **$705–2,110** | |

### Notes on the EV Compressor

This is the pivotal component selection. The Hanon HSC34 and similar units (used in Ioniq 5, EV6, Ioniq 6, various Stellantis EVs) are 400V 3-phase scroll compressors. They are compact (~6 kg), efficient, and produced in enormous volume — which keeps salvage prices low and means replacement parts will be available for decades.

The challenge is the inverter/controller. Some donor vehicles have the inverter ± CAN controller as a separable module; others integrate it tightly with the thermal management ECU. **Before purchasing the compressor, source the inverter from the same donor vehicle.** Then bench-test the pair running on a 400V bench supply before committing to installation.

Alternative: Sanden SD7V EV or Sanden TRSA09 variants designed for OEM EV applications. Slightly higher cost new but more aftermarket controller support exists.

---

## Subsystem 2: Cabin Heating

### Architecture

Primary heat source: **generator engine coolant waste heat** via a liquid-to-air heat exchanger in the cabin supply duct. At cruise power, two 400cc engines produce approximately 10–20 kW of waste heat in their cooling circuits. Even capturing 20% of this for cabin conditioning provides 2–4 kW of heat — more than adequate for cruise heating.

Secondary/ground heat source: **PTC (Positive Temperature Coefficient) resistance heaters** drawing from the 400V bus. Used on the ground before engines are at temperature, and as boost heat.

Tertiary: **Heat pump mode** from the refrigeration circuit above. Useful at low engine power.

### Component BOM — Heating

| Component | Part / Source | Est. Cost | Notes |
|-----------|---------------|-----------|-------|
| **Coolant-to-air heat exchanger** | Automotive heater core, ~10"×7"×2" (e.g., Delphi or Valeo unit from any liquid-cooled passenger car) | $30–80 | Installed in cabin supply duct in series with evaporator. Coolant lines from generator engine circuit routed through pod — length TBD pending layout. |
| **Coolant control valve** | Automotive coolant control valve (e.g., Continental Automotive or Hella) or simple manual ball valve for Phase 1 | $30–120 | Modulates heating output. Simple on/off ball valve adequate for bench development. |
| **PTC heater elements (backup)** | 2× 1.5 kW HV PTC heater elements, 400V nominal (EV/PHEV aftermarket) | $60–150 each | Used in EV cabin heaters — sources: Alibaba industrial suppliers, EV parts suppliers. Specify 300–450V operating range. |
| **PTC controller** | PWM relay or solid-state relay for PTC elements | $20–60 | Simple on/off or staged control for bench Phase 1. PID controller in Phase 2. |
| **Subtotal — Heating** | | **$200–590** | |

---

## Subsystem 3: Pressurization

### Architecture

A dedicated oil-free centrifugal blower draws outside air, compresses it to cabin pressure, and delivers it to the cabin supply duct. Cabin pressure is controlled by a motorized outflow valve exhausting to atmosphere. A differential pressure sensor provides feedback to a cabin pressure controller, which commands the outflow valve.

This is not a bleed-air system. There is no equivalent to a turbocharger bleed tap on motorcycle-derived generator engines running as pure generator drives. This must be an independent electric compressor.

The target: maintain 5 PSI differential (≈8,000 ft cabin at 20,000 ft flight altitude), with maximum outflow rate sufficient to handle door seal leakage and occupant CO₂ scrubbing. Mass flow requirement is modest — approximately 20–40 CFM continuous.

### Component BOM — Pressurization

| Component | Part / Source | Est. Cost | Notes |
|-----------|---------------|-----------|-------|
| **Centrifugal cabin air compressor** | Domel 799.3.xxx series centrifugal blower (brushless DC, oil-free, used in CPAP/medical equipment and industrial applications) — or Ametek Rotron centrifugal blower | $200–800 | These are oil-free centrifugal blowers capable of modest pressure ratios (1.2–1.5:1) at 20–50 CFM. Adequate for pressurization at the cabin volumes involved. Need to bench-verify pressure rise at altitude (lower inlet density). **This is the component requiring most development work.** A proper aviation-grade turbocompressor (Barber-Nichols: $15–30k) is the end-state; a development-grade centrifugal is appropriate for Phase 1 bench work. |
| **Compressor motor controller** | VESC 75/300 (open-source BLDC controller, 300V max) or Kelly KLS-H series (72–120V variants) | $150–400 | For bench development. Final aircraft controller will be sized to the production compressor selection. VESC is configurable and well-documented. |
| **Outflow valve** | Used Piper PA-28/32/34 outflow valve (aircraft salvage) — or fabricate: 2" aluminum butterfly valve + Actuonix linear actuator | $150–500 (used OEM) / $80–200 (fabricated) | Used Piper outflow valves are available through aircraft salvage (Aviall, salvage yards). Fabricated valve adequate for bench. |
| **Outflow valve actuator** | Included in OEM valve, or Actuonix L16 linear actuator for fabricated valve | $40–80 | Proportional control — not on/off. |
| **Cabin differential pressure sensor** | Honeywell PX2 series (0–15 PSI differential) or Sensata 1865 series | $80–200 | Two sensors recommended — primary and backup. Differential reading: cabin – ambient. |
| **Cabin altitude indicator** | United Instruments 3000 cabin altimeter (used aircraft market) | $80–200 | Backup visual display for crew. |
| **Cabin pressure controller** | Custom: Arduino Mega or STM32 + LCD + PID control loop (Phase 1 bench dev) | $50–150 | Purpose-built controller for Phase 1. Software controls outflow valve position to maintain target cabin altitude. ACE Thermal eKAPS (~$3,000) is the production target; custom controller is the bench development tool. |
| **Safety relief valve — positive** | Clippard URV-3 or Parker inline relief valve, set at 5.5 PSI differential | $40–100 | Hard limit — prevents overpressurization regardless of controller state. |
| **Safety relief valve — negative** | Same or equivalent, reverse-mounted, set at -0.5 PSI (prevents vacuum if outflow valve sticks open at altitude) | $40–100 | |
| **Inlet filter/silencer** | Automotive intake filter (K&N or equivalent) + flexible silencer boot | $30–60 | RAM air inlet TBD pending fuselage location. |
| **Subtotal — Pressurization** | | **$960–2,790** | |

---

## Shared Air Handling

| Component | Part / Source | Est. Cost | Notes |
|-----------|---------------|-----------|-------|
| **Cabin supply duct** | 4" diameter spiral aluminum duct (HVAC supply) + custom transitions | $40–100 | Evaporator → heater core → distribution outlets. Insulated where cold exterior surfaces are adjacent. |
| **Distribution outlets** | 4× Automotive-style adjustable vents (dash-mount style) | $20–60 | Positioned per cabin layout. |
| **Cabin recirculation fan** | 12V or 24V brushless blower fan (automotive HVAC blower motor) with DC-DC converter from 400V bus | $30–80 | Provides cabin air circulation independent of fresh-air pressurization flow. |
| **Condensate drain** | Simple gravity drain with check valve, routed overboard | $15–30 | Prevents cabin water accumulation from evaporator. |
| **Subtotal — Air Handling** | | **$105–270** | |

---

## Total System BOM Summary

| Subsystem | Low Est. | High Est. |
|-----------|----------|-----------|
| Refrigeration / AC | $705 | $2,110 |
| Heating | $200 | $590 |
| Pressurization | $960 | $2,790 |
| Shared Air Handling | $105 | $270 |
| **Total** | **$1,970** | **$5,760** |

The wide range reflects the salvage vs. new spread on the compressor and outflow valve, and the development vs. production choice on the pressure controller. A realistic Phase 1 bench build using primarily salvage EV components and a custom pressure controller lands around **$2,500–3,500**.

---

## How It Connects — Integration Notes

**400V bus to compressor:** The EV compressor inverter runs directly from the HV bus. Add a dedicated 20A HV fuse and contactor. Total compressor draw at full load: ~12A at 400V.

**Coolant loop to heater core:** Tee off the generator engine coolant circuit. A proportional coolant valve controls heat delivery to the cabin. Coolant temperature at cruise: ~80–90°C — more than adequate for cabin heating. This circuit is entirely passive when the valve is closed.

**Pressurization compressor to cabin:** Clean filtered air from the blower enters the supply duct upstream of the evaporator and heater core. Processed (conditioned) air exits at cabin distribution outlets. The outflow valve exhausts through the pod skin to atmosphere — this is the only overboard penetration needed for the pressurization circuit.

**Sensors and controller:** The cabin pressure controller reads differential pressure (cabin vs. ambient) and cabin altitude. It commands the outflow valve actuator over a 0–5V or PWM signal. Safety relief valves are purely mechanical — no electrical path, no failure mode.

---

## Bench Test Plan — Phase 1

The value of designing systems first is that you can build and test the ECS before the airframe exists. The bench test proves the components work, characterizes performance, and surfaces problems early.

### Test Article

Build a pressure test box: a plywood-and-fiberglass box approximately 8 cubic feet (representing a scaled section of the cabin volume, sized to fit in a workshop). Seal it with foam weatherstripping. Install two circular penetrations — supply inlet and outflow valve mount.

This is not a fatigue specimen. It is a functional systems test fixture for characterizing flow, pressure, and thermal performance at 5 PSI differential (which the box must survive).

### Test Sequence

**Phase 1A — Pressurization circuit only**

1. Install centrifugal compressor, outflow valve, pressure sensors, and pressure controller on test box
2. Apply 120V AC power to compressor (bench supply, not HV bus yet)
3. Characterize: What flow rate and power draw is needed to maintain 5 PSI differential against simulated leakage (deliberate small orifice)?
4. Tune PID controller — target: stable cabin altitude within ±200 ft, no hunting
5. Test safety relief valves: verify set points

**Phase 1B — Refrigeration circuit**

1. Build refrigeration circuit on bench (not in box yet): compressor, condenser (shop fan for airflow), expansion valve, evaporator
2. Charge with 1234yf, verify for leaks
3. Run compressor on bench HV supply — verify cooling performance, measure COP
4. Heat pump mode if reversing valve installed: verify heating output

**Phase 1C — Integrated**

1. Install evaporator and heater core in supply duct of test box
2. Run pressurization + refrigeration simultaneously
3. Measure: cabin temperature, humidity, pressure, power draw from HV bus
4. Simulate flight profile: ambient temperature change, altitude change (bleed pressurization system to simulate climb/descent)

### Instrumentation Required for Bench Testing

| Instrument | Purpose | Cost |
|-----------|---------|------|
| Differential pressure gauge (0–10 PSI) | Verify actual ΔP across test box | $40–100 |
| Thermocouple + DAQ (4-channel) | Supply air temp, cabin temp, heater core in/out | $80–200 |
| Clamp-type power meter (for HV circuit) | Measure compressor power draw | $50–150 |
| Refrigerant manifold gauges (1234yf compatible) | Refrigerant circuit pressures | $80–200 |
| Anemometer | Supply duct airflow velocity | $30–80 |

---

## What Comes Next (Phase 2)

Phase 1 delivers: working bench proof-of-concept, characterized component performance, validated control logic, verified BOM.

Phase 2 will specify:
- Production compressor (Barber-Nichols or validated production alternative based on Phase 1 flow data)
- Aircraft-grade pressure controller (eKAPS or equivalent)
- Aircraft-grade outflow valve (OEM aviation or engineered custom)
- Final duct routing and cabin integration geometry
- Weight-optimized installation design
- HV harness design for aircraft installation

---

## Related Articles

- [Pressurized Homebuilt Aircraft: A Technical Guide](/articles/2026-03-27-homebuilt-pressurization-guide/) — pressure vessel design, structural requirements
- [Pressurized Homebuilt Case Studies: Lancair IV-P and Veloce 600](/articles/2026-03-27-lancair-veloce-pressurization-case-studies/) — lessons from the field
- [MVS Phase 1: Building a Camera-Only Cockpit for Under $5,000](/articles/2026-04-03-mvs-phase1-component-list/) — window elimination supporting pressurization design

---

*MAOS-ECS Phase 1 — preliminary design*
*All component costs are 2026 estimates based on current salvage and aftermarket pricing. Vendor quotes required before procurement.*
*AeroCommons / MAOS Project — Fort Worth, Texas*
