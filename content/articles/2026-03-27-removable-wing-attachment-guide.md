---
title: "The Removable Wing Problem: Non‑Penetrating Attachments for Pressurized Homebuilts"
date: 2026-03-27
author: "Bill Mallard"
description: "How to design a removable one‑piece wing attachment for pressurized aircraft without penetrating the pressure vessel. Over‑engineered safety factors and external saddle concepts for MAOS pod‑and‑boom architecture."
tags: ["wing attachment", "removable wing", "pressure vessel", "structural design", "experimental", "homebuilt", "glider", "MAOS", "pressurization"]
project: "maos"
article_type: "methodology"
---

Designing a removable wing for a **pressurized** homebuilt aircraft introduces three critical constraints:

1. **No pressure vessel penetration** — the wing attachment must not compromise the pressurized shell
2. **Over‑engineered safety** — 8–12g ultimate factors for this single‑point‑of‑failure joint
3. **Intentional removability** — designed for frequent trailer transport, not just maintenance

This article examines the removable‑wing problem through the lens of the MAOS project (a 4‑seat pressurized pod‑and‑boom experimental), with specific solutions for pressurized aircraft architectures.

---

## The Pressurized Aircraft Constraint

For pressurized aircraft, the pressure vessel integrity is paramount. Every penetration represents:
- A potential leak path (seal degradation over cycles)
- A stress concentration (fatigue initiation site)
- A maintenance burden (seal inspection/replacement)

**MAOS requirement:** Wing attachment must be **entirely external** to the 48″ diameter cylindrical pressure vessel operating at 5 PSI differential.

**Consequence:** No spar‑through‑pod solutions. Loads must transfer through the external skin or dedicated external hardpoints.

---

## Safety Philosophy: Over‑Engineer Critical Joints

The wing‑to‑fuselage attachment is a **single‑point‑of‑failure** joint. If it fails, the aircraft becomes uncontrollable.

### Standard vs. MAOS Safety Factors

| Factor | FAA Normal Category | MAOS Target | Rationale |
|--------|-------------------|-------------|-----------|
| **Limit load** | +3.8 g / –1.5 g | +3.8 g / –1.5 g | Standard maneuvering envelope |
| **Ultimate factor** | 1.5× limit | **2.1–3.2× limit** | Critical joint over‑engineering |
| **Ultimate load** | +5.7 g / –2.25 g | **+8–12 g** / –3.2–4.8 g | Weather penetration, wake turbulence, uncommanded maneuvers |

**Why 8–12g?**  
- Weather penetration can produce brief 5–6g loads
- Wake turbulence from heavy aircraft
- Uncommanded control inputs or pilot error
- This joint should **never** be the limiting factor

**Load calculation for MAOS (MTOW ≈ 2,430 lb):**
- 8g ultimate: ~9,720 lb vertical shear per side
- 12g ultimate: ~14,580 lb per side
- Hardware sized for **12g** if weight permits, **8g** minimum

---

## What Intentionally Removable Designs Teach Us

Only study aircraft **designed for frequent removal** — not those where removal is possible but impractical.

### Gliders: The Gold Standard

Gliders **must** be trailered, so their wing attachments are optimized for frequent disassembly.

**Schleicher ASK 21:**
- Tongue‑and‑fork spar extensions
- Two cylindrical main pins (front) + two rear pins
- Safety hook on main pins; T‑grip on rear pins with **visible lock above pin**
- Quick‑release Hotellier ball‑and‑socket control joints
- **Key insight:** "Safety lock visible above pin" — unambiguous visual verification

**Schempp‑Hirth Discus:**
- Single‑pin attachment per wing
- Automatic control hook‑ups
- **Assembly time:** <5 minutes

**Glider philosophy:** If you can't **see** it's locked, it's not safe enough.

### Light‑Sport Aircraft Designed for Trailering

**Van’s RV‑12:**
- WD‑1217 quick‑disconnect fuselage pins
- One pin per side secures both spars
- Pin stoppers and springs for retention
- **Assembly time:** <5 minutes with 2 people

**Sonex Onex:**
- Single handle retracts two spar pins simultaneously
- Spring‑loaded lock for flight security
- **Assembly time:** 30 seconds per wing (folding)

**Zenith CH 701/750:**
- Bolted attachment (main + aft spars)
- Safety wires/cotter pins
- **Assembly time:** 30–60 minutes — robust but slow

**Spectrum:** "Fast but complex" (Onex) to "slow but simple" (Zenith).

---

## Non‑Penetrating Attachment Concepts

### External Saddle/Clamp System

A structural saddle wraps around the pod exterior, transferring loads through the skin to internal frames without penetrating the pressure boundary.

**Components:**
- **Upper saddle:** Clamps to wing spar carry‑through
- **Lower saddle:** Wraps around pod exterior
- **Shear ties:** Connect saddle to pod frames through skin
- **Tension straps:** React bending moments

**Load paths:**
- **Shear:** Through skin into frames via shear ties
- **Bending:** Tension/compression straps around pod circumference
- **Torsion:** Multiple attachment points around perimeter

**Advantages:**
- Zero pressure boundary penetration
- Maintains pressure vessel integrity
- Distributed load transfer reduces local stresses
- Easier sealing (no moving seals)

### External Structural Bridge

A bridge structure sits atop the pod, attached at door/window frames or other non‑pressurized hardpoints.

**Approach:**
- Bridge attaches at door frames (already reinforced for openings)
- Wing mounts to bridge top surface
- Loads transfer through existing structural elements
- No new pressure penetrations

**Consideration:** Door frame strength must be verified for wing loads.

### Hybrid: External Pylon

Short structural pylon attached to pod at multiple hardpoints, with wing mounting at pylon top.

**Trade‑off:** Adds weight but provides clean load separation.

---

## Hardware for Over‑Engineered Loads

### Taper Pins at 12g Ultimate

**AN386 threaded taper pins** sized for ~14,580 lb shear (12g ultimate):

| Pin Size | Large End Diameter | Ultimate Shear Strength | Status |
|----------|-------------------|-------------------------|--------|
| AN386‑4‑16 | 1/2″ | ~22,000 lb | **Minimum** |
| AN386‑5‑20 | 5/8″ | ~35,000 lb | **Recommended** |
| AN386‑6‑24 | 3/4″ | ~50,000 lb | **Conservative** |

**Selection:** AN386‑5‑20 (5/8″ large end) provides 2.4× margin at 12g ultimate.

### High‑Strength Backup Bolts

**NAS6600 series** high‑strength bolts as secondary load path:

- **Material:** 8740 alloy steel, 180 ksi ultimate
- **Size:** 7/16″‑20 or 1/2″‑20 depending on load share
- **Installation:** Torque + tension (load indicating washers)
- **Safety:** Double‑redundant locking (self‑locking nut + safety wire)

### Additional Redundancy

**Three‑pin system:** Instead of two primary pins:
- Two pins sized for 8g ultimate each
- Third pin as backup/tie‑down
- Any two pins can carry 12g ultimate

**Rationale:** Hardware failure tolerance without single‑point failure.

---

## Pressure Vessel Interface

### Load Transfer Through Skin

**Shear panel concept:** External saddle transfers shear through pod skin into frames.

**Requirements:**
- Skin thickness: 0.040″–0.063″ 6061‑T6 minimum
- Frame spacing: 12″ maximum
- Doublers: 0.063″ 2024‑T3 under saddle attachment points
- Fasteners: Hi‑Lok or Cherry rivets in double shear

**Fatigue consideration:** Cyclic loading at skin‑to‑frame joints requires:
- Interference‑fit fasteners
- Sealant/faying surface treatment
- Regular eddy‑current inspection

### Sealing Approach

**No dynamic seals required** — all joints are static:

- Saddle‑to‑skin: Pro‑Seal PR‑1422 polysulfide sealant
- Fastener holes: Wet installation with sealant
- Perimeter: Continuous fillet seal

**Advantage over spar‑through‑pod:** No flexible boot, no relative motion, simpler inspection.

---

## Verification Systems

### Three‑Tier Verification Philosophy

**Tier 1: Mechanical (Primary)**
- **Visual flags:** Bright orange sleeves extend ¼″ when pin fully seated
- **Inspection windows:** Clear polycarbonate over pin heads
- **Safety‑wire patterns:** Specific routing; broken/missing wire immediately visible

**Tier 2: Electrical (Secondary)**
- **Microswitches:** Sealed limit switches in wing root → "WING LOCK" annunciator
- **Continuity circuits:** Through pins themselves
- **Load‑path sensors:** Strain gauges verify load sharing

**Tier 3: Procedural (Tertiary)**
- **Checklist item:** Explicit "pin visibility" verification
- **Torque‑strip markings:** Paint stripe across bolt/structure interface
- **Witness holes:** Lock wire or colored plug through pin/fitting

**MAOS implementation:** All three tiers mandatory for pressurized aircraft.

---

## Weight Penalty Analysis

| Component | Original (5.7g) | Revised (12g + External) | Delta |
|-----------|----------------|--------------------------|-------|
| Taper pins | 4 × AN386‑3‑14 (0.48 lb) | 4 × AN386‑5‑20 (1.2 lb) | +0.72 lb |
| Backup bolts | 2 × NAS6204‑3‑8 (0.36 lb) | 3 × NAS6600‑7‑16 (1.1 lb) | +0.74 lb |
| Local reinforcement | 6.0 lb (internal) | 8.5 lb (external saddle) | +2.5 lb |
| Wing‑root lugs | 3.0 lb | 4.5 lb (larger for 12g) | +1.5 lb |
| Saddle structure | N/A | 6.0 lb | +6.0 lb |
| Sealing system | 0.5 lb (boot) | 0.8 lb (static seals) | +0.3 lb |
| Verification hardware | 0.32 lb | 0.32 lb (unchanged) | 0 lb |
| **Total** | **10.9 lb** | **22.4 lb** | **+11.5 lb** |

**Weight penalty:** **+11.5 lb** for:
- 12g ultimate vs 5.7g (+100% load capacity)
- External saddle vs internal spar (+6.0 lb)
- Additional redundancy (+1.5 lb)

**Acceptable?** For pressurized aircraft with trailer transport requirement: **yes**. Pressure vessel integrity and over‑engineered safety justify the penalty.

---

## Trailer Transport Practicalities

### Wing‑Specific Trailer Design

**Wing dimensions:**
- **Span:** ~36 ft (requires wide‑load permit in Texas)
- **Root chord:** ~4.5 ft
- **Tip chord:** ~2.5 ft
- **Weight:** ~220 lb (including external saddle)

**Trailer requirements:**
- **Length:** 40 ft (including tongue)
- **Width:** 8.5 ft (standard) with over‑width permit for >8.5 ft
- **Height:** <14 ft (Texas limit) — wing stores at ~5 ft height
- **Capacity:** 1,000 lb minimum (wing + cradle + tools)

**Cradle design:**
- Foam‑lined supports at spar (2) and tip (1)
- Adjustable for different wing incidences
- Tie‑down points integrated
- Weather cover attachment points

---

## Builder's Implementation Checklist

### Design Phase
- [ ] Confirm no pressure vessel penetration in final design
- [ ] Size all hardware for 12g ultimate (8g minimum)
- [ ] Design external saddle with distributed load transfer
- [ ] Plan three‑tier verification system
- [ ] Calculate weight penalty and update budget

### Fabrication Phase
- [ ] Machine saddle components from 2024‑T3 or 6061‑T6
- [ ] Install shear ties to pod frames through skin
- [ ] Apply Pro‑Seal to all static joints
- [ ] Install visual flag and microswitch systems
- [ ] Test verification systems before wing installation

### Testing Phase
- [ ] Proof‑load test to 1.5× limit load (5.7 g) with strain gauges
- [ ] Leak check pressure vessel after saddle installation
- [ ] Verify all verification systems function
- [ ] Document assembly/disassembly procedure
- [ ] Train second person on proper procedure

---

## Why This Matters for Pressurized Aircraft

The removable wing problem takes on new dimensions when the fuselage is a pressure vessel:

1. **Pressure integrity trumps all** — no compromises on sealing
2. **Over‑engineering is justified** — critical joint in safety‑critical system
3. **External solutions exist** — proven by spacecraft and pressure vessel design
4. **Verification is non‑negotiable** — multiple independent methods required

For MAOS, this means:
- **External saddle** wrapping pod exterior
- **AN386‑5‑20 taper pins** (5/8″) for 12g ultimate
- **Three‑tier verification** (mechanical + electrical + procedural)
- **+11.5 lb weight penalty** — acceptable for safety and pressure integrity

The result: A wing that comes off for trailer transport without ever touching the pressure boundary, with safety margins that inspire confidence rather than anxiety.

---

*This revised article addresses critical feedback on safety factors, pressure vessel integrity, and design intent. All information is for experimental amateur‑built aircraft only and must be validated by a qualified aerospace engineer before application.*

**Related Articles:**
- [Pressurized Homebuilt Aircraft: A Technical Guide](/articles/2026-03-27-homebuilt-pressurization-guide/)
- [Fly‑By‑Wire for Homebuilt Aircraft: Why Pod‑and‑Boom Changes the Game](/articles/2026-03-26-fly-by-wire-pod-and-boom-advantages/)

**Tags:** #wing-attachment #removable-wing #pressure-vessel #structural-design #experimental #homebuilt #glider #MAOS #pressurization #safety-factors