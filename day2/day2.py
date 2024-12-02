total = 0

with open("input.txt") as input:
    for line in input:
        nums = line.strip().split(" ")
        ascending = nums[0] < nums[1]
        print(nums)