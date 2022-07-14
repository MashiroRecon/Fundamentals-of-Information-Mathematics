#  Simultaneous equations

#  Imports
import numpy as np
import sympy as sp

print("Solve Simultaneous equations program.")
print("(arr_a) * (ans) = (arr_b) (mod : n)")

arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([1, 2])
arr_a[0][0] = int(input("arr_a(1,1) ="))
arr_a[0][1] = int(input("arr_a(1,2) ="))
arr_a[1][0] = int(input("arr_a(2,1) ="))
arr_a[1][1] = int(input("arr_a(2,2) ="))
arr_b[0] = int(input("arr_b(1) ="))
arr_b[1] = int(input("arr_b(2) ="))
n = int(input("mod ="))

a = ((arr_a[0][0] * arr_a[1][1]) - (arr_a[0][1] * arr_a[1][0])) % n
kx = sp.gcdex(a, n)[0]

arr_a_inv = np.array([[arr_a[1][1], -arr_a[0][1]],
                      [-arr_a[1][0], arr_a[0][0]]])
arr_a_inv = (arr_a_inv * kx) % n

arr_ans = np.array([1, 2])
arr_ans = np.dot(arr_a_inv, arr_b)
arr_ans = arr_ans % n

print("mod =", n)
print("arr_a =", arr_a)
print("arr_inv =", arr_a_inv)

print("arr_ans =", arr_ans)
