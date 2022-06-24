import random

A = []

for i in range(10):
    A.append(random.randint(0,10))

print(A)

soma = 0

for i in range(len(A)):
    soma = soma + A[i]

media = soma / len(A)

print('Media = ', media)
