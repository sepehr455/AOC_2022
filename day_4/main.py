file = open("input.txt")

# part 1
total = 0


def fullyContained(num1, num2, num3, num4):
    if (num1 <= num3 and num2 >= num4) or (num3 <= num1 and num4 >= num2):
        return True
    else:
        return False


print(fullyContained(4, 4, 5, 11))
lines = file.readlines()

for i in lines:
    y = i.replace(",", " ").replace("-", " ").strip()
    elements = y.split(" ")
    num_1, num_2, num_3, num_4 = int(elements[0]), int(elements[1]), int(elements[2]), int(elements[3])

    if fullyContained(num_1, num_2, num_3, num_4):
        total += 1

print(total)

# part 2

total2 = 0


def overlap(num1, num2, num3, num4):
    if (num1 <= num3 <= num2) or (num1 <= num4 <= num2) or (num3 <= num1 <= num4) or (num3 <= num2 <= num4):
        return True
    else:
        return False


for i in lines:
    y = i.replace(",", " ").replace("-", " ").strip()
    elements = y.split(" ")
    num_1, num_2, num_3, num_4 = int(elements[0]), int(elements[1]), int(elements[2]), int(elements[3])

    if overlap(num_1, num_2, num_3, num_4):
        total2 += 1

print(total2)
