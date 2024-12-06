import re

total = 0

mulActive = True

regex = r"mul\(\d{1,3}\,\d{1,3}\)|don't\(\)|do\(\)"

with open("input.txt") as input:
    for line in input:
        result = re.findall(regex, line)
        for operation in result:
            if operation.startswith("mul") and mulActive:
                op = operation.replace("mul(","").replace(")","").split(",")
                total += int(op[0]) * int(op[1])
            elif operation == "don't()":
                mulActive = False
            elif operation == "do()":
                mulActive = True

print(total)