#  Matrix-based decoding

#  Imports
import numpy as np

#  decoding process
q = int(input("Enter the number of ciphertext characters :"))

j = 1
cipher = list(str(input("Enter the first character of ciphertext :")))
while j != q:
    cipher.append(str(input("Enter the " +
                  str(j)+"th character of ciphertext :")))
    j += 1

j = 0
while j != int(len(cipher)):
    cipher[j] = int(ord(cipher[j]))
    j += 1


print(cipher)
print([int(a) for a in cipher])

C = np.array([int(a) for a in cipher]).reshape(int(q ** 0.5), int(q ** 0.5))

N = 1114111

password = list(input("Enter the password :"))

j = 0
while j != int(len(password)):
    password[j] = int(ord(password[j]))
    j += 1

A = np.array([int(a) for a in password]).reshape(int(q ** 0.5), int(q ** 0.5))

#  A Inverse matrix calculation
A_inv = np.linalg.inv(A) % N
# print(A_inv)

decod = np.dot(A_inv, C) % N

# print(decod)
# print(np.dot(A, A_inv) % N)
# print(np.dot(A_inv, A) % N)

decod = np.ravel(decod)
decod = decod % N
decod = [int(a) for a in decod]
# print(decod)
# print(text)

j = 0
while j != int(len(decod)):
    decod[j] = chr(int(decod[j]))
    j += 1
print(decod)
