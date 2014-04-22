"""
Simple recursive implementation of a sierpinski pyramid algorithm for Rhinocerous 5.  Have fun!
adamhreis at gmail dot com
"""

import rhinoscriptsyntax as rs
import math

def midpoint(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2]

def next_pyramids(p):
    next = []
    mid1 = midpoint(p[0], p[1])
    mid2 = midpoint(p[1], p[2])
    mid3 = midpoint(p[0], p[2])
    mid4 = midpoint(p[1], p[3])
    mid5 = midpoint(p[2], p[3])
    mid6 = midpoint(p[0], p[3])
    
    next.append((mid2, mid1, p[1], mid4))
    next.append((mid3, mid2, p[2], mid5))
    next.append((mid1, mid3, p[0], mid6))
    next.append((mid4, mid5, mid6, p[3]))
    
    return next;
    
def sierpinski(scale, angle, generations):
    height_prop = math.sin(angle)
    
    p1 = [0.,0.,0.]
    p2 = [float(scale),0.,0.]
    p3 = [float(scale)/2, height_prop*scale,0.]
    p4 = [float(scale)/2, height_prop*scale/3, height_prop*scale]
    
    _sierpinski([(p1, p2, p3, p4)], 0, generations)
    
def _sierpinski(pyramids, current_generation, max_generation):
    if current_generation >= max_generation:
        return
    
    new_pyramids = []
    
    for p in pyramids:
        rs.AddLine(p[0],p[1])
        rs.AddLine(p[1],p[2])
        rs.AddLine(p[0],p[2])
        rs.AddLine(p[0],p[3])
        rs.AddLine(p[1],p[3])
        rs.AddLine(p[2],p[3])
        new_pyramids.extend(next_pyramids(p))
    
    _sierpinski(new_pyramids, current_generation+1, max_generation)



if __name__ == '__main__':
    side_len = float(raw_input('Outer side length (defaults to 4): ') or 4)
    angle = float(raw_input('Angle (in radians, defaults to pi/3): ') or math.pi/3)
    generations = int(raw_input('Number of generations (defaults to 8): ') or 8)
    sierpinski(side_len, angle, generations)