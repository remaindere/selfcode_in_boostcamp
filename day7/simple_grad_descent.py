from mimetypes import init
import sympy as sym
from sympy.abc import x
from sympy.abc import y
import numpy as np

f = sym.poly(x**2+x*2+3)
diff_f = sym.diff(f, x)
cnt = 0
point = 0 #starts at 0
lr = 1e-3
diff_f_val = diff_f.subs(x, point)
while np.abs(diff_f_val) > 1e-5 :
    point -= lr*diff_f_val
    diff_f_val = diff_f.subs(x, point)
    cnt+=1

print(cnt, point, sym.poly(f, x).subs(x, point))