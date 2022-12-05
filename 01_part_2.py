sums = []
numOfTop = 3
with open("01input.txt") as file:
    while (line := file.readline()):
        elfSum = int(line)
        while ((line := file.readline()) and (line != '\n')):
            elfSum += int(line)
        
        sums.append(elfSum)

if (len(sums) < numOfTop):
    raise Exception('Need more elves')

sums.sort()
answer = sum(sums[-numOfTop:])
print(answer)