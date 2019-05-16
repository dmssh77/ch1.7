# 다양한 import

# import math
# print(math.sin(math.pi / 6), math.cos(math.pi / 6))

# from math import sin, cos, pi
# print(sin(pi / 6), cos(pi / 6))

# from mymath import pi
# print(pi)

# from math import * -> 요걸 가장 많이 씀
# print(sin(pi / 6), cos(pi / 6))

# import math as m
# print(m.pi)

from math import sin as s, cos as c
import mymath as m
print(m.pi, s(m.pi / 6))