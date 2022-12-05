def findRepeatedChar(line):
    lineLen = len(line) - 1     # Ignore newline
    usedChars = set()
    for i in range(int(lineLen / 2)):
        usedChars.add(line[i])
    for i in range(int(lineLen / 2), lineLen):
        if line[i] in usedChars:
            return line[i]
    raise Exception('Expected a repeated char')

def calcPriority(char):
    ch = ord(char)
    if ord('a') <= ch <= ord('z'):
        return ch - ord('a') + 1
    elif ord('A') <= ch <= ord('Z'):
        return ch - ord('A') + 27

def findCommonChar(groupLines):
    groupUsedChars = list()
    for line in groupLines:
        lineUsedChars = set()
        for char in line[:-1]:
            lineUsedChars.add(char)
        groupUsedChars.append(lineUsedChars)
    
    answerSet = groupUsedChars[0]
    for usedChars in groupUsedChars[1:]:
        answerSet = answerSet.intersection(usedChars)
    
    if len(answerSet) != 1:
        raise Exception('Found multiple common chars')
    
    for answer in answerSet:
        return answer

def mainPart1():
    totalPriority = 0
    with open("03input.txt") as file:
        for line in file:
            repeatedChar = findRepeatedChar(line)
            totalPriority += calcPriority(repeatedChar)
    print(totalPriority)

def mainPart2():
    totalPriority = 0
    with open("03input.txt") as file:
        while(firstLine := file.readline()):
            groupLines = [firstLine]
            for _ in range(3 - 1):
                groupLines.append(file.readline())
            commonChar = findCommonChar(groupLines)
            totalPriority += calcPriority(commonChar)
    print(totalPriority)
    pass

if __name__ == "__main__":
    mainPart2()