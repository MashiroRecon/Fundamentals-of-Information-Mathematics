#  Euclidean Algorithm

x = [""]*100
y = [""]*100
q = [""]*100
r = [""]*100

i = 0

x[i] = int(input("The first number = "))
y[i] = int(input("The second number = "))

q[i] = x[i] // y[i]
r[i] = x[i] % y[i]
print(x[i], " = ", q[i], "*", y[i], "+", r[i])

while r != 0:
    x[i+1] = y[i]
    y[i+1] = r[i]
    q[i+1] = x[i+1] // y[i+1]
    r[i+1] = x[i+1] % y[i+1]
    print(x[i+1], " = ", q[i+1], "*", y[i+1], "+", r[i+1])
    i = i + 1

print("GCD = ", y[i])