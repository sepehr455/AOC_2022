file = open("input.txt")

boxStacks = [
    ["T", "D", "W", "Z", "V", "P"],
    ["L", "S", "W", "V", "F", "J", "D"],
    ["Z", "M", "L", "S", "V", "T", "B", "H"],
    ["R", "S", "J"],
    ["C", "Z", "B", "G", "F", "M", "L", "W"],
    ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    ["V", "J", "P", "C", "B", "D", "N"],
    ["P", "T", "B", "Q"],
    ["H", "G", "Z", "R", "C"]
]
lines = file.readlines()

# Part 1
for i in lines:
    editedLine = i.replace("move", "").replace("from", "").replace("to", "").strip()
    nums = editedLine.split(' ')

    while "" in nums:
        nums.remove("")
    numberOfBoxes = int(nums[0])
    moveFrom = int(nums[1]) - 1
    moveTo = int(nums[2]) - 1

    for j in range(numberOfBoxes):
        temp = boxStacks[moveFrom].pop()
        boxStacks[moveTo].append(temp)

for i in boxStacks:
    print(i[-1])

# Part 2

boxStacks_2 = [
    ["T", "D", "W", "Z", "V", "P"],
    ["L", "S", "W", "V", "F", "J", "D"],
    ["Z", "M", "L", "S", "V", "T", "B", "H"],
    ["R", "S", "J"],
    ["C", "Z", "B", "G", "F", "M", "L", "W"],
    ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    ["V", "J", "P", "C", "B", "D", "N"],
    ["P", "T", "B", "Q"],
    ["H", "G", "Z", "R", "C"]
]

for i in lines:
    editedLine = i.replace("move", "").replace("from", "").replace("to", "").strip()
    nums = editedLine.split(' ')

    while "" in nums:
        nums.remove("")

    numberOfBoxes = int(nums[0])
    moveFrom = int(nums[1]) - 1
    moveTo = int(nums[2]) - 1

    boxIndex = numberOfBoxes * (-1)

    for j in range(numberOfBoxes):
        print(f"{boxStacks_2[moveFrom] = }")
        print(f"{moveFrom = }")

        temp = boxStacks_2[moveFrom].pop(boxIndex)
        boxStacks_2[moveTo].append(temp)
        boxIndex += 1

for i in boxStacks_2:
    print(i[-1])


