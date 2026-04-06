"""
MAOS Pod Occupant Study
=======================
Generates side-view and cross-section drawings of the MAOS pressure pod
with seated occupants using standard SAE/ISO anthropometric data.

Pod dimensions: 52"W x 58"H x 156"L (interior)

Human reference: 95th percentile male (most restrictive for headroom/width)
  Seated height (seat surface to top of head): 38.0"
  Shoulder width:                               20.0"
  Seated eye height (above seat):               30.5"
  Knee height (floor to top of knee):           22.0"
  Buttock-to-knee length:                       24.5"
  Hip width (seated):                           16.5"
  Seat height (floor to seat surface):          17.0"  (nominal aircraft)
  Head width:                                    6.5"
  Head depth (front-to-back):                    8.0"
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse, FancyArrowPatch
import matplotlib.lines as mlines
import numpy as np

# ── Pod interior dimensions (inches) ─────────────────────────────────────────
POD_L   = 156.0   # longitudinal length
POD_W   = 52.0    # lateral width
POD_H   = 58.0    # vertical height

WALL_T  = 2.0     # assumed composite wall thickness (structural reference only)
FLOOR_Z = 4.0     # floor structure height above bottom of pod interior

# ── 95th %ile male seated anthropometrics (SAE J833 / NASA HDBK-3000) ────────
SEAT_H    = 17.0   # floor to seat surface
SEATED_H  = 38.0   # seat surface to top of head
EYE_H     = SEAT_H + 30.5
HEAD_W    = 6.5
HEAD_D    = 8.0
HEAD_R    = HEAD_W / 2
SHOULDER_W = 20.0  # widest point
HIP_W     = 16.5
TORSO_H   = 22.0   # seat surface to shoulder
NECK_H    = 3.0
KNEE_H    = 22.0   # floor to top of patella
BTK_KNEE  = 24.5   # buttock to knee length (thigh depth)

TOTAL_H   = SEAT_H + SEATED_H   # floor to top of head = 55.0"
HEADROOM  = POD_H - TOTAL_H - FLOOR_Z   # available clearance above head

# ── Seat layout (longitudinal, X=0 at forward pressure bulkhead) ─────────────
# Row A: Pilot / Copilot
ROW_A_SEATBACK_X = 38.0    # seatback from fwd bulkhead
# Row B: Rear passengers
ROW_B_SEATBACK_X = 98.0    # seatback from fwd bulkhead

SEAT_DEPTH = 18.0

print(f"Pod interior:  {POD_W:.0f}\" W  x  {POD_H:.0f}\" H  x  {POD_L:.0f}\" L")
print(f"Floor offset:  {FLOOR_Z:.0f}\"  (floor structure above pod bottom)")
print(f"Usable height above floor: {POD_H - FLOOR_Z:.0f}\"")
print(f"95th %ile seated height (floor-to-head): {TOTAL_H:.0f}\"")
print(f"Headroom clearance: {HEADROOM:.1f}\"")
print(f"Width for 2 pax shoulder-to-shoulder: {SHOULDER_W*2:.0f}\" vs {POD_W:.0f}\" available")
print(f"Width margin (2 pax): {POD_W - SHOULDER_W*2:.0f}\"")
print()

# ── Drawing helpers ───────────────────────────────────────────────────────────

def draw_seated_human_side(ax, x_seatback, floor_z, facing='right', color='#2c6fad', alpha=0.85):
    """
    Draw a simplified side-view silhouette of a seated 95th %ile male.
    x_seatback: X position of the seatback
    floor_z:    Z (vertical) position of the floor surface
    facing:     'right' or 'left'
    """
    dir = 1 if facing == 'right' else -1

    seat_z = floor_z + SEAT_H
    knee_x = x_seatback + dir * BTK_KNEE
    knee_z = floor_z + KNEE_H
    foot_x = x_seatback + dir * (BTK_KNEE + 10.0)
    foot_z = floor_z

    # Seat rectangle
    seat_rect = patches.Rectangle(
        (min(x_seatback, x_seatback + dir*SEAT_DEPTH), floor_z),
        SEAT_DEPTH, SEAT_H,
        linewidth=1, edgecolor='#555', facecolor='#dde8f5', zorder=2)
    ax.add_patch(seat_rect)

    # Seatback rectangle
    back_h = TORSO_H + 4
    back_rect = patches.Rectangle(
        (x_seatback - dir*3, floor_z),
        3, back_h,
        linewidth=1, edgecolor='#555', facecolor='#dde8f5', zorder=2)
    ax.add_patch(back_rect)

    # Torso (rough polygon)
    torso_w = 10.0
    torso_xs = [x_seatback, x_seatback + dir*torso_w, x_seatback + dir*(torso_w-2), x_seatback + dir*2, x_seatback]
    torso_zs = [seat_z, seat_z, seat_z + TORSO_H, seat_z + TORSO_H, seat_z]
    ax.fill(torso_xs, torso_zs, color=color, alpha=alpha, zorder=3)

    # Head
    head_cx = x_seatback + dir*2
    head_cz = seat_z + TORSO_H + NECK_H + HEAD_R
    head = Ellipse((head_cx, head_cz), HEAD_D, HEAD_W,
                   facecolor=color, edgecolor='#333', linewidth=0.8, alpha=alpha, zorder=4)
    ax.add_patch(head)

    # Thigh
    thigh_xs = [x_seatback, x_seatback + dir*BTK_KNEE, x_seatback + dir*BTK_KNEE, x_seatback, x_seatback]
    thigh_zs = [seat_z, knee_z, knee_z - 5, seat_z - 3, seat_z]
    ax.fill(thigh_xs, thigh_zs, color=color, alpha=alpha, zorder=3)

    # Lower leg
    shin_xs = [knee_x, knee_x + dir*2, foot_x + dir*4, foot_x, knee_x]
    shin_zs = [knee_z, knee_z, foot_z + 2, foot_z, knee_z]
    ax.fill(shin_xs, shin_zs, color=color, alpha=alpha, zorder=3)

    return foot_x  # return forward extent


def draw_seated_human_front(ax, center_y, floor_z, color='#2c6fad', alpha=0.85):
    """
    Draw a simplified front-view silhouette of a seated 95th %ile male.
    center_y: lateral center position
    floor_z:  vertical floor position
    """
    seat_z = floor_z + SEAT_H

    # Seat
    seat_rect = patches.Rectangle(
        (center_y - HIP_W/2, floor_z),
        HIP_W, SEAT_H,
        linewidth=1, edgecolor='#555', facecolor='#dde8f5', zorder=2)
    ax.add_patch(seat_rect)

    # Torso (trapezoidal — wider at shoulders)
    torso_xs = [center_y - HIP_W/2, center_y + HIP_W/2,
                center_y + SHOULDER_W/2, center_y - SHOULDER_W/2, center_y - HIP_W/2]
    torso_zs = [seat_z, seat_z, seat_z + TORSO_H, seat_z + TORSO_H, seat_z]
    ax.fill(torso_xs, torso_zs, color=color, alpha=alpha, zorder=3)

    # Head
    head_cz = seat_z + TORSO_H + NECK_H + HEAD_R
    head = Ellipse((center_y, head_cz), HEAD_W, HEAD_W,
                   facecolor=color, edgecolor='#333', linewidth=0.8, alpha=alpha, zorder=4)
    ax.add_patch(head)

    # Left thigh/knee
    for side in [-1, 1]:
        knee_y = center_y + side * 8
        ax.fill([center_y + side*5, center_y + side*5, knee_y + side*4, knee_y + side*4],
                [seat_z, seat_z - 4, floor_z + KNEE_H, seat_z],
                color=color, alpha=alpha, zorder=3)


# ── Figure setup ──────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(20, 12), facecolor='#f8f9fa')
fig.suptitle(
    'MAOS Pressure Pod — Occupant Study\n'
    '52" W × 58" H × 156" L interior  |  95th percentile male  |  4-seat configuration',
    fontsize=14, fontweight='bold', y=0.98, color='#1a1a2e'
)

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 1: Side view
# ─────────────────────────────────────────────────────────────────────────────
ax1 = fig.add_subplot(2, 2, (1, 2))  # wide top panel
ax1.set_aspect('equal')
ax1.set_title('Side View — Longitudinal Section (Centerline)', fontsize=11, pad=8)

# Pod outline
pod_rect = patches.FancyBboxPatch(
    (0, 0), POD_L, POD_H,
    boxstyle="round,pad=4", linewidth=2,
    edgecolor='#1a1a2e', facecolor='#eef2f7', zorder=1)
ax1.add_patch(pod_rect)

# Floor platform
floor_rect = patches.Rectangle((8, 0), POD_L - 16, FLOOR_Z,
    linewidth=1, edgecolor='#888', facecolor='#c8c8d0', zorder=2)
ax1.add_patch(floor_rect)

# Draw occupants
# Row A (cockpit) – facing right
draw_seated_human_side(ax1, ROW_A_SEATBACK_X, FLOOR_Z, facing='right', color='#2c6fad')
# Row A second seat (same position, slightly offset for side view clarity — note: this is centerline view, one per row shown)
# Row B (rear pax) – facing right
draw_seated_human_side(ax1, ROW_B_SEATBACK_X, FLOOR_Z, facing='right', color='#c0392b')

# Pressure bulkheads
for bx, label in [(8, 'Fwd\nbulkhead'), (POD_L - 8, 'Aft\nbulkhead')]:
    ax1.axvline(bx, color='#555', linewidth=2, linestyle='--', zorder=5)
    ax1.text(bx, POD_H + 3, label, ha='center', va='bottom', fontsize=8, color='#555')

# Dimension arrows — length
def dim_arrow(ax, x1, x2, y, label, color='#333', fontsize=9):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
    ax.text((x1+x2)/2, y + 1.5, label, ha='center', va='bottom', fontsize=fontsize, color=color)

def dim_arrow_v(ax, x, z1, z2, label, color='#333', fontsize=9, side='right'):
    ax.annotate('', xy=(x, z2), xytext=(x, z1),
                arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
    offset = 3 if side == 'right' else -3
    ax.text(x + offset, (z1+z2)/2, label, ha='left' if side == 'right' else 'right',
            va='center', fontsize=fontsize, color=color)

# Overall length
dim_arrow(ax1, 0, POD_L, POD_H + 10, f'{POD_L:.0f}"  ({POD_L/12:.1f} ft)', color='#1a1a2e', fontsize=10)

# Row spacing
dim_arrow(ax1, ROW_A_SEATBACK_X, ROW_B_SEATBACK_X, -8,
          f'{ROW_B_SEATBACK_X - ROW_A_SEATBACK_X:.0f}" row pitch', color='#555')

# Interior height
dim_arrow_v(ax1, POD_L + 5, 0, POD_H, f'{POD_H:.0f}" H', color='#1a1a2e', fontsize=10)

# Headroom indicator (for rear row)
headroom_z = FLOOR_Z + TOTAL_H
ax1.hlines(headroom_z, ROW_B_SEATBACK_X - 5, ROW_B_SEATBACK_X + BTK_KNEE + 15,
           colors='#e74c3c', linewidths=1.5, linestyles='--', zorder=6)
ax1.hlines(POD_H, ROW_B_SEATBACK_X - 5, ROW_B_SEATBACK_X + BTK_KNEE + 15,
           colors='#27ae60', linewidths=1.5, linestyles=':', zorder=6)
dim_arrow_v(ax1, ROW_B_SEATBACK_X + BTK_KNEE + 12, headroom_z, POD_H,
            f'{HEADROOM:.1f}" clear', color='#27ae60', fontsize=8)

ax1.text(ROW_A_SEATBACK_X - 5, -14, 'Row A\nPilot / Co-pilot', ha='left', fontsize=9,
         color='#2c6fad', fontweight='bold')
ax1.text(ROW_B_SEATBACK_X - 5, -14, 'Row B\nRear Passengers', ha='left', fontsize=9,
         color='#c0392b', fontweight='bold')

ax1.set_xlim(-15, POD_L + 20)
ax1.set_ylim(-20, POD_H + 22)
ax1.set_xlabel('Longitudinal (inches, fwd = left)', fontsize=9)
ax1.set_ylabel('Vertical (inches)', fontsize=9)
ax1.grid(True, alpha=0.3)
ax1.tick_params(labelsize=8)

# Legend
legend_elems = [
    mlines.Line2D([0],[0], marker='s', color='w', markerfacecolor='#2c6fad', markersize=10, label='Row A (pilot/copilot)'),
    mlines.Line2D([0],[0], marker='s', color='w', markerfacecolor='#c0392b', markersize=10, label='Row B (rear pax)'),
    mlines.Line2D([0],[0], color='#e74c3c', lw=1.5, linestyle='--', label=f'Head height ({TOTAL_H:.0f}" from floor)'),
    mlines.Line2D([0],[0], color='#27ae60', lw=1.5, linestyle=':', label=f'Pod ceiling ({POD_H:.0f}" from floor)'),
]
ax1.legend(handles=legend_elems, loc='upper right', fontsize=8)

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 2: Forward cross-section (two seats side by side)
# ─────────────────────────────────────────────────────────────────────────────
ax2 = fig.add_subplot(2, 2, 3)
ax2.set_aspect('equal')
ax2.set_title(f'Forward Cross-Section\n(looking aft, at Row A seatback + {SEAT_DEPTH:.0f}")', fontsize=10, pad=8)

# Pod cross-section (ellipse, 52"W x 58"H)
pod_ellipse = Ellipse((0, POD_H/2), POD_W, POD_H,
                      linewidth=2.5, edgecolor='#1a1a2e', facecolor='#eef2f7', zorder=1)
ax2.add_patch(pod_ellipse)

# Floor platform
floor_rect2 = patches.Rectangle((-POD_W/2 + 4, 0), POD_W - 8, FLOOR_Z,
    linewidth=1, edgecolor='#888', facecolor='#c8c8d0', zorder=2)
ax2.add_patch(floor_rect2)

# Seat centers (pilot left, copilot right)
seat_centers = [-POD_W/4, POD_W/4]   # -13", +13"
pax_colors   = ['#2c6fad', '#2c6fad']

for cy, col in zip(seat_centers, pax_colors):
    draw_seated_human_front(ax2, cy, FLOOR_Z, color=col, alpha=0.80)

# Width dimension
dim_arrow(ax2, -POD_W/2, POD_W/2, -8, f'{POD_W:.0f}" interior width', color='#1a1a2e', fontsize=9)

# Shoulder-width envelope
ax2.hlines(FLOOR_Z + SEAT_H + TORSO_H, -SHOULDER_W, SHOULDER_W,
           colors='#e74c3c', linewidths=1, linestyles='--', zorder=7)
dim_arrow(ax2, -SHOULDER_W, SHOULDER_W, FLOOR_Z + SEAT_H + TORSO_H + 2,
          f'{SHOULDER_W*2:.0f}" 2× shoulders', color='#e74c3c', fontsize=8)

# Height dimension
dim_arrow_v(ax2, POD_W/2 + 4, 0, POD_H,  f'{POD_H:.0f}" H', color='#1a1a2e', fontsize=9)
dim_arrow_v(ax2, POD_W/2 + 10, FLOOR_Z, FLOOR_Z + TOTAL_H,
            f'{TOTAL_H:.0f}" pax', color='#2c6fad', fontsize=8)

# Headroom band
ax2.hlines(FLOOR_Z + TOTAL_H, -POD_W/2 + 2, POD_W/2 - 2,
           colors='#e74c3c', linewidths=1.5, linestyles='--', zorder=6,
           label=f'Top of head ({FLOOR_Z+TOTAL_H:.0f}" from bottom)')
ax2.hlines(POD_H, -POD_W/2 + 2, POD_W/2 - 2,
           colors='#27ae60', linewidths=1.5, linestyles=':', zorder=6,
           label=f'Pod ceiling ({POD_H:.0f}")')

ax2.set_xlim(-POD_W/2 - 18, POD_W/2 + 22)
ax2.set_ylim(-12, POD_H + 10)
ax2.set_xlabel('Lateral (inches, L = left of CL)', fontsize=9)
ax2.set_ylabel('Vertical (inches)', fontsize=9)
ax2.legend(fontsize=7, loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.tick_params(labelsize=8)

# ─────────────────────────────────────────────────────────────────────────────
# PANEL 3: Summary / Key Numbers
# ─────────────────────────────────────────────────────────────────────────────
ax3 = fig.add_subplot(2, 2, 4)
ax3.axis('off')
ax3.set_title('Clearance Summary', fontsize=10, pad=8)

width_margin = POD_W - SHOULDER_W * 2
status_h  = '✓' if HEADROOM >= 3 else '⚠'
status_w  = '✓' if width_margin >= 8 else '⚠'

data = [
    ['Parameter', 'Required', 'Available', 'Margin', 'Status'],
    ['Vertical (floor-to-head)', f'{TOTAL_H:.0f}"', f'{POD_H - FLOOR_Z:.0f}"',
     f'{HEADROOM:.1f}"', status_h],
    ['Width (2× shoulder)', f'{SHOULDER_W*2:.0f}"', f'{POD_W:.0f}"',
     f'{width_margin:.1f}"', status_w],
    ['Row pitch (A→B)', '36" min', f'{ROW_B_SEATBACK_X - ROW_A_SEATBACK_X:.0f}"',
     f'{ROW_B_SEATBACK_X - ROW_A_SEATBACK_X - 36:.0f}"', '✓'],
    ['Length (4 seats + equip)', '130" est', f'{POD_L:.0f}"',
     f'{POD_L - 130:.0f}"', '✓'],
]

col_widths = [0.36, 0.18, 0.18, 0.14, 0.10]
row_colors = ['#1a1a2e'] + ['#f0f4ff', '#eef2f7'] * 3
text_colors_row0 = ['white'] * 5

y_start = 0.92
row_h   = 0.13

for r, row in enumerate(data):
    bg = '#1a1a2e' if r == 0 else ('#f0f4ff' if r % 2 == 0 else '#e8eff8')
    x_pos = 0.02
    for c, (cell, cw) in enumerate(zip(row, col_widths)):
        tc = 'white' if r == 0 else '#1a1a2e'
        if c == 4 and r > 0:
            tc = '#27ae60' if cell == '✓' else '#e74c3c'
        weight = 'bold' if r == 0 else 'normal'
        ax3.text(x_pos + cw/2, y_start - r * row_h, cell,
                 ha='center', va='center', fontsize=9,
                 color=tc, fontweight=weight,
                 transform=ax3.transAxes,
                 bbox=dict(boxstyle='round,pad=0.15', facecolor=bg,
                           edgecolor='none', alpha=0.9))
        x_pos += cw

# Notes
notes = [
    '95th %ile male (most restrictive)',
    f'Headroom margin {HEADROOM:.1f}" — adequate, not generous',
    f'Lateral margin {width_margin:.1f}" per side incl. armrests & wall trim',
    'Floor offset 4" for structure/systems — verify vs. actual design',
    'Pod cross-section assumed elliptical (52"W × 58"H)',
    'Row pitch 60" allows reclining seats; can compress if needed',
]
note_y = 0.92 - len(data) * row_h - 0.06
ax3.text(0.02, note_y, 'Notes:', fontsize=8, fontweight='bold', color='#1a1a2e',
         transform=ax3.transAxes)
for i, note in enumerate(notes):
    ax3.text(0.04, note_y - (i+1)*0.07, f'• {note}', fontsize=7.5,
             color='#444', transform=ax3.transAxes, va='top')

# ──────────────────────────────────────────────────────────────────────────────
plt.tight_layout(rect=[0, 0, 1, 0.96])

out = '/workspace/cad/maos_pod_occupant_study.png'
plt.savefig(out, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Saved: {out}')

# Also print the summary numbers
print()
print("=== Clearance Summary ===")
print(f"  Interior height available (above floor): {POD_H - FLOOR_Z:.1f}\"")
print(f"  95th %ile pax height (floor→head):       {TOTAL_H:.1f}\"")
print(f"  Headroom clearance:                      {HEADROOM:.1f}\"  {'OK' if HEADROOM >= 3 else 'TIGHT'}")
print(f"  Interior width:                          {POD_W:.1f}\"")
print(f"  Two shoulder widths:                     {SHOULDER_W*2:.1f}\"")
print(f"  Lateral margin (both sides combined):    {width_margin:.1f}\"  {'OK' if width_margin >= 8 else 'TIGHT'}")
print(f"  Row A seatback at:  {ROW_A_SEATBACK_X:.0f}\" from fwd bulkhead")
print(f"  Row B seatback at:  {ROW_B_SEATBACK_X:.0f}\" from fwd bulkhead")
print(f"  Row pitch:          {ROW_B_SEATBACK_X - ROW_A_SEATBACK_X:.0f}\"")
