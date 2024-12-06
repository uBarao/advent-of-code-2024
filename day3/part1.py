import re

total = 0

regex = r"mul\(\d{1,3}\,\d{1,3}\)"

with open("input.txt") as input:
    for line in input:
        result = re.findall(regex, line)
        for operation in result:
            op = operation.replace("mul(","").replace(")","").split(",")
            total += int(op[0]) * int(op[1])

print(total)