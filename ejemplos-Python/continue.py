userWord = (input("ingrese una plabra : "))
userWord = userWord.upper()
# print(userWord)
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for letra in userWord:
    print(letra)
    if letra in vocales:
        print("vocales: ", letra)
