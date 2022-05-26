def ehQM(mat):
    somaLinha = 0
    somaColuna = 0
    somaDiagonal1 = 0
    somaDiagonal2 = 0
    
    #1) Checando a soma das linhas e colunas
    aux = 0
    somaLinha = 0
    for i in range(3): #percorre linhas/colunas
        somaLinha = 0
        somaColuna = 0
        for j in range(3): #percorre colunas/linhas
            if (i == 0): #primeira linha
                aux += mat[i][j]
            somaLinha += mat[i][j]
            somaColuna += mat[j][i]
        print('Soma elementos linha [{}] = {}'.format(i,somaLinha))
        print('Soma elementos coluna [{}] = {}'.format(i,somaColuna))
        if somaLinha != aux: #depois que percorreu
            return False
        if somaColuna != aux: 
            return False
    
    #2) Checando a soma da diagonal principal
    for i in range (3):
        somaDiagonal1 += mat[i][i]
    print('Soma elementos diagonal principal = {}'.format(somaDiagonal1))
    if somaDiagonal1 != aux:
        return False
    
    #3) Checando a soma da diagonal secundária
    for i in range(1,4):
        somaDiagonal2 += mat[-i][-i]

    print('Soma elementos diagonal secundária = {}'.format(somaDiagonal2))
    if somaDiagonal2 != aux:
        return False
    return True

#################### PROGRAMA PRINCIPAL #######################    

mat1 = [ [8,  0,  7],
        [4,  5,  6],
        [3,  10,  2]
      ]

mat2 = [ [4,  9,  2],
        [3,  5,  7],
        [8,  1,  6]
      ]

mat3 = [ [1,  0,  7],
        [4,  2,  6],
        [3,  10,  3]
      ]

#### TESTANDO

if (ehQM(mat1) == True):
    print('É quadrada!')
else:
    print('Não é quadrada!')
                        
if (ehQM(mat2) == True):
    print('É quadrada!')
else:
    print('Não é quadrada!')

if (ehQM(mat3) == True):
    print('É quadrada!')
else:
    print('Não é quadrada!')