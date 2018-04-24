#!/usr/bin/env python3
from collections import namedtuple
point = namedtuple('Point',['x','y'])
p = point(10,y=20)
print(p)
print(p.x+p.y)
print(p[0]+p[1])
x,y = p
print(x)
print(y)
