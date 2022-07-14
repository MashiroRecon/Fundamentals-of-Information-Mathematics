#  Inverse matrix calculation

#  Imports
import numpy as np
import sympy as sp

print("Inverse matrix calculation program.")

arr_a = np.array([[1, 2], [3, 4]])
arr_a[0][0] = int(input("arr_a(1,1) ="))
arr_a[0][1] = int(input("arr_a(1,2) ="))
arr_a[1][0] = int(input("arr_a(2,1) ="))
arr_a[1][1] = int(input("arr_a(2,2) ="))
n = int(input("mod ="))

a = ((arr_a[0][0] * arr_a[1][1]) - (arr_a[0][1] * arr_a[1][0])) % n
kx = sp.gcdex(a, n)[0]

arr_inv = np.array([[arr_a[1][1], -arr_a[0][1]], [-arr_a[1][0], arr_a[0][0]]])

print("mod =", n)
print("arr_a =", arr_a)
print("arr_inv =", (arr_inv * kx) % n)
