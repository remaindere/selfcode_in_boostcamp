import numpy as np
import sympy as sym
from sympy.abc import x
from sympy.abc import y

f = sym.poly(9*(y**2)+3*y+9*x+3)

f_diff = sym.diff(f, x)

print(f_diff)