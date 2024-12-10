input = ""
total = 0

ordering = {}
paging = []

def validPage(page):
    for number in range(len(page)):
        for number_to_verify in range(number):
            if page[number] not in ordering:
                continue
            if page[number_to_verify] in ordering[page[number]]:
                return False
    return True

def newOrder(oldPage):
    newPage = []
    while len(oldPage) > 0:
        putI = False
        for i in range(len(oldPage)):
            for j in range(len(oldPage)):
                if oldPage[j] not in ordering:
                    continue
                if j != i and oldPage[i] in ordering[oldPage[j]]:
                    break
            else:
                putI = True
            if putI:
                newPage.append(oldPage.pop(i))
                break
    return newPage

for line in open("input.txt"):
    input += line
input = input.split("\n\n")

for order in input[0].split("\n"):
    order = order.split('|')
    o1, o2 = order[0], order[1]
    if o1 not in ordering:
        ordering[o1] = []
    ordering[o1].append(o2)

for page in input[1].split("\n"):
    paging.append(page.split(','))

for page in paging:
    if not validPage(page):
        newPage = newOrder(page)
        total += int(newPage[len(newPage)//2])

print(total)