# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from PIL import Image
import random
import math
 
def generate_voronoi_diagram(width, height, num_cells, num_own):
    image = Image.new("RGB", (width, height))
    putpixel = image.putpixel
    imgx, imgy = image.size
    nx = []
    ny = []

    neighbors = [set() for _ in range(num_cells)]
    area = []
    colors = []
    owner = []
    for i in range(num_own):
        colors.append( (random.randrange(256),random.randrange(256),random.randrange(256)) )

    for i in range(num_cells):
        area.append(0.0)
        nx.append(random.randrange(imgx))
        ny.append(random.randrange(imgy))
        owner.append(random.randrange(num_own))
    for y in range(imgy):
        for x in range(imgx):
            dmin = math.hypot(imgx-1, imgy-1)
            dmin2 = dmin
            j = -1
            for i in range(num_cells):
                d = (math.hypot(nx[i]-x, ny[i]-y))
                if d < dmin:
                    dmin = d
#                    v = j
                    j = i
            area[j] += 1.0
            v = -1
            for k in range(num_cells):
                if k==j: continue
                dist = math.hypot(nx[k]-x, ny[k]-y)
                if dist <= dmin2:
                    dmin2 = dist
                    v = k
            if owner[j] != owner[v]:
                neighbors[owner[j]].add(owner[v])
            if math.fabs(dmin2-dmin) > 0.1:
                putpixel((x, y), colors[owner[j]])
            else:
                putpixel((x, y), (0,0,0))
    for i in range(num_cells):
        putpixel((nx[i], ny[i]), (255,255,255))
        print owner[i], area[i]

    tot_own = []
    for i in range(num_own):

        tot_own.append(0.0)
        for j in range(num_cells):
            if owner[j] == i:
                tot_own[i] += area[j]
        print "Proprietario:", i, "possiede un'area di:", tot_own[i], "e ha come vicini i signori:", list(neighbors[i])
    
    image.save("VoronoiDiagram.png", "PNG")
    image.show()
 
generate_voronoi_diagram(400, 400, 16, 9)

