# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)

# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1


# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         continue
#     print(ch, end="")


# for digito in "0165031806510":
#     if digito == "0":
#         print("x", end="")
#         continue
#     print(digito, end="")


# n = 3
# while n > 0:
#     print(n+1)
#     n -= 1
# else:
#     print(n)


# for numero in range(4):
#     print(numero-1)
# else:
#     print(numero)

# for i in range(0, 6, 3):
#     print(i)
# else:
#     print(i)


# x = 7
# y = 1

# a = x & y
# b = x | y
# c = ~ x
# d = x ^ 5
# e = x >> 2
# f = x << 2

# print(a, b, c, d, e, f)
# print(x)
# print(~x)

# numeros = [2, 4, 5, 6, 7, 9, 23, 14, 64, 75]

# print("tamaño de la lista: ", len(numeros))
# print(numeros)
# del (numeros[9])
# print(numeros)
listaSombrero = [1, 2, 3, 4, 5]
#nuevonum = [1, 2, 9, 4, 5]
nuevonum = int(input("ingrese un numero: "))

print("antes: ", listaSombrero)
listaSombrero[2] = nuevonum
print("despues: ", listaSombrero)
del(listaSombrero[4])
print("tamaño de la lista: ", len(listaSombrero))
print(listaSombrero)
