def imprimirMatriz(mat,linhas,colunas):
    for l in range(linhas):
        for c in range(colunas):
            print(mat[l][c],end=' ')
        print()
    print()

#################### PROGRAMA PRINCIPAL ####################### 
'''
Precisa gerar essa matriz 
1 2 3 4 3 2 1 
2 3 4 5 4 3 2 
3 4 5 6 5 4 3 
3 4 5 6 5 4 3 
2 3 4 5 4 3 2 
1 2 3 4 3 2 1 

Não sei se a forma que fiz foi a mais esperta
'''

mat = []

nLinhas = 6
nColunas = 7

valorLinha = 0
for i in range(nLinhas):
    aux = []
    if i < nLinhas /2:
        valorLinha = valorLinha +1
    elif i> nLinhas/2:
        valorLinha = valorLinha -1  
    valorColuna = valorLinha
    for j in range(nColunas):
        aux.append(valorColuna)
        if j+1 < nColunas/2:
            valorColuna = valorColuna + 1
        else:
            valorColuna = valorColuna - 1
    mat.append(aux)

imprimirMatriz(mat,nLinhas,nColunas)
##################################### OUTRA SOLUÇÃO, MAIS COMPLEXA, MAS QUE APROVEITA OS ESPELHAMENTOS
mat = []
# Criando uma matriz só com zeros
for i in range(nLinhas):
    mat.append([0]*nColunas)

#imprimirMatriz(mat,nLinhas,nColunas)

for i in range(0, int (nLinhas/2)):
    valorLinha = i+1
    valorColuna = valorLinha
    for j in range(0, int(nColunas/2)+1):
        mat[i][j] = valorColuna
        mat[i][-(j+1)] = valorColuna #espelha as colunas na linha
        mat[-(i+1)][j] = valorColuna #espelha as linhas até a metade das colunas
        mat[-(i+1)][-(j+1)] = valorColuna #espelha as linhas da metade até o fim das colunas
        valorColuna = valorColuna+1

imprimirMatriz(mat,nLinhas,nColunas)
    


