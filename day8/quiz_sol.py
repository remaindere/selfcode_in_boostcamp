import sympy as sym
from sympy.abc import x
from sympy.abc import k
from sympy.abc import y
from sympy.abc import z

tan_hyper = sym.tanh(x)
tan_h_diff = sym.diff(tan_hyper, x)
print(tan_hyper)
print(tan_h_diff)
print(tan_h_diff.subs(x, 0))

k = (sym.poly(x+y)**2)
z = ((k+3)**3)

print(k)
print(z)

z_diff_by_x = sym.diff(z, x)
print("sol")
print(z_diff_by_x)
print(sym.poly(6*(((x+y)**2+3)**2)*(x+y)))