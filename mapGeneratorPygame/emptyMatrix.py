# Dwuwymiarowa pusta tabilca
def emptyMatrix():
    emptyMatrix = []
    for row in range(10):
        emptyMatrix.append([])
        for column in range(10):
            emptyMatrix[row].append(0)

    emptyMatrix[0][0] = 1
    print('\nEmpty matrix:')
    for row in emptyMatrix:
        print(row)
    return emptyMatrix
