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


tris = read_stl_ascii('/workspace/cad/maos_aircraft_v1.stl')
print(f'Triangles: {len(tris)}')

fig = plt.figure(figsize=(18, 7), facecolor='#1a1a2e')

views = [
    ('Isometric',         20, -50),
    ('Side (Profile)',     0, -90),
    ('Top (Plan)',        90, -90),
]

for i, (title, elev, azim) in enumerate(views):
    ax = fig.add_subplot(1, 3, i + 1, projection='3d', facecolor='#1a1a2e')
    poly = Poly3DCollection(tris, alpha=0.55, linewidth=0)
    poly.set_facecolor('#4a90d9')
    ax.add_collection3d(poly)
    ax.set_xlim(-2, 28)
    ax.set_ylim(-17, 17)
    ax.set_zlim(-5, 7)
    ax.view_init(elev=elev, azim=azim)
    ax.set_title(title, color='white', fontsize=10, pad=4)
    ax.set_xlabel('X ft', color='#888', fontsize=7)
    ax.set_ylabel('Y ft', color='#888', fontsize=7)
    ax.set_zlabel('Z ft', color='#888', fontsize=7)
    ax.tick_params(colors='#555', labelsize=6)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#333')
    ax.yaxis.pane.set_edgecolor('#333')
    ax.zaxis.pane.set_edgecolor('#333')
    ax.grid(True, alpha=0.12, color='#555')

fig.suptitle(
    'MAOS Aircraft v1  |  OpenVSP 3.48.2  |  Pod + Top Boom + Wing + H/V Tail',
    color='white', fontsize=12, fontweight='bold', y=1.01)

plt.tight_layout()
out = '/workspace/cad/maos_aircraft_v1_preview.png'
plt.savefig(out, dpi=130, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f'Saved: {out}')
