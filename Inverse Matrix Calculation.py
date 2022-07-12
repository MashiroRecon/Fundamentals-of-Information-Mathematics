#  Inverse matrix calculation

#  Imports
import numpy as np
import sympy as sp

print(print("Inverse matrix calculation program."))

arr = np.array([[1, 2], [3, 4]])
arr[0][0] = int(input("arr(1,1) ="))
arr[0][1] = int(input("arr(1,2) ="))
arr[1][0] = int(input("arr(2,1) ="))
arr[1][1] = int(input("arr(2,2) ="))
n = int(input("mod ="))

a = ((arr[0][0] * arr[1][1]) - (arr[0][1] * arr[1][0])) % n
kx = sp.gcdex(a, n)[0]

arr_inv = np.array([[arr[1][1], -arr[0][1]], [-arr[1][0], arr[0][0]]])

print("mod =", n)
print("arr =", arr)
print("arr_inv =", (arr_inv * kx) % n)
