"""
MAOS Pod Occupant Study — Multi-Variant Generator
==================================================
Generates individual PNGs for several pod geometry variants,
plus a combined comparison sheet.

Variants:
  A  58"H / 4" floor  (baseline — shows headroom problem)
  B  60"H / 4" floor  (+2" pod height)
  C  62"H / 4" floor  (+4" pod height)
  D  58"H / 2" floor  (thinner floor structure)
  E  60"H / 2" floor  (recommended: +2"H + thin floor)

Each variant gets a full side-view + cross-section + summary PNG.
A final comparison sheet overlays all cross-sections side-by-side.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse
import matplotlib.lines as mlines
import numpy as np
import os

OUT_DIR = '/workspace/cad'

# ── Anthropometrics ──────────────────────────────────────────────────────────
# 95th %ile male (SAE J833 / NASA HDBK-3000) — most restrictive for headroom
M95 = dict(
    label='95th %ile male',
    seat_h=17.0, seated_h=38.0, torso_h=22.0, neck_h=3.0,
    shoulder_w=20.0, hip_w=16.5, head_w=6.5, head_d=8.0,
    knee_h=22.0, btk_knee=24.5,
)
# 5th %ile female — most restrictive for reach/forward visibility (bonus ref)
F05 = dict(
    label='5th %ile female',
    seat_h=17.0, seated_h=30.5, torso_h=17.0, neck_h=2.5,
    shoulder_w=14.0, hip_w=13.0, head_w=5.5, head_d=6.5,
    knee_h=17.5, btk_knee=20.0,
)

# ── Pod variants ─────────────────────────────────────────────────────────────
POD_L = 156.0
POD_W = 52.0

VARIANTS = [
    dict(id='A', pod_h=58.0, floor_z=4.0, label='Variant A\n58"H / 4" floor (baseline)'),
    dict(id='B', pod_h=60.0, floor_z=4.0, label='Variant B\n60"H / 4" floor (+2" height)'),
    dict(id='C', pod_h=62.0, floor_z=4.0, label='Variant C\n62"H / 4" floor (+4" height)'),
    dict(id='D', pod_h=58.0, floor_z=2.0, label='Variant D\n58"H / 2" floor (thinner floor)'),
    dict(id='E', pod_h=60.0, floor_z=2.0, label='Variant E — Recommended\n60"H / 2" floor'),
]

ROW_A_X = 38.0
ROW_B_X = 98.0
SEAT_DEPTH = 18.0

# ── Drawing helpers ──────────────────────────────────────────────────────────

def human_color(pct, male=True):
    if male:
        return '#2c6fad' if pct == 95 else '#5ba3e0'
    return '#c0392b' if pct == 5 else '#e07070'


def draw_human_side(ax, anthro, x_sb, floor_z, facing='right',
                    color='#2c6fad', alpha=0.82):
    d = 1 if facing == 'right' else -1
    a = anthro
    seat_z  = floor_z + a['seat_h']
    knee_x  = x_sb + d * a['btk_knee']
    knee_z  = floor_z + a['knee_h']
    foot_x  = x_sb + d * (a['btk_knee'] + 10)
    head_r  = a['head_w'] / 2
    head_cx = x_sb + d * 2.5
    head_cz = seat_z + a['torso_h'] + a['neck_h'] + head_r

    # Seat cushion
    ax.add_patch(patches.Rectangle(
        (min(x_sb, x_sb + d * SEAT_DEPTH), floor_z),
        SEAT_DEPTH, a['seat_h'],
        lw=0.8, ec='#666', fc='#d6e4f5', zorder=2))
    # Seatback
    ax.add_patch(patches.Rectangle(
        (x_sb - d*3, floor_z), 3, a['torso_h'] + 4,
        lw=0.8, ec='#666', fc='#d6e4f5', zorder=2))
    # Torso
    tw = 10
    ax.fill([x_sb, x_sb+d*tw, x_sb+d*(tw-2), x_sb+d*2, x_sb],
            [seat_z, seat_z, seat_z+a['torso_h'], seat_z+a['torso_h'], seat_z],
            color=color, alpha=alpha, zorder=3)
    # Head
    ax.add_patch(Ellipse(
        (head_cx, head_cz), a['head_d'], a['head_w'],
        fc=color, ec='#333', lw=0.7, alpha=alpha, zorder=4))
    # Thigh
    ax.fill([x_sb, knee_x, knee_x, x_sb, x_sb],
            [seat_z, knee_z, knee_z-5, seat_z-3, seat_z],
            color=color, alpha=alpha, zorder=3)
    # Shin
    ax.fill([knee_x, knee_x+d*2, foot_x+d*4, foot_x, knee_x],
            [knee_z, knee_z, floor_z+2, floor_z, knee_z],
            color=color, alpha=alpha, zorder=3)
    return seat_z + a['seated_h']   # returns top-of-head Z


def draw_human_front(ax, anthro, cy, floor_z, color='#2c6fad', alpha=0.82):
    a = anthro
    seat_z  = floor_z + a['seat_h']
    head_r  = a['head_w'] / 2
    head_cz = seat_z + a['torso_h'] + a['neck_h'] + head_r
    # Seat cushion
    ax.add_patch(patches.Rectangle(
        (cy - a['hip_w']/2, floor_z), a['hip_w'], a['seat_h'],
        lw=0.8, ec='#666', fc='#d6e4f5', zorder=2))
    # Torso (trapezoid)
    ax.fill(
        [cy - a['hip_w']/2, cy + a['hip_w']/2,
         cy + a['shoulder_w']/2, cy - a['shoulder_w']/2, cy - a['hip_w']/2],
        [seat_z, seat_z, seat_z + a['torso_h'],
         seat_z + a['torso_h'], seat_z],
        color=color, alpha=alpha, zorder=3)
    # Head
    ax.add_patch(Ellipse(
        (cy, head_cz), a['head_w'], a['head_w'],
        fc=color, ec='#333', lw=0.7, alpha=alpha, zorder=4))
    # Legs (sketchy blocks)
    for side in [-1, 1]:
        kx = cy + side * 7
        ax.fill([cy + side*4, cy + side*4, kx+side*4, kx+side*4],
                [seat_z, seat_z-4, floor_z + a['knee_h'], seat_z],
                color=color, alpha=alpha, zorder=3)


def dim_h(ax, x1, x2, y, label, color='#333', fs=8.5):
    ax.annotate('', xy=(x2,y), xytext=(x1,y),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.1))
    ax.text((x1+x2)/2, y+1.5, label, ha='center', va='bottom',
            fontsize=fs, color=color)

def dim_v(ax, x, z1, z2, label, color='#333', fs=8.5, side='right'):
    ax.annotate('', xy=(x,z2), xytext=(x,z1),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.1))
    off = 2.5 if side == 'right' else -2.5
    ha  = 'left' if side == 'right' else 'right'
    ax.text(x+off, (z1+z2)/2, label, ha=ha, va='center',
            fontsize=fs, color=color)


def clearance_color(margin):
    if margin >= 4:   return '#27ae60'   # green — comfortable
    if margin >= 1:   return '#f39c12'   # amber — tight
    return '#e74c3c'                     # red — fails


# ── Per-variant full figure ───────────────────────────────────────────────────

for v in VARIANTS:
    pid   = v['id']
    POD_H = v['pod_h']
    FLZ   = v['floor_z']
    lbl   = v['label']

    m = M95
    f = F05
    total_h_m = m['seat_h'] + m['seated_h']   # 55"
    usable    = POD_H - FLZ
    headroom  = usable - total_h_m

    fig = plt.figure(figsize=(20, 12), facecolor='#f8f9fa')
    hc  = clearance_color(headroom)

    fig.suptitle(
        f'MAOS Pressure Pod — Occupant Study  |  {lbl}\n'
        f'{POD_W:.0f}"W × {POD_H:.0f}"H × {POD_L:.0f}"L interior  |  '
        f'95th %ile male  |  headroom clearance: {headroom:+.1f}"',
        fontsize=13, fontweight='bold', y=0.98,
        color='#1a1a2e' if headroom >= 0 else '#c0392b')

    # ── Panel 1: Side view ────────────────────────────────────────────────────
    ax1 = fig.add_subplot(2, 2, (1,2))
    ax1.set_aspect('equal')
    ax1.set_title('Side View — Longitudinal Centreline Section', fontsize=10, pad=6)

    ax1.add_patch(patches.FancyBboxPatch(
        (0,0), POD_L, POD_H, boxstyle='round,pad=4',
        lw=2, ec='#1a1a2e', fc='#eef2f7', zorder=1))
    ax1.add_patch(patches.Rectangle(
        (8,0), POD_L-16, FLZ,
        lw=1, ec='#888', fc='#c0c4ce', zorder=2))

    # Row A — M95
    top_A = draw_human_side(ax1, m, ROW_A_X, FLZ, 'right', '#2c6fad')
    # Row B — M95
    top_B = draw_human_side(ax1, m, ROW_B_X, FLZ, 'right', '#1a6b4a')

    # Head-height line and pod ceiling
    ax1.hlines(total_h_m + FLZ, 20, POD_L-20,
               colors='#e74c3c', lw=1.5, ls='--', zorder=6,
               label=f'Top of head: {total_h_m+FLZ:.0f}" from pod bottom')
    ax1.hlines(POD_H, 20, POD_L-20,
               colors=hc, lw=1.8, ls=':', zorder=6,
               label=f'Pod ceiling: {POD_H:.0f}"  (clearance {headroom:+.1f}")')

    # Dimensions
    dim_h(ax1, 0, POD_L, POD_H+10, f'{POD_L:.0f}"  ({POD_L/12:.1f} ft)', '#1a1a2e', 10)
    dim_h(ax1, ROW_A_X, ROW_B_X, -8, f'{ROW_B_X-ROW_A_X:.0f}" row pitch', '#555')
    dim_v(ax1, POD_L+5, 0, POD_H, f'{POD_H:.0f}"', '#1a1a2e', 10)
    dim_v(ax1, POD_L+12, FLZ, FLZ+total_h_m, f'{total_h_m:.0f}" pax', '#2c6fad', 8)
    BTK_KN = m['btk_knee']
    if abs(headroom) > 0.3:
        dim_v(ax1, ROW_B_X+BTK_KN+14, FLZ+total_h_m, POD_H,
              f'{headroom:+.1f}"', hc, 8)

    ax1.text(ROW_A_X-2, -14, 'Row A  Pilot/Copilot', ha='left', fontsize=9,
             color='#2c6fad', fontweight='bold')
    ax1.text(ROW_B_X-2, -14, 'Row B  Rear Passengers', ha='left', fontsize=9,
             color='#1a6b4a', fontweight='bold')

    ax1.set_xlim(-15, POD_L+25)
    ax1.set_ylim(-20, POD_H+22)
    ax1.set_xlabel('Longitudinal (inches)', fontsize=9)
    ax1.set_ylabel('Vertical (inches)', fontsize=9)
    ax1.legend(fontsize=8, loc='lower right')
    ax1.grid(True, alpha=0.25)
    ax1.tick_params(labelsize=8)

    # ── Panel 2: Forward cross-section ───────────────────────────────────────
    ax2 = fig.add_subplot(2, 2, 3)
    ax2.set_aspect('equal')
    ax2.set_title(f'Forward Cross-Section  ({POD_W:.0f}"W × {POD_H:.0f}"H)', fontsize=10, pad=6)

    ax2.add_patch(Ellipse(
        (0, POD_H/2), POD_W, POD_H,
        lw=2.5, ec='#1a1a2e', fc='#eef2f7', zorder=1))
    ax2.add_patch(patches.Rectangle(
        (-POD_W/2+4, 0), POD_W-8, FLZ,
        lw=1, ec='#888', fc='#c0c4ce', zorder=2))

    # Two M95 seated side-by-side
    for cy, col in [(-POD_W/4, '#2c6fad'), (POD_W/4, '#2c6fad')]:
        draw_human_front(ax2, m, cy, FLZ, color=col, alpha=0.80)

    # Shoulder span
    ax2.hlines(FLZ+m['seat_h']+m['torso_h'],
               -m['shoulder_w'], m['shoulder_w'],
               colors='#e74c3c', lw=1.2, ls='--', zorder=7)
    dim_h(ax2, -m['shoulder_w'], m['shoulder_w'],
          FLZ+m['seat_h']+m['torso_h']+2,
          f'{m["shoulder_w"]*2:.0f}" 2× shoulders', '#e74c3c', 8)

    # Head-height line
    ax2.hlines(FLZ+total_h_m, -POD_W/2+3, POD_W/2-3,
               colors='#e74c3c', lw=1.5, ls='--', zorder=6)
    ax2.hlines(POD_H, -POD_W/2+3, POD_W/2-3,
               colors=hc, lw=1.8, ls=':', zorder=6)

    dim_h(ax2, -POD_W/2, POD_W/2, -8, f'{POD_W:.0f}" interior width', '#1a1a2e', 9)
    dim_v(ax2, POD_W/2+4, 0, POD_H, f'{POD_H:.0f}"H', '#1a1a2e', 9)
    dim_v(ax2, POD_W/2+11, FLZ, FLZ+total_h_m, f'{total_h_m:.0f}"', '#2c6fad', 8)
    dim_v(ax2, POD_W/2+18, FLZ+total_h_m, POD_H, f'{headroom:+.1f}"', hc, 9)

    ax2.set_xlim(-POD_W/2-20, POD_W/2+28)
    ax2.set_ylim(-12, POD_H+10)
    ax2.set_xlabel('Lateral (inches)', fontsize=9)
    ax2.set_ylabel('Vertical (inches)', fontsize=9)
    ax2.grid(True, alpha=0.25)
    ax2.tick_params(labelsize=8)

    # ── Panel 3: Summary table ────────────────────────────────────────────────
    ax3 = fig.add_subplot(2, 2, 4)
    ax3.axis('off')
    ax3.set_title('Clearance Summary', fontsize=10, pad=6)

    width_margin = POD_W - m['shoulder_w']*2

    rows = [
        ['Parameter',               'Needed',    'Available', 'Margin',              'OK?'],
        ['Vertical (floor→head)',    f'{total_h_m:.0f}"',
                                     f'{usable:.0f}"',
                                     f'{headroom:+.1f}"',
                                     '✓' if headroom >= 1 else '⚠'],
        ['Width (2× shoulder)',      f'{m["shoulder_w"]*2:.0f}"',
                                     f'{POD_W:.0f}"',
                                     f'{width_margin:+.1f}"',
                                     '✓' if width_margin >= 8 else '⚠'],
        ['Row pitch A→B',           '36" min',  f'{ROW_B_X-ROW_A_X:.0f}"',
                                     f'{ROW_B_X-ROW_A_X-36:.0f}"',  '✓'],
        ['Usable length (4 seats)', '130" est', f'{POD_L:.0f}"',
                                     f'{POD_L-130:.0f}"',            '✓'],
        ['Floor structure',         '—',        f'{FLZ:.0f}"',
                                     '—',                            '—'],
    ]

    rh, y0 = 0.12, 0.94
    for ri, row in enumerate(rows):
        bg = '#1a1a2e' if ri == 0 else ('#f0f4ff' if ri%2==0 else '#e8eff8')
        fc = 'white' if ri == 0 else '#1a1a2e'
        x0 = 0.02
        for ci, (cell, cw) in enumerate(zip(row, [0.38, 0.14, 0.14, 0.14, 0.10])):
            tc = fc
            if ci == 4 and ri > 0:
                tc = '#27ae60' if cell == '✓' else ('#e74c3c' if cell == '⚠' else '#999')
            if ci == 3 and ri == 1:   # headroom margin — colour by clearance
                tc = clearance_color(headroom)
            ax3.text(x0 + cw/2, y0 - ri*rh, cell,
                     ha='center', va='center', fontsize=9,
                     color=tc, fontweight='bold' if ri == 0 else 'normal',
                     transform=ax3.transAxes,
                     bbox=dict(boxstyle='round,pad=0.12', fc=bg, ec='none', alpha=0.9))
            x0 += cw

    # Verdict box
    if headroom >= 4:
        verdict, vc = 'COMFORTABLE — no changes needed', '#27ae60'
    elif headroom >= 1:
        verdict, vc = 'ACCEPTABLE — tight but workable', '#f39c12'
    elif headroom >= -0.5:
        verdict, vc = 'MARGINAL — review floor structure', '#e67e22'
    else:
        verdict, vc = 'FAILS — pod height must increase', '#e74c3c'

    ax3.text(0.5, y0 - len(rows)*rh - 0.06, verdict,
             ha='center', va='top', fontsize=10, fontweight='bold',
             color='white', transform=ax3.transAxes,
             bbox=dict(boxstyle='round,pad=0.4', fc=vc, ec='none'))

    notes = [
        f'Anthropometric basis: 95th %ile male — most restrictive case',
        f'50th %ile male seated height ≈ 34.5" → {POD_H - FLZ - (m["seat_h"]+34.5):+.1f}" clearance',
        f'5th %ile female seated height ≈ 30.5" → {POD_H - FLZ - (m["seat_h"]+30.5):+.1f}" clearance',
        f'Seat height 17" (standard aircraft bucket seat)',
        f'Pod cross-section: elliptical {POD_W:.0f}"W × {POD_H:.0f}"H',
    ]
    ny = y0 - len(rows)*rh - 0.20
    ax3.text(0.02, ny, 'Notes:', fontsize=8, fontweight='bold',
             color='#1a1a2e', transform=ax3.transAxes)
    for i, note in enumerate(notes):
        ax3.text(0.04, ny - (i+1)*0.075, f'• {note}', fontsize=7.5,
                 color='#444', transform=ax3.transAxes, va='top')

    plt.tight_layout(rect=[0,0,1,0.95])
    fname = os.path.join(OUT_DIR, f'maos_pod_{pid}.png')
    plt.savefig(fname, dpi=130, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f'Saved {fname}  |  headroom {headroom:+.1f}"  [{verdict.split("—")[0].strip()}]')


# ── Comparison overview — all cross-sections side-by-side ────────────────────
print('\nGenerating comparison overview...')

fig2, axes = plt.subplots(1, len(VARIANTS), figsize=(22, 9), facecolor='#f8f9fa')
fig2.suptitle(
    'MAOS Pressure Pod — Cross-Section Comparison  |  All Variants  |  95th %ile Male',
    fontsize=13, fontweight='bold', y=0.99, color='#1a1a2e')

max_h = max(v['pod_h'] for v in VARIANTS)

for ax, v in zip(axes, VARIANTS):
    POD_H = v['pod_h']
    FLZ   = v['floor_z']
    pid   = v['id']

    m = M95
    total_h_m = m['seat_h'] + m['seated_h']
    headroom  = POD_H - FLZ - total_h_m
    hc        = clearance_color(headroom)
    usable    = POD_H - FLZ

    # Pod ellipse
    ax.add_patch(Ellipse(
        (0, POD_H/2), POD_W, POD_H,
        lw=2.5, ec='#1a1a2e', fc='#eef2f7', zorder=1))
    # Floor
    ax.add_patch(patches.Rectangle(
        (-POD_W/2+4, 0), POD_W-8, FLZ,
        lw=1, ec='#888', fc='#c0c4ce', zorder=2))

    # Two passengers
    for cy in [-POD_W/4, POD_W/4]:
        draw_human_front(ax, m, cy, FLZ, color='#2c6fad', alpha=0.80)

    # Reference lines
    ax.hlines(FLZ+total_h_m, -POD_W/2+3, POD_W/2-3,
              colors='#e74c3c', lw=1.5, ls='--', zorder=6)
    ax.hlines(POD_H, -POD_W/2+3, POD_W/2-3,
              colors=hc, lw=2.0, ls=':', zorder=6)

    # Headroom arrow + label
    if abs(headroom) > 0.2:
        ax.annotate('', xy=(POD_W/2-4, POD_H),
                    xytext=(POD_W/2-4, FLZ+total_h_m),
                    arrowprops=dict(arrowstyle='<->', color=hc, lw=1.5))
        ax.text(POD_W/2-3, (POD_H + FLZ+total_h_m)/2, f'{headroom:+.1f}"',
                ha='left', va='center', fontsize=9, color=hc, fontweight='bold')

    ax.set_aspect('equal')
    ax.set_xlim(-POD_W/2-8, POD_W/2+14)
    ax.set_ylim(-6, max_h+8)
    ax.grid(True, alpha=0.2)
    ax.tick_params(labelsize=7)
    ax.set_xlabel('Lateral (in)', fontsize=8)
    ax.set_ylabel('Vertical (in)' if ax == axes[0] else '', fontsize=8)

    if headroom >= 4:   vstatus, vc = 'COMFORTABLE', '#27ae60'
    elif headroom >= 1: vstatus, vc = 'ACCEPTABLE',  '#f39c12'
    elif headroom >= -0.5: vstatus, vc = 'MARGINAL',  '#e67e22'
    else:               vstatus, vc = 'FAILS',        '#e74c3c'

    ax.set_title(
        f'Variant {pid}\n{POD_W:.0f}"W × {POD_H:.0f}"H  /  {FLZ:.0f}" floor',
        fontsize=9, fontweight='bold', pad=4)
    ax.text(0.5, -0.13, vstatus, transform=ax.transAxes,
            ha='center', fontsize=9, fontweight='bold',
            color='white',
            bbox=dict(boxstyle='round,pad=0.3', fc=vc, ec='none'))

plt.tight_layout(rect=[0,0,1,0.95])
comp_path = os.path.join(OUT_DIR, 'maos_pod_comparison.png')
plt.savefig(comp_path, dpi=130, bbox_inches='tight', facecolor=fig2.get_facecolor())
plt.close()
print(f'Saved {comp_path}')
print('\nDone.')
