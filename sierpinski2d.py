"""
Simple recursive implementation of a sierpinski triangle algorithm for Rhinocerous 5.  Have fun!
adamhreis at gmail dot com
"""

import rhinoscriptsyntax as rs
import math

def midpoint(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2]

def next_triangles(t):
    next = []
    mid1 = midpoint(t[0], t[1])
    mid2 = midpoint(t[1], t[2])
    mid3 = midpoint(t[0], t[2])
    next.append((mid2, mid1, t[1]))
    next.append((mid3, mid2, t[2]))
    next.append((mid1, mid3, t[0]))
    return next;
    
def sierpinski(scale, angle, generations):
    height_prop = math.sin(angle)
    
    p1 = [0.,0.,0.]
    p2 = [float(scale),0.,0.]
    p3 = [float(scale)/2, height_prop*scale,0.]
    
    _sierpinski([(p1, p2, p3)], 0, generations)
    
def _sierpinski(triangles, current_generation, max_generation):
    if current_generation >= max_generation:
        return
    
    new_triangles = []
    
    for t in triangles:
        rs.AddLine(t[0],t[1])
        rs.AddLine(t[1],t[2])
        rs.AddLine(t[0],t[2])
        new_triangles.extend(next_triangles(t))
    
    _sierpinski(new_triangles, current_generation+1, max_generation)



if __name__ == '__main__':
    side_len = float(raw_input('Outer side length (defaults to 4): ') or 4)
    angle = float(raw_input('Angle (in radians, defaults to pi/3): ') or math.pi/3)
    generations = int(raw_input('Number of generations (defaults to 9): ') or 9)
    sierpinski(side_len, angle, generations)