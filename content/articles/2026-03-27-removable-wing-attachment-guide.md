---
title: "The Removable Wing Problem: Secure Attachments for Trailer‑Transportable Homebuilts"
date: 2026-03-27
author: "Bill Mallard"
description: "How to design a removable one‑piece wing attachment that balances structural integrity with practical trailer transport. A technical guide for experimental aircraft builders considering trailer‑transportable designs."
tags: ["wing attachment", "removable wing", "trailer transport", "structural design", "experimental", "homebuilt", "glider", "MAOS"]
---

Designing a removable wing for a homebuilt aircraft presents a fundamental engineering dilemma: **How do you make a structural joint strong enough for flight but easy enough to disassemble for trailer transport?**

This article examines the removable‑wing problem through the lens of the MAOS project (a 4‑seat pod‑and‑boom experimental), but the principles apply to any builder considering a trailer‑transportable aircraft. We'll look at existing aviation solutions, analyze structural trade‑offs, and provide specific hardware recommendations.

---

## The Engineering Dilemma

**Flight loads:** A wing attachment must withstand:
- Ultimate shear: 5.7 g (3.8 g normal × 1.5 safety factor)
- Bending moments: Wing lift, weight, inertia
- Torsion: Control surface and aerodynamic twisting
- Fatigue: Thousands of flight cycles

**Trailer requirements:** The same joint must:
- Disassemble with basic tools in 5–15 minutes
- Re‑assemble with precise alignment (≤0.010″ tolerance)
- Provide unambiguous verification of correct installation
- Withstand wear over hundreds of assembly cycles

**Conflict:** Permanent joints excel at load transfer; quick‑disconnect joints introduce points of weakness. The solution lies in borrowing proven concepts from gliders, light‑sport aircraft, and military stores‑release systems.

---

## Figure 1: Aviation Solutions Comparison

*SVG Description: A bar chart comparing removal time vs. number of people required for different aircraft types.*

```svg
<!-- Bar chart showing:
Gliders: 5–10 min (3–4 people)
LSA/Experimental: 5–60 min (2–3 people)
Certified: 60–120 min (3–4 people) -->
```

---

## What Gliders Teach Us

Modern gliders have perfected the removable wing because they must be trailered to contests and soaring sites.

### Schleicher ASK 21: The Gold Standard

**Attachment system:**
- Tongue‑and‑fork spar extensions
- Two cylindrical main pins (front) + two rear wing‑attachment pins
- Safety hook on main pins; T‑grip on rear pins with visible lock above pin
- Quick‑release Hotellier ball‑and‑socket joints for flight controls

**Pre‑flight check:** "Safety lock visible above pin" — a simple, unambiguous visual indicator.

**Assembly time:** 5–10 minutes with 3–4 people.

### Schempp‑Hirth Discus: Simplicity

**Single‑pin attachment** per wing with automatic control hook‑ups. Light wings, automatic connections, and a single visible pin make this remarkably simple.

**Key insight:** Gliders prioritize **visible verification** over complex mechanisms. If you can't see it's locked, it's not safe enough.

---

## Light‑Sport & Experimental Approaches

### Van’s RV‑12: Quick‑Disconnect Pins

**WD‑1217 fuselage pins** — one pin per side secures both spars. Pins slide out; wing spar slots into fuselage bushings. Pin stoppers and springs provide retention.

**Assembly time:** <5 minutes with 2 people.

**Limitation:** Pins are straight (not tapered), requiring precise manufacturing tolerances.

### Sonex Onex: Single‑Handle System

**Single handle** retracts two spar pins simultaneously. Spring‑loaded lock for flight security.

**Assembly time:** 30 seconds per wing for folding.

**Trade‑off:** Complex mechanism but incredibly fast operation.

### Zenith CH 701/750: Bolted Simplicity

**Bolted attachment** at main and aft spars (no quick‑disconnect). Safety wires/cotter pins.

**Assembly time:** 30–60 minutes with 3 people — slow but robust.

**Takeaway:** There's a spectrum from "fast but complex" to "slow but simple."

---

## Figure 2: Pylon vs. Direct Attachment

*SVG Description: Two structural diagrams comparing wing attachment approaches.*

```svg
<!-- Left: Pylon Interface
Wing → Pylon (short column) → Pod
Shows extra joint and longer load path

Right: Direct Attachment  
Wing → Reinforced pod hardpoints
Shows shorter, more direct load path -->
```

---

## Structural Concepts: Pylon vs. Direct Attachment

### Pylon Interface (Extra Structure)

A structural pylon between pod and wing:
- **Pros:** Clean load separation, standardized mating surface, simplifies fairings
- **Cons:** +8–12 lb weight, extra joint, more complexity
- **Verdict:** Rarely justified — adds weight without clear benefit

### Direct Attachment (Recommended)

Wing spars attach directly to reinforced pod hardpoints:
- **Pros:** Fewer parts, lighter (+2–4 lb), shorter load paths
- **Cons:** Precision alignment critical, complicates pressurization sealing
- **Verdict:** Preferred for most designs, including MAOS

**MAOS approach:** Single‑spar carry‑through with 6.0″ OD, 0.25″ wall 6061‑T6 tube passing through pod, reinforced at frames FS48 and FS60.

---

## Spar Carry‑Through Options

### 1. Single‑Spar Carry‑Through
Continuous main spar passes through fuselage/pod. Wing‑root lugs accept pins/bolts.
- **Weight:** Lightest option
- **Complexity:** Simple, fewer joints
- **Sealing:** Large cutout requires flexible boot

### 2. Multiple‑Spar Attachment  
Separate left/right spars attach to central wing box.
- **Weight:** Moderate (+)
- **Complexity:** More joints, alignment challenges
- **Sealing:** Smaller penetrations

### 3. Hybrid (Glider Style)
Single spar with detachable outboard sections (tongue‑and‑fork).
- **Weight:** Moderate
- **Complexity:** High precision machining required
- **Sealing:** Compact interface

**Recommendation:** **Single‑spar carry‑through** for homebuilders — proven, simple, light.

---

## Figure 3: Single‑Spar Carry‑Through

*SVG Description: Cross‑section showing spar tube passing through pod with reinforced frames and sealing boot.*

```svg
<!-- Cross‑section view:
Left Wing → 6″ OD spar tube → Pod with frames at FS48/FS60 → Right Wing
Show: Reinforced frames, wing‑root lugs, tapered pins, silicone‑impregnated sealing boot -->
```

---

## Hardware Specifications

### Taper Pins: The Aviation Standard

**AN386 threaded taper pins:**
- **Taper:** Brown & Sharp #3 (0.500″ per foot)
- **Function:** Self‑locking, precise fit, distributes shear load
- **Installation:** Requires taper reamer, anti‑seize compound
- **Security:** Cotter pin through threaded end

**Example:** AN386‑3‑14 (1/4‑28 thread, 1‑7/8″ length)

### High‑Strength Bolts: Backup Load Path

**NAS6204 close‑tolerance bolts:**
- **Material:** 8740 alloy steel, cadmium plated
- **Strength:** 125 ksi ultimate tensile
- **Installation:** Torque to 250 in‑lb with self‑locking nut (MS21042)
- **Safety:** Safety‑wire in approved pattern

### Quick‑Release Alternatives

**MS17987C ball‑lock pins:**  
- **Use:** Non‑primary structural attachments (access panels)
- **Strength:** ~15,000 lb shear
- **Security:** Ball detent, pull‑ring release

---

## Load Calculations

**For MAOS (MTOW ≈ 2,430 lb):**
- Ultimate vertical shear at wing root: ~6,925 lb per side (5.7 g ultimate)
- With two pins sharing shear: ~3,460 lb per pin
- Pin diameter selection: ≥3/8″ based on shear strength

**Safety factor check:**  
Normal category: +3.8 g/–1.5 g  
Ultimate: 1.5 × limit = +5.7 g/–2.25 g

**Fatigue consideration:** Removable joints prone to fretting. Mitigate with:
- Hard coatings (cadmium, anodizing)
- Anti‑fretting paste (Loctite 8060)
- Wire‑thread inserts in tapped holes
- Regular torque checks

---

## Figure 4: Verification Systems

*SVG Description: Flowchart showing three‑tier verification approach.*

```svg
<!-- Three columns:
1. Mechanical: Visual flags, inspection windows
2. Electrical: Microswitches, continuity checks, annunciator lights  
3. Procedural: Checklist, torque‑strip marks, witness holes -->
```

---

## Pilot Verification: Three‑Tier System

You must know — absolutely — that the wing is properly attached.

### Tier 1: Mechanical Indicators

**Visual flags:** Bright orange anodized sleeves extend ¼″ when pin fully seated. Spring‑loaded sleeve captures ring; if pin isn't home, ring remains recessed.

**Inspection windows:** Clear polycarbonate covers over pin heads — see without removing fairings.

**Safety‑wire loops:** Specific routing pattern; missing/broken wire immediately visible.

### Tier 2: Electrical Sensors

**Microswitches:** Sealed limit switches mounted in wing root close when pin fully inserted. Wired to cockpit "WING LOCK" annunciator.

**Continuity check:** Circuit through pin itself — if pin present and making contact, continuity light illuminates.

**Strain‑gauge load verification:** Measures whether pin is carrying load (requires calibration).

### Tier 3: Procedural Verification

**Pre‑flight checklist:** Explicit "pin visibility" check item.

**Torque‑strip markings:** Paint stripe across bolt head and adjacent structure; rotation visible.

**Witness holes:** Small hole through pin and fitting; lock wire or colored plug must be visible.

**Recommended MAOS system:** Visual flags + microswitch annunciators + checklist.

---

## Weight Penalty Analysis

| Component | Quantity | Unit Weight | Total |
|-----------|----------|-------------|-------|
| Taper pins (AN386‑3‑14) | 4 | 0.12 lb | 0.48 lb |
| Backup bolts (NAS6204‑3‑8) | 2 | 0.18 lb | 0.36 lb |
| Local reinforcement | 2 frames | 3.0 lb | 6.0 lb |
| Wing‑root lugs (2024‑T3) | 4 | 0.75 lb | 3.0 lb |
| Sealing boot | 1 set | 0.5 lb | 0.5 lb |
| Microswitches & wiring | 4 | 0.05 lb | 0.20 lb |
| Visual‑flag assemblies | 4 | 0.03 lb | 0.12 lb |
| **Total** | | | **10.9 lb** |

**Weight vs. permanent mount:** ~8–10 lb penalty for removability.

**Acceptable?** Yes — enables trailer transport (wing ≈200 lb, 36 ft span) while staying within structural budget.

---

## Trailer Transport Practicalities

### Wing Dimensions
- **Span:** ~36 ft (requires wide‑load permit in Texas)
- **Chord:** ~4.5 ft (root), ~2.5 ft (tip)
- **Height on trailer:** ~5 ft (well under 14 ft Texas limit)
- **Weight:** ~200 lb (manageable with 2‑3 people)

### Lifting Requirements
- **Crane/hoist:** 500 lb capacity minimum
- **Lifting points:** Designed into wing structure (spar hardpoints)
- **Balance:** Marked on wing skin for proper handling

### Storage & Protection
- **Custom cradle:** Foam‑lined supports at spar and tip
- **Weather protection:** Canvas cover or enclosed trailer
- **Security:** Tie‑downs to prevent movement in transit

---

## Lessons from Certified Aircraft

### Piper Cub Wing Removal
- Two bolts (front & rear spar) + strut bolts
- Cotter pins, washers, nuts
- **Time:** 1–2 hours with 3 people
- **Lesson:** Simple but slow — acceptable for annual maintenance, not for frequent transport

### Cessna 150 Procedure
- Two main spar bolts + strut bolts
- Drain fuel, disconnect cables, jack tail
- **Time:** 1–2 hours per wing with 2–4 people
- **Lesson:** Fuel system complicates removal — consider dry wings or quick‑disconnects

---

## Military Inspiration: Stores Release

**Weapons pylons (F‑16, etc.):**
- Lugs with shear pins, MAU‑12 ejection rack
- Multiple shear pins as weak links
- Fusible/jettisonable elements for emergency release

**Relevance:** Not directly applicable to wing attachment but demonstrates highly reliable quick‑release under extreme loads.

---

## MAOS‑Specific Recommendations

### Design Approach
1. **Single‑spar carry‑through** with 6″ OD tube
2. **Forged 2024‑T3 lugs** clamped to spar tube
3. **Two AN386 taper pins** per wing (primary)
4. **One NAS6204 bolt** per wing (secondary/backup)
5. **Three‑tier verification:** Visual flags, microswitch annunciators, checklist

### Build Considerations
- **Tolerance stacking:** Critical — use dowel pins for initial alignment, then ream for taper pins
- **Sealing:** Silicone‑impregnated fabric boot clamped to pod shell and wing‑root fairing
- **Inspection:** Regular torque checks, anti‑fretting paste application

### Safety Philosophy
- **Dual load‑path:** Pins (primary) + bolt (secondary)
- **Independent verification:** Mechanical + electrical + procedural
- **Failure analysis:** Single‑pin failure → bolt carries load; both fail → structural redundancy in spar

---

## Common Pitfalls to Avoid

### 1. Under‑Sized Pins
Using hardware‑store clevis pins instead of aviation‑rated taper pins. **Result:** Shear failure at limit load.

### 2. Poor Alignment
Assuming "close enough" for straight pins. **Result:** Uneven load distribution, premature wear.

### 3. Inadequate Verification
Relying only on "feel" or visual inspection without positive indicators. **Result:** Undetected incomplete engagement.

### 4. Ignoring Wear
Not planning for inspection/maintenance of removable joints. **Result:** Loosening over time, increased play.

### 5. Weight Optimism
Underestimating reinforcement weight for removable attachments. **Result:** Empty weight over budget.

---

## The Builder's Checklist

### Before Designing
- [ ] Define required removal frequency (contest vs annual)
- [ ] Calculate ultimate shear loads for your aircraft
- [ ] Study similar aircraft (gliders, LSA) for proven approaches
- [ ] Decide on verification philosophy (mechanical/electrical/procedural)

### During Design
- [ ] Select aviation‑standard hardware (AN/NAS/MS)
- [ ] Design positive alignment features (dowel pins, guide cones)
- [ ] Incorporate visual verification (flags, windows, markings)
- [ ] Plan for wear inspection and maintenance

### Before First Flight
- [ ] Proof‑load test attachment to 1.5× limit load
- [ ] Verify all verification systems function
- [ ] Document assembly/disassembly procedure
- [ ] Train second person on proper procedure

---

## Conclusion: Removable ≠ Compromised

A removable wing attachment doesn't have to be a structural compromise. By borrowing proven concepts from gliders, implementing aviation‑standard hardware, and building in redundant verification, you can achieve:

- **Structural integrity:** Meets or exceeds permanent‑mount strength
- **Practical removability:** 5–15 minute assembly with basic tools
- **Unambiguous safety:** Multiple independent verification methods
- **Manageable weight:** 8–12 lb penalty for trailer‑transport capability

The key is recognizing that **removability is a first‑class design requirement**, not an afterthought. Design it in from the beginning, test it thoroughly, and verify it redundantly.

For MAOS, this means a single‑spar carry‑through with taper pins, visual flags, and electrical annunciation — a 10.9 lb investment that enables trailer transport without compromising flight safety.

---

*This article synthesizes technical research conducted for the MAOS Design Review Board. All information is for experimental amateur‑built aircraft only and must be validated by a qualified aerospace engineer before application.*

**Related Articles:**
- [Pressurized Homebuilt Aircraft: A Technical Guide](/articles/2026-03-27-homebuilt-pressurization-guide/)
- [Fly‑By‑Wire for Homebuilt Aircraft: Why Pod‑and‑Boom Changes the Game](/articles/2026-03-26-fly-by-wire-pod-and-boom-advantages/)

**Tags:** #wing-attachment #removable-wing #trailer-transport #structural-design #experimental #homebuilt #glider #MAOS #engineering