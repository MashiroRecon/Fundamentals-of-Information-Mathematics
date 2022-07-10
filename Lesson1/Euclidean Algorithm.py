#  Euclidean Algorithm

a = int(input("The first number = "))
b = int(input("The second number = "))

q = a // b
r = a % b
print(a, " = ", q, "*", b, "+", r)

while r != 0:
    a = b
    b = r
    q = a // b
    r = a % b
    print(a, " = ", q, "*", b, "+", r)

print("GCD = ", b)