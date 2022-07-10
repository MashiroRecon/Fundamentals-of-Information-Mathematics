#  Diophantine equation

print("Solve [ax + by = 1] program.")

a = int(input("a = "))
b = int(input("b = "))

#  変数のswap
if a < b :
    a,b = b,a

x = [""]
y = [""]
q = [""]
r = [""]

i = 0

x[i] = a
y[i] = b

q[i] = x[i] // y[i]
r[i] = x[i] % y[i]
print("(",i, ") ", x[i], " = ", q[i], "*", y[i], "+", r[i])

while r[i] != 0:
    x.append(y[i])
    y.append(r[i])
    q.append(x[i+1] // y[i+1])
    r.append(x[i+1] % y[i+1])
    print("(",i+1, ") ", x[i+1], " = ", q[i+1], "*", y[i+1], "+", r[i+1])
    i = i + 1

print("GCD = ", y[i])

print("Solve Diophantine equation.")

kx = [""] * i
ky = [""] * i

i = i - 1
kx[i] = 1
ky[i] = -q[i]

print("(",i, ") ", "1 = ", "(", kx[i], ")", "*", x[i],"+", "(", ky[i], ")", "*", y[i] )

while i != 0 :
    i = i - 1
    kx[i] = ky[i - 1]
    ky[i] = kx[i + 1] + y[i] * ky[i + 1]
    print("(",i, ") ", "1 = ", "(", kx[i], ")", "*", x[i],"+", "(", ky[i], ")", "*", y[i] )