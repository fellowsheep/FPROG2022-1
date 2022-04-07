import random
#------------------
# FUNCOES
def OlaPessoa():
    print('Ola pessoa!')
    #...

def OlaNome(par1):
    print('Ola, ', par1)

def somar(n1, n2):
    res = n1 + n2
    return res

def ParImpar(n):
    if (n % 2 == 0):
        print('PAR')
    else:
        print('IMPAR')
#-----------------
# BLOCO PRINCIPAL

OlaPessoa()
OlaNome('Rossana')
nome = input('Digite seu nome')
OlaNome(nome)
resultado = somar(5, 10)
print(resultado) 
a = int(input('Digite um nro'))
b = int(input('Digite um nro'))
resultado = somar(a, b)
print(resultado) 

for n in range(5):
    s1 = random.randint(0,10)
    s2 = random.randint(0,10)
    res = somar(s1,s2)
    print(s1,' + ',s2,' = ',res)

for i in range(20,30):
    print(i)
    ParImpar(i)
    print('---')


