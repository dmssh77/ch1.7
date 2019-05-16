# 동적 import 를 위한 함수 -> __import__ 함수

import sys

# 동적으로 python path 잡기
sys.path.append("../python_modules")

mod = __import__("mymath")

print(mod.pi)
print(mod.area_circle(5))