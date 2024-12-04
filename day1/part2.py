list = []
dict = {}

with open("input.txt") as input:
    for line in input:
        line = line.strip()
        splitLine = line.split(' ')
        n1 = int(splitLine[0])
        n2 = int(splitLine[len(splitLine)-1])
        list.append(n1)
        if n2 in dict:
            dict[n2] += 1
        else:
            dict[n2] = 1

total = 0

for n in list:
    if n in dict:
        total += n * dict[n]

print(total)