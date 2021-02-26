# palabra = "Python"
# for letra in palabra:
#     print(letra)

# for i in range(1, 10):
#     if i % 2 == 0:
#         print(i)
# *******************************
texto = "pyxpyxpyx"

for letra in texto:
    if letra == "x":
        continue
    print(letra, end="*")

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
# *******************************
