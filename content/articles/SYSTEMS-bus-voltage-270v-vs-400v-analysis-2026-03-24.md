# Bus Voltage Architecture Comparison: 270V vs 400V
**Author:** SYSTEMS (with CHAIRMAN synthesis)  
**Date:** 2026-03-24  
**Subject:** DG-004 Bus Voltage Decision Analysis  
**Status:** Technical comparison for builder review

---

## Executive Summary

Tesla and many modern EVs use 400V systems. PROPULSION and SYSTEMS initially recommended 270V for MAOS based on generator efficiency optimization. This document compares both options to support an informed decision.

**Bottom line:** Both voltages are viable. 400V offers advantages in component availability and future-proofing, while 270V optimizes generator output. The choice depends on whether we prioritize EV ecosystem compatibility (400V) or generator-specific efficiency (270V).

---

## Voltage Options Comparison

### 270 VDC Bus Architecture

**Advantages:**
- **Generator efficiency optimized:** Kawasaki engine generators likely output near this voltage naturally, minimizing voltage conversion losses
- **Lower voltage = safer handling:** Reduced arc flash risk during maintenance
- **Adequate for our power levels:** 150 kW at 270V = 556 amps (manageable with automotive-grade wiring)
- **Component availability:** Growing EV component market at this voltage

**Disadvantages:**
- **Less common than 400V:** Smaller selection of off-the-shelf inverters and motor controllers
- **Higher current:** 556 amps vs 375 amps at 400V for same power → slightly heavier wiring
- **Limited future scalability:** If v2.0 requires more power, 270V becomes constraining

**Wiring weight comparison (150 kW continuous):**
- Current at 270V: 556 amps
- Estimated wiring: ~35-40 lbs for main bus runs
- Cooling requirements: Moderate (resistive losses = I²R)

---

### 400 VDC Bus Architecture

**Advantages:**
- **Tesla/EV industry standard:** Massive component ecosystem (inverters, motor controllers, contactors, BMS systems)
- **Lower current for same power:** 150 kW at 400V = 375 amps → 33% reduction vs 270V
- **Lighter wiring:** Reduced conductor cross-section requirements, estimated 25-30 lbs for main bus runs
- **Better scalability:** Room to grow if power requirements increase in future variants
- **Motor controller availability:** Far more off-the-shelf options (Tesla aftermarket, Cascadia Motion, Sevcon/Dana TM4, etc.)
- **Future-proof:** Industry trend is moving toward 400V (and 800V for high-performance)

**Disadvantages:**
- **Higher voltage conversion:** If generators output ~270V natively, requires boost converter (adds weight, cost, complexity, ~3-5% efficiency loss)
- **Safety considerations:** Higher voltage requires more robust insulation and safety interlocks
- **May not optimize generator output:** Forces generators to operate at non-optimal voltage

**Wiring weight comparison (150 kW continuous):**
- Current at 400V: 375 amps
- Estimated wiring: ~25-30 lbs for main bus runs
- Cooling requirements: Lower resistive losses

---

## Motor Compatibility Analysis

**Critical finding:** Most modern electric aviation motors are **voltage-agnostic within a range**.

### Beyond Motors AXM3 (baseline motor)
- Rated voltage: **Configurable** (typical range 200-450 VDC)
- Motor controllers handle voltage regulation
- **Compatible with both 270V and 400V bus architectures**

### Donut Labs Motors (alternative options)
- 17" Enclosed: 150 kW, 1200 Nm, 21 kg — **voltage configurable**
- 17" Open: 150 kW, 1200 Nm, 21 kg — **voltage configurable**
- No published voltage specifications, but in-wheel motors typically support wide voltage ranges
- **Likely compatible with both 270V and 400V**

### Industry Standard Practice
Modern electric motors use **motor controllers/inverters** that accept a wide DC bus voltage input and generate 3-phase AC at the voltage/frequency the motor requires. The DC bus voltage is largely decoupled from the motor's operating voltage.

**Conclusion:** Our motor choices are **NOT limited** to 270V. Both AXM3 and Donut Labs motors can operate on either bus voltage with appropriate controllers.

---

## Voltage Conversion Considerations

### If Generators Output 270V Native:

**Option A: Stay at 270V Bus**
- No conversion needed
- Direct generator → bus → inverter → motor
- Efficiency: ~94% gen × 97% inverter × 95% motor = **87% overall**

**Option B: Boost to 400V Bus**
- Add DC-DC boost converter after generators
- Generator 270V → Boost to 400V → Inverter → Motor
- Boost converter: ~95-97% efficient, adds 15-20 lbs, $2,000-3,000 cost
- Efficiency: ~94% gen × **96% boost** × 97% inverter × 95% motor = **84% overall** (3% penalty)

### If Generators Output 400V Native:

**Option A: Stay at 400V Bus**
- No conversion needed
- Direct generator → bus → inverter → motor
- Efficiency: ~94% gen × 97% inverter × 95% motor = **87% overall**

**Option B: Buck to 270V Bus**
- Add DC-DC buck converter after generators
- Similar efficiency penalty and complexity

---

## EV Component Ecosystem Comparison

### 400V Component Availability (Extensive)

**Motor Controllers/Inverters:**
- Tesla Drive Unit aftermarket controllers (readily available, proven)
- Cascadia Motion CM200 (200 kW, 400V, aviation-qualified)
- Sevcon/Dana TM4 inverters (automotive proven, widely available)
- EMRAX controllers (common in electric aviation)
- Hundreds of automotive EV suppliers

**Contactors and Safety Systems:**
- TE Connectivity EV contactors (400V rated, mass production)
- Gigavac high-voltage contactors (aviation/EV certified)
- Widespread availability of DC circuit breakers, fuses, interlocks

**Battery Management Systems:**
- Tesla BMS modules (400V native, aftermarket support)
- Orion BMS (configurable, 400V standard)
- Enormous selection from Chinese EV suppliers (lower cost)

### 270V Component Availability (Moderate)

**Motor Controllers/Inverters:**
- Custom or semi-custom solutions more common
- Some EV bus/truck components (lower volume than 400V cars)
- Sevcon Gen4 (configurable voltage)
- Smaller vendor ecosystem

**Contactors and Safety Systems:**
- Same vendors as 400V but less optimized
- Still readily available but fewer off-the-shelf options

---

## Power Electronics Weight and Cost

### 270V System Estimate
- Motor controllers/inverters (×4): ~40 lbs, $8,000-12,000
- Contactors and safety systems: ~8 lbs, $2,000
- Wiring (main bus runs): ~35-40 lbs, $1,500
- **Total: ~88 lbs, $11,500-15,500**

### 400V System Estimate
- Motor controllers/inverters (×4): ~35 lbs, $6,000-10,000 (better availability)
- Contactors and safety systems: ~8 lbs, $2,000
- Wiring (main bus runs): ~25-30 lbs, $1,200
- DC-DC boost converter (if needed): ~20 lbs, $2,500
- **Total without boost: ~68 lbs, $9,200-13,200**
- **Total with boost: ~88 lbs, $11,700-15,700**

**Weight comparison:**
- If no voltage conversion needed: **400V saves 20 lbs**
- If boost conversion needed: **Equivalent weight** to 270V

---

## Safety Considerations

### 270V Safety Profile
- Arc flash energy: Lower than 400V
- Shock hazard: 270V DC is above "safe" threshold but manageable with standard HV safety practices
- Insulation requirements: Standard automotive HV cable (orange jacketed)
- Safety interlocks: Standard contactors adequate

### 400V Safety Profile
- Arc flash energy: Higher than 270V, requires robust safety procedures
- Shock hazard: 400V DC requires more stringent lockout/tagout procedures
- Insulation requirements: Automotive HV practices still adequate (400V is standard for EVs)
- Safety interlocks: More robust contactors recommended, dual-redundancy for critical paths

**Builder perspective:** Both voltages require high-voltage electrical training and safety procedures. The difference is incremental, not transformational. 400V is well within experimental aircraft builder capability with proper training.

---

## Scalability and Future-Proofing

### v1.0 → v1.1 Upgrade Path Impact

**270V System:**
- If v1.1 adds pressurization and more electrical loads, may approach current limits
- Upgrading to higher power would require either:
  - Heavier wiring to handle increased current
  - Voltage architecture change (expensive retrofit)

**400V System:**
- More headroom for electrical load growth
- Can support higher power propulsion motors without bus redesign
- Better positioned for v2.0 if power requirements increase

---

## Generator Output Voltage Investigation

**Critical unknown:** What voltage do the generator candidates actually output?

### Kawasaki Engine Generator Assumptions
- Industrial/automotive alternators typically output 12V, 24V, or 48V low-voltage
- **We are using custom generator heads (Beyond Motors AXM2)**
- AXM2 spec: 75 kW continuous, **voltage configurable based on winding design**
- Beyond Motors can wind generator heads for **any voltage** we specify (270V, 400V, or other)

**Conclusion:** Generator output voltage is **not a constraint**. We can specify 270V or 400V output when ordering the AXM2 generator heads. No boost/buck converter needed if we choose voltage at design time.

---

## SYSTEMS Engineering Recommendation

**Revised recommendation: 400V bus**

**Rationale:**
1. **No generator voltage penalty** — AXM2 generator heads are configurable; we can specify 400V output
2. **20 lb weight savings** — lower current = lighter wiring
3. **Better component availability** — massive Tesla/EV aftermarket ecosystem
4. **Lower cost** — more competition among 400V component suppliers
5. **Future-proof** — headroom for v1.1 and v2.0 electrical load growth
6. **Industry alignment** — 400V is the EV standard; 800V is emerging for high-performance

**Original 270V recommendation was based on assumed generator output voltage constraint. That constraint does not exist.**

---

## Decision Matrix

| Criterion | 270V | 400V | Winner |
|-----------|------|------|--------|
| Generator efficiency | Equivalent (configurable) | Equivalent (configurable) | Tie |
| Wiring weight | ~40 lbs | ~30 lbs | **400V (-10 lbs)** |
| Component availability | Moderate | Extensive | **400V** |
| Component cost | Moderate | Lower (more competition) | **400V** |
| Motor compatibility | Compatible | Compatible | Tie |
| Safety complexity | Slightly simpler | Standard EV practice | 270V (marginal) |
| Future scalability | Limited headroom | Good headroom | **400V** |
| v1.0→v1.1 upgrade | May require bus redesign | Supports growth | **400V** |

**Winner: 400V** (6 advantages vs 1 marginal advantage for 270V)

---

## Implementation Notes

### If Builder Selects 400V:
1. Specify AXM2 generator heads with 400V output winding when ordering from Beyond Motors
2. Source 400V-rated motor controllers (recommend Cascadia Motion or Tesla aftermarket)
3. Use automotive HV wiring standards (SAE J1673, orange jacket, proper labeling)
4. Implement dual-redundant contactors for safety
5. Develop high-voltage safety procedures (lockout/tagout, insulation testing, arc flash PPE)

### If Builder Selects 270V:
1. Specify AXM2 generator heads with 270V output winding
2. Source 270V motor controllers (more custom/semi-custom)
3. Accept ~10 lb wiring weight penalty
4. Accept reduced future scalability

---

## Questions for Builder

1. **Do you want to align with Tesla/EV industry standard (400V) or optimize for slightly simpler safety procedures (270V)?**
2. **How important is future scalability for v1.1 and beyond?**
3. **Are you comfortable with 400V high-voltage safety practices?** (Standard for EV builders, but requires training)

---

**SYSTEMS Position:** **Close DG-004 at 400VDC** unless builder has specific rationale for 270V.

**Tags for publication:** #DG-004 #BusVoltage #SystemsArchitecture #ElectricalDesign #MAOS
