#  Matrix-based cryptography

#  Imports
import numpy as np
import random

#  Enter the text you want to encrypt
text = list(input("Enter the text :"))

#  Input for mod:n (fixed at 1114112: see Python,chr documentation)
N = 1114112

#  Find the size of the smallest square matrix
#   that can encapsulate the string to be encrypted
q = 1
while int(len(text)) > q**2:
    q += 1

#  Enter a trailing space when the number of characters
#   in the sentence to be encrypted is not q squared
while int(len(text)) != q**2:
    text.append(" ")

#  Convert all characters to ASCII and assign as int
print(text)
j = 0
while j != int(len(text)):
    text[j] = int(ord(text[j]))
    j += 1

#  Assign list to P as an array of q rows
P = np.array([int(a) for a in text]).reshape(q, q)
# print(text)
# print(P)

#  Random letter at the end when the encryption key is not q squared
#  ASCII:42~126("*" ~ "~")
password = list(chr(random.randint(42, 126)))
while int(len(password)) != q**2:
    password.append(chr(random.randint(42, 126)))

#  Convert all characters to ASCII and assign as int
print(password)
j = 0
while j != int(len(password)):
    password[j] = int(ord(password[j]))
    j += 1

#  Assign the encryption key to A as an array of q rows
A = np.array([int(a) for a in password]).reshape(q, q)
# print(password)
# print(A)

#  encryption
C = np.dot(A, P) % N
# print(C)

#  Converted to 1 line
cipher = np.ravel(C)
print(cipher)

#  Generate a string that can secure the required number of lines using
#   a random function when creating the encryption key.
#  Then the string is converted to a sequence of numbers and
#   the encryption process is executed.

#  decoding process

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

j = 0
while j != int(len(cipher)):
    print(chr(int(cipher[j])))
    j += 1
print(cipher)
