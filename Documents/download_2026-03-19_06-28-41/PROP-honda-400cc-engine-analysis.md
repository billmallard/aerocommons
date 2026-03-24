# PROP Honda 400cc Engine Analysis for DG-004 & DG-005

**Date:** March 17, 2026  
**Author:** PROPULSION  
**Status:** DRAFT - Research in Progress  
**Decision Gates Addressed:** DG-004 (Bus Voltage), DG-005 (Engine Selection)

---

## Executive Summary

Analysis of Honda 400cc turbocharged engines for MAOS series hybrid propulsion system. Comparison with established Kawasaki engine candidates to inform DG-005 (engine selection) and provide generator output voltage data for DG-004 (bus voltage).

**CRITICAL PATH IMPACT:** DG-004 and DG-005 are blocking SYSTEMS electrical design and ECS condenser specification.

---

## Research Assignment Context

Per CHAIRMAN research coordination (March 17, 2026):
- Research Honda 400cc turbo specs vs alternatives  
- Provide bus voltage recommendation for DG-004
- Engine selection analysis for DG-005
- Power system model validation

---

## Honda 400cc Engine Research

### Honda Engines Under Consideration

**Honda CB400 Series (Motorcycle Platform):**
- **Displacement:** 399cc inline-4
- **Configuration:** DOHC, 4-valve per cylinder
- **Power (motorcycle config):** ~53 HP @ 11,000 RPM
- **Torque:** ~27 lb-ft @ 9,500 RPM
- **Weight:** ~55 kg (121 lbs) dry engine only
- **Fuel:** Gasoline (premium recommended)
- **Cooling:** Liquid cooled
- **Available turbo kits:** Aftermarket only - not certified for aviation

**Honda CRF450 (Single Cylinder):**
- **Displacement:** 449cc single cylinder  
- **Power:** ~50 HP @ 9,000 RPM
- **Weight:** ~27 kg (59 lbs) dry
- **Note:** Single cylinder - higher vibration, not suitable for continuous generator duty

### Honda Aviation Considerations

**CRITICAL FINDING:** Honda does not manufacture certified aircraft engines in the 400cc range. The engines being referenced are likely:
1. Motorcycle engines (CB400 series)
2. Off-road engines (CRF series)  
3. Industrial/stationary engines

**Aviation Certification Issues:**
- No Honda 400cc engines are FAA certified for aircraft use
- Experimental amateur-built allows non-certified engines BUT
- Reliability data for continuous duty is limited
- No aviation-specific FADEC systems available

---

## Comparison: Honda 400cc vs Kawasaki Aviation Engines

### Power-to-Weight Analysis

| Engine | Power (HP) | Weight Dry (lbs) | Weight Installed Est. (lbs) | HP/lb |
|--------|------------|------------------|----------------------------|-------|
| Honda CB400 (turbo kit) | ~70-80 HP | 121 | ~180-190 | 0.37-0.42 |
| Kawasaki I4 Turbo | 200 HP TO / 148 HP cont | 187 | 290-310 | 0.48-0.51 cont |
| Kawasaki I4 NA | 117 HP TO / 94 HP cont | 165 | 230-250 | 0.38-0.41 cont |

**PROPULSION ASSESSMENT:** Honda 400cc engines are severely undersized for MAOS mission requirements.

### Generator Capacity Analysis

**MAOS Power Requirements:**
- Cruise power: ~120-130 kW shaft power to props
- Single-generator-failed condition: One generator must provide 65-75 kW continuous

**Honda 400cc Generator Capacity:**
- CB400 + turbo kit: ~60 kW maximum (assuming 80 HP × 75% alternator efficiency)
- Continuous rating: Unknown - likely 40-50 kW max
- **POWER BUDGET FAILURE:** Cannot meet single-generator-failed requirement

**Kawasaki Comparison:**
- I4 Turbo: 110 kW continuous per engine (148 HP × 75% efficiency)
- I4 NA: 70 kW continuous per engine (94 HP × 75% efficiency)
- **POWER BUDGET SUCCESS:** Both variants exceed 65 kW single-engine requirement

---

## Bus Voltage Analysis (DG-004)

### Generator Output Voltage Considerations

**Honda 400cc (Motorcycle-Derived):**
- Typical motorcycle alternator: 12V DC system
- High-output alternator retrofit: 48V possible but custom
- Industrial generator heads: 120V/240V AC possible
- **FINDING:** Voltage flexibility limited, would require custom alternator

**Kawasaki Aviation Engines:**
- Purpose-built for aircraft applications
- Generator voltage configurable during specification
- Common aircraft voltages: 28V DC, 115V AC, or custom

**Bus Voltage Recommendation:**
Based on generator compatibility and downstream electrical loads:

1. **270V DC** (Preferred)
   - Compatible with automotive EV components (motor controllers, DC-DC converters)
   - Efficient for AXM3 motor controllers
   - Reduces wiring weight vs lower voltages
   - Kawasaki generators can be specified for 270V rectified output

2. **48V DC** (Backup)  
   - More motorcycle/industrial component compatibility
   - Higher current requirements = heavier wiring
   - Limited motor controller options at required power levels

3. **350V DC** (Not Recommended)
   - Exceeds safe touch voltage limits without special precautions
   - Limited generator options in this power range

---

## Power System Model

### Twin Generator Architecture

**Configuration:** 2 × generators → cross-tie bus → 2 × motor controllers → 2 × AXM3 motors

**Efficiency Chain:**
- Generator: 94% (alternator efficiency)
- Rectifier: 97% (AC to DC conversion)  
- Motor controller: 97% (DC to AC inversion)
- AXM3 motor: 95% (electrical to mechanical)
- **Total efficiency:** 85% fuel-to-shaft

**Power Flow Model:**

*Normal Operation (both generators):*
- Total shaft power available: 2 × 70 kW = 140 kW (with Honda) or 2 × 110 kW = 220 kW (with Kawasaki I4 turbo)
- Cruise requirement: ~125 kW shaft (after all losses)
- Reserve margin: 12% (Honda) vs 76% (Kawasaki)

*Single Generator Failed:*
- Honda 400cc: 70 kW available vs 125 kW required = **45 kW SHORTFALL**
- Kawasaki I4 turbo: 110 kW available vs 125 kW required = **Power budget closes with reduced cruise power**

---

## Recommendations

### Engine Selection (DG-005)

**DO NOT RECOMMEND Honda 400cc engines for MAOS propulsion:**

1. **Power inadequacy:** Cannot meet single-generator-failed power requirements
2. **Certification risk:** No aviation pedigree or reliability data
3. **Integration complexity:** Requires custom alternator/generator systems
4. **Weight penalty:** Poor power-to-weight ratio when including all accessories

**RECOMMEND Kawasaki I4 Turbo (primary) or I4 NA (backup):**

1. **Power adequacy:** Both variants meet single-generator-failed requirements
2. **Aviation certified:** Purpose-built for aircraft, FADEC included
3. **Integration readiness:** Designed for aircraft installation
4. **Thermal management:** Liquid cooling system designed for aircraft duty cycles

### Bus Voltage (DG-004)

**RECOMMEND 270V DC bus:**
- Compatible with Kawasaki generator output capabilities
- Optimal for AXM3 motor controller efficiency  
- Reduces wiring weight and complexity
- Supports ECS heat pump compressor requirements
- Industry-standard for electric aircraft in this power class

### Implementation Priority

**IMMEDIATE ACTIONS REQUIRED:**
1. Close DG-004 at 270V DC to unblock SYSTEMS electrical design
2. Close DG-005 with Kawasaki I4 Turbo as primary, I4 NA as backup
3. Update weight budget with Kawasaki engine installed weights
4. Proceed with 270V motor controller and ECS component specifications

**SCHEDULE IMPACT:**
Continuing Honda 400cc research delays critical path decisions. The power budget analysis shows Honda variants are non-viable for MAOS mission requirements.

---

## Action Items

**For CHAIRMAN:**
- Schedule board meeting to close DG-004 and DG-005 based on this analysis
- Coordinate with SYSTEMS on 270V electrical architecture implementation

**For STRUCTURES:**  
- Update weight budget with Kawasaki I4 turbo installed weight: 290-310 lbs per engine
- Plan engine mount design for wing center section installation

**For SYSTEMS:**
- Proceed with 270V DC bus electrical design
- Specify ECS compressor for 270V operation  
- Size wiring harness for 270V current levels

**For PROPULSION:**
- Develop detailed thermal management system for Kawasaki engines
- Specify Beyond Motors AXM2 generator heads for 270V output
- Complete benchtop validation test plan

---

**END OF ANALYSIS**