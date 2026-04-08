---
title: "Smooth Area Progression: The Subsonic Case for Getting Fuselage Volume Right"
date: 2026-04-08T10:00:00-05:00
description: "How Jones' equivalent body theorem and the Sears-Haack body apply to subsonic aircraft design — and why where you put fuselage volume relative to the wing matters even when you're nowhere near transonic speeds."
tags: ["aerodynamics", "analysis", "design-decisions", "geometry", "drag", "maos"]
author: "AeroCommons Design Board"
project: "maos"
article_type: "analysis"
draft: false
---

Most homebuilder aerodynamics resources mention the area rule once — in the context of 1950s jet fighters developing a "wasp waist" to break the transonic drag barrier — and then move on. The implication is that below Mach 0.7, cross-sectional area distribution doesn't matter. That's not quite right.

The underlying principle extends to subsonic speeds in a different form, with a smaller but still meaningful drag penalty for getting it wrong. For MAOS, which is designed around a large-diameter pressurized pod and a pylon-mounted wing, understanding the mechanism is directly useful.

---

## The Foundation: Jones' Equivalent Body Theorem

In 1956, Robert T. Jones at NACA published a result that connects any aircraft configuration — no matter how complex — to a single equivalent body of revolution. The theorem states:

> The wave drag of an aircraft configuration equals the wave drag of the body of revolution whose cross-sectional area at each longitudinal station matches the summed cross-sectional area of the real aircraft at that station.

Take any cross-section perpendicular to the aircraft axis at position *x* along the fuselage. Add up the area of every component that slice passes through — fuselage, wing, nacelle, pylon, everything. That total is *S(x)*. Plot *S(x)* from nose to tail and you have the area distribution of the equivalent body.

For a conventional aircraft, that plot has a characteristic shape: it rises from zero at the nose, peaks somewhere in the cabin/wing region, and returns to zero at the tail. The shape of that curve drives the pressure drag associated with pushing the volume of the aircraft through the air.

---

## The Sears-Haack Body: The Ideal Reference

The theoretical optimum for a closed body of a given volume and length is the **Sears-Haack body**, derived by Wolfgang Sears and Wolfgang Haack independently in the 1940s. Its area distribution follows:

```
S(x) = A_max × [4x(1−x)]^(3/2)     x ∈ [0, 1], normalized nose to tail
```

This produces a smoothly biconvex shape — wide in the middle, tapering to points at both ends — that minimizes pressure drag for the enclosed volume. The wave drag of a Sears-Haack body is:

```
D = (9π/2) × q × A_max² / L²
```

Two things are immediately apparent from this expression:

1. **Drag scales with the square of maximum cross-sectional area.** Doubling the fuselage diameter quadruples the pressure drag contribution.
2. **Drag scales inversely with the square of body length.** A longer, thinner body is always aerodynamically cheaper than a shorter, fatter one of the same volume.

The Sears-Haack derivation is technically supersonic (linearized potential flow), but the smooth-area-distribution principle it encodes applies at all speeds. In subsonic flow the mechanism is different — not wave drag but interference drag and adverse pressure gradients — but the same geometric property (smooth, monotonically varying area distribution) minimizes both.

---

## What Goes Wrong When the Distribution Isn't Smooth

For a conventional aircraft, the largest area-distribution problem occurs at the wing-body junction. The wing adds significant cross-sectional area at a fairly narrow band of *x* stations. If the fuselage is still growing or at its maximum diameter at those same stations, the combined equivalent body has a pronounced "hump" — a rapid increase in *S(x)* followed by a rapid decrease after the wing chord ends.

A hump in *S(x)* means a hump in d²S/dx². In linearized theory, pressure drag is proportional to the integral of (d²S/dx²)² — any sharp change in area distribution slope is expensive. In subsonic flow, the rapid area increase creates a local adverse pressure gradient. The boundary layer, already thick on the aft fuselage, is asked to climb a steeper hill. The result is either early separation (large pressure drag from a separated wake) or, if the shape is good enough to avoid full separation, an elevated skin friction coefficient from a thickened turbulent boundary layer in the adverse region.

Hoerner quantifies the penalty for a non-optimized wing-fuselage junction as typically **5–15 drag counts** (ΔCD = 0.0005–0.0015) relative to a configuration with a well-managed area distribution and properly faired junctions. At MAOS cruise, that range represents:

| Interference drag penalty | CD_total | L/D |
|---|---|---|
| 0 (optimized) | 0.0151 | 17.4 |
| 10 counts (moderate) | 0.0161 | 16.3 |
| 15 counts (poor) | 0.0166 | 15.8 |

The difference between optimized and moderate is roughly **6% in range** — for free, without touching the wing or propulsion system.

---

## The Practical Rule: Put the Volume Forward

The actionable consequence of the theory is straightforward. For a conventional tractor aircraft:

**Place the fuselage maximum cross-section forward of the wing leading edge, and arrange the fuselage to be tapering when the wing's area contribution is growing.**

As the equivalent body's *S(x)* sum moves aft through the wing station, the fuselage component is decreasing while the wing component is increasing. The total area function stays flatter — the "hump" is smaller or absent. The result is a smoother d²S/dx² and lower interference drag.

In practice this means:
- Nose section: rapid area growth from zero (acceptable — nose pressure is favorable)
- Maximum fuselage cross-section: reached well forward of the wing
- Through the wing chord extent: fuselage tapering, wing contributing
- Aft of wing: fuselage continuing to taper smoothly to the tail

This is not always achievable. A pressurized aircraft that needs a full-height cabin from the cockpit all the way aft to the rear seats will maintain maximum cross-section through most of the wing station. That is the MAOS constraint, and it is the same constraint that every pressurized single-engine aircraft from the Piper Malibu to the TBM 960 lives with.

---

## The Pylon Wing as a Partial Mitigation

A pylon-mounted wing changes the geometric relationship between wing and fuselage surfaces without changing the equivalent body area distribution. The area slice at each *x* station still adds up to the same total — pylon-mounted or not, the wing contributes its thickness-area to *S(x)*.

What the pylon eliminates is the **junction interference** component: the viscous drag from two surfaces meeting at an angle in an adverse pressure gradient. When the wing root intersects the fuselage skin directly, the corner flow between them experiences flow acceleration, an adverse gradient on the aft side of the junction, and potential local separation. A pylon physically separates the two surfaces. The wing sees clean freestream-influenced flow at its root. The fuselage skin sees no geometric interruption.

| Mechanism | Direct wing attachment | Pylon mounting |
|---|---|---|
| Equivalent body area distribution | Identical | Identical |
| Wing-fuselage corner interference | Present — 5–10 drag counts | Eliminated |
| Pylon-fuselage junction interference | Not applicable | Small — 1–3 drag counts |
| Wing-pylon junction interference | Not applicable | Small — 1–3 drag counts |
| Net interference drag (est.) | 5–10 counts | 2–6 counts |

The pylon does not exempt the design from area progression considerations. It does reduce the junction-specific interference term, and on a large-diameter fuselage like the MAOS pod — where the fuselage-wing area mismatch is large — the relief is meaningful.

---

## Applying This to MAOS

The current MAOS pod is 14 ft long with a maximum cross-section at approximately 30% station (XSec_1, ~4.2 ft from nose) and the same maximum width maintained through 67% station (XSec_2, ~9.4 ft from nose). The wing root is located at approximately 6.4 ft from the nose (45% of pod length) in the current pylon configuration.

The equivalent body area distribution for the current configuration has a persistent plateau from 30% to 67%, with the wing contribution adding on top of maximum-diameter fuselage through the entire wing chord extent. This is the largest available area progression improvement opportunity on the aircraft.

Three levers are available, which can be used independently or together:

**1. Move the wing aft.** If CG balance allows the wing to move to 55–60% station, the forward fuselage peak (XSec_1 at 30%) is clearly upstream and the fuselage is already tapering when the wing adds its area. Even a 10% station shift measurably improves the equivalent body shape.

**2. Taper XSec_2 width.** The rear-cabin cross-section is currently nearly as wide as the front cabin. Reducing XSec_2 from 60" to something closer to 52–54" — which is still more than adequate for rear seat occupants — begins the fuselage taper before the wing station rather than after it.

**3. Root fillet.** Regardless of area progression, a well-designed wing root fillet blends the pylon-fuselage junction to a smooth surface and reduces the local adverse pressure gradient. This is the compensation tool when geometry prevents ideal area placement. On a pylon-mounted wing the fillets are smaller than on a conventional wing-body junction, but they still matter.

The combination of a moderately aft wing position, a gently tapered rear cabin cross-section, and properly designed pylon fillets could realistically recover 6–8 drag counts relative to an unoptimized installation. At MAOS design point, that is approximately 0.8–1.0% improvement in cruise L/D — not transformative, but not trivial either, and obtainable purely through geometry choices already under discussion.

---

## A Note on Quantitative Analysis

The estimates in this article are based on Hoerner empirical data and linearized-theory scaling from Jones and Sears-Haack. They are directionally reliable but not substitutes for analysis on the actual geometry.

The QNAP analysis stack has the tools to go further:

- **CompGeom** in OpenVSP will compute the equivalent body area distribution directly from the vsp3 geometry — this is the most useful near-term check on whether area progression is improving as the geometry evolves.
- **VSPAERO** panel method will capture the induced effects of wing-body proximity but not the viscous corner flow at pylon junctions.
- **OpenFOAM RANS** (available in `maos-openfoam`) is the right tool for quantifying pylon junction interference drag once the configuration stabilizes — that analysis is worth running before finalizing pylon geometry.

The equivalent body plot from CompGeom is the cheapest and most informative first step. It costs nothing and directly shows whether the fuselage-wing area combination is producing the smooth distribution the theory calls for.
