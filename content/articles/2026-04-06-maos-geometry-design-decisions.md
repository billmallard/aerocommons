---
title: "MAOS Geometry: First-Pass Design Decisions and Open Questions"
date: 2026-04-06T20:00:00-05:00
description: "Working design notes from the first VSPAERO aerodynamic analysis and geometry build-out: pod wetted area, boom position, wing mounting, and landing gear trade-offs."
tags: ["design-decisions", "aerodynamics", "structures", "geometry", "maos", "vspaero"]
author: "AeroCommons Design Board"
project: "maos"
article_type: "design"
draft: false
---

## Where We Are

The MAOS aircraft now has a first-pass 3D geometry in OpenVSP — pressurized pod fuselage (13 ft × 52" W × 58" H interior), tail boom mounted along the pod crown, cantilever wing, and conventional H/V tail surfaces. A VSPAERO vortex-lattice analysis gives us a first look at the aerodynamic picture. This article captures the decisions made during that process and the open questions that need answers before the geometry locks in.

---

## Aerodynamics: The Wetted Area Problem

The VLM analysis says the lifting surfaces (wing + tails only, bodies excluded per correct VLM methodology) produce a cruise L/D of approximately **16.3** at MTOW = 2600 lb, 155 KTAS, sea level. That sounds encouraging until you add the bodies back in.

Estimated body drag via the Swet method:

| Component | Cf | Form Factor | Swet (est.) | CD contribution |
|---|---|---|---|---|
| Pod | 0.0030 | 1.40 | 180 ft² | 0.00622 |
| Boom | 0.0027 | 1.15 | 47 ft² | 0.00120 |
| Gear (faired fixed) | — | — | — | 0.00500 |
| **Total CD₀ (bodies)** | | | | **0.01242** |

At cruise CL = 0.263, induced drag adds ~0.0037, giving CD_total ≈ 0.0161 and **L/D ≈ 16.3**. That clears the L/D = 14 design target from the propulsion sizing article — but only barely once real-world interference drag at the wing-pod root and boom junctions is accounted for. The pod wetted area is the dominant issue. It's a large, blunt pressure vessel flying broadside through the air.

**The only durable fix is altitude.** At FL200 (20,000 ft), air density is approximately 50% of sea level. For the same true airspeed, dynamic pressure halves and drag force halves. The required cruise power drops in proportion. A turbocharged ICE engine can get there with difficulty; an electric motor doesn't care — efficiency is nearly altitude-independent. This was a deliberate design bet and the numbers support it.

**One watch item:** at altitude, motor controller and battery cooling become harder. There is less convective air available. This needs to be a first-class design concern in the thermal architecture — not an afterthought.

---

## Boom Position: Top Mount vs. Mid Mount

The current geometry has the tail boom running along the pod crown (top). This was a deliberate choice for structural reasons: the wing spar, boom attach, and pod shell all meeting at the same point creates a closed structural box at the most highly loaded junction on the airframe. Structurally this is efficient.

The aerodynamic concern is **T-tail deep stall**. When the horizontal tail sits at the top of a vertical boom, the wing wake can blanket it at high angles of attack. If that happens, the aircraft has no pitch recovery authority and the stall becomes unrecoverable. This is the failure mode that killed the BAC 1-11 prototype in 1963.

For a low-speed, light GA aircraft the risk is lower than for a jet transport — but it's a real design constraint that limits the achievable aft CG range and places requirements on the pitch stability margins that need to be validated before the configuration is finalized.

A **mid-boom position** (boom centerline at Z ≈ 0 to +1.0 ft, between pod centerline and crown) largely mitigates the deep stall exposure while keeping most of the structural box benefit. This is worth a trade study before the geometry is committed.

---

## Wing Mounting: Direct vs. Pylon

The current design has the wing attached directly to the pod at the crown (Z = 2.417 ft, the top of the full cross-section). This is structurally simple and the current VSPAERO model handles it.

A **short pylon above the pod** is worth evaluating seriously. The case for it:

- **Cleaner pod cross-section.** No wing root blend, no large fairing. The pod stays as close to an optimal pressure vessel shape as possible.
- **Lower interference drag.** The wing-body junction is one of the highest-risk locations for interference drag. Lifting it off the pod surface on a pylon reduces that interaction.
- **Structural separation.** Primary wing loads (bending, torsion) don't pass directly through the pod pressure vessel wall. The pylon becomes the load path, and the pod and wing can be designed more independently.
- **Propulsion options.** A pylon creates a natural location for pusher or tractor propulsion above or ahead of the wing without proximity to the pod.

The cost is pylon wetted area and weight. For a short pylon (~1 ft height), those penalties are modest.

**Open question:** Does a pylon change the structural box argument for the boom? If the wing no longer attaches directly to the pod crown, the case for a top-mounted boom weakens. These two decisions may be coupled.

---

## Landing Gear: Half-Retract with Single-Axis Pivot

Fixed gear with wheel fairings burns about 0.0050 CD in the current budget — roughly 30% of the total estimated body drag. That's enough to matter. But full retraction into a pressurized composite pod is mechanically complex: it requires gear wells, doors, actuators, sealing at the pressure boundary, and a structural hard-point that competes directly with the pod's primary load-carrying shell.

The working idea is a **single-axis pivot gear** — the leg rotates on one hinge axis to fold up into a shallow belly fairing, semi-exposed but dramatically lower in drag than fully extended fixed gear. Relevant considerations:

- **One axis of motion** is the right constraint to impose. Each additional degree of freedom in a mechanism multiplies the failure modes and the certification burden.
- **Stroke for hard landings.** A typical light aircraft must absorb a 6–10 ft/s sink rate at MTOW without structural damage. The gear leg itself (composite spring or oleo) needs enough travel to absorb that energy. A short, stiff half-retract leg may not have adequate stroke in the "up" position — this needs to be resolved before the pod belly geometry is finalized.
- **Ground clearance.** The pod belly is the lowest point of the aircraft in cruise. In the gear-up (taxi/takeoff) position, prop clearance and belly clearance in roll need to be checked against the runway geometry.
- A **trailing-link main gear** (as used on the Piper Comanche and several kit aircraft) provides good stroke on a simple pivot and is well understood structurally. This may be the most direct adaptation.

---

## Open Questions (Ranked by Impact)

1. **Boom position** — top vs. mid mount. Deep stall risk quantification is needed before configuration lock.
2. **Cruise altitude assumption** — the L/D = 14 target was set at sea level conditions. If the design point is FL180–220, the drag picture and motor sizing both change. The propulsion article should be revisited with an altitude-corrected analysis.
3. **Pylon vs. direct wing attach** — coupled with boom position decision. May be the right time to run both configurations in VSPAERO.
4. **Gear half-retract stroke** — belly geometry and structural hard-point need to be defined before pod cross-section is finalized.
5. **Motor/controller cooling at altitude** — first-order thermal estimate needed.
6. **Wing-pod interference drag** — current Swet estimate does not include junction drag. A higher-fidelity estimate (panel code or CFD) is warranted once the geometry matures.

---

## Current Geometry Status

The OpenVSP model (`maos_aircraft_v1.vsp3`) is the working reference. The pod aft body taper is under active refinement in the GUI — the scripted approach using symmetric ellipse sections cannot produce the desired asymmetric fairing (flat top, bottom curving up toward the boom). That requires `Edit Curve` cross-sections set interactively in OpenVSP. Once the pod aft fairing is finalized, the geometry parameters will be synced back into the parametric script.

The VSPAERO analysis uses only the lifting surfaces (wing + H-tail + V-tail) in the VLM thin-surface set. Body drag is estimated analytically via the Swet method. This is appropriate for early-stage analysis and the polar results are internally consistent.
