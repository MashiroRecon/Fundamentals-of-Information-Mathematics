#  First-order congruence equation

import sympy as sp

print("Solve [ax ≡ 1 (mod n)] program.")

a = int(input("a = "))
n = int(input("n = "))

print(a, "x ≡ 1 (mod ", n, ")")
print("x ≡", sp.gcdex(a, n)[0],)
print("(y ≡", sp.gcdex(a, n)[1], ", mod", n, ")")
