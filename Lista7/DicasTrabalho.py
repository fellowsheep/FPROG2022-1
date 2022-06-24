def imprimirMatriz(mat,linhas,colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(mat[l][c],end=' ')
        print()

def salvarMatriz(nomeArquivo,mat,linhas,colunas):
    arqEscrita = open(nomeArquivo, 'w')
    for l in range(linhas):
        for c in range(colunas):
            arqEscrita.write(mat[l][c] + ' ')
        arqEscrita.write('\n')
    arqEscrita.close()

def salvarMatrizCSV(nomeArquivo,mat,linhas,colunas):
    arqEscrita = open(nomeArquivo, 'w')
    for l in range(linhas):
        for c in range(colunas):
            arqEscrita.write(mat[l][c] + ';')
        arqEscrita.write('\n')
    arqEscrita.close()

def lerArquivo(nomeArquivo):
    #fazer a leitura e armazenar numa matriz
    mat = [1, 2, 3]
    #...
    return mat


def getI(letra):
    if letra == 'A':
        return 5
    elif letra == 'B':
        return 4
    elif letra == 'C':
        return 3
    elif letra == 'D':
        return 2
    elif letra == 'E':
        return 1
    elif letra == 'F':
        return 0
    else:
        return -1

################################

matAssentos = [] #matriz vazia

for i in range(6): #linhas
    aux = ['-'] * 29
    matAssentos.append(aux)

imprimirMatriz(matAssentos,6,29)

matAssentos[getI('A')][10] = 'X'

imprimirMatriz(matAssentos,6,29)

nomeArquivo = input('Digite o nome do arquivo: ')

salvarMatriz(nomeArquivo,matAssentos,6,29)

matAssentos = lerArquivo('lalala')

print(matAssentos)
#mat[fileiras.A][0] = 'X'
