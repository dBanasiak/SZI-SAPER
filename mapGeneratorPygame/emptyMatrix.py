# Dwuwymiarowa pusta tabilca
def emptyMatrix():
    emptyMatrix = []
    for row in range(20):
        emptyMatrix.append([])
        for column in range(20):
            emptyMatrix[row].append(0)

    emptyMatrix[0][0] = 1
    print('Empty matrix:')
    for row in emptyMatrix:
        print(row)
    return emptyMatrix
