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


