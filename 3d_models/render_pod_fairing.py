"""Render FreeCAD pod fairing alongside OpenVSP aircraft (boom + wing + tails).
The FreeCAD pod replaces the symmetric pod from OpenVSP — shown in a distinct
colour so the asymmetric aft taper is clearly visible.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def read_stl_ascii(path):
    tris = []
    with open(path) as f:
        verts = []
        for line in f:
            line = line.strip()
            if line.startswith('vertex'):
                verts.append([float(x) for x in line.split()[1:4]])
            elif line.startswith('endloop'):
                if len(verts) == 3:
                    tris.append(verts)
                verts = []
    return tris


pod_tris  = read_stl_ascii('/workspace/cad/maos_pod_fairing.stl')
acft_tris = read_stl_ascii('/workspace/cad/maos_aircraft_v1.stl')
print(f'Pod triangles:      {len(pod_tris)}')
print(f'Aircraft triangles: {len(acft_tris)}')

fig = plt.figure(figsize=(18, 7), facecolor='#1a1a2e')

views = [
    ('Isometric',       20, -50),
    ('Side (Profile)',   0, -90),
    ('Top (Plan)',      90, -90),
]

for i, (title, elev, azim) in enumerate(views):
    ax = fig.add_subplot(1, 3, i + 1, projection='3d', facecolor='#1a1a2e')

    # Aircraft structure (boom, wing, tails) from OpenVSP — steel blue
    c_acft = Poly3DCollection(acft_tris, alpha=0.25, linewidth=0)
    c_acft.set_facecolor('#4a6fa5')
    ax.add_collection3d(c_acft)

    # FreeCAD pod with asymmetric aft taper — brighter to stand out
    c_pod = Poly3DCollection(pod_tris, alpha=0.70, linewidth=0)
    c_pod.set_facecolor('#5bc8af')
    ax.add_collection3d(c_pod)

    ax.set_xlim(-2, 28)
    ax.set_ylim(-17, 17)
    ax.set_zlim(-5, 7)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(title, color='white', fontsize=10, pad=4)
    ax.set_xlabel('X ft', color='#888', fontsize=7)
    ax.set_ylabel('Y ft', color='#888', fontsize=7)
    ax.set_zlabel('Z ft', color='#888', fontsize=7)
    ax.tick_params(colors='#555', labelsize=6)
    for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
        pane.fill = False
        pane.set_edgecolor('#333')
    ax.grid(True, alpha=0.12, color='#555')

fig.suptitle(
    'MAOS Aircraft  |  FreeCAD pod (teal) + OpenVSP structure (blue)  |  Flat-top aft taper',
    color='white', fontsize=11, fontweight='bold', y=1.01)

plt.tight_layout()
out = '/workspace/cad/maos_pod_fairing_preview.png'
plt.savefig(out, dpi=130, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Saved: {out}')
