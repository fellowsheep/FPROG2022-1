import random

# Extra! Brincando com a biblioteca matplot
# Para isso, abra um terminal e digite pip install matplotlib para instalar
# Se não for fazer isso agora, então comente as linhas 6, 7, 8 e as linhas 35 em diante!
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import numpy as np

N = random.randint(10, 100) #entre 10 e 100 lancamentos
lancamentosDado = [0] * 6

print(lancamentosDado)

print('Executando {} lancamentos...'.format(N),end=' ')
for i in range(N):
    nSorteado = random.randint(1,6)
    lancamentosDado[nSorteado-1] += 1
print('feito!')

print(lancamentosDado)

porcentagens = [] #para plotar o gráfico depois
rotulos = []
explode = [0.0] * 6

print(rotulos)
for i in range(len(lancamentosDado)):
    porcentagem = lancamentosDado[i]/N*100 
    print('Porcentagem de lancamentos do valor {}: {:.2f}%'.format(i+1,porcentagem))
    porcentagens.append(porcentagem/100.0)
    rotulos.append(str(i+1))


# Criando o gráfico
fig, (graphic) = plt.subplots()

# gráfico de pizza
# rotate so that first wedge is split by the x-axis
angle = -180 * porcentagens[0]
graphic.pie(porcentagens, autopct='%1.1f%%', startangle=angle, labels=rotulos, explode=explode)

#gráfico de barras
# graphic.bar(rotulos,porcentagens,color = 'blue',width = 0.4)
# graphic.set_aspect('auto')

plt.xlabel("Face do dado")
plt.ylabel("Porcentagem de lancamentos do dado")
plt.title("Dado viciado?")
plt.show()