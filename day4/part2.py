x_masCount = 0

list = []

def x_masFinder(x,y,map):
    if x == 0 or y == 0 or y == len(map)-1 or x == len(map[x])-1:
        return

    top_left = map[y-1][x-1]
    top_right = map[y+1][x-1]
    down_right = map[y+1][x+1]
    down_left = map[y-1][x+1]

    if any(var not in {'M', 'S'} for var in (top_left, top_right, down_right, down_left)):
        return
    
    if top_left != down_right and top_right != down_left:
        global x_masCount
        x_masCount += 1

with open("input.txt") as input:
    for line in input:
        list.append(line.strip())

for y in range(len(list)):
    for x in range(len(list[y])):
        if list[y][x] == 'A':
            x_masFinder(x,y,list)

print(x_masCount)