import math


def maxNum(limit):
    f = open("day_1/input.txt")
    max_cals = 0

    temp_max_cals = 0

    for i in f.readlines():
        if i.strip() == "":
            if max_cals < temp_max_cals < limit:
                max_cals = temp_max_cals
            temp_max_cals = 0

        else:
            temp_max_cals += int(i)
    return max_cals


first_num = maxNum(math.inf)
print(first_num)
second_num = maxNum(first_num)
third_num = maxNum(second_num)
result = first_num + second_num + third_num

print(result)
