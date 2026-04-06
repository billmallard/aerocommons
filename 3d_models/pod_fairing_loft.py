"""
MAOS Pod — FreeCAD loft with asymmetric aft body.
Forward sections:  symmetric ellipses (normal pod tube).
Aft sections:      flat top (constant Z_TOP = pod crown) + curved bottom rising toward boom.
Exports: /workspace/cad/maos_pod_fairing.stl
"""
import sys, math
sys.path.insert(0, '/usr/lib/freecad-python3/lib')

import FreeCAD as App
import Part

App.newDocument("pod_fairing")

# ── Parameters (feet) ─────────────────────────────────────────────────────────
POD_L   = 13.0
POD_W   = 4.3333
POD_H   = 4.8333
Z_TOP   = POD_H / 2          # pod crown = 2.4167 ft  (top of full section)

# ── Cross-section generators ──────────────────────────────────────────────────

def sym_pts(W, H, Zc=0.0, n=40):
    """Symmetric ellipse, starting at rightmost point (Y=W/2, Z=Zc), going CCW."""
    return [
        App.Vector(0, (W/2)*math.cos(2*math.pi*i/n),
                      Zc + (H/2)*math.sin(2*math.pi*i/n))
        for i in range(n)
    ]

def asym_pts(W, Z_bot, n_bot=32, n_top=10):
    """
    Flat-top asymmetric section.
      Top : straight line at Z = Z_TOP (pod crown held constant)
      Bottom: ellipse-derived arc curving down to Z_bot
    Starts at (Y = W/2, Z = Z_TOP), goes through bottom, back along flat top.
    This is in the local XSec plane, so X=0 here; caller offsets to fuselage X.
    """
    H = max(Z_TOP - Z_bot, 0.01)
    pts = []
    # ── bottom arc: (W/2, Z_TOP) → (0, Z_bot) → (-W/2, Z_TOP) ──────────────
    for i in range(n_bot + 1):
        theta = math.pi * i / n_bot           # 0 → π
        y = (W/2) * math.cos(theta)
        z = Z_TOP - H * math.sin(theta)       # drops to Z_bot at θ=π/2, back up
        pts.append(App.Vector(0, y, z))
    # ── flat top: (-W/2, Z_TOP) → (W/2, Z_TOP) ──────────────────────────────
    for i in range(1, n_top):
        frac = i / n_top
        pts.append(App.Vector(0, -W/2 + W*frac, Z_TOP))
    # (closure back to start handled by PeriodicFlag=True)
    return pts

def make_wire(pts, X_offset):
    """Translate pts to fuselage X, interpolate a periodic BSpline, return Wire."""
    pts3 = [App.Vector(p.x + X_offset, p.y, p.z) for p in pts]
    bc = Part.BSplineCurve()
    bc.interpolate(pts3, PeriodicFlag=True)
    return Part.Wire([bc.toShape()])

# ── Section table ──────────────────────────────────────────────────────────────
# (X_frac, pts_generator_call)
# Forward sections all use sym_pts starting at (W/2, Zc=0).
# To keep consistent wire orientation (same start direction), sym_pts starts at
# θ=0 → (W/2, 0).  The asym_pts also start at (W/2, Z_TOP).
# There is a positional jump at the sym→asym boundary; we bridge it with one
# "blended" section at 55% that is still symmetric but starts the Z_TOP logic.

raw_sections = [
    (0.00,  sym_pts(0.08,  0.10, Zc=0)),          # nose tip  (tiny)
    (0.10,  sym_pts(POD_W, POD_H, Zc=0)),          # windscreen shoulder
    (0.293, sym_pts(POD_W, POD_H, Zc=0)),          # 29% full cabin
    (0.50,  sym_pts(POD_W, POD_H, Zc=0)),          # 50% max section
    # aft taper: top locked to Z_TOP, bottom rises
    (0.64,  asym_pts(3.8,  Z_bot=-2.0)),
    (0.74,  asym_pts(2.8,  Z_bot=-1.0)),
    (0.83,  asym_pts(1.8,  Z_bot= 0.0)),
    (0.92,  asym_pts(1.0,  Z_bot= 1.1)),
    (1.00,  asym_pts(0.55, Z_bot= 1.8)),           # tail: near boom diameter
]

wires = [make_wire(pts, frac * POD_L) for frac, pts in raw_sections]
print(f"Built {len(wires)} cross-section wires")

# ── Loft ──────────────────────────────────────────────────────────────────────
try:
    loft = Part.makeLoft(wires, True, False, False)   # solid, not ruled, not closed
    print("Loft succeeded")
    out = "/workspace/cad/maos_pod_fairing.stl"
    loft.exportStl(out)
    print(f"Exported: {out}")
except Exception as e:
    print(f"Loft failed: {e}")
    # Fall back: export each wire as individual STL for debugging
    for i, w in enumerate(wires):
        w.exportStl(f"/workspace/cad/wire_{i:02d}.stl")
    print("Exported individual wires for inspection")
