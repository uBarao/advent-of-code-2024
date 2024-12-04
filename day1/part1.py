list1 = []
list2 = []

with open("input.txt") as input:
    for line in input:
        line = line.strip()
        splitLine = line.split(' ')
        list1.append(int(splitLine[0]))
        list2.append(int(splitLine[len(splitLine)-1]))

list1.sort()
list2.sort()

total = 0

for i in range(min(len(list1),len(list2))):
    total += abs(list1[i]-list2[i])

print(total)