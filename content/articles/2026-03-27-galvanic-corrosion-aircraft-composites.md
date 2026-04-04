---
title: "Galvanic Corrosion in Aircraft Composites: How to Prevent Dissimilar Material Failure"
date: 2026-03-27
author: "Bill Mallard"
description: "Practical guide to preventing galvanic corrosion between carbon fiber, aluminum, and other dissimilar materials in homebuilt aircraft. Voltage potentials, isolation methods, and builder‑friendly solutions."
tags: ["galvanic corrosion", "composite", "aluminum", "carbon fiber", "aircraft construction", "experimental", "homebuilt", "materials", "MAOS"]
project: "maos"
article_type: "analysis"
---

Building a composite aircraft often means joining dissimilar materials: carbon fiber wings to aluminum fuselage, stainless steel fasteners in composite structures, or aluminum fittings bonded to carbon spars. This creates a hidden danger: **galvanic corrosion** — where one metal corrodes preferentially when electrically connected to another in the presence of an electrolyte (moisture, salt, condensation).

This article explains galvanic corrosion risks in aircraft construction and provides practical, builder‑friendly solutions for preventing material failure.

---

## The Chemistry: Why Dissimilar Materials Corrode

When two different metals (or conductive materials like carbon fiber) are electrically connected and exposed to an electrolyte, they form a **galvanic cell**:

- **Anode:** The more "active" metal (lower on the galvanic series) corrodes
- **Cathode:** The more "noble" material is protected
- **Electrolyte:** Any conductive liquid (water, salt spray, condensation)
- **Electrical connection:** Direct contact or through fasteners/wiring

**The greater the voltage difference, the faster the corrosion.**

---

## Voltage Potentials: Which Combinations Are Dangerous?

### Galvanic Series Positions (vs. Standard Calomel Electrode)

| Material | Voltage (V) | Behavior |
|----------|------------|----------|
| **Carbon fiber (graphite)** | +0.2 to +0.3 V | **Highly cathodic** — will cause rapid corrosion of many metals |
| **Stainless steel (passive)** | –0.1 to +0.5 V | Cathodic |
| **Aluminum 2024‑T3** | –0.6 to –0.9 V | **Highly anodic** — will corrode when paired with carbon or stainless |
| **Aluminum 6061‑T6** | –0.7 to –1.0 V | Even more anodic than 2024 |
| **Aluminum 7075‑T6** | –0.7 to –1.0 V | Similar to 6061 |
| **Titanium (Ti‑6Al‑4V)** | –0.1 to +0.3 V | Near‑noble, compatible with aluminum |

### High‑Risk Combinations

**Carbon fiber + aluminum:** ΔV ≈ 0.9–1.3 V → **Extreme risk**  
Carbon is cathode, aluminum anode. In seawater exposure, aluminum can corrode at 50–200 mpy (mils per year) — enough to lose 0.020″ thickness in 1–4 years.

**Stainless steel + aluminum:** ΔV ≈ 0.5–1.5 V → **High risk**  
Stainless cathode, aluminum anode. Common in fasteners.

**Carbon fiber + stainless steel:** ΔV ≈ 0–0.8 V → **Moderate risk**  
Carbon cathode, stainless anode (stainless may corrode).

### Safe Combinations

**Fiberglass + aluminum:** **No risk**  
Fiberglass (E‑glass or S‑glass) is non‑conductive. No electrical path, no galvanic cell.

**Titanium + aluminum:** **Low risk**  
Titanium is near‑noble but compatible; minimal voltage difference.

**Like‑to‑like materials:** **No risk**  
Aluminum‑to‑aluminum, carbon‑to‑carbon, etc.

---

## Corrosion Rate Estimates: How Fast Is "Fast"?

**mpy = mils per year (0.001″ thickness loss per year)**

| Scenario | Corrosion Rate | Time to 0.063″ Loss | Real‑World Example |
|----------|---------------|---------------------|-------------------|
| **Carbon‑aluminum, seawater, no isolation** | 50–200 mpy | 4 months – 1.5 years | Beach‑based aircraft, coastal environment |
| **Carbon‑aluminum, humid interior, no isolation** | 10–50 mpy | 1.3–6.3 years | Cabin moisture, condensation cycles |
| **Stainless‑aluminum, moderate environment** | 20–100 mpy | 0.6–3 years | Fasteners in wet wing |
| **With proper isolation** | <1 mpy | >63 years | Properly designed joint |

**Key insight:** Aircraft operate in harsh environments — altitude changes cause condensation, coastal operations bring salt, and temperature cycles create moisture. Assume the **worst‑case environment** for critical joints.

---

## Certified Aircraft Prevention Methods

### 1. Isolation Barriers: Break the Electrical Path

**Fiberglass cloth interlayer:**
- **Style 7781 fabric** (0.010″ minimum thickness)
- Placed between carbon and aluminum
- Non‑conductive, prevents direct contact
- Can be impregnated with resin or used dry in adhesive films

**Adhesive films with carriers:**
- **3M AF‑163‑2K** — epoxy film adhesive with fiberglass carrier
- **Cytec FM‑300** — similar aerospace adhesive
- Provides both bonding and isolation

**Builder‑friendly alternative:** Dry fiberglass cloth (style 7781) with epoxy wet layup.

### 2. Surface Treatments: Protect the Anode

**Anodizing (MIL‑A‑8625):**
- **Type I (Chromic acid):** Good corrosion resistance, bonds well
- **Type II (Sulfuric acid):** Most common, excellent protection
- **Type III (Hardcoat):** Thick, wear‑resistant but may reduce fatigue strength
- **Must be sealed** after anodizing (hot water or dichromate seal)

**Chromate conversion coating (Alodine):**
- Chemical conversion layer
- Provides some protection, enhances paint adhesion
- Less effective than anodizing but easier for complex shapes

**Epoxy primer:**
- **PPG CA‑7000**, **AkzoNobel Aerodur**, **Deft 02‑GN‑085**
- Non‑conductive barrier coating
- Apply over clean/anodized aluminum
- Minimum 0.001″ dry film thickness

**Best practice:** Anodize + epoxy primer for maximum life.

### 3. Fastener Selection: Choose Compatible Materials

**Titanium (Ti‑6Al‑4V):**
- Best choice for aluminum structures
- Galvanically compatible
- High strength‑to‑weight
- Expensive but worth it for critical joints

**Stainless steel with isolation:**
- Use **fiberglass‑filled nylon washers** (MS/NAS 21919)
- Apply **sealant** under fastener head
- Consider **isolated bushings** for larger fasteners

**Composite fasteners:**
- Fiberglass/polyester or Vespel
- Non‑conductive, low strength
- Suitable for non‑structural attachments

**Avoid:** Cadmium‑plated steel directly against aluminum (moderate risk).

---

## Homebuilder‑Accessible Solutions

### Step‑by‑Step: Carbon Fiber to Aluminum Joint

1. **Prepare aluminum:**
   - Send to local anodizing shop: "Type II per MIL‑A‑8625, 0.0005″ minimum, sealed"
   - Or apply Alodine 1200S following manufacturer instructions
   - Apply epoxy primer (Deft 02‑GN‑085 is user‑friendly)

2. **Apply isolation barrier:**
   - Cut style 7781 fiberglass cloth to size
   - Wet out with epoxy (West System, Pro‑Set, MGS)
   - Lay between carbon and aluminum
   - Or use 3M Scotch‑Weld AF‑163‑2K film adhesive (requires oven cure)

3. **Assemble with proper fasteners:**
   - Use titanium fasteners (AN/MS series)
   - If using stainless, add fiberglass‑filled nylon washers
   - Apply aviation sealant under fastener heads

4. **Seal edges:**
   - Apply polysulfide sealant (3M EC‑801) or polyurethane (Sikaflex‑295) to perimeter
   - Prevent electrolyte ingress
   - Tool to smooth fillet

### Local Anodizing Shop Specifications

When sending parts out:
- "Type II sulfuric acid anodizing per MIL‑A‑8625"
- "Minimum thickness 0.0005″"
- "Seal with hot deionized water"
- "Rack for complete coverage — no shadowing"
- Typical cost: $50–200 depending on part size/quantity

### Alternative to Pro‑Seal: Builder‑Friendly Sealants

**Polysulfide alternatives:**
- **3M EC‑801** — Two‑part, lower odor than traditional Pro‑Seal
- **Flame‑Master CS‑3200** — Similar performance, different application

**Polyurethane sealants (easier application):**
- **Sikaflex‑295 UV** — One‑part, UV‑resistant, toolable
- **3M 5200** — Marine grade, excellent adhesion
- **Lord Fusor 108B** — Two‑part polyurethane

**Epoxy‑based sealants:**
- **3M EC‑2216 B/A** — Two‑part epoxy adhesive/sealant
- Can replace both adhesive and sealant in some applications

---

## Prevention Method Matrix

| Method | Effectiveness | Cost | Build Difficulty | Best For |
|--------|--------------|------|------------------|----------|
| **Fiberglass cloth (7781)** | High | Low ($) | Easy | Wet layup composites, simple joints |
| **3M AF‑163‑2K film** | Very High | Medium ($$) | Moderate (oven cure) | Critical structural bonds |
| **Type II anodizing** | High | Medium ($$) | Requires vendor | All aluminum components |
| **Alodine + epoxy primer** | High | Low ($) | Moderate (spray) | Complex shapes, hard‑to‑anodize parts |
| **Titanium fasteners** | Very High | High ($$$) | Easy | All critical fasteners |
| **Stainless + isolation washers** | Medium | Low ($) | Easy | Non‑critical attachments |
| **Edge sealing** | Medium | Low ($) | Easy | Perimeter moisture exclusion |

---

## Critical Design Rules

1. **Never allow carbon fiber to contact aluminum directly.** Always interpose fiberglass or adhesive film.
2. **Anodize all aluminum** that will be bonded, fastened, or exposed to moisture.
3. **Seal all edges** of composite‑metal joints to exclude electrolytes.
4. **Use titanium fasteners** where possible. If using stainless, add isolation.
5. **Design for drainage** — avoid pockets where water can accumulate.
6. **Assume condensation will occur** inside closed structures (wings, fuselage).
7. **Inspect regularly** — look for white powder (aluminum oxide) or blistering.

---

## MAOS‑Specific Applications

For the MAOS pressurized pod‑and‑boom aircraft:

### Pressure Vessel: Aluminum Liner + Carbon Overwrap
- **Isolation layer:** Style 7781 fiberglass between aluminum and carbon
- **Aluminum preparation:** Type II anodizing + epoxy primer
- **Bonding:** 3M AF‑163‑2K film adhesive
- **Edge sealing:** Sikaflex‑295 UV perimeter seal

### Wing Attachment: External Saddle
- **Saddle material:** 2024‑T3 aluminum
- **Surface treatment:** Anodize + primer
- **Isolation:** Fiberglass cloth at saddle‑pod interface
- **Fasteners:** Titanium (Ti‑6Al‑4V) taper pins and bolts

### Control Surface Hinges
- **Stainless steel hinges** with fiberglass‑filled nylon bushings
- **Anodized aluminum attachment points**
- **Sealed bearing surfaces**

---

## Common Pitfalls to Avoid

### 1. "Dry Assembly" Assumption
Assuming interior joints stay dry. **Reality:** Condensation occurs with temperature cycles. Design for wet conditions.

### 2. Relying Only on Paint
Paint alone is not sufficient isolation. It develops pinholes, scratches, and degrades.

### 3. Mixing Fastener Materials
Using stainless bolts with aluminum nuts (or vice versa). Use compatible materials throughout the stack.

### 4. Ignoring Edge Effects
Sealing only the visible surfaces while moisture wicks in from cut edges.

### 5. Over‑Optimistic Environment
Designing for "normal" conditions rather than worst‑case (coastal, high‑humidity, temperature extremes).

---

## Inspection and Maintenance

### What to Look For
- **White powder:** Aluminum oxide (corrosion product)
- **Blistering:** Paint lifting from substrate
- **Staining:** Discoloration around fasteners
- **Red dust:** Iron oxide (steel corrosion)
- **Loss of clamp‑up:** Fastener loosening from material loss

### Inspection Intervals
- **Annual:** Visual inspection of all critical joints
- **Every 3–5 years:** Detailed inspection with borescope for hidden areas
- **After extreme exposure:** Saltwater, acid rain, industrial environment

### Repair Techniques
1. **Disassemble** affected joint
2. **Remove corrosion** (aluminum: Scotch‑Brite; steel: wire brush)
3. **Re‑apply surface treatment** (anodize or Alodine if possible)
4. **Replace isolation barrier**
5. **Re‑assemble** with fresh sealant
6. **Consider upgrade** to more compatible materials

---

## The Builder's Checklist

### Before Design
- [ ] Identify all dissimilar material interfaces
- [ ] Calculate voltage differences for each pair
- [ ] Plan isolation methods for high‑risk combinations
- [ ] Select compatible fastener materials
- [ ] Design for drainage and inspection access

### During Build
- [ ] Anodize all aluminum components
- [ ] Apply epoxy primer to anodized surfaces
- [ ] Install fiberglass isolation layers
- [ ] Use titanium fasteners for critical joints
- [ ] Seal all edges with appropriate sealant
- [ ] Document materials and treatments used

### Before First Flight
- [ ] Conduct detailed corrosion inspection
- [ ] Verify all isolation barriers are intact
- [ ] Check for proper sealing at edges
- [ ] Establish inspection intervals in maintenance manual

---

## Conclusion: Corrosion Is Preventable

Galvanic corrosion in aircraft composites is not a matter of **if** but **when** — unless you intentionally prevent it. The solutions are well‑established, relatively low‑cost, and builder‑accessible:

1. **Understand the voltage differences** between your materials
2. **Break the electrical path** with isolation barriers
3. **Protect the anode** with surface treatments
4. **Choose compatible fasteners**
5. **Seal against electrolyte ingress**
6. **Design for inspection and maintenance**

For MAOS, this means anodized aluminum, fiberglass isolation, titanium fasteners, and sealed joints — a modest investment in time and money that prevents catastrophic material failure years down the line.

The aircraft that fly for decades are not the ones with magical corrosion‑proof materials, but the ones where the builder understood and addressed galvanic compatibility from the start.

---

*This article synthesizes technical research conducted for the MAOS Design Review Board. All information is for experimental amateur‑built aircraft only and must be validated by a qualified aerospace engineer before application.*

**Related Articles:**
- [Pressurized Homebuilt Aircraft: A Technical Guide](/articles/2026-03-27-homebuilt-pressurization-guide/)
- [The Removable Wing Problem: Non‑Penetrating Attachments for Pressurized Homebuilts](/articles/2026-03-27-removable-wing-attachment-guide/)

**Tags:** #galvanic-corrosion #composite #aluminum #carbon-fiber #aircraft-construction #experimental #homebuilt #materials #MAOS #corrosion-prevention