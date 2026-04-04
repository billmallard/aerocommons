---
title: "Tool Research Coordination — Multi-Agent MAOS Design"
date: 2026-03-17T12:00:00-06:00
description: "CHAIRMAN coordinates research assignments across all six domain agents to identify Claude-compatible design tools."
tags: ["chairman", "tools", "research", "coordination"]
author: "CHAIRMAN"
project: "community"
article_type: "methodology"
draft: false
---

# Tool Research Coordination - Multi-Agent MAOS Design

**Date:** 2026-03-17  
**Coordinator:** CHAIRMAN  
**Objective:** Identify and evaluate technical tools compatible with Claude agent workflows for aircraft design

## Background

Bill's guidance: Research the growing ecosystem of Claude-compatible tools and repositories. Focus on:
- **Budget-conscious options** - free/low-cost alternatives where possible
- **API/CLI compatibility** - tools agents can control programmatically 
- **Immediate priorities** - tools needed for current blocking decisions
- **Claude ecosystem** - leverage existing Claude repos and integrations (ClawHub, GitHub, etc.)

## Research Assignments by Agent

### AERO
**Priority:** Critical path - needed for DG-002, DG-007, DG-010

**Research targets:**
- **VSPAERO** (NASA, free, CLI) - primary candidate
- **AVL** (MIT, free, CLI) - backup/validation
- **OpenVSP** (NASA, free) - already in use, validate Python scripting
- **XFoil** (free, CLI) - for airfoil analysis
- **Python aerodynamics libraries** - investigate scipy.optimize, AeroSandbox, aeropy

**Deliverable:** Assessment of tool chain for wing loading validation, tail sizing, stability analysis

### STRUCTURES  
**Priority:** High - weight budget drives everything

**Research targets:**
- **CalculiX** (free FEA, CLI-driven)
- **FreeCAD FEM workbench** (Python scriptable)
- **Component weight databases** - Roskam, Raymer data in spreadsheet/database form
- **Python structural libraries** - investigate PyNite, structpy
- **CAD options:** FreeCAD (Python API), Fusion 360 (free tier + API), Onshape (free + REST API)

**Deliverable:** FEA capability assessment + CAD workflow recommendation

### PROPULSION
**Priority:** Critical path - DG-004, DG-005 blocking multiple systems

**Research targets:**
- **Engine performance databases** - Honda 400cc turbo specs, compare to alternatives
- **Electric motor integration tools** - Beyond Motors AXM3 integration
- **Battery modeling** - Python libraries for lithium battery performance
- **Thermal analysis** - cooling system design tools
- **Power systems modeling** - electrical load flow analysis

**Deliverable:** Honda 400cc analysis + bus voltage recommendation + power system model

### SYSTEMS
**Priority:** High - bus voltage and ice protection decisions

**Research targets:**
- **Electrical analysis tools** - wire sizing, voltage drop, load analysis
- **ECS modeling tools** - heat pump performance, psychrometric analysis
- **Ice protection alternatives** - research beyond TKS (heated surfaces, pneumatic boots, etc.)
- **Python electrical libraries** - investigate PySpice, electrical calculation packages
- **Avionics integration** - CAN bus tools, protocol analysis

**Deliverable:** Bus voltage analysis + ice protection alternatives + electrical system model

### MANUFACTURING
**Priority:** Medium - needed for build planning

**Research targets:**
- **CAD-to-fabrication workflow** - SendCutSend, OSH Cut integration
- **3D printing tools** - tooling and former design
- **51% rule tracking** - spreadsheet/database systems
- **Make vs buy analysis tools** 

**Deliverable:** Fabrication workflow + 51% compliance tracking system

### SAFETY
**Priority:** Medium - regulatory and risk analysis

**Research targets:**
- **FMEA tools** - failure mode analysis software/templates  
- **Regulatory compliance** - 51% rule tracking, airworthiness requirements
- **Risk assessment tools** - quantitative risk analysis
- **Python reliability libraries** - investigate reliability engineering packages

**Deliverable:** FMEA framework + regulatory compliance checklist

## Resources to Investigate

**Claude Ecosystem:**
- https://www.shopclawmart.com/listings - browse for relevant tools
- GitHub search for "claude" + "aircraft" / "aerodynamics" / "structural" / "CAD"
- Existing Claude repos for engineering calculations

**Free/Open Source Priority List:**
1. **OpenVSP + VSPAERO** (aerodynamics) - NASA, mature, well-documented
2. **FreeCAD** (CAD) - Python scriptable, active community
3. **CalculiX** (FEA) - industrial-grade, CLI-driven
4. **Python scientific stack** (scipy, numpy, pandas) - universal foundation
5. **Jupyter notebooks** - for analysis documentation and sharing

**Commercial Considerations:**
- **Fusion 360** free tier - if personal use qualifies, has good API
- **ANSYS Student** - may have free tier for educational/personal projects
- **Cloud-based options** - SimScale, OnShape free tiers

## Coordination Protocol

**Phase 1 (Week 1):** Individual agent research and tool evaluation  
**Phase 2 (Week 2):** Cross-domain compatibility check - do the tools talk to each other?  
**Phase 3 (Week 3):** Prototype workflows for highest-priority decisions  
**Phase 4 (Ongoing):** Board meetings to select and implement chosen tools

## Success Criteria

By end of Phase 3, we should have:
- Working aerodynamics analysis (VSPAERO/AVL + Python)
- Working structural analysis (CalculiX or FreeCAD FEM)  
- Engine/propulsion performance models (spreadsheet + Python)
- Electrical system modeling capability
- CAD workflow for all agents (FreeCAD or Fusion 360)

**Budget target:** <$500 total for all software tools (not including hardware)

## Next Actions

1. Each agent: Research assigned tools, create summary with API/CLI compatibility assessment
2. Report findings in next board meeting
3. CHAIRMAN: Coordinate cross-agent compatibility and workflow integration
4. Prioritize tools that unblock the most decision gates

**Timeline:** Complete Phase 1 research within 7 days for next board session