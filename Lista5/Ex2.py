import random

# Ao invés de ler vou sortear
v = []
for i in range(5):
    v.append(random.randint(1,5))

print(v)

for i in range(5):
    print(i,' * ',v[i],' = ', i * v[i])

