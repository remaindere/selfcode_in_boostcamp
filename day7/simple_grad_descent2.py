from mimetypes import init
import sympy as sym
from sympy.abc import x
from sympy.abc import y
import numpy as np

f2 = sym.poly(x**2+(2*(y**2)))
cnt = 0
point = 0 #starts at 0
points = [-4, -4]
lr = 1e-1
diff_f_x = sym.diff(f2, x)
diff_f_y = sym.diff(f2, y)
diff_f_xval = diff_f_x.subs(x, points[0]).subs(y, points[1])
diff_f_yval = diff_f_y.subs(x, points[0]).subs(y, points[1])
nparr = np.array([diff_f_xval, diff_f_yval], float)
print(diff_f_xval, diff_f_yval)
while np.linalg.norm(nparr) > 1e-2 :
    points -= lr*nparr
    diff_f_xval = diff_f_x.subs(x, points[0]).subs(y, points[1])
    diff_f_yval = diff_f_y.subs(x, points[0]).subs(y, points[1])
    nparr = np.array([diff_f_xval, diff_f_yval], float)
    cnt+=1

print(cnt, points, sym.poly(f2, x).subs(x, points[0]))