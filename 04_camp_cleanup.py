def overlapFully(startA, endA, startB, endB):
    return ((startB >= startA and endB <= endA) or 
            (startA >= startB and endA <= endB))

def overlapAtAll(startA, endA, startB, endB):
    ret = ((startB >= startA and startB <= endA) or 
            (startA >= startB and startA <= endB))
    return ret

def main():
    overlapCount = 0
    with open("04input.txt") as file:
        for line in file:
            ranges = line.split(',')
            startA = int(ranges[0].split('-')[0])
            endA = int(ranges[0].split('-')[1])
            startB = int(ranges[1].split('-')[0])
            endB = int(ranges[1].split('-')[1])
            if overlapAtAll(startA, endA, startB, endB):
                overlapCount = overlapCount + 1
    print(overlapCount)

if __name__ == "__main__":
    main()