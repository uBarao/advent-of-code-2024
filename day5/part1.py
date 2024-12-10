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
    if validPage(page):
        total += int(page[len(page)//2])

print(total)