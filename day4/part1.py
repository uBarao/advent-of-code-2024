xmasCount = 0
list = []

directions = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (1, 1),
    (-1, -1),
    (1, -1)
]

def xmasFinder(x,y,map):
    for dir in directions:
        if y+dir[1]*3 < 0 or y+dir[1]*3 >= len(map):
            continue
        if x+dir[0]*3 < 0 or x+dir[0]*3 >= len(map[y]):
            continue
        if map[y+dir[1]][x+dir[0]] == 'M' and map[y+dir[1]*2][x+dir[0]*2] == 'A' and map[y+dir[1]*3][x+dir[0]*3] == 'S':
            global xmasCount
            xmasCount += 1

with open("input.txt") as input:
    for line in input:
        list.append(line.strip())

for y in range(len(list)):
    for x in range(len(list[y])):
        if list[y][x] == 'X':
            xmasFinder(x,y,list)

print(xmasCount)