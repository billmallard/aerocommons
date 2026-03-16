

**MAOS**

Mobile Aviation Operating System

**Trailer and Ground Support System**

**Development Plan**

Document: MAOS-TRL-DEV-001

Revision: A (Initial Draft)

Date: March 12, 2026

**Status: DRAFT — Pre-Decisional**

# **Introduction**

## **Purpose**

This document defines the development plan for the MAOS aircraft trailer and ground support system. The trailer serves four integrated functions: road transport of the disassembled aircraft, field deployment and recovery via an integrated crane, mobile workshop for maintenance and repair, and ground power and charging infrastructure for the aircraft systems.

The trailer is not an afterthought to be designed once the aircraft is complete. Key aircraft design decisions, particularly wingspan, wing attachment geometry, and boom configuration, are directly coupled to trailer dimensions, crane loads, and road-legal compliance. This plan recognizes that coupling and structures the development to resolve the interdependencies in the correct order.

## **Scope**

This plan covers the full trailer system from requirements definition through integration testing. It does not cover aircraft design decisions in detail, but identifies the specific aircraft parameters that must be locked before trailer work can proceed, and documents the interfaces between the two systems.

## **Design Philosophy**

The trailer development follows the same principles as the aircraft program:

* Start with a commercial off-the-shelf (COTS) enclosed gooseneck trailer as the base platform. Do not build a trailer from scratch.

* Minimize custom fabrication. Buy the rolling chassis, suspension, brakes, DOT lighting, and weatherproofing. Customize only the parts unique to the aircraft mission.

* Design for single-person operation. Every step of the deployment and recovery sequence must be achievable by one person without external assistance.

* The trailer must be road-legal in Texas without special permits under normal operating conditions. Wing tip overhang with proper flagging is acceptable.

* Weight matters on the trailer too. Every pound of trailer structure is a pound subtracted from useful payload or added to tow vehicle demand.

## **Reference Documents**

* MAOS-GA-001: General arrangement concept rendering

* MAOS-ECS-DEV-001 Rev B: Environmental control system development plan

* Texas Transportation Code, Chapter 621: Vehicle size and weight limits

* TxDMV Size/Weight Limits (txdmv.gov)

* FMVSS 108: Lamps, reflective devices, and associated equipment

# **Aircraft Interface Requirements**

The following aircraft parameters drive trailer design. Parameters marked TBD are open decision gates that must be resolved in Phase 0 before trailer procurement.

| Parameter | Current Value | Impact on Trailer |
| :---- | :---- | :---- |
| **Wingspan** | **TBD (est. 32–38 ft)** | Sets trailer length, wing overhang, crane extension, and rotation clearance envelope |
| **Wing assembly dry weight** | **TBD (est. 250–400 lbs)** | Sizes crane beam, hoist, trolley, and counterweight. Includes structure, two Honda 400cc generators, coolant, TKS, and plumbing. |
| **Wing attachment type** | Single-piece, lifts off as one unit | Crane lifts full wing from spar carry-through. Single lift point near root CG. |
| **Wing root chord** | **TBD (est. 54–72 in)** | Sets wing storage channel width in trailer roof |
| **Pod dimensions** | 52"W × 58"H × 156"L | Pod fits within 8.5 ft trailer width. Floor loading and tie-down locations. |
| **Boom length** | **TBD (est. 9–13 ft)** | Total fuselage length (pod \+ boom) determines floor space and trailer length requirement |
| **Boom attachment** | **TBD: stays attached or detaches** | If attached: trailer stores 22–25 ft fuselage. If detachable: separate stowage required. |
| **Tail configuration** | Conventional (not T-tail) | Tail surfaces at boom end must clear trailer interior or fold for stowage |
| **Propulsion motors** | Rim-drive on boom (Donut Motor or Beyond Motors AXM2) | Motors are on boom, not in wing. Reduces wing weight, simplifies crane loads. |
| **Generators** | 2× Honda 400cc (\~50–60 lbs each) | Mounted in wing. Much lighter than Kawasaki alternative. Generators are protected under roof during transport. |
| **Flight battery capacity** | **TBD** | Determines ground charging power requirement and trailer electrical system sizing |
| **Gross weight** | **TBD (est. 2,600–3,200 lbs)** | Affects trailer GVWR selection and tow vehicle requirement |
| **Flap configuration** | **TBD: flapless under consideration** | Flapless increases required wing area and span by 3–5 ft, directly affecting trailer length and overhang |

**Note:** Red-highlighted values are open decision gates. These must be resolved before the trailer COTS selection in Phase 1A. The flaps decision is especially impactful: going flapless adds approximately 3–5 feet of wingspan, which cascades through every trailer dimension.

# **Road-Legal Envelope**

## **Texas Size Limits (Without Permit)**

| Dimension | Texas Legal Limit | MAOS Implication |
| :---- | :---- | :---- |
| **Width** | 8 ft 6 in (102 in) | Standard 8.5 ft trailer is at limit. Wing chord must fit within this during transport. |
| **Height** | 14 ft | Critical constraint. Trailer floor (\~18 in) \+ interior height (\~90 in) \+ wing thickness (\~12 in) \+ crane beam (\~10 in) \= \~130 in (10 ft 10 in). Margin exists but must be verified. |
| **Combination length** | 65 ft (truck \+ trailer) | Tow vehicle \~20 ft \+ 32 ft trailer \+ 6 ft wing overhang \= 58 ft. Within limit. |
| **Rear overhang** | 4 ft without flag; greater with red flag/light | Wing tips extend past trailer rear. Flag/light required if overhang exceeds 4 ft. Tips are expendable composite structure; generators are protected inboard. |

## **Height Budget Detail**

The 14-foot height limit is the tightest constraint and must be tracked carefully through design:

| Component | Height (in) | Running Total (in) |
| :---- | :---- | :---- |
| Ground to trailer floor (tires \+ suspension \+ frame) | 18–22 | 18–22 |
| Interior height (standard car hauler) | 84–90 | 102–112 |
| Roof structure | 2–3 | 104–115 |
| Wing storage channel (wing thickness at root \+ padding) | 14–18 | 118–133 |
| Crane beam \+ trolley \+ hardware | 8–12 | 126–145 |
| **14 ft limit** | **168** | **23–42 in margin** |

The margin appears comfortable but depends heavily on actual trailer floor height and wing root thickness. A low-deck trailer design or drop-axle configuration would increase margin. This must be verified with the actual COTS trailer selected.

## **Tow Vehicle Requirements**

A gooseneck trailer in the 28–32 ft, 14,000 lb GVWR class requires a 3/4-ton or 1-ton pickup truck (e.g., Ford F-250/350, Ram 2500/3500, Chevrolet 2500/3500). The truck must have a gooseneck hitch rated for the loaded trailer weight and a combined GCWR sufficient for the total combination. Estimated loaded trailer weight: trailer empty (\~4,500 lbs) \+ aircraft (\~2,800 lbs) \+ tools/equipment (\~500 lbs) \= \~7,800 lbs, well within the 14,000 lb GVWR.

# **COTS Trailer Baseline**

## **Recommended Base Platform**

The recommended starting point is a standard enclosed gooseneck car hauler trailer in the 8.5 ft × 28–32 ft size class. This is a mature, high-volume market segment with dozens of manufacturers and well-understood construction practices.

### **Minimum Specifications for COTS Selection**

* Exterior width: 8 ft 6 in (102 in) maximum (at Texas legal limit)

* Box length: 28–32 ft (determined by Phase 0A wingspan decision)

* Interior height: 7 ft 6 in minimum (90 in)

* Frame: Aluminum preferred for weight savings; steel acceptable at lower cost

* Axles: Tandem 7,000 lb torsion axles with electric brakes (14,000 lb GVWR)

* Hitch: Gooseneck coupler (not 5th wheel)

* Rear door: Ramp door (for aircraft roll-on if needed) or barn doors

* Side door: 36 in minimum entry door

* Electrical: Basic 7-way connector; 110V package optional (will be replaced in Phase 3\)

* Roof: Standard construction; will be modified in Phase 2

* Interior: Minimal finish (plywood walls acceptable; will be refinished)

### **Candidate Manufacturers**

Preliminary candidate list (not exhaustive, to be refined during Phase 1A):

* Featherlite (all-aluminum, premium, higher cost)

* CargoPro / Mission (aluminum frame, good value)

* Rock Solid Cargo (steel and aluminum options, wide size range)

* MO Great Dane / Total Trailers (custom builds with workshop options including roof-mounted crane and compressor)

* Millennium Trailers (custom gooseneck builds, motorsport focus)

### **Budget Estimate**

| Item | Low Estimate | High Estimate |
| :---- | :---- | :---- |
| COTS trailer (steel frame, basic) | $15,000 | $22,000 |
| COTS trailer (aluminum frame) | $22,000 | $35,000 |
| Crane system materials | $2,000 | $5,000 |
| Electrical system (battery, inverter, wiring) | $3,000 | $8,000 |
| Air compressor and plumbing | $400 | $800 |
| Workshop fit-out (bench, cabinets, lighting) | $1,500 | $3,000 |
| DOT compliance modifications | $300 | $800 |
| **Total estimated range** | **$22,200** | **$54,600** |

The electrical system cost range is wide because the aircraft charging decision (Phase 3A) determines whether this is a 2 kW tool-power system or a 10–15 kW aircraft-charging system. Resolve early.

# **Development Phases**

The following phases are sequenced to resolve dependencies in the correct order. Phases marked as parallelizable can overlap in time. Decision gates must be resolved before dependent phases proceed.

## **Phase 0: Requirements Lock**

Nothing is purchased or fabricated until Phase 0 is complete. These are decisions, not hardware.

| 0A | Aircraft Geometry Freeze |
| ----- | :---- |
| **Scope** | Lock wingspan, pod+boom total length, wing root chord, wing attach point location (distance aft of pod nose), wing dry weight estimate, V-strut attach geometry, and spar carry-through dimensions. The flaps/flapless decision must be resolved here as it directly affects wingspan. All trailer dimensions derive from these numbers. |
| **Flags** | **DECISION GATE**  **GATE: Wingspan decided**  **GATE: Boom attach/detach decided**  **GATE: Flaps/flapless decided** |
| **Outputs** | Aircraft external dimensions drawing (3-view), wing weight budget with component breakdown, wing attach fitting preliminary design, CG envelope for wing-on and wing-off loading conditions |

| 0B | Road-Legal Envelope Verification |
| ----- | :---- |
| **Scope** | Confirm all Texas size/weight limits against the aircraft geometry from Phase 0A. Determine wing-tip overhang length and required flagging/lighting. Confirm tow vehicle selection and verify GCWR is sufficient. Verify height budget with estimated trailer and crane dimensions. Contact TxDMV if any dimension is ambiguous. |
| **Flags** | **Depends on 0A**  **External: TxDMV** |
| **Outputs** | Legal envelope summary document, tow vehicle selection with GCWR verification, overhang flagging/lighting specification, height budget calculation |

| 0C | Operational Concept of Use (CONOPS) |
| ----- | :---- |
| **Scope** | Write the complete deployment and recovery sequence, step by step, with time estimates. Cover: normal deployment (trailer to flight-ready), normal recovery (taxi to road-ready), degraded-mode operations (rain, wind, darkness, equipment failure), abort procedures (what happens if crane jams mid-lift, if wing binds in storage channel, if wind gust catches wing during rotation). Every step must be achievable by a single operator. This document drives all subsequent design decisions and is the acceptance test for Phase 5\. |
| **Flags** | **Depends on 0A, 0B** |
| **Outputs** | CONOPS document with illustrated step-by-step sequences, time budget per step, single-operator verification analysis, abort/contingency procedures, environmental operating limits |

## **Phase 1: Base Trailer Procurement**

| 1A | COTS Trailer Selection and Order |
| ----- | :---- |
| **Scope** | Using the locked geometry from Phase 0A and legal envelope from Phase 0B, select the optimal COTS enclosed gooseneck trailer. Key decision: aluminum vs steel frame (weight vs cost). Request manufacturer drawings and structural details before ordering. Order with minimal interior finish; the interior will be rebuilt. Consider requesting the trailer without a standard roof if the manufacturer supports this, as the roof will be heavily modified. Typical lead time is 8–16 weeks for a custom gooseneck order. |
| **Flags** | **Depends on 0A, 0B**  **External: Trailer manufacturer** |
| **Outputs** | Purchase order with specifications, manufacturer structural drawings, delivery timeline, inspection checklist for delivery acceptance |

| 1B | Structural Survey and CAD Model |
| ----- | :---- |
| **Scope** | Upon trailer delivery, survey all actual dimensions: frame member sizes, cross-sections, and locations; roof truss spacing and member sizes; axle positions; floor structure; wall framing. Build a complete CAD model of the as-received trailer in FreeCAD (STEP export). Identify structural load paths and determine where roof modifications can be made without compromising the frame. The roof on most enclosed trailers is a stressed-skin panel that contributes to torsional rigidity; cutting it requires compensating structure. |
| **Flags** | **Depends on 1A delivery** |
| **Outputs** | As-built CAD model (FreeCAD/STEP), structural member map with cross-sections, roof modification feasibility analysis including required reinforcement |

## **Phase 2: Crane and Wing Storage System**

This is the most technically challenging phase. The crane system must safely lift, rotate, and stow the wing assembly, and the roof modification must maintain trailer structural integrity while creating a weatherproof wing storage channel.

| 2A | Crane Beam and Trolley Design |
| ----- | :---- |
| **Scope** | Design the longitudinal I-beam (or box beam), vertical support columns tying into the trailer main frame (not just the roof), traveling trolley with hoist mechanism, and the rearward extension beyond the trailer end. The beam must cantilever approximately 5–6 feet past the trailer rear to reach the wing attach fittings when the aircraft is parked nose-to-trailer. Design the swivel/rotation bearing at the hoist point to allow controlled 90-degree wing rotation. Specify electric winch (preferred for single-person operation) or manual come-along. Design the wing cradle/sling that interfaces with the wing spar carry-through or dedicated lift fittings on the wing. Safety factor: 2.0× on wing dry weight for all structural members. Include analysis for dynamic loads during rotation (wind gust on half-span wing acting as a sail). |
| **Flags** | **Depends on 0A, 1B**  **DECISION GATE** |
| **Outputs** | Crane assembly design drawings, beam stress analysis (hand calcs and/or FEA), trolley and hoist specification, swivel bearing specification, wing cradle design with interface to wing fittings, dynamic load analysis for rotation in wind, load test plan |

| 2B | Roof Modification and Wing Storage Channel |
| ----- | :---- |
| **Scope** | Design the roof opening, wing storage rails, and weather protection system. The wing slides into the roof space parallel to the trailer length (chord-wise, leading edge forward) and rests on padded rails. Channel width must accommodate the root chord plus clearance for V-struts (if stowed attached) or just the bare wing (if struts detach first). Provide structural reinforcement to compensate for the roof material removed. Design a weather protection system: options include hinged roof panels that close over the wing, a fitted tarp/cover with tie-downs, or a sliding roof section. The system must be operable by one person. |
| **Flags** | **Depends on 1B, 2A**  **GATE: V-struts on or off during stow?** |
| **Outputs** | Roof modification drawings with reinforcement details, wing rail and cradle design, weather protection system design, structural analysis of modified roof |

| 2C | Fabrication and Load Testing |
| ----- | :---- |
| **Scope** | Build the crane system, execute the roof modification, and install wing storage rails. Conduct load testing with a sandbag dummy wing at 1.5× design load before lifting the real wing. Perform the full deployment and recovery sequence with the dummy load, measuring time per step against the CONOPS targets from Phase 0C. Iterate on any element that binds, jams, interferes, or takes too long. This phase ends when the crane system passes load testing and the dummy-wing deployment sequence meets CONOPS time targets. |
| **Flags** | **Depends on 2A, 2B** |
| **Outputs** | Completed crane and roof installation, load test report with photographs, deployment/recovery time-motion study vs CONOPS targets, punch list of items requiring iteration |

## **Phase 3: Workshop and Support Systems**

Phases 3A through 3C can begin design work in parallel with Phase 2, but installation must wait until Phase 2 roof modifications are complete (to avoid rework). Design work can proceed using the CAD model from Phase 1B.

| 3A | Electrical System |
| ----- | :---- |
| **Scope** | Design the complete trailer electrical system. Shore power inlet: 30A (TT-30, common at campgrounds) or 50A (14-50, common at RV parks). Battery bank: LiFePO4 chemistry for weight savings and deep-cycle tolerance. Inverter/charger: pure sine wave, sized for peak tool loads and aircraft charging if applicable. DC distribution panel with circuit protection. LED interior work lighting (high CRI for maintenance tasks) and exterior ground lighting for night operations. 120V GFCI outlets at workbench and rear door. USB outlets for devices. Decision gate: will the trailer electrical system charge the aircraft flight battery? If yes, the system scales from approximately 3 kW (tools and lights only) to 10–15 kW (aircraft charging), which fundamentally changes battery bank size, wire gauge, shore power requirements, and cost. |
| **Flags** | **Can run in parallel**  **DECISION GATE**  **GATE: Aircraft charging from trailer?** |
| **Outputs** | Single-line electrical diagram, load analysis for all operating modes, component specification list with sources, wire routing plan on CAD model, shore power interface specification |

| 3B | Compressed Air System |
| ----- | :---- |
| **Scope** | Install a small, quiet air compressor permanently mounted with vibration isolation. Primary uses: tire inflation, dust removal, pneumatic rivet gun (if used in assembly). The compressor does not need to sustain continuous air tool operation; modern cordless tools handle most tasks. Recommended: California Air Tools or equivalent ultra-quiet oil-free compressor, 1–2 HP, 4–8 gallon tank. Plumb to quick-disconnect fittings at workbench area and at rear door. Consider supplementing with a CO2 bottle for portable high-volume inflation (tire service away from trailer). |
| **Flags** | **Can run in parallel** |
| **Outputs** | Compressor specification with mounting design, air line routing plan, quick-disconnect locations, vibration isolation detail |

| 3C | Interior Layout and Tool Storage |
| ----- | :---- |
| **Scope** | Design the interior arrangement accounting for the pod+boom sitting on the trailer floor and the wing stowed overhead. Key elements: workbench (folding or fixed, along one side wall), tool cabinets or wall-mounted panels, spare parts storage bins, wing stand fixtures (for working on the wing when it is removed but not yet on the aircraft), consumables storage (TKS fluid, coolant, oil), fire extinguisher (dry chemical, accessible from both interior and exterior), and first aid kit. The interior must allow maintenance access to the aircraft while stowed. The layout must not interfere with the crane operation or the wing insertion path. |
| **Flags** | **Depends on 1B**  **Can run in parallel** |
| **Outputs** | Interior layout drawings on CAD model, workbench design, cabinet and storage design with tool inventory list, maintenance access analysis showing reach to critical aircraft service points |

## **Phase 4: Road Compliance and Safety**

| 4A | DOT Lighting and Safety Compliance |
| ----- | :---- |
| **Scope** | The COTS trailer arrives DOT-compliant, but modifications (crane structure above roofline, wing overhang at rear) change the vehicle profile and may require additional lighting. Verify: rear clearance and stop lights are visible with wing stowed, clearance/marker lights are installed on crane structure if it projects above the original roofline, reflective conspicuity tape is applied to any new structural elements visible from the sides or rear, breakaway brake system remains functional after all modifications. For transport with wing overhang: red flag (minimum 12 in square, daytime) and red light (nighttime) on each wing tip. |
| **Flags** | **Depends on 2C**  **External: DOT inspection** |
| **Outputs** | Lighting modification plan, DOT compliance checklist, reflective tape placement diagram, wing-tip flag/light specification, inspection scheduling |

| 4B | Weight Distribution and Towing Dynamics |
| ----- | :---- |
| **Scope** | Calculate loaded trailer CG and verify: tongue weight is 10–15% of total loaded trailer weight (gooseneck standard), axle loads do not exceed rated capacity, total combination weight is within tow vehicle GCWR. The trailer CG shifts significantly depending on pod position on the floor versus wing position on the roof; produce a loading diagram showing the correct pod placement for each loading condition (wing-on, wing-off, empty). Conduct road test: highway stability at legal speed, braking distances (loaded and unloaded), backing maneuvers through typical airport gate, fuel consumption impact on tow vehicle. |
| **Flags** | **Depends on 2C** |
| **Outputs** | Weight and balance calculation with CG diagram, loading checklist for correct pod placement, tow test report with stability assessment, braking distance measurements |

| 4C | Insurance and Registration |
| ----- | :---- |
| **Scope** | Register the modified trailer with TxDMV. Verify insurance coverage: the trailer itself needs liability coverage, and the aircraft while on the trailer may need separate inland marine coverage. Some aviation insurance policies cover ground transport incidents; verify with your aviation insurer before purchasing separate coverage. Document trailer modifications for the insurance file. |
| **Flags** | **External: Insurance broker**  **External: TxDMV** |
| **Outputs** | Trailer registration, insurance binder with documented coverage scope, modification disclosure to insurer, aircraft-in-transit coverage confirmation |

## **Phase 5: Integration and Validation**

| 5A | Full Integration Test |
| ----- | :---- |
| **Scope** | Load the real aircraft (with wing attached) onto the trailer using the complete deployment and recovery sequence defined in the Phase 0C CONOPS. Time every step. Identify all interference fits, clearance issues, and operational problems. Iterate on crane controls, wing cradle fit, rotation clearance, wing rail alignment, and tie-down system. Goal: one person, under 45 minutes total, from wing-removal through road-ready (or the reverse). Conduct the sequence at least three times to verify repeatability. Test in wind conditions up to the CONOPS environmental limit. |
| **Flags** | **Depends on All prior phases** |
| **Outputs** | Integration test report with photographs and video, final deployment/recovery procedure (revision of CONOPS), measured time per step, operator training checklist, list of remaining discrepancies and resolution plan |

# **Decision Gates Summary**

The following decisions are unresolved and block downstream work. They are listed in priority order. Resolving the first three unlocks Phase 1 (trailer procurement).

| \# | Decision | Options Under Consideration | Blocks | Notes |
| :---- | :---- | :---- | :---- | :---- |
| **1** | **Wingspan** | 32–38 ft range; coupled to wing loading and flap decision | Trailer length, crane extension, overhang | The single most impactful decision for trailer design |
| **2** | **Flaps or flapless** | Flapless simplifies wing, adds 3–5 ft span | Wingspan (Gate 1), trailer length | Flapless preferred for simplicity; span penalty is absorbed by trailer overhang |
| **3** | **Boom attach or detach** | Stays attached (recommended) vs detachable | Trailer floor layout, tail clearance | Attached eliminates a flight-critical joint and a second handling operation |
| **4** | **V-struts during stow** | Wing stows with struts attached vs struts detach first | Wing channel width, crane operation | Struts attached saves time; struts off gives narrower channel |
| **5** | **Aircraft charging from trailer** | Yes (10–15 kW system) vs No (3 kW system) | Electrical system size, cost, weight | Charging capability makes trailer a complete mobile base |
| **6** | **Shore power standard** | 30A TT-30 vs 50A 14-50 | Inlet hardware, wiring gauge | 50A required if aircraft charging; 30A sufficient for tools only |

# **Crane System Concept**

## **Reference Design**

The crane concept is derived from burial vault delivery trucks, which use a longitudinal overhead beam with a traveling hoist that extends past the rear of the vehicle bed. This proven industrial concept is adapted for aircraft wing handling.

## **Operational Sequence**

The following sequence describes wing removal from the aircraft for transport loading. The reverse sequence is used for deployment.

1. Aircraft taxis forward to the rear of the trailer, oriented nose-to-trailer, and is chocked.

2. Crane beam extends rearward from the trailer roof (telescoping or fixed overhang) to position the trolley/hoist above the wing center of gravity (near the root, at the spar carry-through).

3. Hoist lowers the wing cradle/sling. Operator attaches the cradle to the wing lift fittings.

4. Wing attachment bolts are removed, disconnecting the wing from the fuselage. Electrical, fuel, coolant, and TKS quick-disconnects are separated.

5. Hoist lifts the wing clear of the fuselage. At this point, the wing is suspended from the crane in its flight orientation (perpendicular to the trailer).

6. The wing rotates 90 degrees on the swivel bearing, from perpendicular to parallel with the trailer. This rotation is operator-controlled (not free-swinging). Each wing tip sweeps through a half-circle of radius equal to half the wingspan; adequate clearance from the trailer, fuselage, and any obstacles must be maintained.

7. Trolley retracts forward along the beam, sliding the now-parallel wing into the roof storage channel. Wing rests on padded rails.

8. Wing is secured with tie-downs in the storage channel. Weather cover is closed.

9. Pod+boom is rolled or winched onto the trailer floor and secured.

10. Crane beam is retracted or locked in travel position. Wing tip overhang flagged/lit as required.

## **Key Design Parameters**

| Parameter | Estimated Value | Driver |
| :---- | :---- | :---- |
| Crane overhang past trailer rear | 5–6 ft | Distance from trailer end to wing attach point when aircraft is parked nose-to-trailer |
| Lift load (wing dry weight) | 250–400 lbs | Wing structure \+ 2× Honda generators \+ coolant \+ TKS \+ plumbing. Fuel drained before removal. |
| Beam bending moment | 1,250–2,400 ft·lbs | Overhang × lift load. Sizes beam cross-section. |
| Rotation clearance radius | 16–19 ft | Half wingspan. Area must be clear of obstacles during rotation. |
| Hoist travel (beam length) | 30–36 ft | From overhang position to full-forward stow position. Approximately equals trailer box length. |
| Safety factor | 2.0× static, verified by load test at 1.5× | Standard practice for lifting equipment |

# **Preliminary Risk Register**

| \# | Risk | Likelihood | Impact | Mitigation |
| :---- | :---- | :---- | :---- | :---- |
| **R1** | Height exceeds 14 ft with crane and wing stowed | Medium | High | Verify height budget with actual trailer dimensions before purchasing. Select low-deck trailer if needed. Design crane beam to fold flat for transport. |
| **R2** | Wind gust catches wing during 90-degree rotation | Medium | High | Define CONOPS wind limit for crane operations (suggest 15 kt max). Design controlled rotation mechanism (not free-swinging). Include abort procedure: if gust occurs mid-rotation, lower wing to ground on padded cradle. |
| **R3** | Roof modification compromises trailer torsional rigidity | Medium | Medium | Analyze roof contribution to frame stiffness before cutting. Add compensating structure (longitudinal stiffeners, cross-bracing) as part of Phase 2B design. |
| **R4** | Single-person operation takes too long (\>60 min) | Medium | Low | Prioritize electric hoist over manual. Design all connections for quick-disconnect. Practice sequence with dummy wing. Accept that early operations may be slower; speed comes with practice. |
| **R5** | Wingspan decision changes after trailer purchased | Low | High | Do not purchase trailer until Phase 0A is complete. Size trailer for the upper end of the expected wingspan range to provide margin. |
| **R6** | Trailer weight with modifications exceeds tow vehicle capacity | Low | Medium | Track weight budget through all phases. Prefer aluminum trailer and lightweight crane materials. Verify GCWR before and after modifications. |

# **Immediate Next Actions**

The following actions are needed to begin Phase 0:

11. Resolve the wingspan decision. Run the trade study linking wing loading, stall speed, aspect ratio, and trailer length. The interactive trade tool developed in the design sessions provides the parametric framework; the decision requires fixing the gross weight estimate and choosing the acceptable stall speed for the flapless case.

12. Resolve the flaps/flapless decision. This is tightly coupled to wingspan. Recommendation: go flapless. The simplicity benefit is large, the span penalty is modest (3–5 ft), and the trailer overhang concept absorbs the extra length without requiring a longer trailer.

13. Resolve the boom attachment decision. Recommendation: boom stays permanently attached. This eliminates a flight-critical joint, eliminates a second handling operation during deployment, and the length penalty (pod+boom \~23–25 ft) fits easily within a 28–32 ft trailer.

14. Produce the aircraft 3-view drawing with frozen external dimensions. This drawing is the master reference for all trailer work.

15. Write the CONOPS (Phase 0C). This can be drafted in parallel with the geometry decisions, but must be finalized after dimensions are locked.

16. Begin surveying COTS trailer options and requesting quotes. This can happen informally during Phase 0 to develop cost understanding, but the purchase order waits for Phase 0 completion.