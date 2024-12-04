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
        originalLevels = [int(i) for i in line.strip().split(' ')]
        if isSafe(originalLevels):
            total += 1
        else:
            for i in range(len(originalLevels)):
                shallowLevels = originalLevels.copy()
                shallowLevels.pop(i)
                if isSafe(shallowLevels):
                    total += 1
                    break
    print(total)