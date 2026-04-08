"""
MAOS Pod Human Sizing Visualization
Shows 95th-percentile male seated figures (tandem layout) against pod cross-section.
Output: /workspace/cad/maos_pod_human_sizing.png
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse, FancyArrowPatch
import numpy as np

# ── Anthropometric data: 95th-percentile male (SAE J833 / FAR Part 23 design basis) ──
# All dimensions in inches

# Seated posture measurements (from seat bottom datum = 0)
SEATED_HT        = 37.4   # seat bottom to top of head
EYE_HT           = 31.2   # seat bottom to eye level
SHOULDER_HT      = 24.8   # seat bottom to shoulder / acromion
ELBOW_HT         = 9.5    # seat bottom to elbow (arm at rest)
HIP_W            = 16.8   # hip breadth seated
SHOULDER_W       = 20.8   # bideltoid (shoulder) breadth
HEAD_W           = 6.2    # head width
HEAD_HT          = 9.5    # head height

# Leg geometry (seated, legs forward to pedals)
POPLITEAL_HT     = 17.2   # floor to underside of knee
BUTTOCK_KNEE     = 24.4   # horizontal: seat back to front of knee
FOOT_LENGTH      = 11.0   # foot length for pedal reach estimate
THIGH_CLR        = 5.5    # seat surface to top of thigh (clearance needed)

# ── Pod geometry ──────────────────────────────────────────────────────────────
# Script parameters: outer dimensions (these are the OpenVSP ellipse dims)
# Article states "52" W × 58" H interior" — we plot the outer profile.
POD_OD_W_IN  = 52.0    # outer width (4.333 ft)
POD_OD_H_IN  = 58.0    # outer height (4.833 ft)
SHELL_T      =  1.5    # approx composite shell + insulation, inches
INT_W        = POD_OD_W_IN - 2 * SHELL_T   # 49.0"
INT_H        = POD_OD_H_IN - 2 * SHELL_T   # 55.0"
POD_L_IN     = 168.0   # 14 ft total length

# ── Cabin layout ──────────────────────────────────────────────────────────────
# Origin at pod nose tip.  X positive aft.  Z positive up.
# Pod centerline is at Z = 0.  Floor is ~11" below centerline (rough estimate):
#   inner radius at max section ≈ 27.5", seat pan sits on floor which is at -11" from CL
FLOOR_Z      = -11.0   # floor height relative to pod CL, inches

# Station cutoffs
X_NOSE_DOME   =  24.0  # nose pressure dome ends
X_INSTR_PANEL =  34.0  # instrument panel
X_FWD_PEDALS  =  44.0  # front pedal face (ahead of seat by ~18")
X_FWD_SEAT    =  62.0  # front seat bottom X
X_SEAT_PITCH  =  42.0  # tandem seat pitch
X_AFT_SEAT    = X_FWD_SEAT + X_SEAT_PITCH  # = 104.0"
X_AFT_DOME    = 152.0  # aft pressure dome begins
X_TAIL_END    = POD_L_IN  # 168.0"

# ── Helper: draw a stick-figure seated pilot ──────────────────────────────────
def draw_pilot(ax, seat_x, color='#e8c46a', label=None):
    """
    Draw a simplified seated humanoid silhouette.
    seat_x: X position of seat bottom center (seat pan).
    The figure sits with back roughly vertical (forward seat-back at seat_x - 5").
    """
    # seat bottom datum
    sx = seat_x
    sz = FLOOR_Z     # seat pan on floor

    # torso bottom -> shoulder
    torso_bot_x = sx
    torso_bot_z = sz
    torso_top_x = sx - 1.5   # slight backward lean
    torso_top_z = sz + SHOULDER_HT

    # head center
    head_cx = torso_top_x
    head_cz = torso_top_z + HEAD_HT * 0.5 + 0.5

    # arm (elbow down, showing arm at rest)
    elbow_x = sx + 4.0
    elbow_z = sz + ELBOW_HT

    # thigh (horizontal from seat, knee at front)
    knee_x = sx + BUTTOCK_KNEE
    knee_z = sz + THIGH_CLR

    # lower leg (vertical down from knee to floor)
    foot_x = knee_x + 3.0
    foot_z = FLOOR_Z

    kw = dict(color=color, linewidth=2.5, solid_capstyle='round')

    # torso
    ax.plot([torso_bot_x, torso_top_x], [torso_bot_z, torso_top_z], **kw)
    # head (ellipse)
    head = Ellipse((head_cx, head_cz), HEAD_W, HEAD_HT, color=color, zorder=5)
    ax.add_patch(head)
    # upper arm stub
    ax.plot([torso_top_x, elbow_x], [torso_top_z - 4, elbow_z], **kw)
    # thigh
    ax.plot([sx, knee_x], [sz + THIGH_CLR, knee_z], **kw)
    # shin
    ax.plot([knee_x, foot_x], [knee_z, foot_z], **kw)
    # foot
    ax.plot([foot_x, foot_x + FOOT_LENGTH], [foot_z, foot_z], **kw)

    # eye reference dashed line
    eye_z = sz + EYE_HT
    ax.plot([torso_top_x - 2, torso_top_x + 14],
            [eye_z, eye_z],
            color=color, linewidth=0.8, linestyle='--', alpha=0.5)

    if label:
        ax.text(sx + 2, sz - 4, label, color=color, fontsize=7, ha='center')

    return sz + SEATED_HT  # top-of-head Z for clearance check


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE
# ═══════════════════════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(20, 9), facecolor='#12121e')
fig.suptitle(
    'MAOS Pod — Human Sizing  |  95th-Percentile Male  |  POD: 52"W × 58"H outer / 14 ft long',
    color='white', fontsize=13, fontweight='bold', y=0.98)

# ── LEFT PANEL: Side view (XZ) ────────────────────────────────────────────────
ax1 = fig.add_subplot(1, 2, 1, facecolor='#1a1a2e')
ax1.set_title('Side View — Tandem Seating Layout', color='white', fontsize=11, pad=8)

# Pod outer profile (simplified: rectangular top, curved bottom ellipse-ish)
# Model the pod side profile as an ellipse for the upper lobe and lower lobe
# At max section (30% = 50.4" from nose): half-height up = 29", half-height down = 29"
# Approximate the side silhouette as an oval
from matplotlib.patches import FancyBboxPatch

# Draw pod outline using a simple poly approximation of the side view:
# Nose: tapered to X=0
# Max section runs from ~30" to ~105" (between XSec_1 and near XSec_2)
# Aft taper from ~105" to 168"
# Top is roughly flat; bottom tapers up toward boom at 168".

pod_top_z    = POD_OD_H_IN / 2   # +29"
pod_bot_z    = -POD_OD_H_IN / 2  # -29"

# Build side silhouette polygon (rough shape)
top_pts_x = [0, 18, 50, 105, 152, 168]
top_pts_z = [0,  22,  pod_top_z, pod_top_z,  20, 12]  # top flattens, aft tapers slightly
bot_pts_x = [0, 18, 50, 105, 152, 168]
# aft bottom curves up toward boom (ZLocPercent = 0.0918 * 14ft * 12 = 15.4" above CL at X=168)
aft_tail_z = 0.0918 * POD_L_IN  # ~15.4" above CL at tail end
bot_pts_z = [0, -18, pod_bot_z, pod_bot_z, -10, aft_tail_z]

outline_x = top_pts_x + list(reversed(bot_pts_x))
outline_z = top_pts_z + list(reversed(bot_pts_z))

pod_poly = plt.Polygon(list(zip(outline_x, outline_z)),
                        closed=True,
                        facecolor='#1e3a5f', edgecolor='#4a90d9',
                        linewidth=1.5, alpha=0.7, zorder=1)
ax1.add_patch(pod_poly)

# Floor line
ax1.axhline(FLOOR_Z, xmin=X_NOSE_DOME/POD_L_IN, xmax=X_AFT_DOME/POD_L_IN,
            color='#aaaaaa', linewidth=1.0, linestyle=':', alpha=0.7)
ax1.text(X_NOSE_DOME + 4, FLOOR_Z - 3.5, 'floor', color='#aaaaaa', fontsize=7)

# Instrument panel
ax1.plot([X_INSTR_PANEL, X_INSTR_PANEL], [FLOOR_Z, 15],
         color='#888888', linewidth=1.5, linestyle='-')

# Seat pans
for sx in [X_FWD_SEAT, X_AFT_SEAT]:
    ax1.add_patch(patches.FancyBboxPatch(
        (sx - 10, FLOOR_Z - 3), 20, 3,
        boxstyle="round,pad=0.5",
        facecolor='#555577', edgecolor='#9999bb', linewidth=1, zorder=3))

# Draw pilots
head_z_fwd = draw_pilot(ax1, X_FWD_SEAT, color='#e8c46a', label='Pilot (FWD)')
head_z_aft = draw_pilot(ax1, X_AFT_SEAT, color='#6ae8c4', label='Pilot (AFT)')

# Headroom annotations
for hd_z, label, color in [(head_z_fwd, 'FWD head', '#e8c46a'),
                             (head_z_aft, 'AFT head', '#6ae8c4')]:
    margin = pod_top_z - hd_z
    ax1.annotate('', xy=(X_FWD_SEAT if 'FWD' in label else X_AFT_SEAT, pod_top_z),
                 xytext=(X_FWD_SEAT if 'FWD' in label else X_AFT_SEAT, hd_z),
                 arrowprops=dict(arrowstyle='<->', color=color, lw=1.2))
    ax1.text(X_FWD_SEAT + 8 if 'FWD' in label else X_AFT_SEAT + 8,
             (pod_top_z + hd_z) / 2,
             f'{margin:.0f}" clr', color=color, fontsize=7.5, va='center')

# Nose dome / aft dome
ax1.axvline(X_NOSE_DOME, color='#cc6666', linewidth=1.0, linestyle='--', alpha=0.6)
ax1.axvline(X_AFT_DOME,  color='#cc6666', linewidth=1.0, linestyle='--', alpha=0.6)
ax1.text(X_NOSE_DOME + 2, -25, 'fwd\ndome', color='#cc6666', fontsize=7, ha='left')
ax1.text(X_AFT_DOME - 2,  -25, 'aft\ndome', color='#cc6666', fontsize=7, ha='right')

# Knee clearance annotation for front pilot
knee_x_fwd = X_FWD_SEAT + BUTTOCK_KNEE
ax1.annotate(f'knee\n{knee_x_fwd:.0f}" from nose', xy=(knee_x_fwd, FLOOR_Z + POPLITEAL_HT),
             xytext=(knee_x_fwd + 8, FLOOR_Z + POPLITEAL_HT + 6),
             color='#e8c46a', fontsize=7,
             arrowprops=dict(arrowstyle='->', color='#e8c46a', lw=0.8))

# Seat pitch annotation
ax1.annotate('', xy=(X_AFT_SEAT, FLOOR_Z - 7), xytext=(X_FWD_SEAT, FLOOR_Z - 7),
             arrowprops=dict(arrowstyle='<->', color='white', lw=1.0))
ax1.text((X_FWD_SEAT + X_AFT_SEAT) / 2, FLOOR_Z - 11,
         f'seat pitch = {X_SEAT_PITCH:.0f}"', color='white', fontsize=7.5, ha='center')

# Pod length annotation
ax1.annotate('', xy=(POD_L_IN, -35), xytext=(0, -35),
             arrowprops=dict(arrowstyle='<->', color='#4a90d9', lw=1.0))
ax1.text(POD_L_IN / 2, -39, f'Pod = {POD_L_IN:.0f}" ({POD_L_IN/12:.1f} ft)',
         color='#4a90d9', fontsize=8, ha='center')

ax1.set_xlim(-10, 185)
ax1.set_ylim(-50, 45)
ax1.set_aspect('equal')
ax1.set_xlabel('X — Nose to Tail (inches)', color='#aaaaaa', fontsize=9)
ax1.set_ylabel('Z — Vertical (inches, pod CL = 0)', color='#aaaaaa', fontsize=9)
ax1.tick_params(colors='#666', labelsize=7)
for sp in ax1.spines.values():
    sp.set_edgecolor('#333')
ax1.grid(True, alpha=0.10, color='#555')
ax1.set_facecolor('#12121e')

# ── LEGEND panel markers
for label, color in [('95th-pct pilot FWD', '#e8c46a'), ('95th-pct pilot AFT', '#6ae8c4'),
                      ('Pod outer shell', '#4a90d9'), ('Pressure domes', '#cc6666')]:
    ax1.plot([], [], color=color, linewidth=2, label=label)
ax1.legend(loc='upper right', framealpha=0.25, fontsize=7, labelcolor='white',
           facecolor='#222233', edgecolor='#444')


# ── RIGHT PANEL: Front view (YZ cross-section) ───────────────────────────────
ax2 = fig.add_subplot(1, 2, 2, facecolor='#12121e')
ax2.set_title('Front View — Max Cross-Section at XSec_1 (30% station = 50" from nose)',
              color='white', fontsize=10, pad=8)

# Outer ellipse
ow = POD_OD_W_IN / 2
oh = POD_OD_H_IN / 2
theta = np.linspace(0, 2 * np.pi, 300)
ax2.fill(ow * np.cos(theta), oh * np.sin(theta), color='#1e3a5f', alpha=0.8, zorder=1)
ax2.plot(ow * np.cos(theta), oh * np.sin(theta), color='#4a90d9', linewidth=2, zorder=2)
ax2.text(0, -oh - 3, f'Outer: {POD_OD_W_IN:.0f}"W × {POD_OD_H_IN:.0f}"H',
         color='#4a90d9', fontsize=8, ha='center')

# Inner ellipse (after shell thickness)
iw = INT_W / 2
ih = INT_H / 2
ax2.plot(iw * np.cos(theta), ih * np.sin(theta),
         color='#88aacc', linewidth=1, linestyle='--', alpha=0.7, zorder=2)
ax2.text(0, -ih - 2, f'Interior: ~{INT_W:.0f}"W × {INT_H:.0f}"H (est. {SHELL_T:.1f}"\\ shell)',
         color='#88aacc', fontsize=7.5, ha='center')

# Floor line
ax2.axhline(FLOOR_Z, color='#aaaaaa', linewidth=1.0, linestyle=':', alpha=0.8)

# Seated figure: 95th-pct male (front view, bilateral symmetry)
# Seat bottom at Y=0 (centerline seat), Z = FLOOR_Z
sz_front = FLOOR_Z
# Hip outline
ax2.add_patch(patches.FancyBboxPatch(
    (-HIP_W / 2, sz_front), HIP_W, 4,
    boxstyle="round,pad=0.5",
    facecolor='#e8c46a', edgecolor='none', alpha=0.6, zorder=3))
# Torso
ax2.add_patch(patches.FancyBboxPatch(
    (-SHOULDER_W / 2, sz_front + 4), SHOULDER_W, SHOULDER_HT - 4,
    boxstyle="round,pad=1",
    facecolor='#e8c46a', edgecolor='none', alpha=0.55, zorder=3))
# Head
ax2.add_patch(Ellipse((0, sz_front + SHOULDER_HT + HEAD_HT / 2 + 1),
                       HEAD_W + 1, HEAD_HT + 2,
                       color='#e8c46a', alpha=0.65, zorder=3))

# Shoulder width annotation
sw_y = sz_front + SHOULDER_HT + 3
ax2.annotate('', xy=(SHOULDER_W / 2, sw_y), xytext=(-SHOULDER_W / 2, sw_y),
             arrowprops=dict(arrowstyle='<->', color='#e8c46a', lw=1.2))
ax2.text(0, sw_y + 2, f'shoulder {SHOULDER_W:.0f}"', color='#e8c46a', fontsize=7.5, ha='center')

# Hip width annotation
hip_y = sz_front + 2
ax2.annotate('', xy=(HIP_W / 2, hip_y), xytext=(-HIP_W / 2, hip_y),
             arrowprops=dict(arrowstyle='<->', color='#ffaa66', lw=1.0))
ax2.text(HIP_W / 2 + 2.5, hip_y, f'hip {HIP_W:.0f}"', color='#ffaa66', fontsize=7, va='center')

# Interior clearance annotations (shoulder to wall)
# Inner wall at ±iw at floor Z (approximate — inner ellipse narrows at shoulder height)
shoulder_z_rel = sz_front + SHOULDER_HT - (-ih)  # how far shoulder_z is from bottom of interior ellipse
# Compute inner wall Y at shoulder height
shoulder_z_abs = sz_front + SHOULDER_HT  # absolute Z of shoulder
# On the inner ellipse: y = iw * sqrt(1 - (z/ih)^2)  where z is measured from ellipse center (0)
z_from_center = shoulder_z_abs  # CL is at z=0
if abs(z_from_center) < ih:
    wall_y_at_shoulder = iw * np.sqrt(1.0 - (z_from_center / ih) ** 2)
else:
    wall_y_at_shoulder = 0.0

clearance = wall_y_at_shoulder - SHOULDER_W / 2
ax2.annotate('', xy=(wall_y_at_shoulder, shoulder_z_abs),
             xytext=(SHOULDER_W / 2, shoulder_z_abs),
             arrowprops=dict(arrowstyle='<->', color='#66ffaa', lw=1.2))
ax2.text((wall_y_at_shoulder + SHOULDER_W / 2) / 2, shoulder_z_abs + 2,
         f'{clearance:.1f}" clr\neach side', color='#66ffaa', fontsize=7, ha='center')

# Mirror clearance
ax2.annotate('', xy=(-wall_y_at_shoulder, shoulder_z_abs),
             xytext=(-SHOULDER_W / 2, shoulder_z_abs),
             arrowprops=dict(arrowstyle='<->', color='#66ffaa', lw=1.2))

# Seated height annotation
top_head_z = sz_front + SEATED_HT
ax2.annotate('', xy=(SHOULDER_W / 2 + 6, top_head_z),
             xytext=(SHOULDER_W / 2 + 6, sz_front),
             arrowprops=dict(arrowstyle='<->', color='#ccccff', lw=1.0))
ax2.text(SHOULDER_W / 2 + 9, (top_head_z + sz_front) / 2,
         f'{SEATED_HT:.0f}"\nseated\nheight', color='#ccccff', fontsize=7, va='center')

# Headroom
pod_top_inside = ih  # approx top of interior ellipse at CL
head_margin = pod_top_inside - top_head_z
ax2.annotate('', xy=(0, pod_top_inside), xytext=(0, top_head_z),
             arrowprops=dict(arrowstyle='<->', color='#ff9966', lw=1.2))
ax2.text(2, (pod_top_inside + top_head_z) / 2,
         f'{head_margin:.1f}"\nhead\nroom', color='#ff9966', fontsize=7, va='center')

# Eye height reference
eye_z = sz_front + EYE_HT
ax2.axhline(eye_z, color='#e8c46a', linewidth=0.7, linestyle='--', alpha=0.5)
ax2.text(iw + 2, eye_z, f'eye {eye_z:.0f}"', color='#e8c46a', fontsize=6.5, va='center')

# Vertical and horizontal dimension lines on ellipse
ax2.annotate('', xy=(ow, 0), xytext=(-ow, 0),
             arrowprops=dict(arrowstyle='<->', color='#4a90d9', lw=1.0))
ax2.text(0, 2, f'{POD_OD_W_IN:.0f}" outer width', color='#4a90d9', fontsize=7.5, ha='center')
ax2.annotate('', xy=(-ow - 5, oh), xytext=(-ow - 5, -oh),
             arrowprops=dict(arrowstyle='<->', color='#4a90d9', lw=1.0))
ax2.text(-ow - 8, 0, f'{POD_OD_H_IN:.0f}"\nheight', color='#4a90d9', fontsize=7.5,
         ha='center', va='center', rotation=90)

ax2.set_xlim(-40, 40)
ax2.set_ylim(-38, 42)
ax2.set_aspect('equal')
ax2.set_xlabel('Y — Lateral (inches, CL = 0)', color='#aaaaaa', fontsize=9)
ax2.set_ylabel('Z — Vertical (inches, pod CL = 0)', color='#aaaaaa', fontsize=9)
ax2.tick_params(colors='#666', labelsize=7)
for sp in ax2.spines.values():
    sp.set_edgecolor('#333')
ax2.grid(True, alpha=0.10, color='#555')
ax2.set_facecolor('#12121e')
ax2.axhline(0, color='#444', linewidth=0.5)
ax2.axvline(0, color='#444', linewidth=0.5)

# ── Summary table (text inset) ─────────────────────────────────────────────────
summary = [
    '95th-pct male ref dims:',
    f'  Seated height:    {SEATED_HT:.1f}"',
    f'  Eye height:       {EYE_HT:.1f}"',
    f'  Shoulder width:   {SHOULDER_W:.1f}"',
    f'  Hip width:        {HIP_W:.1f}"',
    '',
    'Pod interior (est.):',
    f'  Width at max:    {INT_W:.0f}"',
    f'  Height at max:   {INT_H:.0f}"',
    f'  Length (total):  {POD_L_IN:.0f}" ({POD_L_IN/12:.1f} ft)',
    '',
    f'Shoulder clearance: {clearance:.1f}" / side',
    f'Headroom (seated):  {head_margin:.1f}"',
    f'Seat pitch:         {X_SEAT_PITCH:.0f}"',
]
ax2.text(0.02, 0.02, '\n'.join(summary),
         transform=ax2.transAxes,
         color='#cccccc', fontsize=6.8,
         verticalalignment='bottom',
         fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#111122', edgecolor='#333355', alpha=0.85))

plt.tight_layout(rect=[0, 0, 1, 0.96])
out = '/workspace/cad/maos_pod_human_sizing.png'
plt.savefig(out, dpi=140, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Saved: {out}')
print(f'Shoulder clearance per side: {clearance:.2f}"')
print(f'Headroom (seated 95th pct): {head_margin:.2f}"')
print(f'FWD pilot head top: {head_z_fwd:.1f}" above pod CL (pod top inner: {ih:.1f}")')
