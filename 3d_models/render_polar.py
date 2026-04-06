"""
MAOS Aircraft — Drag Polar Renderer
Reads VSPAERO .polar file and generates a four-panel drag polar chart.

Columns in .polar (space-separated, after 3-line header):
  0:Beta  1:Mach  2:AoA  3:Re/1e6  4:CLo  5:CLi  6:CLtot
  7:CDo   8:CDi   9:CDtot  ...  22:CMytot
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import math
import re

POLAR_FILE = '/workspace/cad/maos_aircraft_v1.polar'

# ── Body drag estimates (Swet method, same as vspscript) ─────────────────────
Sref      = 121.5   # ft²
CD_pod    = 0.0030 * 1.4  * 180.0 / Sref   # 0.00622
CD_boom   = 0.0027 * 1.15 *  47.0 / Sref   # 0.00120
CD_gear   = 0.0050
CD0_body  = CD_pod + CD_boom + CD_gear      # ~0.01242

# ── Parse polar file ─────────────────────────────────────────────────────────
rows = []
with open(POLAR_FILE) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('Surface') or line.startswith('Surf-') \
                or line.startswith('Beta') or line.startswith('Wake-'):
            continue
        # Replace -nan/nan with NaN
        line = re.sub(r'\s+-nan\b', ' nan', line)
        parts = line.split()
        if len(parts) < 23:
            continue
        try:
            rows.append([float(x) for x in parts[:23]])
        except ValueError:
            continue

data = np.array(rows)
aoa     = data[:, 2]
CLtot   = data[:, 6]
CDi_vlm = data[:, 8]
CDtot_vlm = data[:, 9]
CMytot  = data[:, 22]

# Total drag = VLM profile + body estimate
CD_total = CDtot_vlm + CD0_body
LD_total = np.where(CD_total > 1e-4, CLtot / CD_total, np.nan)

# ── Cruise condition ─────────────────────────────────────────────────────────
W      = 2600.0   # lbs
V_ktas = 155.0    # KTAS at sea level
rho_sl = 0.002377 # slug/ft³
V_fps  = V_ktas * 1.6878099   # kts → ft/s
q      = 0.5 * rho_sl * V_fps**2
CL_cr  = W / (q * Sref)
AR     = 30.0**2 / Sref          # 7.41
e      = 0.80
CDi_cr = CL_cr**2 / (math.pi * AR * e)
CD_cr  = CD0_body + CDi_cr
LD_cr  = CL_cr / CD_cr

# Alpha at cruise (interpolate from polar)
aoa_cr = float(np.interp(CL_cr, CLtot, aoa))

print(f"Parsed {len(rows)} alpha points")
print(f"CD0_body = {CD0_body:.5f}")
print(f"CL_cruise = {CL_cr:.4f}  at alpha ~ {aoa_cr:.2f} deg")
print(f"L/D cruise = {LD_cr:.2f}")
print(f"\nalpha     CL       CDi      CDtot    CD_total  L/D      CMy")
print(f"--------------------------------------------------------------")
for i in range(len(aoa)):
    print(f"{aoa[i]:6.1f}  {CLtot[i]:7.4f}  {CDi_vlm[i]:7.5f}  "
          f"{CDtot_vlm[i]:7.5f}  {CD_total[i]:7.5f}  {LD_total[i]:6.2f}  {CMytot[i]:7.4f}")

# ── Figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 11), facecolor='#1a1a2e')
gs  = gridspec.GridSpec(2, 3, figure=fig, hspace=0.42, wspace=0.38)
ax_polar   = fig.add_subplot(gs[0, 0])   # CL vs CD
ax_lift    = fig.add_subplot(gs[0, 1])   # CL vs alpha
ax_drag    = fig.add_subplot(gs[0, 2])   # Drag breakdown vs alpha
ax_ld      = fig.add_subplot(gs[1, 0])   # L/D vs alpha
ax_cm      = fig.add_subplot(gs[1, 1])   # CMy vs alpha
ax_text    = fig.add_subplot(gs[1, 2])   # Summary table

TEXT_C = '#e0e0e0'
GRID_C = '#333355'
ACCENT = '#4a90d9'
WARN_C = '#f39c12'
GOOD_C = '#27ae60'

for ax in [ax_polar, ax_lift, ax_drag, ax_ld, ax_cm, ax_text]:
    ax.set_facecolor('#0d0d1e')
    ax.tick_params(colors=TEXT_C, labelsize=8)
    ax.spines[:].set_color('#445')
    for lbl in (ax.get_xticklabels() + ax.get_yticklabels()):
        lbl.set_color(TEXT_C)
    ax.xaxis.label.set_color(TEXT_C)
    ax.yaxis.label.set_color(TEXT_C)
    ax.title.set_color(TEXT_C)
    ax.grid(True, color=GRID_C, alpha=0.6, linewidth=0.5)

# ── Panel 1: Drag polar CL vs CD ─────────────────────────────────────────────
ax_polar.plot(CDtot_vlm, CLtot, 'o--', color='#888', lw=1.2, ms=4, label='VLM only (no bodies)')
ax_polar.plot(CD_total,  CLtot, 'o-',  color=ACCENT, lw=2,   ms=5, label=f'Total (+ CD0={CD0_body:.4f})')
ax_polar.axvline(CD_cr, color=WARN_C, lw=1.2, ls='--', alpha=0.7)
ax_polar.axhline(CL_cr, color=WARN_C, lw=1.2, ls='--', alpha=0.7)
ax_polar.annotate(f'Cruise\nCL={CL_cr:.3f}\nCD={CD_cr:.4f}',
    xy=(CD_cr, CL_cr), xytext=(CD_cr+0.003, CL_cr-0.12),
    color=WARN_C, fontsize=7.5,
    arrowprops=dict(arrowstyle='->', color=WARN_C, lw=1))
ax_polar.set_xlabel('CD total', fontsize=9)
ax_polar.set_ylabel('CL', fontsize=9)
ax_polar.set_title('Drag Polar', fontsize=10, fontweight='bold')
ax_polar.legend(fontsize=7, facecolor='#1a1a2e', labelcolor=TEXT_C, edgecolor='#445')

# ── Panel 2: CL vs alpha ─────────────────────────────────────────────────────
ax_lift.plot(aoa, CLtot, 'o-', color=ACCENT, lw=2, ms=5)
ax_lift.axhline(CL_cr, color=WARN_C, lw=1.2, ls='--', alpha=0.7, label=f'CL cruise = {CL_cr:.3f}')
ax_lift.axvline(0, color='#445', lw=0.8)
ax_lift.set_xlabel('Alpha (deg)', fontsize=9)
ax_lift.set_ylabel('CL', fontsize=9)
ax_lift.set_title('Lift Curve', fontsize=10, fontweight='bold')
ax_lift.legend(fontsize=7, facecolor='#1a1a2e', labelcolor=TEXT_C, edgecolor='#445')

# ── Panel 3: Drag breakdown ───────────────────────────────────────────────────
CD0_line = np.full_like(aoa, CD0_body)
ax_drag.fill_between(aoa, 0,        CD0_line,  alpha=0.35, color='#e74c3c', label=f'CD0 bodies = {CD0_body:.4f}')
ax_drag.fill_between(aoa, CD0_line, CD_total,  alpha=0.40, color=ACCENT,    label='CDi VLM (induced)')
ax_drag.plot(aoa, CD_total, '-', color=TEXT_C, lw=1.5)
ax_drag.axvline(aoa_cr, color=WARN_C, lw=1.2, ls='--', alpha=0.7, label=f'α cruise={aoa_cr:.1f}°')
ax_drag.set_xlabel('Alpha (deg)', fontsize=9)
ax_drag.set_ylabel('CD', fontsize=9)
ax_drag.set_title('Drag Breakdown', fontsize=10, fontweight='bold')
ax_drag.legend(fontsize=7, facecolor='#1a1a2e', labelcolor=TEXT_C, edgecolor='#445')

# ── Panel 4: L/D vs alpha ─────────────────────────────────────────────────────
ax_ld.plot(aoa, LD_total, 'o-', color=GOOD_C, lw=2, ms=5)
ax_ld.axhline(14.0,  color='#e74c3c',  lw=1.2, ls='--', label='Target L/D = 14')
ax_ld.axhline(LD_cr, color=WARN_C, lw=1.2, ls=':', label=f'Cruise L/D = {LD_cr:.1f}')
ax_ld.axvline(aoa_cr, color=WARN_C, lw=0.8, ls='--', alpha=0.6)
ax_ld.set_xlabel('Alpha (deg)', fontsize=9)
ax_ld.set_ylabel('L/D', fontsize=9)
ax_ld.set_title('Lift-to-Drag Ratio', fontsize=10, fontweight='bold')
ax_ld.legend(fontsize=7, facecolor='#1a1a2e', labelcolor=TEXT_C, edgecolor='#445')

# ── Panel 5: CMy vs alpha ─────────────────────────────────────────────────────
ax_cm.plot(aoa, CMytot, 'o-', color='#c084fc', lw=2, ms=5)
ax_cm.axhline(0, color='#445', lw=0.8)
ax_cm.axvline(aoa_cr, color=WARN_C, lw=0.8, ls='--', alpha=0.6, label=f'α cruise={aoa_cr:.1f}°')
ax_cm.set_xlabel('Alpha (deg)', fontsize=9)
ax_cm.set_ylabel('CMy (pitch moment)', fontsize=9)
ax_cm.set_title('Pitching Moment', fontsize=10, fontweight='bold')
ax_cm.legend(fontsize=7, facecolor='#1a1a2e', labelcolor=TEXT_C, edgecolor='#445')

# ── Panel 6: Summary text ─────────────────────────────────────────────────────
ax_text.axis('off')
target_met = LD_cr >= 14.0
lines = [
    ('MAOS Aircraft — VSPAERO v1.3', TEXT_C, 10, 'bold'),
    ('Wing+Tails VLM + Body Swet Drag', '#888', 8, 'normal'),
    ('', TEXT_C, 7, 'normal'),
    (f'Reference:  Sref={Sref:.0f} ft²   AR={AR:.2f}   e={e:.2f}', TEXT_C, 8.5, 'normal'),
    (f'Mach 0.234   (155 KTAS SL)', TEXT_C, 8.5, 'normal'),
    ('', TEXT_C, 7, 'normal'),
    ('── Cruise (@ 2,600 lb MTOW) ──', '#aaa', 8.5, 'bold'),
    (f'CL_cruise   = {CL_cr:.4f}', TEXT_C, 8.5, 'normal'),
    (f'CDi_cruise  = {CDi_cr:.5f}', TEXT_C, 8.5, 'normal'),
    (f'CD0_bodies  = {CD0_body:.5f}', TEXT_C, 8.5, 'normal'),
    (f'   Pod  : Cf·FF·Swet/S = {CD_pod:.5f}', '#888', 7.5, 'normal'),
    (f'   Boom : Cf·FF·Swet/S = {CD_boom:.5f}', '#888', 7.5, 'normal'),
    (f'   Gear (fixed faired) = {CD_gear:.5f}', '#888', 7.5, 'normal'),
    (f'CD_total    = {CD_cr:.5f}', TEXT_C, 8.5, 'normal'),
    (f'L/D cruise  = {LD_cr:.2f}', GOOD_C if target_met else WARN_C, 9, 'bold'),
    ('', TEXT_C, 7, 'normal'),
    ('── Target ──', '#aaa', 8.5, 'bold'),
    (f'L/D = 14.0  (propulsion sizing)', '#888', 8, 'normal'),
    (f'Δ L/D = {LD_cr - 14.0:+.2f}  {"EXCEEDS target ✓" if target_met else "BELOW target ⚠"}',
     GOOD_C if target_met else '#e74c3c', 9, 'bold'),
    ('', TEXT_C, 7, 'normal'),
    ('NOTE: CG=0 (nose). CMy not trimmed.', WARN_C, 7.5, 'normal'),
    ('Pod/boom drag = Swet estimate only.', WARN_C, 7.5, 'normal'),
]
y = 0.97
for text, color, fs, weight in lines:
    ax_text.text(0.04, y, text, transform=ax_text.transAxes,
                 color=color, fontsize=fs, fontweight=weight, va='top')
    y -= 0.052 if fs >= 9 else 0.048 if fs >= 8 else 0.040

fig.suptitle(
    'MAOS Aircraft — First Aerodynamic Analysis  |  OpenVSP 3.48.2 VSPAERO 7.2.2  |  VLM + Swet Drag Estimate',
    color=TEXT_C, fontsize=11, fontweight='bold', y=0.995)

out = '/workspace/cad/maos_aircraft_polar.png'
plt.savefig(out, dpi=130, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'\nSaved: {out}')
