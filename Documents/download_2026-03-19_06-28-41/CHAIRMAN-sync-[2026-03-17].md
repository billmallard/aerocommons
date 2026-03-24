# CHAIRMAN Sync Item - Design State Discrepancies

**Date:** 2026-03-17  
**Type:** Information sync and validation  
**Priority:** High - affects multiple decision gates

## Issue

Discrepancies identified between current design state document and latest project information from GitHub repo and builder discussions:

### Corrected Items
1. **Engine selection**: Updated from Kawasaki I4/I6 to Honda 400cc turbocharged motorcycle engines as primary candidate
2. **Propulsion architecture**: Clarified as series hybrid with twin generators feeding common HV bus + battery buffer
3. **Motor specs**: Beyond Motors AXM3 - 27kg each, 220kW peak
4. **Ice protection**: TKS effectiveness under review - may not be optimal choice

### Still Needs Agent Input
- **Bus voltage decision (DG-004)**: Critical blocking item for PROPULSION, SYSTEMS, and ECS
- **Generator engine final selection**: Honda 400cc turbo vs alternatives
- **Ice protection alternatives**: If not TKS, what options do we evaluate?

## Recommendation

Schedule board meeting to:
1. Have each agent confirm current design state accuracy for their domain
2. Address bus voltage decision - this blocks multiple systems
3. Get PROPULSION assessment of Honda 400cc engines vs alternatives
4. Get SYSTEMS input on ice protection options

## Next Actions

- PROPULSION: Analyze Honda 400cc turbo performance, weight, integration
- SYSTEMS: Evaluate ice protection alternatives to TKS
- ALL AGENTS: Review design state document for accuracy in their domains
- CHAIRMAN: Schedule board meeting once agents have filed positions