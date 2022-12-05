file = open("input.txt")

Result = 0

for i in file:

    if i != '\n':
        firstHalf = i[0:len(i) // 2]
        secondHalf = i[len(i) // 2:-1]

        tempList = list(set(firstHalf) & set(secondHalf))
        if tempList[0].isupper():
            Result += ord(tempList[0]) - 38
        elif tempList[0].islower():
            Result += ord(tempList[0]) - 96

print(Result)

# part 2
Result_two = 0

f = open("input.txt")
a = iter(f)

for x, y, z in zip(*[a, a, a]):

    firstElf = x
    secondElf = y
    thirdElf = z

    tempList = list(set(firstElf) & set(secondElf) & set(thirdElf))
    tempList.remove('\n')
    if tempList[0].isupper():
        Result_two += ord(tempList[0]) - 38
    elif tempList[0].islower():
        Result_two += ord(tempList[0]) - 96

print(Result_two)
