startPos = (0, 0)

# zrob z tego liste
bombPosList = [(100, 20), (320, 0), (512, 64), (800, 64), (128, 128)]

def returnBombPos():
    return bombPosList

# zrob to petla
bomb1Dist = bombPosList[0][0] + bombPosList[0][1]
bomb2Dist = bombPosList[1][0] + bombPosList[1][1]
bomb3Dist = bombPosList[2][0] + bombPosList[2][1]
bomb4Dist = bombPosList[3][0] + bombPosList[3][1]
bomb5Dist = bombPosList[4][0] + bombPosList[4][1]

# posortuj
bombDistList = [bomb1Dist, bomb2Dist, bomb3Dist, bomb4Dist, bomb5Dist]
bombDistList.sort()

print(bombDistList)
