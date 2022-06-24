import random #pq tenho preguiça de ler, eu sorteio

def imprimirMatriz(mat,linhas,colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(mat[l][c],end='\t')
        print()
    print()

#################### PROGRAMA PRINCIPAL ####################### 

mat = [] #matriz/vetor vazio

# criando a matriz 4x4, inicialmente com zeros
for i in range(4):
    aux = [0] * 4 #cria a linha para a mat
    mat.append(aux) #adiciona a linha na mat

#preencher com 1 acima da diagonal e com 2 abaixo
for i in range(4):
    for j in range(4):
        if j > i:
            mat[i][j] = 1
        elif j < i:
            mat[i][j] = 2
        else: #i == j, então é diagonal, "ler" (sortear)
            mat[i][j] = random.randint(3,10) 

imprimirMatriz(mat,4,4)