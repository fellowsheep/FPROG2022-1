import random 

def achou(numero,lista):
    for i in range(len(lista)):
        if lista[i] == numero:
            return True 
    return False



S = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(S)

print(S)

J1 = []
J2 = []

for i in range(10):
    if i % 2 == 0:
        J1.append(S[i])
    else:
        J2.append(S[i])

print(J1)
print(J2)

#embaralha de novo, para "sortear"
random.shuffle(S)

contJ1 = 0
contJ2 = 0
bingo = False

while bingo == False:
    #Pega sempre o indice do ultimo elemento da Lista S
    i = len(S) - 1
    # copiando o valor do elemento i 
    nroSorteado = S[i]
    # removendo o elemento da lista S
    S.pop()
    print(nroSorteado)
    print(S)

    #Verifica em qual cartela está o nro sorteado
    if achou(nroSorteado,J1) == True:
        contJ1 = contJ1 + 1
    
    if achou(nroSorteado,J2) == True:
        contJ2 = contJ2 + 1

    #testa se já acabou
    if contJ1 == 5:
        print('BINGO! jogador 1 venceu!')
        bingo = True
    elif contJ2 == 5:
        print('BINGO! jogador 2 venceu!')
        bingo = True
    

    if len(S) == 0:
        bingo = True

    

