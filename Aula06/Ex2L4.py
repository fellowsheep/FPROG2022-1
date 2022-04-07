# a) 10 primeiros nros positivos
for n in range(10):
    print(n)

print("-----------")

#b) 10 nros sequenciais começando em -6
for n in range(-6, -6+10):
    print(n)

print("-----------")

#c) os 10 primeiros pares positivos
for n in range(0,20,2):
    print(n)

print("-----------")

#d) 10 primeiros m~ultiplos pos de 4
for n in range(0,40,4):
    print(n)

nome = input('Digite um nome:')
primeiroNome = nome

for n in range(4):
    nome = input("Digite um nome ")
    if (nome < primeiroNome):
        primeiroNome = nome 

print('o primeiro e ', primeiroNome)