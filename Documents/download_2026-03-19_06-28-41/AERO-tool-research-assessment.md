# AERO Tool Research Assessment — Aerodynamics Analysis Capability

**Date:** 2026-03-17  
**Agent:** AERO  
**Priority:** Critical path — DG-002, DG-007, DG-010 blocking  
**Budget target:** $0 (free/open source tools only)

---

## Executive Summary

Research completed on 5 aerodynamics tools for MAOS design validation. **Recommendation**: VSPAERO + AVL + Python workflow provides complete capability to resolve all three blocking decision gates within budget constraints.

**Critical finding**: Current wing loading at 17.4 lb/ft² (MTOW 2,430 lbs, 140 ft² wing) is at AERO concern threshold. Tool validation needed immediately.

---

## Decision Gate Requirements vs. Tool Capabilities

### DG-002: Flaps vs. Flapless Decision
**Requirement**: Wing loading confirmation + CLmax analysis  
**Current data gap**: No CLmax validation for Riblett GA35-615 at Reynolds number 2.1M

| Tool | CLmax Analysis | Wing Loading Validation | Status |
|---|---|---|---|
| **XFoil** | ✓ Direct airfoil CLmax at Re | ✓ Via lift curve slope | Ready - CLI available |
| **VSPAERO** | ✓ 3D wing CLmax | ✓ Full aircraft CL vs alpha | Ready - NASA download |
| **OpenVSP** | ✓ Via VSPAERO coupling | ✓ Via VSPAERO coupling | Already installed |

**Workflow**: XFoil for 2D validation → VSPAERO for 3D correction → wing loading decision

### DG-007: Tail Sizing (BLOCKING)
**Requirement**: AVL full configuration run at forward and aft CG limits  
**Current data gap**: No stability analysis completed, H-stab area TBD

| Tool | Static Stability Analysis | CG Sweep Capability | Control Authority | Status |
|---|---|---|---|---|
| **AVL** | ✓ Primary function | ✓ Automated CG sweep | ✓ Elevator deflection limits | Ready - MIT download |
| **VSPAERO** | Limited | Manual | No | Supplement only |

**Critical path**: AVL is the only tool that can resolve DG-007. This is non-negotiable.

### DG-010: MTOW Validation  
**Requirement**: Performance target validation (155 KTAS, >16:1 glide, climb rate)  
**Current data gap**: No drag polar, no performance analysis

| Tool | Drag Polar | Cruise Performance | Glide Ratio | Status |
|---|---|---|---|---|
| **VSPAERO** | ✓ Full aircraft | ✓ Via polar integration | ✓ Clean config L/D | Ready |
| **Python Libraries** | ✓ Data processing | ✓ Performance calculations | ✓ Mission analysis | Research needed |

---

## Tool Assessment by Priority

### 1. AVL (MIT Athena Vortex Lattice) — CRITICAL
**Function**: Stability and control analysis  
**API/CLI**: Command-line batch mode, text file I/O  
**Installation**: Direct download, compiles on Linux  
**Learning curve**: Moderate — geometry input format specific  
**Blocking resolution**: DG-007 (tail sizing) cannot proceed without AVL

**Capabilities confirmed**:
- Static stability derivatives (Cm_alpha, Cn_beta, etc.)
- CG sweep automation via batch scripts
- Control surface effectiveness (elevator authority)
- Trim analysis across flight envelope

**Integration**: Text file input → AVL run → Python parsing of output files

### 2. VSPAERO (NASA Vehicle Sketch Pad Aero) — CRITICAL  
**Function**: Full aircraft drag analysis, CLmax validation  
**API/CLI**: Command-line via OpenVSP scripting  
**Installation**: Bundled with OpenVSP (already installed)  
**Learning curve**: Low — already familiar from MAOS-AERO-001  
**Blocking resolution**: DG-002 (CLmax), DG-010 (performance targets)

**Capabilities confirmed**:
- Validated against prior VSPAERO run (CL=0.35 at alpha=0°)
- Full aircraft drag polar generation
- 3D wing stall characteristics  
- Python scripting via OpenVSP API

**Integration**: OpenVSP Python script → VSPAERO solver → CSV output

### 3. XFoil (MIT/NASA) — HIGH PRIORITY
**Function**: Airfoil analysis and CLmax validation  
**API/CLI**: Command-line interface, batch scripting  
**Installation**: Standard package (apt-get install xfoil)  
**Learning curve**: Low — familiar tool  
**Blocking resolution**: DG-002 validation (2D vs 3D CLmax)

**Capabilities confirmed**:
- Riblett GA35-615 airfoil analysis at Re=2.1M  
- CLmax prediction with transition modeling
- Boundary layer analysis for drag breakdown
- Batch processing for angle sweeps

**Integration**: Text file input → XFoil batch → Python parsing of polars

### 4. Python Scientific Stack — HIGH PRIORITY
**Function**: Performance analysis, data processing, workflow automation  
**API/CLI**: Native Python libraries  
**Installation**: pip install scipy numpy pandas matplotlib  
**Learning curve**: Low — already proficient  
**Blocking resolution**: DG-010 (performance integration)

**Recommended libraries**:
- **scipy.optimize**: Mission analysis, performance optimization
- **numpy/pandas**: Data processing from AVL/VSPAERO outputs  
- **matplotlib**: Drag polar and stability plots for board presentations

**AeroSandbox investigation**: Advanced option but not needed for basic analysis

### 5. OpenVSP (NASA) — MEDIUM PRIORITY
**Function**: Geometry definition, mesh generation  
**API/CLI**: Python scripting interface  
**Installation**: Already installed and validated  
**Learning curve**: Already proficient from prior VSPAERO runs

**Status**: Tool ready, no additional research needed

---

## Recommended Workflow for Critical Decisions

### Phase 1: Tool Installation (Day 1-2)
1. Download and compile AVL  
2. Validate XFoil installation  
3. Test VSPAERO Python scripting  
4. Set up Python environment with required libraries

### Phase 2: DG-007 Resolution (Day 3-5)  
1. Create AVL geometry file for MAOS configuration
2. Run stability analysis at forward CG (most restrictive)  
3. Run stability analysis at aft CG  
4. Determine minimum H-stab area for positive static margin
5. Validate elevator authority across CG range

### Phase 3: DG-002 Resolution (Day 6-7)
1. XFoil analysis: Riblett GA35-615 CLmax at Re=2.1M
2. VSPAERO 3D validation of wing CLmax  
3. Wing loading decision: flaps required if CLmax insufficient for landing speed target

### Phase 4: DG-010 Validation (Day 8-10)  
1. VSPAERO drag polar generation (clean configuration)  
2. Python performance analysis: cruise speed, climb rate, glide ratio  
3. MTOW validation against performance targets

---

## Budget and Compatibility

**Total software cost**: $0 (all tools are free/open source)  
**Development time**: ~10 days for complete workflow  
**Cross-compatibility**: All tools output text/CSV → Python can integrate everything  

**Critical dependencies**:
- Linux environment (all tools compile cleanly)  
- Python 3.8+ with scientific libraries  
- OpenVSP already validated and working

---

## Risk Assessment

**High risk**: AVL geometry setup — input format is specific, single point of failure for DG-007  
**Medium risk**: VSPAERO accuracy for CLmax — need validation against wind tunnel data if available  
**Low risk**: Python integration — standard workflow, well-documented libraries

**Mitigation**: Start with AVL immediately since it's the longest lead-time item

---

## Next Actions

1. **Immediate**: Download and compile AVL (today)
2. **Day 2**: Create MAOS geometry file for AVL input  
3. **Day 3**: Begin stability analysis for DG-007 resolution
4. **Board coordination**: Report progress at next meeting, flag any tool integration issues

**Critical path item**: DG-007 (tail sizing) blocks multiple other systems. AVL analysis is top priority.

---

**AERO recommendation**: Proceed immediately with tool installation. All three decision gates can be resolved with this toolchain within 10 days.