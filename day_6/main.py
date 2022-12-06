file = open("Input.txt")

line = file.readline()
signalChars = []


def findSignalChar(size):
    i = 0
    while len(signalChars) != size:
        if len(signalChars) == 0:
            signalChars.append(line[i])
        else:
            if line[i] not in signalChars:
                signalChars.append(line[i])
            else:
                temp = signalChars[-1]
                signalChars.clear()
                signalChars.append(temp)
                signalChars.append(line[i])
        i += 1
    return i

print(findSignalChar(4))
print(findSignalChar(14))
