  
**MAOS AIRCRAFT PROJECT**

**Environmental Control System**

Development Plan

Pressurization · Climate Control · Controller Electronics

Document: MAOS-ECS-DEV-001  
Revision: A (Draft)  
Date: March 12, 2026

# **1\. System Overview & Design Philosophy**

The MAOS Environmental Control System (ECS) provides cabin pressurization, heating, cooling, ventilation, and dehumidification as a single integrated subsystem. Unlike conventional light aircraft that bleed compressed air from engine turbochargers, the MAOS ECS is fully electric: all compressors, fans, valves, and controllers run from the aircraft DC electrical bus with no pneumatic connections to the wing-mounted generators.

This architecture is driven by the pod-and-boom configuration. The wing-to-pod interface is the primary modularity boundary for transport and assembly. Keeping the ECS entirely within the pod means that wing attachment and removal requires only structural fasteners, electrical connectors, and fuel quick-disconnects. No hot pneumatic ducting crosses this boundary.

## **1.1 Design Requirements**

| Parameter | Requirement |
| :---- | :---- |
| Cabin volume | \~150–180 cu ft (4 occupants \+ baggage) |
| Max flight altitude | 25,000 ft (Kawasaki engine max operating) |
| Target cabin altitude | 8,000 ft maximum at all flight altitudes |
| Max differential pressure | 5.5 psi (at 25,000 ft / 8,000 ft cabin) |
| Normal differential | 3.5 psi (at 20,000 ft / 8,000 ft cabin) |
| Ventilation flow | 10 CFM/person minimum, 40–60 CFM total |
| Ground cooling | Full AC at 40°C ambient, 4 occupants, sun load |
| Ground heating | Cabin to 20°C from \-10°C ambient within 10 min |
| Max ECS power draw | 5 kW peak (ground hot day), 2–3 kW cruise |
| Target weight (complete) | 18–25 kg (40–55 lbs) all-in |
| Pod-external connections | Electrical only. Zero pneumatic connections. |

## **1.2 System Architecture Summary**

The ECS consists of two independent compression loops plus shared distribution and controls:

* **Pressurization loop:** Electric air compressor draws ambient air through filtered pod inlet, compresses to cabin pressure, delivers to mixing plenum. Outflow valve on aft bulkhead regulates cabin pressure.

* **Climate loop:** Closed-circuit vapor-cycle refrigerant system (R-1234yf) with reversible heat pump capability. EV-class scroll compressor, condenser with ram air and electric fan, evaporator in cabin air path, electronic expansion valve.

* **Controls:** Custom ESP32-based controller managing both loops, cabin pressure regulation, temperature control, safety interlocks, and CAN bus integration with aircraft systems.

# **2\. Development Phases**

Development proceeds in five phases. The key principle is that each phase produces a testable system that validates assumptions before committing to the next level of integration. The pod-only architecture makes this possible: every phase through Phase 3 can be tested on the ground with the pod on its trailer.

| Phase | Objective | Deliverable | Duration | Cost Est. |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Requirements & component selection | BOM, schematic, sourced parts | 6–8 weeks | $2,000–$3,500 |
| 2 | Bench test rig | Working ECS on open frame | 8–12 weeks | $3,000–$5,000 |
| 3 | Pod integration | ECS installed in pressure shell | 8–12 weeks | $2,000–$4,000 |
| 4 | Ground pressure test | Sealed pod holds 5.5 psi diff. | 4–6 weeks | $500–$1,500 |
| 5 | Flight test integration | ECS operational in flight | Ongoing | Incl. in flight test |

## **2.1 Phase 1: Requirements Lockdown & Component Selection**

**Duration:** 6–8 weeks

**Objective:** Finalize thermal loads, select all major components, produce complete bill of materials, and design the controller electronics for PCB outsourcing.

### **2.1.1 Thermal Load Analysis**

Before selecting hardware, quantify the actual thermal loads for the three design cases:

1. **Ground hot day (design driver):** 40°C ambient, direct solar through windscreen (\~800 W/m² on \~0.5 m² glazing \= 400W solar gain), 4 occupants at 100W metabolic each, avionics heat \~100W. Total cooling load approximately 900–1,100W. Add safety margin: size climate compressor for 3–4 kW cooling capacity.

2. **Cruise at 20,000 ft:** OAT approximately \-25°C, pressurization compressor adds \~40°C to inlet air, cabin heat loss through fuselage skin significant. Net heating load likely 500–800W. Heat pump mode or pressurization compression heat may suffice.

3. **Cold soak / ground cold:** \-10°C ambient, need to warm cabin to 20°C. Heat pump COP drops at low ambient temps. May need supplemental resistive heat element (\~1 kW PTC heater as backup) for initial warmup.

### **2.1.2 Component Selection**

All major components should be selected during this phase. The following table identifies the target components and selection criteria:

| Component | Target Specification | Sourcing Notes |
| :---- | :---- | :---- |
| Pressurization compressor | Electric centrifugal or scroll, 60 CFM at 2:1 PR, 12–48V or 200–400V DC, \<4 kg | EV/fuel cell air supply units (e.g., Busch, Rotrex, Thomas). Evaluate automotive fuel cell cathode air compressors. |
| Climate compressor | EV scroll compressor, R-1234yf, 3–4 kW cooling, 200–400V DC, \<7 kg | Denso, MAHLE, Hanon Systems, Valeo. Used EV parts from Tesla Model 3/Y, Hyundai Ioniq salvage as test units. |
| Condenser | Microchannel, \~2–3 kW rejection, ram air \+ 12V fan, \<3 kg | Automotive universal condensers. Size for ground ops with fan only (no ram air). |
| Evaporator | Compact plate-fin, fits under-floor or behind panel, \<2 kg | Universal automotive evaporator cores. Custom bracket via 3D print / sheet aluminum. |
| Outflow valve | Motorized butterfly or poppet, 2–3 in diameter, proportional control | COTS motorized damper or custom: stepper motor \+ 3D-printed or waterjet butterfly. Fail-open design mandatory. |
| Expansion valve | Electronic expansion valve (EEV), R-1234yf rated | Danfoss, Sanhua, or automotive OEM. EEV preferred over TXV for heat pump reversibility. |
| Reversing valve | 4-way valve for heat pump mode | Standard HVAC 4-way reversing valve, R-1234yf compatible. |
| Cabin pressure sensor | Absolute pressure, 0.1% accuracy, 6–15 psia range | Honeywell ABP2 series or TE MS5611. Dual redundant. |
| Temperature sensors | NTC thermistors or digital (DS18B20), cabin \+ evap \+ condenser \+ ambient | Commodity parts. 6–8 sensors total across system. |
| Dump valve | Manual cable-actuated, 3–4 in, fail-open | Aircraft Spruce or custom. Pilot-accessible red handle, zero electrical dependency. |
| PTC heater (backup) | 1–2 kW, 12V or HV DC, self-regulating | Automotive PTC cabin heater elements. Compact, intrinsically safe. |

### **2.1.3 Controller Electronics Design**

The ECS controller is the heart of the system and the primary custom-development effort. It manages cabin pressure regulation, climate control, safety interlocks, and system health monitoring. The architecture uses an ESP32-S3 as the main processor with purpose-built I/O and power driver boards.

**Controller architecture:** One main controller board (ESP32-S3) handles all ECS logic. A separate power driver board carries the high-current switching for compressor enable, fan PWM, valve actuation, and PTC heater switching. The two boards connect via a ribbon cable. This separation keeps noise-sensitive analog sensing away from high-current switching.

Phase 1 deliverables for electronics:

1. Complete schematic capture in KiCad (open-source, PCB fab houses accept natively)

2. Bill of materials with LCSC/DigiKey/Mouser part numbers for all components

3. PCB layout to 90% completion, ready for review before sending to fab

4. Firmware architecture document defining state machines, control loops, and CAN message definitions

5. Gerber files and pick-and-place files ready for JLCPCB or PCBWay assembly

### **2.1.4 Main Controller Board — Block Diagram**

The main board includes:

* **ESP32-S3-WROOM-1 module:** Dual-core 240 MHz, WiFi/BLE for ground diagnostics and firmware updates, sufficient ADC channels and GPIO.

* **Pressure sensing:** Dual redundant absolute pressure sensors (SPI or I2C), 0.1% accuracy. Cross-checked in firmware; disagreement triggers alert.

* **Temperature inputs:** 8-channel analog mux for NTC thermistors (cabin air, evaporator surface, condenser air, ambient inlet, compressor discharge, refrigerant suction, refrigerant discharge, electronics enclosure).

* **Humidity sensor:** SHT40 or BME280 for cabin humidity monitoring and dehumidification control.

* **CAN transceiver:** SN65HVD230 or MCP2562 for integration with aircraft CAN bus. Receives altitude, airspeed, and electrical bus status. Transmits ECS status and alerts.

* **Display interface:** SPI output to a small TFT or OLED for maintenance/debug. In flight, ECS status displays on the primary EFIS via CAN.

* **SD card slot:** Flight data logging of all ECS parameters at 1 Hz for post-flight analysis.

### **2.1.5 Power Driver Board — Block Diagram**

The power driver board includes:

* **Pressurization compressor driver:** If using a brushless DC compressor, either an integrated inverter (preferred) or an external ESC. Enable/speed command from main controller via PWM or analog voltage.

* **Climate compressor driver:** EV scroll compressors typically include an integrated inverter accepting a CAN or PWM speed command. The power board provides the HV DC contactor and precharge circuit.

* **Fan PWM outputs:** 2 channels (condenser fan, cabin recirculation fan), MOSFET-driven, 12V, 5A each.

* **Outflow valve driver:** Stepper motor driver (TMC2209 or A4988) for proportional valve control. Endstop inputs for full-open and full-closed positions.

* **EEV driver:** Stepper driver for electronic expansion valve (500-step typical).

* **Reversing valve:** Relay or MOSFET for 4-way valve solenoid actuation.

* **PTC heater switching:** High-side MOSFET switch with current sensing for the backup heater element.

* **Power monitoring:** INA226 or equivalent for bus voltage and current measurement on both LV (12/28V) and HV (if applicable) buses.

## **2.2 Phase 2: Bench Test Rig**

**Duration:** 8–12 weeks

**Objective:** Prove the thermodynamics, validate component selections, tune the control loops, and identify integration issues before touching the actual pod.

The bench rig is the most important phase. It catches problems when they are cheap to fix. Build it on a workbench or rolling cart using a simplified test enclosure.

### **2.2.1 Test Enclosure**

Build a sealed plywood or insulated foam box roughly approximating the pod internal volume (about 4 ft × 4 ft × 8 ft). It does not need to hold 5.5 psi differential. Use a shop vacuum or auxiliary blower connected to the outflow path to simulate cabin leakage and draw air through the system. The goal is airflow and thermal testing, not pressure testing.

For the pressurization compressor specifically, test it against a throttled outlet to confirm it can achieve the required pressure ratio and flow rate at the expected inlet pressures. You cannot simulate 20,000 ft ambient pressure on a bench, but you can verify the compressor performance curve and extrapolate.

### **2.2.2 Bench Test Sequence**

1. **Climate loop only (no pressurization):** Charge refrigerant circuit, run cooling mode, verify evaporator temperature, condenser rejection, and cabin temperature pulldown in the test box. Tune EEV superheat control.

2. **Heat pump mode:** Reverse the 4-way valve, verify heating capacity and COP at various ambient conditions. Test defrost logic if evaporator ices.

3. **Pressurization compressor:** Run independently. Measure flow vs. pressure ratio curve. Verify discharge temperature. Test speed control response.

4. **Combined operation:** Run both loops simultaneously. Verify no interactions (electrical noise, vibration coupling). Test worst-case power draw.

5. **Controller integration:** Install the prototype PCBs. Run automated test sequences. Verify all sensor readings, actuator responses, safety interlocks. Test CAN bus communication with a simulated aircraft bus.

6. **Failure mode testing:** Simulate sensor failures (disconnect each sensor individually), compressor failures (kill power to each compressor), and electrical bus faults. Verify the controller responds correctly to each scenario.

### **2.2.3 Instrumentation**

The bench rig should be heavily instrumented beyond what the flight controller needs. Add a USB data acquisition system logging at 10 Hz minimum, with thermocouples at every point in the refrigerant circuit, pitot tubes in the air ducts for flow measurement, a watt meter on the electrical supply, and a refrigerant pressure gauge set. This data validates the thermal model and catches issues the flight sensors might miss.

## **2.3 Phase 3: Pod Integration**

**Duration:** 8–12 weeks

**Objective:** Install the proven bench system into the actual pod structure, route ducting, mount the condenser, seal penetrations, and verify fitment.

By this point, the thermodynamics are validated and the controller is tuned. This phase is about packaging, routing, and sealing. The pod is on the trailer with no wing attached. Shore power (120/240V AC via an inverter or directly) drives the system.

Key integration tasks:

1. **Condenser mounting:** Install on lower aft pod surface with NACA scoop or flush inlet for ram air. Verify fan-only ground cooling capacity before assuming any ram air credit.

2. **Evaporator installation:** Mount in under-floor plenum or behind aft cabin panel. Route cabin air recirculation ducting. Verify condensate drain path exits the pressure shell through a trapped drain (P-trap or check valve to prevent pressure loss).

3. **Pressurization inlet:** Install filtered inlet on pod exterior with rain/FOD protection. Route to pressurization compressor. Consider inlet location relative to exhaust and engine fumes.

4. **Outflow valve:** Install on aft pressure bulkhead. Verify full-open and full-closed positions. Test manual dump valve independently.

5. **Controller and wiring:** Mount controller enclosure in avionics bay area. Route sensor wiring and power cables. Verify EMI compatibility with avionics. Test CAN bus through actual aircraft harness.

6. **Seal all penetrations:** Every wire, tube, and control cable passing through the pressure shell gets a sealed bulkhead fitting. Document every penetration location and sealing method.

## **2.4 Phase 4: Ground Pressure Test**

**Duration:** 4–6 weeks

**Objective:** Prove the pod holds the design differential pressure with acceptable leak rate. This is the structural validation of the pressure vessel.

This is the first time you pressurize the actual pod to 5.5 psi differential. This is a significant structural test and must be conducted carefully:

1. **Pre-test inspection:** Visual inspection of all seams, bulkheads, penetrations, and the windscreen seal. Fix anything that looks questionable before pressurizing.

2. **Incremental pressurization:** Increase in 0.5 psi steps with 5-minute holds at each step. Listen for creaking, popping, or air leaks at every step. Abort and investigate any anomaly.

3. **Proof pressure:** Hold at 1.33× design differential (7.3 psi) for a minimum duration per your structural analysis requirements. This is a one-time proof test, not a cyclic fatigue test.

4. **Leak rate measurement:** At design pressure (5.5 psi), shut off the pressurization compressor and measure cabin pressure decay rate over 30 minutes. Calculate leak rate in CFM. Target: the pressurization compressor can maintain pressure with margin to spare.

5. **ECS functional test under pressure:** Run the complete ECS while the pod is pressurized. Verify outflow valve regulation, temperature control, and all controller functions under actual pressure differential.

**Safety note:** A 52-inch-diameter cylinder at 5.5 psi contains significant stored energy. Conduct pressure testing outdoors or in a well-ventilated space. Keep all personnel clear of the windscreen and any large flat panels during pressurization. A catastrophic failure at 5.5 psi is survivable at distance but can cause serious injury if you are leaning against a panel that lets go.

## **2.5 Phase 5: Flight Test Integration**

**Duration:** Ongoing (part of the overall MAOS flight test program)

**Objective:** Validate ECS performance at actual cruise altitudes and across the full flight envelope.

ECS flight testing is integrated into the broader MAOS flight test program. The system should be installed but operated unpressurized during initial flight tests, with the outflow valve locked open. This allows the controller to log altitude, ambient conditions, and system responses without imposing pressure loads on a structure that is being validated for other things simultaneously.

Pressurized flight testing begins only after the aircraft has demonstrated satisfactory handling qualities and structural integrity through the initial flight test envelope expansion. ECS-specific flight test points include cabin pressure control during climb and descent, temperature regulation across the altitude envelope, emergency depressurization from maximum differential, and single-generator-failure operation.

# **3\. Controller Firmware Architecture**

The ECS firmware runs on the ESP32-S3 using FreeRTOS. The architecture uses three main tasks running at different rates, plus interrupt-driven CAN communication.

## **3.1 Task Structure**

| Task | Rate | Responsibility |
| :---- | :---- | :---- |
| Pressure Control | 10 Hz | Read pressure sensors, compute cabin altitude and rate of change, command outflow valve position and pressurization compressor speed via PID loop. Safety checks for overpressure and excessive rate of change. |
| Climate Control | 1 Hz | Read temperature and humidity sensors, compute heating/cooling demand, command climate compressor speed, fan speeds, EEV position, and reversing valve state. Superheat monitoring and protection. |
| System Health | 0.5 Hz | Cross-check redundant sensors, monitor bus voltage and current, check compressor operating parameters against limits, manage SD card logging, handle WiFi diagnostics connection, transmit CAN status messages. |

## **3.2 State Machine**

The ECS operates in five primary states:

* **OFF:** System powered but all actuators inactive. Entered on power-up and on pilot command.

* **GROUND (unpressurized):** Climate control active, pressurization compressor off, outflow valve locked open. Used for ground operations, taxi, and initial climb below transition altitude.

* **PRESSURIZING:** Transitional state during climb. Outflow valve modulating closed, pressurization compressor ramping up. Cabin rate of change limited to 500 ft/min equivalent for passenger comfort.

* **CRUISE (pressurized):** Both loops active, cabin pressure regulated to schedule. This is the normal in-flight state above transition altitude.

* **DEPRESSURIZING:** Transitional state during descent. Outflow valve opening, pressurization compressor ramping down. Cabin rate of change limited to 300 ft/min equivalent.

Emergency states (entered automatically or by pilot action):

* **DUMP:** Pilot pulls manual dump handle. Outflow valve driven full open. Pressurization compressor off. Climate continues if power available. Non-recoverable without pilot reset.

* **FAULT:** Controller detects sensor disagreement, overpressure, or actuator failure. Outflow valve driven to safe position (open or cracked, depending on failure mode). Alert on CAN bus and annunciator.

## **3.3 Cabin Pressure Schedule**

The controller maintains cabin altitude according to a schedule based on actual aircraft altitude (received via CAN bus from the air data computer or GPS altitude). A simple linear schedule works well:

* Sea level to 8,000 ft aircraft altitude: cabin unpressurized (1:1 with ambient)

* 8,000 to 25,000 ft aircraft altitude: cabin altitude held at 8,000 ft (differential increases from 0 to \~5.5 psi)

* Rate limiting: cabin altitude change rate capped at 500 ft/min climb, 300 ft/min descent regardless of aircraft rate

The pilot can override the schedule to request a lower cabin altitude (higher differential) or manual control of the outflow valve for abnormal situations. Override requires a deliberate two-step input to prevent accidental engagement.

# **4\. Safety & Failure Modes**

Every failure mode must result in a safe condition without pilot intervention. The fundamental principle: loss of pressurization is uncomfortable but not immediately dangerous. The aircraft can always descend. Loss of structural integrity of the pressure vessel is the only catastrophic failure mode, and that is addressed by structural design and proof testing, not by the ECS controller.

## **4.1 Failure Mode Summary**

| Failure | Automatic Response | Pilot Action Required |
| :---- | :---- | :---- |
| Pressurization compressor failure | Outflow valve holds position, cabin slowly depressurizes as leakage exceeds zero inflow | Descend to unpressurized altitude or don supplemental O2 |
| Climate compressor failure | Climate loop shuts down, pressurization continues normally | Accept temperature discomfort. Open vents for ventilation. |
| Outflow valve stuck closed | Pressurization compressor speed reduced. Safety relief valve opens at max differential \+ 0.5 psi | Monitor cabin pressure. Use manual dump if needed. |
| Outflow valve stuck open | Pressurization compressor at max speed. If unable to maintain cabin altitude, alert pilot. | Descend to unpressurized altitude. |
| Pressure sensor disagreement | Use remaining good sensor. If both suspect, drive outflow valve to mid-position and alert pilot. | Manual pressure control or descend. |
| Total electrical failure | Outflow valve spring-returns to full open (fail-safe). Both compressors stop. | Aircraft is now unpressurized. Descend. Manual dump available (cable, no electrical). |
| Windscreen seal failure | Rapid cabin pressure loss. Controller detects rate and shuts down pressurization compressor. | Don O2, descend immediately. Structural: windscreen retained by mechanical stops. |
| Refrigerant leak | Climate compressor shuts down on low suction pressure. Alert pilot. | No immediate safety concern. Climate comfort only. |

## **4.2 Mandatory Safety Hardware (Non-Electronic)**

These items operate with zero electrical power and zero controller involvement:

* **Manual dump valve:** Cable-actuated, red T-handle accessible to pilot. Mechanically opens a 3–4 inch port in the pressure shell. No electronics in the path.

* **Positive pressure relief valve:** Spring-loaded, set to open at max differential \+ 0.5 psi (6.0 psi). Prevents overpressure even if the controller and outflow valve both fail simultaneously.

* **Negative pressure relief valve:** Prevents external pressure from exceeding cabin pressure during rapid descent. Spring-loaded inward-opening flap.

* **Outflow valve return spring:** If the stepper motor loses power or the controller fails, the outflow valve spring-returns to full open. Fail-safe to unpressurized.

# **5\. Weight & Power Budget**

## **5.1 Weight Breakdown**

| Component | Weight (kg) | Notes |
| :---- | :---- | :---- |
| Pressurization compressor \+ motor | 3.0–4.0 | Centrifugal preferred for weight |
| Climate scroll compressor \+ inverter | 5.0–7.0 | EV HVAC unit, integrated inverter |
| Condenser \+ fan | 2.0–3.0 | Microchannel automotive |
| Evaporator | 1.0–2.0 | Compact plate-fin |
| Refrigerant lines, EEV, receiver-drier, reversing valve | 2.0–3.0 | Standard automotive |
| Outflow valve \+ actuator | 0.5–1.0 | Custom: waterjet butterfly \+ stepper |
| Relief valves (positive \+ negative) | 0.5–1.0 | Aircraft-grade spring valves |
| Manual dump valve \+ cable | 0.3–0.5 | Cable-actuated, mechanical |
| PTC backup heater | 0.5–1.0 | Automotive PTC element |
| Controller boards \+ wiring harness | 1.0–1.5 | ESP32 \+ power driver \+ harness |
| Ducting, plenum, brackets, inlet filter | 2.0–3.0 | 3D-printed formers \+ fabric duct or sheet aluminum |
| TOTAL | 17.8–27.0 | Target: \<25 kg (55 lbs) |

## **5.2 Electrical Power Budget**

| Consumer | Power (kW) | Condition |
| :---- | :---- | :---- |
| Pressurization compressor | 1.5–2.0 | Cruise at 20,000–25,000 ft |
| Climate compressor (cooling) | 2.0–3.0 | Ground hot day (peak) |
| Climate compressor (cruise) | 0.5–1.5 | Cruise (reduced load) |
| Condenser fan | 0.1–0.2 | Ground ops (max); ram air reduces in flight |
| Cabin recirc fan | 0.05–0.1 | Continuous |
| PTC heater (if used) | 1.0–2.0 | Cold ground startup only |
| Controller \+ sensors \+ valves | 0.02–0.05 | Continuous |
| TOTAL — worst case ground | 4.0–5.5 | Hot day, full cooling, no pressurization |
| TOTAL — typical cruise | 2.0–3.5 | Pressurized, moderate climate load |

With twin wing-mounted generators producing well over 100 kW combined electrical output, the ECS represents approximately 2–5% of available bus power. This is negligible and leaves ample margin for all other electrical consumers.

# **6\. Open Questions & Decisions Needed**

The following items require resolution before or during Phase 1\. Each represents a design decision that affects multiple downstream components:

4. **Bus voltage for ECS:** The aircraft electrical architecture needs to be defined sufficiently to select compressor voltage ratings. If the main bus is high-voltage DC (e.g., 270V or 350V, common in series hybrid architectures), the EV climate compressor runs natively. If the bus is 48V or 28V, a DC-DC converter or different compressor selection is needed. The pressurization compressor may run on a different voltage than the climate compressor.

5. **Refrigerant choice:** R-1234yf is the automotive standard and has favorable environmental properties (low GWP). R-134a is cheaper and has a wider component ecosystem. Both work. R-1234yf is mildly flammable (A2L classification) which requires consideration for an enclosed pressurized cabin, though automotive use in enclosed vehicles is considered safe. Decision needed.

6. **Pod cross-section geometry:** The pressurization loads are directly affected by whether the pod is a true circle, an ellipse, or a cylinder-with-flat-segments. This must be resolved before structural analysis of the pressure shell. A true \~55-inch-diameter circle is structurally ideal.

7. **Windscreen design:** The windscreen is the weakest link in any pressurized cabin. Flat panels in pressurized fuselages require heavy frames. Curved windscreens are structurally efficient but optically complex. The windscreen geometry must be designed for pressure from the start.

8. **Transition altitude:** At what altitude does the system begin pressurizing? 8,000 ft (start of cabin altitude schedule) is the logical choice, but this could be pilot-selectable. Affects controller logic and the climb/descent profiles.

9. **Shore power interface:** For pre-cooling on the ground, the system needs a way to run from external power. Define the connector type, voltage, and power level. A standard J1772 EV charging connector is an interesting option if the aircraft HV bus is compatible.

10. **Oxygen system integration:** Supplemental oxygen is required above 12,500 ft (FAR 91.211) if the pressurization system is inoperative or not yet activated. The ECS plan should define how the O2 system interfaces, even though O2 is a separate subsystem.

**Next action:** Resolve the bus voltage question (item 1\) and pod cross-section geometry (item 3\) as they gate the most Phase 1 work. Everything else can be decided in parallel with Phase 1 execution.