from mapGeneratorPygame.setBomb import returnBombAndPos

startPos = (0, 0)

bombMatrix = returnBombAndPos()[0]
bombPos = returnBombAndPos()[1]
bombImgPos = []


x = 0
y = 0

# for row in range(10):
#     bombImgPos.append([])
#     for col in range(10):
#         bombImgPos[row].append(5)
#
# for row in bombImgPos:
#     print(row)


# def returnBombPos():
#     return bombPosList
#
# # zrob to petla
# bomb1Dist = bombPosList[0][0] + bombPosList[0][1]
# bomb2Dist = bombPosList[1][0] + bombPosList[1][1]
# bomb3Dist = bombPosList[2][0] + bombPosList[2][1]
# bomb4Dist = bombPosList[3][0] + bombPosList[3][1]
# bomb5Dist = bombPosList[4][0] + bombPosList[4][1]
#
# # posortuj
# bombDistList = [bomb1Dist, bomb2Dist, bomb3Dist, bomb4Dist, bomb5Dist]
# bombDistList.sort()

print('\nBomb Matrix')
for row in bombMatrix:
    print(row)
print('\nPositions on matrix:\n', bombPos)
