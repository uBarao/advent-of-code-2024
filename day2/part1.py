def isSafe(levels):
    isDecreasing = True
    isIncresing = True

    for i in range(1,len(levels)):
        difference = levels[i] - levels[i-1]

        if difference > 3 or difference < -3 or difference == 0:
            return False
        
        if difference < 0:
            isIncresing = False
        elif difference > 0:
            isDecreasing = False

    return isIncresing or isDecreasing

with open("input.txt") as input:
    total = 0
    for line in input:
        if isSafe([int(i) for i in line.strip().split(' ')]):
            total += 1
    print(total)