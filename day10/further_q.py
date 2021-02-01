import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy.abc import x
theta = np.arange(0, 1, 0.001) 
print(theta) #0.000~0.999
p = theta ** 3 * (1 - theta) ** 7
#print(p)
p_sum = p.sum()

p_intg = sym.integrate((x**3)*(1-x)**7, x)
print(p_intg.subs(x, 1))

p_intg_sum = 0
for x_i in theta :
    p_intg_sum += p_intg.subs(x, x_i)

print(p_intg_sum)    
plt.plot(theta, p)
plt.show()