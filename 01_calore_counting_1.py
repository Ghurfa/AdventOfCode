best = 0
with open("01input.txt") as file:
    while (line := file.readline()):
        elfSum = int(line)
        while ((line := file.readline()) and (line != '\n')):
            elfSum += int(line)
        
        if (elfSum > best):
            best = elfSum

print(best)