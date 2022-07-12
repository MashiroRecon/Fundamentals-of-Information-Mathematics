#  Diophantine equation

import sympy as sp

print("Solve [ax + by = 1] program.")

a = int(input("a = "))
b = int(input("b = "))

print("gcd = ", sp.gcdex(a, b)[2])
print(a, "x +", b, "y = 1")
print("Particular solution : x0 =", sp.gcdex(a, b)[0])
print("                      y0 =", sp.gcdex(a, b)[1])
