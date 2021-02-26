import sys
from datetime import datetime
posibilidades = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
                 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
justo_este_minuto = datetime.today().minute
if justo_este_minuto in posibilidades:
    print("Este minuto parese una pequeña posibildad | ", justo_este_minuto)
else:
    print("Este minuto no es posible | ", justo_este_minuto)
