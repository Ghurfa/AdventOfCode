def calcScore(opponent, you):
    gameScores = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }
    shapeScores = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    return gameScores[(opponent, you)] + shapeScores[you]

def calcScorePart2(opponent, outcome):
    gameScores = {
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    shapeScores = {
        ('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
        ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
        ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
    }
    return gameScores[outcome] + shapeScores[(opponent, outcome)]

def main():
    score = 0
    with open("02input.txt") as file:
        for line in file:
            opponent = line[0]
            second = line[2]
            # score += calcScore(opponent, second)
            score += calcScorePart2(opponent, second)
    print(score)

if __name__ == "__main__":
    main()