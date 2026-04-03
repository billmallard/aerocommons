# MVS (MAOS Vision System) – Phase 1: Component List & Cost Summary
**Date:** 2026-04-03  
**Author:** CHAIRMAN  
**Project:** MAOS Vision System – side‑window replacement by camera/display  
**Phase:** 1 – Executive Summary & Shopping List  
**Next Phase:** Technical Architecture & Integration Details

---

## Executive Summary

The **MAOS Vision System (MVS)** replaces conventional side windows with a hybrid camera/display approach:
- **Windshield retained** for forward direct‑view
- **Three (3) or four (4) HD‑SDI cameras** mounted externally (left, right, aft, optionally forward)
- **Two (2) rugged sunlight‑readable displays** inside the cockpit, fed by a quad multiplexer
- **No‑latency live view** via direct loop‑through or minimal‑delay processing
- **Budget target:** $5,000 (excluding displays, which may exceed this cap)

**Why this approach:**
1. **Structural benefit:** Eliminates side‑window cutouts, simplifying pressurization and improving pressure‑vessel integrity
2. **Weight neutral/saving:** Cameras + wiring ≈ weight of traditional window frames + glass
3. **Operational flexibility:** Can switch between individual camera views, quad‑split, or picture‑in‑picture
4. **First‑of‑its‑kind for EAB:** Demonstrates a path toward fully synthetic vision cockpits

**Key constraints:**
- **Budget:** $5,000 for cameras, multiplexer, wiring, power (displays separate)
- **Redundancy:** Minimum 3 cameras (left, right, aft); forward camera still recommended
- **Timeline:** Months (component spec, purchase, wiring harness fabrication, software if needed)
- **Regulatory:** EAB – no FAA certification required, but must be safe and reliable as primary vision system

This Phase 1 document lists the recommended components, approximate costs, and a high‑level architecture. Phase 2 will detail integration, failure modes, testing, and full project timeline.

---

## Component List & Estimated Costs

| Component | Model / Description | Qty | Unit Price | Line Total | Vendor / Source | Notes |
|-----------|---------------------|-----|------------|------------|-----------------|-------|
| **HD‑SDI Cameras** | BW‑CAM‑HDNANO (or equivalent) | 4 | $450 | $1,800 | Datatoyz / Badwolf Tech | 1080p, IP67, aviation‑rated bullet cam, 19×56 mm, wide‑angle lens |
| **Quad HDMI Multiplexer** | OREI HD‑401MR (or gofanco QuadView) | 1 | $300 | $300 | OREI / Amazon | 4× HDMI in, 1× HDMI out, 5 display modes, 1080p60, low latency (~32 ms) |
| **HD‑SDI to HDMI Converters** | Blackmagic Design Micro Converter SDI to HDMI | 4 | $80 | $320 | B&H / Amazon | Converts camera HD‑SDI to HDMI for multiplexer input |
| **Power Supply (28 V → 12 V)** | Mean Well SD‑100C‑12 (100 W, 12 V) | 2 | $40 | $80 | Mouser / Digi‑Key | Aircraft 28 VDC → 12 VDC for cameras & multiplexer |
| **Wiring & Connectors** | MIL‑DTL‑38999 series III (or equivalent) | 1 kit | $250 | $250 | Mouser / Aircraft Spruce | Connectors, backshells, pins, wire (shielded, 22 AWG) |
| **Mounting Hardware** | Aluminum brackets, vibration isolators | 1 kit | $150 | $150 | McMaster‑Carr | Custom camera mounts, display panel brackets |
| **Cabling (HD‑SDI)** | Belden 1694A (or equivalent), 25 ft each | 4 | $50 | $200 | Belden distributor | Low‑loss 75 Ω coax for HD‑SDI runs |
| **Cabling (HDMI)** | High‑flex HDMI 2.0, 10 ft | 2 | $30 | $60 | Amazon | From multiplexer to displays |
| **Fuses & Circuit Protection** | Automotive blade fuses, holders | 1 kit | $40 | $40 | Auto parts store | Over‑current protection per camera & display feed |
| **Spares / Contingency** | Extra connectors, cables, misc. | 1 | $300 | $300 | — | 10 % buffer for unforeseen parts / mistakes |
| | | | **Subtotal** | **$3,500** | | **Under $5K budget** |
| **Displays (Not in $5K budget)** | GK‑FA1019 (10.1″, 1500 nits, IP65) | 2 | $600 | $1,200 | Geekland / industrial suppliers | Sunlight‑readable, 9‑36 V DC, capacitive touch, HDMI |
| | | | **Total with Displays** | **$4,700** | | Entire system under $5K if displays included |

**Budget Status:** **$3,500** for core components (cameras, multiplexer, wiring, power) – **$1,500 under** the $5,000 target.  
**Total with Displays:** **$4,700** – still under $5,000 if displays are counted.

---

## High‑Level Architecture

```
External Cameras (4) → HD‑SDI (75 Ω coax) → SDI‑to‑HDMI Converters (4) → HDMI cables → Quad Multiplexer → HDMI output → Displays (2)
                                                     ↓
                                              28 V Aircraft Bus → 12 V DC Power Supplies
```

**Camera placement:**
1. **Left camera** – mounted on left fuselage, forward of wing, looking aft/sideways
2. **Right camera** – mirror of left
3. **Aft camera** – mounted on tail boom or vertical stabilizer, looking forward/down for ground maneuvering
4. **Forward camera** – optional, mounted on nose or windshield frame, provides redundancy to direct windshield view

**Display placement:**
- **Primary display** – pilot’s side, positioned where a traditional side window would be
- **Secondary display** – copilot’s side, same position
- Both displays can show:
  - **Quad‑split** (all four cameras)
  - **Single camera** full‑screen (selectable)
  - **Picture‑in‑picture** (one large, one small)

**Power:**
- Cameras: 12 VDC (typical)
- Multiplexer: 5 VDC via adapter, fed from 12 V supply
- Displays: 9‑36 VDC direct from aircraft 28 V bus (or via DC‑DC converter)

---

## Key Technical Risks & Mitigations (Phase 1 View)

| Risk | Mitigation |
|------|------------|
| **Latency** (delay between real world and display) | Use direct loop‑through mode on multiplexer; avoid frame buffers; target <50 ms end‑to‑end |
| **Vibration / EMI** (consumer parts in aircraft environment) | Select industrial‑grade components; use vibration‑isolating mounts; shield all cables |
| **Single‑point failure** (multiplexer dies, lose all cameras) | Design for bypass: ability to connect one camera directly to one display if multiplexer fails |
| **Display failure** (one display goes dark) | Second display remains; can switch views between displays |
| **Camera failure** (one camera dies) | Four‑camera system provides redundancy; remaining three still cover critical arcs |

---

## Next Steps (Phased Approach)

**Phase 1 (Complete)** – Component list & cost summary (this document)  
**Phase 2** – Detailed technical architecture, wiring diagrams, mounting drawings, failure‑mode analysis  
**Phase 3** – Integration plan, software/firmware requirements (if any), testing/validation procedure  
**Phase 4** – Procurement, build, ground testing, flight testing  

**Immediate action items:**
1. **Review this component list** – adjust models/quantities as needed
2. **Begin sourcing quotes** for cameras, multiplexer, displays
3. **Sketch mounting locations** on MAOS pod & boom
4. **Draft Phase 2** – technical architecture (wiring, power, mechanical integration)

---

## Article‑Ready Excerpt

*“Building a camera‑only cockpit for under $5,000 is possible today with off‑the‑shelf industrial components. The MAOS Vision System (MVS) uses four HD‑SDI bullet cameras, a quad HDMI multiplexer, and sunlight‑readable displays to replace side windows entirely—improving structural integrity while providing redundant, selectable views. Total hardware cost: $3,500 for the core system, $4,700 including displays. This Phase 1 shopping list shows exactly what to buy and where to get it.”*

---

**End of Phase 1**  
*Prepared by CHAIRMAN, MAOS Design Board*  
*Next: Phase 2 – Technical Architecture & Integration Details*