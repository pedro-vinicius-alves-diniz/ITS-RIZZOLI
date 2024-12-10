matrix = [[2,0,4,5],
          [4,6,8,10],
          [0,1,77,3],
          [1,2,3,4]
          ]

colIndexZero = []

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 0:
            # print(f"C'è zero: {matrix[row]}")
            pass
            # matrix[row][0] = 0
            # matrix[row][1] = 0
            # matrix[row][2] = 0
            # matrix[row][3] = 0
            # print(f"C'è zero: {matrix.index(matrix[col])}")

            # matrix[0][matrix.index(matrix[col])] = 0
            # matrix[1][matrix.index(matrix[col])] = 0
            # matrix[2][matrix.index(matrix[col])] = 0
            # matrix[3][matrix.index(matrix[col])] = 0



# print(matrix[0])
# print(matrix[1])
# print(matrix[2])
# print(matrix[3])

indexRow = []
indexCol = []

for liste in matrix:
    # print(lista)
    for row in liste:
        if row == 0:
            indexRow.append(matrix.index(liste)) # Prendere gli indici delle righe che ci sono 0
            indexCol.append(liste.index(row))   # Prendere gli indici delle colone che ci sono 0

for zeri in indexRow:
    print(zeri)
    for i in range(len(matrix)):
        matrix[zeri][i] = 0 #Modificare i valori delle righe che ci sono 0 come 0

for zeri in indexCol:
    print(zeri)
    for i in range(len(matrix)):
        matrix[i][zeri] = 0 #Modificare i valori delle colone che ci sono 0 come 0




print(f"Le righe che ci sono zero sono: {indexRow}")
print(f"Le colone che ci sono zero sono: {indexCol}")
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])

"""
matrix = [
    [0,0,0,0],
    [0,0,8,10],
    [0,0,0,0].
    [0,0,3,4]
]
"""