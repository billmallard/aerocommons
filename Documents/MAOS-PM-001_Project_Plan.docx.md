  
**MOBILE AVIATION**  
**OPERATING SYSTEM**

*Project Plan  ·  Team Architecture  ·  Agentic AI Integration*

| Document | MAOS-PM-001  Rev A |
| :---- | :---- |
| **Date** | March 2026 |
| **Status** | Active — Concept Phase |
| **Regulatory** | FAA Experimental Amateur-Built (51% Rule) |
| **Propulsion** | Series hybrid — ICE generator \+ dual rim-drive electric motors |
| **Config** | Pod-and-boom, high wing, fixed gear, 4-seat |
| **Performance** | 155 KTAS cruise, 17,500 ft service ceiling, 1,000 nm range |

| NORTH STAR | MAOS is a complete mobile aviation operating system. The airplane and trailer are co-equal components designed together from first principles. The system requires no fixed infrastructure. A single pilot can deploy, operate, and recover the system from any suitable airstrip. Every design decision is evaluated against this principle. |
| :---: | :---- |

# **1 — Concept Summary**

MAOS is not a controversial airplane. It is a novel assemblage of proven technologies on a new platform. Series hybrid drivetrains power locomotives and submarines. Rim-drive motors exist in marine propulsion. Contra-rotating propellers are standard in high-performance aviation. Pod-and-boom fuselages have flown for decades. The innovation is the integration: a coherent system designed from the ground up around complete operational independence from fixed infrastructure.

## **1.1  The Core Differentiators**

| Element | Conventional | MAOS Approach | Advantage |
| :---- | :---- | :---- | :---- |
| Propulsion | Single ICE, direct drive, CS prop | Series hybrid: ICE generator \+ dual rim-drive electric | No asymmetric thrust, full power at altitude, graceful failure |
| Engine failure | Emergency — seconds to respond | Generator fails → battery sustains → managed descent | Minutes to respond, not seconds |
| Infrastructure | Fixed hangar, FBO required | Trailer carries all support | Operates from any suitable airstrip |
| Power at altitude | ICE loses \~3%/1,000 ft | Electric motors unaffected by altitude | Full performance at service ceiling |
| Prop system | CS prop, governor, gearbox | Fixed-pitch or folding, direct drive | Lower cost, no governor failure mode |
| Safety | Depends on single engine | Redundant generators, cross-tied bus, battery reserve | Near-impossible total power loss scenario |

## **1.2  Propulsion Architecture**

| CORE | Two small ICE engines (generator duty only, fixed RPM) feed two independent electrical buses. Each bus powers one contra-rotating rim-drive motor on the tail boom. A solid-state battery buffer covers peak demand and provides 10+ minute emergency reserve. Cross-tied bus allows any single component failure to be absorbed without loss of propulsion. |
| :---: | :---- |

| GENERATOR AICE \+ Gen\~60 HP | BATTERY BUFFER3–5 kWh10 min reserve | RIM MOTOR 1Fwd stageClockwise | RIM MOTOR 2Aft stageCounter-CW |
| :---: | :---: | :---: | :---: |

*Generator B mirrors Generator A on independent bus. Cross-tie normally open, closes automatically on any single system fault.*

# **2 — Risk Register & Sequencing Rationale**

Work is sequenced highest-risk first. A validated propulsion system is the prerequisite for all other major commitments. A beautiful airframe built around an unproven drivetrain is an expensive mistake.

| Risk Item | Probability | Impact | Sequence | Mitigation |
| :---- | :---- | :---- | :---- | :---- |
| **Series hybrid propulsion** | HIGH | **CRITICAL** | **1 — FIRST** | Benchtop → ground test → flight test as hard gates |
| **Rim-drive motor availability** | MEDIUM — Donut Lab unverified; alternatives exist | HIGH | **1 — CONCURRENT** | Identify 3+ alternative ring motor suppliers before committing |
| **Generator ECU altitude compensation** | MEDIUM — motorcycle ECU not mapped above 12,000 ft | MEDIUM | **1 — EARLY** | Custom Speeduino with wideband O2 closed-loop control |
| **Wing integral fuel tank sealing** | LOW-MEDIUM — proven method (DA40), requires discipline | MEDIUM | 3 — after structure | ProSeal process, pressure test before closing skin |
| **Whole-aircraft parachute integration** | LOW — BRS proven in EAB category | MEDIUM | 4 — systems phase | Standard BRS installation, canister location reserved from day 1 |
| **FAA Experimental documentation** | LOW — well-understood EAB process | LOW | Ongoing | EAA technical counselor engaged early, 51% tracked from start |

# **3 — Project Phases**

Six phases with hard gates between each. No phase begins until the previous gate is met. Propulsion validation gates everything downstream.

| PHASE 0  ·  FOUNDATION & PROPULSION CONCEPT   |   Months 1–4 *Gate: Propulsion architecture selected, key suppliers identified, AI team infrastructure operational* |
| :---- |
| • Propulsion Team stood up — AI research agents activated • Survey all rim-drive / ring motor suppliers — minimum 3 viable alternatives to Donut Lab identified • Generator engine candidates benchmarked — Honda CBR300, CBR600, Kawasaki equivalents • Custom ECU architecture selected — Speeduino or equivalent, altitude compensation strategy confirmed • Donut Lab partnership evaluation — contact initiated only if Verge motorcycle deliveries verified • MAOS-PROP-001: Propulsion Architecture Selection Document signed off before any hardware purchased • Project Git repository established, all MAOS documents committed, teams onboarded • EAA technical counselor identified and engaged |

| PHASE 1  ·  PROPULSION BENCHTOP VALIDATION   |   Months 3–10 *Gate: Generator \+ motor \+ inverter system produces target power, sustains 2-hour run, survives simulated failure* |
| :---- |
| • Generator A benchtop: ICE engine coupled to permanent magnet generator — power output measured • ECU altitude simulation: intake pressure simulation to 20,000 ft equivalent — closed-loop mixture confirmed • Rim-drive motor benchtop: selected motor at target RPM under load — thermal, efficiency, vibration measured • Bus cross-tie test: simulate Generator A failure — confirm automatic bus tie and sustained operation on B • Battery buffer integration: charge/discharge cycle under simulated climb demand — 3 kWh covers takeoff gap • 2-hour continuous run at cruise power setting — no degradation, temperatures stable • Vibration signature measured — confirm contra-rotation torque cancellation • MAOS-PROP-TEST-001: Benchtop Validation Report signed off before ground test begins |

| PHASE 2  ·  AIRFRAME DESIGN & ANALYSIS   |   Months 4–14  (concurrent with Phase 1 after month 4\) *Gate: Aerodynamic model frozen, structures sized, weight budget closed within 5% of target* |
| :---- |
| • XFLR5 viscous analysis — Riblett GA35-615 airfoil, CLmax and stall speed validated • AVL stability analysis — tail surfaces sized, boom length confirmed, static margin verified • CG calculation closed — all major mass items located on station map • Wing spar sizing confirmed — aluminum tube, fuel volume verified against mission requirement • Structural analysis: spar, spar saddle, boom attach, generator mount — all critical joints documented • Weight budget closed: target 1,230 lbs empty, 2,430 lbs gross • FreeCAD models: spar saddle, boom attach flange, generator mount, rim motor mounts • DXF files prepared for SendCutSend: all flat-cut aluminum parts |

| PHASE 3  ·  PROPULSION GROUND TEST & AIRFRAME BUILD   |   Months 10–24 *Gate: Propulsion system ground-tested in airframe. Airframe structurally complete.* |
| :---- |
| • Propulsion system installed in ground test rig — full airframe loads simulated • Throttle response, failure simulation, emergency bus-tie tested at full power • Pod primary structure complete — frames, floor, skin, spar saddle installed • One-piece wing built — spar installed, ribs, skin, fuel tanks sealed and pressure-tested • Tail boom fabricated — aluminum tube with motor mount rings and stabilizer attach • Rim-drive motors installed on boom — alignment, clearance, prop track verified • Control system rigged — all surfaces, cables, pushrods • Ground run \#1: taxi test, prop track, vibration check, thermal survey • Phase 3 gate: DAR structural inspection before closing |

| PHASE 4  ·  SYSTEMS INTEGRATION & FIRST FLIGHT PREP   |   Months 22–30 *Gate: Aircraft airworthy. All systems functional. Phase 1 flight test plan approved.* |
| :---- |
| • Avionics installed — Garmin G3X or equivalent, IFR capable • Power management system integrated — generator control, battery BMS, motor controllers unified • TKS ice protection installed — wings, windscreen, prop anti-ice (resistive blade elements) • Whole-aircraft parachute installed and rigged • Weight and balance confirmed — actual weighing • DAR inspection — Experimental certificate issued • First flight crew briefing — abort criteria, emergency procedures, chase aircraft |

| PHASE 5  ·  FLIGHT TEST & ENVELOPE EXPANSION   |   Months 30–40 *Gate: 40-hour Phase 1 complete. Aircraft released to full operating envelope.* |
| :---- |
| • Phase 1: 25 nm radius, pilot only, VMC only — basic airworthiness • Stall series: clean and configured — confirm root-first stall behavior • Generator failure simulation in flight: confirm battery sustains controlled flight to landing • Single motor failure: confirm manageable asymmetric torque, controlled flight maintained • Climb performance: full power at altitude, generator/battery behavior during climb verified • Cruise efficiency: fuel flow, power output, L/D validation against predictions • IFR systems checkout: autopilot, nav, ice protection activation • Phase 1 complete at 40 hours; Phase 2 begins: IFR, cross-country, full useful load |

# **4 — Team Structure**

Six functional teams plus an Integration lead. Each team pairs a human lead with AI agents in a defined role. Teams are small by design — one or two humans plus AI agents is the target. The AI agents do not replace human judgment on safety-critical decisions. They eliminate the research, documentation, analysis, and iteration burden that consumes most of a builder's time.

| AI PRINCIPLE | Agents handle: search, synthesis, simulation loops, documentation generation, BOM research, first-pass analysis, and compliance tracking. Humans own: all safety decisions, all sign-offs, all physical builds, all test conduct, and all regulatory submissions. The agent is the crew chief who has read everything and forgotten nothing. The human is the pilot-in-command. |
| :---: | :---- |

| 01 | TEAM 01: PROPULSION *Design, build, and validate the complete series hybrid drivetrain before any other major commitment is made.* |  |
| ----- | :---- | :---- |
| **TEAM LEAD** Project Lead / Systems Engineer | **AI AGENT ROLE** Motor survey agent monitors supplier announcements continuously. ECU mapping agent runs altitude simulation tables. Power budget agent models generator/battery interaction across full flight envelope. FMEA agent generates failure mode analysis automatically from system descriptions. | **HUMAN CONTRIBUTORS** • Mechanical / electrical engineer • Embedded systems developer (custom ECU) • EAA technical counselor (advisory) |
| **KEY DELIVERABLES** • MAOS-PROP-001: Architecture selection • Motor supplier matrix — 5+ candidates • Generator engine test report • ECU altitude compensation validation • 2-hour benchtop run report • FMEA — complete failure mode analysis | **RISK ITEMS** • Rim-drive motor availability / timeline • ECU altitude tables above 12,000 ft • Generator thermal management buried in wing • Bus cross-tie response time validation |  |

| 02 | TEAM 02: AERODYNAMICS & PERFORMANCE *Validate the aerodynamic model, size the tail, confirm stall safety, and close the performance budget.* |  |
| ----- | :---- | :---- |
| **TEAM LEAD** Aeronautical Engineer / Pilot | **AI AGENT ROLE** XFLR5 automation agent runs airfoil parameter sweeps and formats results. AVL agent iterates tail volume coefficients to hit stability targets. Performance agent builds flight envelope charts from analysis outputs. OpenVSP agent maintains geometry model as design changes propagate. | **HUMAN CONTRIBUTORS** • Pilot (operational requirements ownership) • Aeronautical engineer or EAA technical counselor |
| **KEY DELIVERABLES** • MAOS-AERO-002: XFLR5 viscous results • MAOS-AERO-003: AVL stability report • Tail surface sizing — boom length confirmed • CLmax and stall speed validated • Preliminary performance manual | **RISK ITEMS** • Riblett airfoil CLmax confirmation • Static margin with aft CG loading • Tail volume adequacy with short boom |  |

| 03 | TEAM 03: STRUCTURES *Size all primary structure, produce fabrication drawings, and deliver a buildable kit of flat-cut parts.* |  |
| ----- | :---- | :---- |
| **TEAM LEAD** Structural Engineer / Builder | **AI AGENT ROLE** FreeCAD automation agent converts analysis outputs to parametric models. DXF agent prepares SendCutSend-ready files and cut lists. Weight agent tracks every component against budget in real time. BOM agent cross-references Aircraft Spruce and McMaster-Carr for pricing and availability. | **HUMAN CONTRIBUTORS** • Builder with composites and aluminum experience • Structural engineer (advisory, critical joints) |
| **KEY DELIVERABLES** • Wing spar analysis and sizing • Spar saddle detail design • Boom attach flange • Generator mount design • Rim motor mount rings • Full DXF package for SendCutSend • Weight budget — closed to 5% | **RISK ITEMS** • Spar tube sizing vs. fuel volume tradeoff • Boom tensile loads from dual motor thrust • Generator mount vibration isolation design |  |

| 04 | TEAM 04: SYSTEMS & AVIONICS *Design and integrate all aircraft systems: electrical, avionics, ice protection, parachute, and power management.* |  |
| ----- | :---- | :---- |
| **TEAM LEAD** Systems / Avionics Engineer | **AI AGENT ROLE** Wiring diagram agent generates interconnect diagrams from system descriptions. Regulatory agent cross-references FAA AC 43.13 and EAB guidance. Power load agent calculates bus loads across all operational modes. IFR compliance agent tracks avionics requirements against intended operation. | **HUMAN CONTRIBUTORS** • Avionics installer / A\&P (advisory) • Electrical engineer • Software developer (power management ECU) |
| **KEY DELIVERABLES** • Electrical architecture document • Power management software spec • Avionics installation plan • Ice protection system design • Parachute integration • Wiring diagrams — complete | **RISK ITEMS** • Power management software validation • Failure detection and bus-tie response logic • Prop anti-ice slip ring design and reliability |  |

| 05 | TEAM 05: TRAILER & GROUND SUPPORT *Design and build the trailer system as a co-equal component: transport, deployment, charging infrastructure, maintenance support.* |  |
| ----- | :---- | :---- |
| **TEAM LEAD** Mechanical / Integration Engineer | **AI AGENT ROLE** Structural agent sizes trailer frame for aircraft transport loads. Crane geometry agent optimizes lift point for one-person operation. Solar layout agent calculates panel area vs. charging rate. Logistics agent tracks component sourcing, lead times, and total system cost. | **HUMAN CONTRIBUTORS** • Fabricator / welder • Electrician (shore power and solar systems) |
| **KEY DELIVERABLES** • Trailer structural design • Crane system — one-person 37-ft wing lift • Shore power inlet — 50A/240V • Solar panel mounting provision • Battery charging infrastructure provision • Deployment procedure — target 45 minutes | **RISK ITEMS** • Crane counterbalance with one-piece wing • Road legal dimensions and weight limits • Shore power compatibility across airstrip types |  |

| 06 | TEAM 06: DOCUMENTATION & REGULATORY *Maintain 51% compliance record, produce all required documentation, and manage the path to Experimental certificate.* |  |
| ----- | :---- | :---- |
| **TEAM LEAD** Documentation & Compliance Lead | **AI AGENT ROLE** Regulatory agent monitors FAA policy updates and flags relevant changes. 51% compliance agent tracks builder hours against the rule in real time. Documentation agent converts engineering notes and test results into formal document format. Decision log agent captures every major design choice with rationale automatically. | **HUMAN CONTRIBUTORS** • Project lead (document owner) • EAA technical counselor • DAR (Designated Airworthiness Representative) |
| **KEY DELIVERABLES** • Builder log — continuous from day 1 • 51% compliance matrix • Design decision log • Operating Limitations draft • Flight manual preliminary • Experimental certificate package | **RISK ITEMS** • 51% rule interpretation for novel power systems • Generator engine approval pathway • Documenting AI-assisted design decisions for compliance |  |

# **5 — Agentic AI Architecture**

The AI architecture is designed around one principle: agents eliminate the overhead that kills homebuilt projects. Most airplane projects die not from lack of skill but from the accumulated weight of undone research, unwritten documents, and untracked decisions. Agents handle that entire category of work.

## **5.1  Agent Categories**

| Agent Type | Function | Tools | Human Oversight |
| :---- | :---- | :---- | :---- |
| **Research Agents** | Monitor technical literature, supplier announcements, regulatory updates, and test results | Web search, document indexing, summarization | Weekly briefing review — human approves action items |
| **Analysis Agents** | Run parametric loops in XFLR5, AVL, OpenVSP. Format results. Flag anomalies. Propose next step. | XFLR5 scripting, AVL input files, OpenVSP Python API | Human reviews all conclusions before they inform design |
| **Documentation Agents** | Convert engineering discussions and test data into formatted documents. Maintain decision log. Update BOM. | Document templates, spreadsheet, Git commits | Human reviews and signs off all released documents |
| **Design Agents** | Iterate parametric CAD models, generate DXF files, track weight against budget as geometry changes | FreeCAD Python API, DXF export, weight spreadsheet | Human approves all geometry changes affecting performance or structure |
| **Compliance Agents** | Track 51% builder hours, monitor FAA regulatory database, maintain inspection readiness checklist | FAA database queries, hour tracking, document cross-reference | Human owns all regulatory submissions and sign-offs |
| **Supplier Agents** | Monitor Aircraft Spruce, McMaster-Carr, SendCutSend pricing. Alert on lead time changes. Maintain live BOM cost. | Web queries, BOM spreadsheet, alerts | Human approves all purchases |

## **5.2  Infrastructure**

| Component | Implementation | Est. Monthly Cost |
| :---- | :---- | :---- |
| AI model | Claude API — claude-sonnet, per-token billing | $50–200 at active development pace |
| Orchestration | Python scripts — open source, stored in /tools in project repo | $0 — builder writes and owns |
| Document store | Git repository — all docs, analysis files, decisions in version control | $0 — GitHub free tier |
| Analysis tools | XFLR5, AVL, OpenVSP — all open source, all scriptable | $0 |
| CAD | FreeCAD with Python API — all files in STEP/DXF open formats | $0 |
| BOM tracking | CSV files in Git — agent reads and writes directly | $0 |

## **5.3  Phase 0 Propulsion Agent Priorities**

Since propulsion is the first priority, the following agents activate in the first week:

| Agent | Immediate Task | Output | Cadence |
| :---- | :---- | :---- | :---- |
| **Motor Survey** | Search and catalog all rim-drive / ring motor / axial flux motor suppliers at 100–200 kW suitable for aviation | Supplier matrix with specs, pricing, aviation precedent | Weekly refresh |
| **Donut Lab Monitor** | Track Verge Motorcycle delivery reports, VTT independent test results, aviation partnership announcements | Weekly go/no-go recommendation on partnership timing | Daily scan |
| **Generator Engine** | Survey motorcycle and small auto engines 60–120 HP range. Research aircraft conversion history. Identify ECU options. | Engine candidate matrix with weight, cost, conversion history | Monthly refresh |
| **FMEA** | Build failure mode analysis from propulsion architecture description. Identify single-point failures. Propose mitigations. | Initial FMEA document updated as design evolves | On arch change |
| **Power Budget** | Model generator output vs demand across full flight envelope at sea level and 20,000 ft. Size battery buffer. | Power flow charts: cruise, climb, takeoff, emergency modes | On param change |

# **6 — Immediate Next Steps**

Phase 0 begins now. These actions are sequenced for the first 30 days, executable by one person with AI agent support.

| Priority | Action | AI Support | Timeline |
| :---- | :---- | :---- | :---- |
| **1 — THIS WEEK** | Activate Motor Survey Agent. Generate initial rim-drive supplier matrix with 5+ candidates beyond Donut Lab. | Research agent — web search, spec compilation | Days 1–5 |
| **2 — THIS WEEK** | Activate Donut Lab Monitor. Establish baseline — what has been independently verified as of today. | Research agent — Electrek, VTT reports, Verge delivery tracking | Days 1–5 |
| **3 — WEEK 2** | Generator engine candidate list: Honda CBR300, CBR600, Kawasaki equivalents. Weight, cost, conversion history. | Research agent — EAA forums, aircraft conversion databases | Days 7–14 |
| **4 — WEEK 2** | Speeduino ECU evaluation. Confirm altitude compensation via closed-loop wideband O2. Identify hardware config. | Technical research agent | Days 7–14 |
| **5 — WEEK 3** | MAOS-PROP-001 first draft: propulsion architecture selection document with all candidates and recommendation. | Documentation agent formats from engineering discussion | Days 14–21 |
| **6 — WEEK 4** | Establish project Git repository. All existing MAOS documents committed. All team members onboarded. | Documentation agent organizes existing files | Days 14–28 |
| **7 — MONTH 2** | XFLR5 installed. Riblett GA35-615 airfoil loaded. Viscous analysis run. CLmax confirmed. | Analysis agent — XFLR5 scripting, result formatting | Days 28–45 |
| **8 — MONTH 2** | EAA technical counselor identified. First meeting. 51% compliance tracking initialized. | Compliance agent — hour tracking initialized | Days 28–60 |

 

***The airplane that wants to be built.***

*Every major design decision in this project has reinforced the previous ones. The series hybrid architecture makes the trailer infrastructure more valuable. The rim-drive makes contra-rotation natural. The contra-rotation makes redundancy elegant. The battery buffer makes the generator altitude limitation irrelevant. This is what convergent design feels like. Proceed.*