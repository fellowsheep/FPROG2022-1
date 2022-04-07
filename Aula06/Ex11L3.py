valor = float(input('Digite o valor a retirar: '))

#notas de R$ 100
notas100 = int(valor / 100)
#valor = valor - notas100 * 100
valor = valor % 100

#notas de R$ 50
notas50 = int(valor / 50)
valor = valor % 50

#notas de R$ 20
notas20 = int (valor / 20)
valor = valor % 20

#notas de R$ 10
notas10 = int (valor /10)
valor = valor % 10

#notas de R$ 5
notas5 = int (valor / 5)
valor = valor % 5

#notas de R1
notas1 = int (valor)

if (notas100 > 0):
    print(notas100,' nota(s) de R$ 100')

if (notas50 > 0):
    print(notas50,' nota(s) de R$ 50')

if (notas20 > 0):
    print(notas20,' nota(s) de R$ 20')

if (notas10 > 0):
    print(notas10,' nota(s) de R$ 10')

if (notas5 > 0):
    print(notas5,' nota(s) de R$ 5')

if (notas1 > 0):
    print(notas1,' nota(s) de R$ 1')

