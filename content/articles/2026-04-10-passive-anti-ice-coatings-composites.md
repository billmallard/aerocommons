---
title: "Passive Anti-Ice Coatings for Composite Aircraft: Superhydrophobic and Hydrophilic Approaches"
date: 2026-04-10T09:00:00-05:00
description: "Two fundamentally different strategies — repelling water and embracing it — are emerging as passive complements to active ice protection. Here's what the research says, and what's actually available to buy."
tags: ["structures", "composites", "analysis", "design-decisions", "maos", "ice-protection"]
author: "AeroCommons Design Board"
project: "maos"
article_type: "analysis"
draft: false
---

Ice protection in general aviation has traditionally meant one of two things: a pneumatic boot that cracks ice off the leading edge, or a thermal system that prevents it from forming in the first place. Both work. Both add weight, complexity, and power demand. For a composite aircraft in the experimental category, the absence of a certification burden opens a third path worth taking seriously: passive coatings that change how ice interacts with the surface itself.

This article isn't about eliminating an active ice protection system. It's about understanding what passive coatings can contribute — either as a standalone layer for light icing environments, or as an efficiency multiplier that reduces the energy demand of an active system. For MAOS, which already carries a waste-heat-fed thermal system as its primary strategy, a passive coating on composite leading edges could meaningfully reduce the threshold at which that system needs to engage.

Two distinct coating philosophies have emerged from the research. They operate by opposite mechanisms, and understanding why reveals a lot about what each can and cannot do.

---

## The Problem with Composites Specifically

Metal wings present a relatively forgiving surface for ice accretion — the material itself is thermally conductive, which helps with electrothermal systems, and is robust enough to accept adhesive tape, metal shields, and aggressive mechanical solutions. Carbon fiber composite surfaces are a different substrate. CFRP has low thermal conductivity, is sensitive to mechanical stress concentrators, and can delaminate if an adhesive bond fails under cyclic thermal loads.

This makes passive coatings particularly attractive for composite structures. A coating applied to the gel coat or clear top coat adds negligible weight, no power draw, and no mechanical interface with the laminate. If it wears, you reapply. There's no structural consequence.

The catch is that coatings have to survive the same environment that creates icing — rain, airborne particulates, UV, and high-velocity airflow — and do so while remaining thin enough not to affect aerodynamics. That durability challenge is the central problem in this field, and it's what separates laboratory results from flight-ready products.

---

## Strategy One: Superhydrophobic Coatings

A superhydrophobic surface is one where water contact angles exceed 150°. The classic example is a lotus leaf: water droplets bead into near-perfect spheres and roll off rather than wetting the surface. The mechanism is a combination of low surface energy chemistry (often fluorinated or silicone-based) and microscale or nanoscale surface texture that traps air beneath the droplet. This is called the Cassie-Baxter state — the droplet rests on a composite surface of solid and air, touching neither fully.

### How It Prevents Ice

Superhydrophobic surfaces address icing through several simultaneous mechanisms:

- **Droplet rebound:** Supercooled water droplets impacting the surface at flight speed bounce off before they can nucleate. This has been measured directly in icing wind tunnel tests, with droplet contact times reduced dramatically compared to untreated surfaces.
- **Delayed nucleation:** Because contact area between water and surface is minimized, the surface has fewer sites for heterogeneous ice nucleation to begin. Freezing is delayed even when droplets do stay.
- **Reduced adhesion:** Ice that does form bonds primarily through mechanical interlocking with surface texture. On a smooth surface, ice pulls free more easily. On a superhydrophobic surface, the air layer beneath ice formation reduces the real contact area and therefore the adhesion force.

Research published in MDPI's *Aerospace* journal on small aircraft applications found that superhydrophobic coatings could delay ice formation significantly under simulated conditions, and that when combined with an active thermal system, they reduced the power required for anti-icing by 60% or more when applied to the first 30% of chord. The coating shifts the active system from a prevention mode to a management mode.

Studies on carbon fiber-reinforced composite surfaces specifically confirm compatibility — the coatings bond to cured CFRP and gel coat substrates, and ice that forms on treated CFRP surfaces releases with substantially less force than on untreated composite. One study using commercial permanent superhydrophobic coatings on CFRP found ice could be removed by hand with forces that would be achievable aerodynamically at cruise speed.

### The Erosion Problem

This is where the field runs into a wall. The micro/nano surface texture that creates the Cassie-Baxter state is mechanically fragile. Rain droplets at flight speed — 50 to 150 m/s impact velocities — gradually destroy the surface topology. This is called the wetting transition: once the texture is eroded enough that water penetrates to the surface, the coating transitions from the Cassie-Baxter state to the Wenzel state, where water fills the texture grooves and actually increases contact area. The coating doesn't just degrade — it can become *worse* than a bare surface.

Research on UAV icing mitigation identifies this erosion challenge as the primary obstacle to practical deployment. Durability varies significantly by formulation, but even well-optimized coatings show measurable degradation after simulated rain erosion tests equivalent to a few hundred flight hours.

This doesn't make superhydrophobic coatings useless — it means they require maintenance, and they may not be suitable for high-impact zones like the very tip of a leading edge without additional mechanical protection (metal or tape strips). Aft of the leading edge stagnation point, erosion rates drop considerably, and coating durability improves.

---

## Strategy Two: Hydrophilic Coatings

The hydrophilic approach is counterintuitive. Where superhydrophobic coatings try to minimize water contact, hydrophilic coatings attract it. A hydrophilic surface has a very low contact angle — water spreads rather than beads. The question is why this would be useful for anti-icing, and the answer lies in what happens at the molecular level when a hydrophilic polymer is in contact with cold water.

### The Quasi-Liquid Layer Mechanism

Certain hydrophilic polymers bind water molecules tightly enough through hydrogen bonding that the bound water cannot crystallize at temperatures where bulk water would freeze. This creates a quasi-liquid, non-frozen layer at the interface between the coating and any ice above it. The layer acts as a self-lubricating film — ice forms above it, but it never fully bonds to the substrate. The result is very low ice adhesion strength, not because ice can't form, but because it can't grip.

Research on poly[poly(ethylene glycol) methyl ether methacrylate] (PPEGMA) polymer brush coatings measured ice adhesion strengths below 100 kPa across a range of temperatures. Critically, the adhesion showed a strong dependence on measurement speed consistent with viscous liquid behavior — the interfacial layer is genuinely fluid even below 0°C. In-situ observation of the ice-adhesion interface confirmed the mechanism directly.

Polyzwitterion brush coatings — specifically poly(sulfobetaine methacrylate) (PSBMA) — show even stronger effects. DSC analysis of PSBMA confirms it contains more non-freezable bound water than typical polyelectrolytes. At −20°C, PSBMA brush coatings demonstrate ice adhesion of approximately 60 kPa, a 75% reduction compared to bare silicon. Poly-acrylic acid cross-linked systems have achieved below 12 kPa — below the threshold where accumulated ice will shed under its own weight or aerodynamic drag without any active intervention.

A 2025 study published in *Nature Communications Materials* on concentrated polymer brushes (CPBs) established that the brush density matters critically. Only surfaces in the concentrated polymer brush regime (σ* ≥ 0.15) achieved both high anti-icing performance and meaningful durability. Sparse brush layers had lower performance and degraded faster.

### Why This Might Be More Durable

The durability comparison with superhydrophobic coatings is important. Superhydrophobic performance depends on micro/nano surface texture remaining intact. Hydrophilic polymer brush coatings don't rely on texture — they're chemically smooth surfaces. Rain erosion degrades them by removing polymer chains, which is a slower and more gradual failure mode than the abrupt wetting transition that superhydrophobic coatings experience. A partially degraded hydrophilic coating still reduces ice adhesion; it just does so less effectively than when new.

This makes hydrophilic coatings potentially more suitable for leading edge zones where erosion rates are highest, even though the ice-shedding mechanism is passive rather than preventive.

### Honest Limitations

Hydrophilic coatings don't prevent ice formation — they prevent ice bonding. An aircraft flying through icing conditions with only a hydrophilic coating will accrete ice; the ice will just shed more readily once formed. In heavy icing, shedding may not be fast enough to prevent aerodynamically significant accumulation.

At extreme cold (below approximately −30°C), even the quasi-liquid layer can freeze, and adhesion rises. The mechanism is most effective in the moderate icing temperature range of 0°C to −20°C, which happens to be where supercooled liquid water — the most dangerous form for inflight icing — is most common.

No FAA certification pathway currently exists for hydrophilic coatings as a primary ice protection method, but that's irrelevant for MAOS under the experimental amateur-built category.

---

## A Third Option: SLIPS (Slippery Liquid-Infused Porous Surfaces)

SLIPS technology is worth mentioning because it occupies a middle ground. A SLIPS surface is a porous substrate — often PTFE fiber or a nano-textured polymer — infused with a lubricating liquid (typically silicone oil or fluorinated oil) that is immiscible with water and ice. The lubricant fills the pores, creating a smooth liquid surface that water and ice cannot bond to.

Ice adhesion on SLIPS surfaces has been measured below 20 kPa in laboratory testing — comparable to the best hydrophilic results. Because the interface is always liquid, ice slides off with minimal force. The surface is also self-healing to a degree: if the lubricant is disturbed, capillary forces redistribute it.

The drawback is that the lubricant depletes over time. Wind, rain, and UV gradually remove it, and the coating becomes less effective as the pores dry out. This makes SLIPS more maintenance-intensive than either solid coating strategy. It's a promising technology but not yet practical for persistent real-world aviation use without a mechanism for lubricant replenishment.

---

## Comparison Summary

| Property | Superhydrophobic | Hydrophilic (Polymer Brush) | SLIPS |
|---|---|---|---|
| Primary mechanism | Droplet rebound, nucleation delay | Ice adhesion reduction via liquid layer | Ice adhesion reduction via liquid interface |
| Ice adhesion at −20°C | 50–200 kPa (varies widely) | 12–100 kPa | <20 kPa |
| Prevents ice formation? | Partially (delays nucleation) | No | No |
| Reduces ice adhesion? | Yes | Yes, strongly | Yes, strongly |
| Leading edge durability | Poor (texture erosion) | Moderate (gradual polymer loss) | Poor (lubricant depletion) |
| Composite compatibility | Confirmed (CFRP studies) | Research phase | Research phase |
| Active system energy savings | Up to 60–80% | Not yet quantified | Not yet quantified |
| Commercial availability | Yes (several products) | Limited | Not widely available |

---

## What You Can Actually Buy

This is where the experimental category matters. A certified aircraft has to use qualified products applied per approved data. An experimental amateur-built aircraft can apply any coating the builder judges appropriate and document the results. That's a meaningful freedom.

### AeroPel NPL — The Most Impressive Numbers

AeroPel, developed by Oceanit originally for military aerospace applications and tested by the Army Corps of Engineers Cold Regions Research and Engineering Laboratory (CRREL), holds the most compelling commercial performance data. Independent testing measured ice adhesion strength below 10 kPa — compared to bare aluminum at over 1,200 kPa. That's two orders of magnitude reduction.

AeroPel is formulated as an icephobic/omniphobic coating, meaning it repels both water and oils. It's available commercially through Oceanit's AeroPel product line. The product page lists APC200 and APC400 series variants. It's not inexpensive and requires a quote, but it's a real product that has been tested in actual aerospace icing conditions rather than just a university laboratory.

For MAOS, AeroPel NPL applied to composite leading edges — inboard of the stagnation point where aerodynamic loads are lower — is a credible candidate for the most protective passive layer currently purchasable.

### NEI Corporation NANOMYTE SuperAi

NEI Corporation's NANOMYTE® SuperAi is a nanocomposite coating that reduces ice adhesion by up to 80% compared to untreated surfaces. It's a single-component, ambient-cure product available in quantities from 1 liter upward (quote required). The product page explicitly lists aerospace as a target application including aircraft wings and propellers.

SuperAi has a ceramic nanocomposite character — it's harder and more scratch-resistant than many superhydrophobic coatings, which likely improves its durability profile. The smooth, glossy finish also avoids the rough, matte appearance of some superhydrophobic coatings that can cause aerodynamic penalties. NEI has published independent icing test results confirming performance.

This product sits somewhere between a pure superhydrophobic and an icephobic coating in its mechanism — the surface isn't heavily textured, relying more on low surface energy chemistry than micro-structure.

### PPG HYDROSKIP

PPG's HYDROSKIP was originally developed for the F-16 program to maintain windshield visibility in rain without wipers. It's hydrophobic but not superhydrophobic in the full lotus-effect sense — it's intended primarily for aircraft transparencies (acrylic and polycarbonate). It meets ASTM F791 and ASTM 484 standards and is available through PPG Aerospace and distributors like Skygeek.

HYDROSKIP is probably not the right choice for structural composite surfaces, but it's worth knowing about for MAOS's windshield and any polycarbonate fairings. It's a mature, proven product with a long service record and is priced accessibly for small-scale purchase.

### NeverWet (Consumer Grade — Know Its Limits)

NeverWet and similar consumer superhydrophobic sprays are widely available, inexpensive, and genuinely superhydrophobic when freshly applied. The dramatic water-beading behavior is real, and short-term anti-ice delay effects have been demonstrated even with consumer products.

The honest assessment: contact angle performance is good; durability is not. Most consumer formulations show significant degradation within weeks in outdoor exposure, and flight-speed rain erosion would accelerate this substantially. For ground testing on non-critical surfaces — understanding what the lotus effect looks like, testing application techniques, exploring coverage areas — NeverWet is a legitimate experimental tool. For a surface expected to perform over a season of flying, it is not.

---

## MAOS Application Strategy

MAOS already documents a waste-heat-fed thermal ice protection system as its primary strategy, using engine and battery thermal output to heat leading edge surfaces. Passive coatings fit as a complementary layer, not a replacement.

The practical approach for MAOS during Phase 1 and early flight testing:

**Leading edge zone (0–15% chord):** This is the highest erosion zone and the most critical aerodynamically. A product like NEI SuperAi or AeroPel NPL applied here provides the most durable passive reduction in ice adhesion available commercially. Expect to inspect and reapply periodically. Metal tape at the very stagnation line protects the coating at the zone of highest impact.

**Aft of leading edge (15–60% chord):** Lower erosion rates here make superhydrophobic coatings more durable. This is where energy savings from coating synergy with the thermal system are most achievable — coatings here can reduce thermal system engagement time significantly. NEI SuperAi or AeroPel are both reasonable choices.

**Propeller leading edges:** Propellers operate at tip speeds where erosion rates are severe. No current passive coating is likely to survive long-term at high-RPM prop leading edges without mechanical protection. Erosion tape with anti-ice chemistry infused is a more realistic near-term option.

**Testing approach:** Because MAOS is experimental, it's feasible to instrument a wing panel, apply coating, and fly instrumented icing passes to directly observe performance. The certification burden that prevents certified operators from doing this kind of first-principles measurement doesn't apply here. Document ice accretion patterns, shedding behavior, and thermal system engagement events before and after coating application. That data would be genuinely useful to the broader experimental community.

**Hydrophilic coatings:** Currently, the most advanced hydrophilic polymer brush coatings are still research-phase materials not available as off-the-shelf products. This is a space to watch. If PEG or polyzwitterion brush coatings become commercially available at reasonable scale — and the research trajectory suggests they will — they become particularly interesting for MAOS composite surfaces given their durability advantage over texture-dependent approaches.

---

## Where This is Going

The research literature through 2025 shows clear convergence toward multifunctional coatings that combine mechanisms: hydrophilic base layers for low ice adhesion paired with photothermal or electrothermal top layers for active heat generation, all in a single formulation. Carbon nanotube-reinforced coatings that are both icephobic and resistively heatable have been demonstrated. For a vehicle like MAOS where the electrical bus is already present, a coating that could be powered to supplement the passive layer would be architecturally interesting.

PFAS-free formulations are also advancing — the traditional superhydrophobic chemistry relied heavily on perfluorinated compounds that face increasing regulatory pressure. Replacements using 1,2-epoxyhexadecane and similar alternatives are showing comparable performance, which matters for long-term product availability.

The durability problem is not solved. That's the honest state of the field. But it is being narrowed, and the performance numbers — 80% reduction in ice adhesion, 60–80% reduction in thermal system energy consumption when coatings are combined with active systems — are large enough to justify applying what's available now while the science matures.

---

*MAOS is an experimental amateur-built aircraft project operating under FAA 14 CFR Part 21.191(g). Coating strategies discussed here are evaluated outside any certification framework and should not be interpreted as guidance for certificated aircraft operations. Always evaluate passive coating strategies in conjunction with, not as replacement for, a primary ice protection system appropriate to the flight envelope.*

*Further reading: [Waste Heat Ice Protection and Battery Thermal Management](../2026-04-03-waste-heat-ice-protection-battery-thermal/)*
