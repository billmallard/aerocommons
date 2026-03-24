# Board Meeting 001 - MAOS Design Review

**Date:** 2026-03-17  
**Meeting Type:** Emergency - Critical Path Blocking  
**Chairman:** CHAIRMAN  
**Status:** READY TO CONVENE

---

## AGENDA ITEMS

### 1. ENGINE SELECTION CONFLICT (Critical Path - DG-005)

**Conflict:** PROPULSION vs STRUCTURES on engine choice

**PROPULSION Position:** 
- Recommends Kawasaki I4 Turbo (290-310 lbs each, 580-620 lbs total)
- Honda 400cc engines fail power requirements by 45 kW in single-generator-failed condition
- Analysis shows Honda cannot meet mission requirements

**STRUCTURES Position:**
- Formal objection to Kawasaki weight (500 lb penalty vs budget)
- Current empty weight budget: 1,230 lbs → would become 1,690-1,730 lbs  
- Useful load: 1,200 lbs → would become 470-500 lbs (mission failure)
- Demands power requirement calculations and weight offset plan

**Blocking:** DG-005 engine selection, weight budget completion, MTOW definition

---

### 2. BUS VOLTAGE DECISION (Critical Path - DG-004)

**PROPULSION Recommendation:** 270V DC bus
- Optimal for AXM3 motor controller efficiency
- Reduces wiring weight  
- Compatible with ECS heat pump requirements
- Industry standard for this power class

**Blocking:** SYSTEMS electrical design, ECS condenser specification, motor controller procurement

---

### 3. TOOL RESEARCH COORDINATION RESULTS

**AERO Assessment:** Complete tool chain identified (AVL, VSPAERO, Python)
- Can resolve DG-002 (flaps), DG-007 (tail sizing), DG-010 (MTOW) within 10 days
- AVL setup is critical path for tail sizing

**Status:** Other agents' tool assessments pending

---

### 4. DESIGN STATE SYNC ISSUES

**Issue:** Multiple discrepancies between design state document and current project status
- Engine selection candidates updated
- TKS ice protection under review
- Need agent validation of all domain information

---

## DECISION GATES AFFECTED

| Decision Gate | Description | Status | Blocking |
|---|---|---|---|
| DG-004 | Bus voltage | OPEN - has recommendation | SYSTEMS, ECS, motor controllers |
| DG-005 | Engine selection | OPEN - conflicting positions | Weight budget, MTOW, mission viability |
| DG-002 | Flaps vs flapless | OPEN - tooled for resolution | Wing planform |
| DG-007 | Tail sizing | OPEN - tooled for resolution | Stability, boom length |  
| DG-010 | MTOW target | OPEN - depends on weight budget | Everything |

---

## ROUND STRUCTURE

### Round A - Opening Positions
1. AERO: Wing loading position at current 17.4 lb/ft², tool capabilities
2. STRUCTURES: Weight budget constraint, engine weight objection  
3. PROPULSION: Power requirement justification, Kawasaki recommendation
4. SYSTEMS: Bus voltage position, electrical integration requirements
5. MANUFACTURING: Tool selection, fabrication impact
6. SAFETY: Engine selection safety implications, regulatory concerns

### Round B - Rebuttals
- **Primary conflict:** PROPULSION power analysis vs STRUCTURES weight constraint
- **PROPULSION must answer:** Specific kW requirement calculation, flight envelope with Honda
- **STRUCTURES must answer:** What weight offsets are possible, minimum useful load acceptable
- **Secondary issues:** Other agents address tool selection and bus voltage

### Round C - Final Positions  
Each agent: "I agree with [position]" or "I object because [specific reason]"

---

## MEETING OUTCOME REQUIREMENTS

**Must close at least 2 decision gates or defer with specific resolution criteria**

**Priority closures:**
1. **DG-004 (Bus voltage)** - PROPULSION recommendation appears uncontested
2. **DG-005 (Engine selection)** - Requires weight/power trade analysis or Bill's input on mission change

**If DG-005 cannot close:** Define specific analysis tasks and deadlines for resolution

---

## NOTIFICATION

**@Bill:** Board meeting ready to convene. Critical path blocking items require resolution:

1. **Engine selection crisis:** Kawasaki engines provide required power but add 500 lbs, killing useful load. Honda engines save weight but may be underpowered.

2. **Bus voltage ready to close:** 270V DC recommended, no apparent conflicts.

**Meeting Duration:** Estimated 60-90 minutes  
**Outcome:** Close 2 decision gates or escalate to builder for mission trade decisions

Ready to convene on your schedule.