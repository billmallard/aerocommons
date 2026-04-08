---
title: "Smooth Area Progression: The Subsonic Aerodynamics Principle Engineers Underuse"
date: 2026-04-07T10:00:00-05:00
description: "The Whitcomb area rule gets the spotlight, but the underlying principle — smooth total cross-sectional area distribution — earns real drag savings at any speed. A look at the math, the interference drag numbers, and how MAOS wing placement and fuselage shaping apply it."
tags: ["aerodynamics", "analysis", "design-decisions", "drag", "geometry", "maos", "jones-equivalent-body"]
author: "AeroCommons Design Board"
project: "maos"
article_type: "analysis"
draft: false
---

The Whitcomb area rule has a certain glamour to it. Photographs of the original F-102 Delta Dagger alongside its wasp-waisted successor — the aircraft that actually broke the sound barrier in level flight — tell a compelling story. The visual drama of an indented fuselage made the area rule famous, and "area ruling" became shorthand for any aerodynamic sophistication involving cross-sectional area distribution.

That spotlight has a shadow. The underlying principle extends well below transonic speeds, earns measurable drag savings on every production airliner and well-designed general aviation aircraft, and receives almost no discussion in the experimental aircraft community. It goes by several names — smooth area progression, favorable area distribution, equivalent body optimization — and it matters for MAOS.

---

## The Foundation: Jones' Equivalent Body Theorem

In 1956, Robert T. Jones of NACA published a result that unified the aerodynamics of arbitrary aircraft configurations at the speed of sound. His **equivalent body theorem** states:

> The wave drag of any aircraft configuration at M = 1 equals the wave drag of its equivalent body of revolution — a body whose cross-sectional area at each station equals the summed cross-sectional area of the actual configuration at that station.

"Summed cross-sectional area" means exactly that: at every longitudinal station, you add together the fuselage slice, the wing slices, the nacelle slices, the tail slices — everything. The resulting distribution, plotted against aircraft length, defines the equivalent body. Its drag equals the configuration's drag.

This is the theoretical basis for Whitcomb's area rule. If the wing and fuselage happen to reach their combined maximum cross-section at the same station, the equivalent body has a large, sudden area hump at that point — and large, non-smooth humps mean high wave drag. Indenting the fuselage where the wing adds its area flattens the equivalent body's distribution.

**The key word is "smooth."** Wave drag at M = 1 is minimized not by shrinking the aircraft, but by making the area distribution change gradually and continuously along the full length.

---

## The Sears-Haack Body: The Mathematical Lower Bound

The ideal reference shape — the closed body of revolution with the absolute minimum pressure drag for a given volume and length — was derived independently by Sears and Haack. Its area distribution follows:

```
S(x) = A_max × [1 − (2x/L − 1)²]^(3/2)
```

where x runs from 0 to L and A_max is the cross-sectional area at the midpoint. This is a smooth, rounded shape that looks like an elongated American football: symmetric, with the peak exactly at mid-length, tapering continuously to zero at both ends.

Its volume relates to maximum cross-section by:

```
Volume = (3π / 16) × A_max × L
```

And its minimum wave drag is:

```
D_wave = (9π/2) × q × A_max² / L²
```

Two things stand out in that drag formula:

**Area squared.** Double the maximum cross-section and wave drag quadruples. The incentive to keep cross-sections small and to avoid unnecessary area peaks is not linear — it is punishing.

**Length squared in the denominator.** A longer fuselage, all else equal, produces less wave drag. This is why supersonic aircraft are slender. It also explains why the penalty for a given volume of fuselage grows as you compress it into a shorter body.

At MAOS cruise speeds — Mach 0.23 — there is no wave drag. The Sears-Haack derivation uses linearized supersonic theory and is strictly inapplicable below Mach 0.7 or so. But the formula is not the point here. What carries over is the physical logic: **large, abrupt changes in cross-sectional area distribution cause pressure gradients that the flow cannot easily negotiate, and the resulting drag penalty is real at any speed.**

---

## Where the Benefit Actually Lives at Subsonic Speeds

In subsonic flow, the equivalent penalty to wave drag is **interference drag** at the wing-fuselage junction. When the fuselage and wing each contribute expanding cross-sections at the same longitudinal station — creating a combined area hump — the flow at the junction must decelerate and recover pressure over a short distance. That adverse gradient promotes boundary layer separation, and even where separation does not occur, the pressure recovery is incomplete and appears as additional pressure drag on both surfaces.

This penalty is quantified in Hoerner's *Fluid-Dynamic Drag* and confirmed in numerous NACA and NASA reports on wing-body combinations. The empirical range:

| Configuration | Interference Drag Penalty |
|---|---|
| Blunt junction, no fillet, overlapping area peaks | +10 to +15 drag counts (ΔCD = 0.0010–0.0015) |
| Rounded junction with basic fairing | +5 to +8 drag counts |
| Well-designed fillet, moderate area overlap | +2 to +4 drag counts |
| Optimized area progression + full root fillet | ~0 drag counts (can turn slightly favorable) |

A drag count is ΔCD = 0.0001 referenced to wing area. For MAOS at its current cruise condition (CL = 0.263, Sref = 121.5 ft², CD_total ≈ 0.0161, L/D ≈ 16.3), the value of each drag count is tangible:

```
Recovering 10 drag counts:
  CD_total: 0.0161 → 0.0151
  L/D:      16.3   → 17.4     (+6.7%)
```

A 6.7% improvement in L/D is not cosmetic. At fixed cruise power, it is a direct range multiplier. Over a 400 nm leg, it is approximately 25 additional nautical miles with zero change to the engine, propeller, battery, or wing planform.

---

## The Practical Rule: Maximum Fuselage Section Forward of the Wing

Jones' theorem gives an operational design heuristic that applies at all speeds:

**Position the fuselage's maximum cross-sectional area station forward of the wing attachment. As the wing begins adding its own cross-sectional area, the fuselage should already be tapering.**

When this is achieved, the equivalent body's combined area distribution passes through the wing station smoothly — the fuselage contribution is declining at the same stations where the wing contribution is growing. In favorable cases these trends partially offset each other, producing a total equivalent body that is more Sears-Haack-like through the mid-section of the aircraft than either component would be individually.

This is why well-designed aircraft consistently place the wing on the aft portion of the fuselage's "shoulder" — not at its widest point. Piper's Malibu/Meridian is a useful reference: the fuselage is clearly at full section ahead of the wing root, and the cabin taper that makes the aft fuselage so graceful is not purely aesthetic.

The reverse arrangement — wing attached where the fuselage is still expanding toward its maximum, or where the maximum section persists through the entire wing root zone — creates interference drag that no amount of root fillet can fully recover.

---

## Application to MAOS

The current MAOS pod places the wing root at **X = 5.975 ft**, which is 43% of the 14 ft pod length. The pod maintains its maximum cross-section from XSec_1 (30%) through XSec_2 (67%) — a span of 5.2 ft that brackets the wing root station on both sides. The combined equivalent body at the wing station has both contributions near their peaks simultaneously.

Several active design decisions are moving this in the right direction:

**Wing moving aft.** CG balance on a hybrid-electric aircraft with a forward battery pack and pod-mounted motor will likely push the wing aft of 43%. Every foot aft improves the area progression at the junction and, from a structures standpoint, shortens the moment arm of the aft fuselage.

**XSec_2 narrowing.** The max-section pod width of 60" is needed through the cockpit and front seat area (XSec_1 at 30%), but the rear seating zone (XSec_2 at 67%) can taper to something closer to 54–56" — enough for rear-seat comfort without the full aisle width that the forward section provides. Narrowing XSec_2 reduces the equivalent body's area at exactly the station closest to the wing root, which is the most effective place to reduce it.

**XSec_3 needs attention.** Currently still at 52" width (the pre-widening value), XSec_3 at 77% represents a step-in that breaks the smooth taper. It should be treated as part of a deliberate progression — something like 57" at XSec_2, 53" at XSec_3, closing to zero at the tail — rather than a sudden jump.

A rough estimate of the achievable improvement from these three changes combined — wing to ~52%, XSec_2 to 56", smooth XSec_3 transition, and a full root fillet — is in the range of **6 to 10 drag counts** relative to the current configuration. At the conservative end, L/D improves from 16.3 to approximately 16.9. At the optimistic end, it approaches the 17.4 figure computed above. Neither figure depends on any change to the wing, propulsion, or tail.

---

## The Root Fillet: What to Do When Geometry Prevents the Ideal

The pilot must sit somewhere. The cabin must have a usable cross-section through the wing station. Perfect area progression is not available to any aircraft that also needs to carry people. The root fillet is the compensation tool.

A well-designed root fillet does two things simultaneously. It smooths the **geometric junction** between fuselage skin and wing lower surface, eliminating the sharp corner that trips the boundary layer and acts as a bluff-body drag source. And it adds a local area distribution that acts as a **miniature area rule** — slightly increasing the fuselage cross-section just ahead of the wing root and decreasing it just aft, which smooths the combined equivalent body through the junction without requiring the global fuselage geometry to change.

Good fillet design is non-trivial. A fillet that is too short recovers little. One that is too large can actually increase drag by adding wetted area without sufficient interference recovery. The optimum extends upstream of the wing leading edge by roughly one wing-root chord and downstream of the trailing edge by a similar distance, with a maximum fillet radius chord at roughly 15% of the half-span inboard chord.

For MAOS, the pod-wing junction is a natural candidate for detailed attention once the pod geometry and wing position stabilize. At that point, a CFD session — or at minimum a CompGeom interference analysis in VSPAERO — can quantify the residual interference drag and guide fillet sizing.

---

## The Principle, Restated Simply

The Mach number at which the Whitcomb area rule matters is not the Mach number at which the underlying logic matters. Every aircraft flying in air is pushing volume through a medium that resists abrupt changes. The smoother the combined cross-sectional area distribution of the entire aircraft — fuselage plus wing plus tail plus nacelles — the less the flow is forced to negotiate sudden pressure gradients, and the less energy is deposited in the wake.

Put the bulk of the fuselage forward (or aft depending on your aircraft design) of the wing. Let the fuselage be contracting as the wing begins to add its area. Smooth the junction with a fillet that extends a full chord length in each direction. These three steps do not require a redesign — they require awareness of what the flow sees, and deliberate choices about where things go.

For MAOS, those choices are still being made. That is the right time to make them.

---

## Open Questions

1. **How far aft should the MAOS wing move?** CG analysis will set the constraint, but the aerodynamic optimum is as far aft as balance allows. A sensitivity study — L/D vs. wing X position, holding tail volume coefficients constant — is the right tool once a mass breakdown is available.

2. **What width for XSec_2?** The transition from 60" (XSec_1, cockpit) to something narrower at XSec_2 should be sized so the rear seats remain comfortable for two adults side by side, not for aisle width. That target is approximately 52–54" interior, or 55–57" outer. The aerodynamic and ergonomic answers happen to be compatible.

3. **Does the boom-pod junction need its own equivalent-body treatment?** The tail boom attaches at the top of the pod aft section, adding cross-sectional area at a station that is already complicated by the aft pod taper. A small fairing or the boom-root geometry itself may need to be treated as a secondary area-rule problem.
