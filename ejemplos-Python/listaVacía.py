miLista = []
miLista2 = []

for j in range(10):
    miLista.append(j)

print(miLista)
print("nueva linea")

for i in range(10):
    miLista2.insert(0, i)

print(miLista2)

miLista3 = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista3)):
    suma += miLista3[i]
#    print(miLista3[i])
print(suma)
