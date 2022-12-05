file = open("input.txt")
lines = file.readlines()
total_score = 0


####PART 1####
def draw(x, y):
    if (x == "A" and y == "X") or (x == "B" and y == "Y") or (x == "C" and y == "Z"):
        return True

def win(x, y):
    if (x == "A" and y == "Y") or (x == "B" and y == "Z") or (x == "C" and y == "X"):
        return True

def loss(x, y):
    if (x == "A" and y == "Z") or (x == "B" and y == "X") or (x == "C" and y == "Y"):
        return True

def addShapePoint(x):
    if x == "X":
        return 1
    elif x == "Y":
        return 2
    elif x == "Z":
        return 3

for i in lines:

    p1 = i[0]
    p2 = i[2]
    if draw(p1, p2):
        total_score += 3 + addShapePoint(p2)
    elif win(p1, p2):
        total_score += 6 + addShapePoint(p2)
    elif loss(p1, p2):
        total_score += addShapePoint(p2)

print(total_score)

####PART 2####
new_total_score = 0


def beat(x):
    if x == "A":
        return 8
    elif x == "B":
        return 9
    elif x == "C":
        return 7

def loseTo(x):
    if x == "A":
        return 3
    elif x == "B":
        return 1
    elif x == "C":
        return 2

def drawWith(x):
    if x == "A":
        return 4
    elif x == "B":
        return 5
    elif x == "C":
        return 6

for i in lines:

    p1 = i[0]
    p2 = i[2]

    if p2 == "X":
        new_total_score += loseTo(p1)
    elif p2 == "Y":
        new_total_score += drawWith(p1)
    elif p2 == "Z":
        new_total_score += beat(p1)

print(new_total_score)
