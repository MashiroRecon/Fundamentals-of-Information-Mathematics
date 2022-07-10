#  Euclidean Algorithm

x = [""]
y = [""]
q = [""]
r = [""]

i = 0

x[i] = int(input("The first number = "))
y[i] = int(input("The second number = "))

q[i] = x[i] // y[i]
r[i] = x[i] % y[i]
print(x[i], " = ", q[i], "*", y[i], "+", r[i])

while r[i] != 0:
    x.append(y[i])
    y.append(r[i])
    q.append(x[i+1] // y[i+1])
    r.append(x[i+1] % y[i+1])
    print(x[i+1], " = ", q[i+1], "*", y[i+1], "+", r[i+1])
    i = i + 1

print("GCD = ", y[i])

#  Use math

from gettext import npgettext
import math
math_gcd = math.gcd(x[0], y[0])
print("math.gcd = ", math_gcd)

#  Use NumPy

import numpy as np
numpy_gcd = np.gcd(x[0], y[0])
print("numpy.gcd = ", numpy_gcd)

#  Use SymPy

import sympy as sp
sympy_gcd = sp.gcd(x[0], y[0])
print("sympy.gcd = ", sympy_gcd)