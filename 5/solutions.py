def partOne():
    filepath = 'input.txt'
    input = ''
    with open(filepath) as fp:
        lines = fp.readlines()
        input = lines[0]

    c = 0
    temp = list(input)
    while c < len(temp) - 1:
        if temp[c] != temp[c+1] and temp[c].lower() == temp[c + 1].lower():
            temp.pop(c)
            temp.pop(c)
            c = 0
        else:
            c += 1

def reactPolymer(input):
    temp = list(input)
    c = 0
    while c < len(temp) - 1:
        if temp[c] != temp[c+1] and temp[c].lower() == temp[c + 1].lower():
            temp.pop(c)
            temp.pop(c)
            c = 0
        else:
            c += 1
    return len(temp)

def calculateLength(input, a):
    temp = input
    c = 0
    while c < len(temp):
        if temp[c] == a or temp[c] == a.upper():
            temp.pop(c)
        else:
            c += 1
    return reactPolymer(temp)

def partTwo():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    results = {}

    filepath = 'input.txt'
    input = ''
    with open(filepath) as fp:
        lines = fp.readlines()
        input = lines[0][:-1]

    for a in alpha:
        temp = list(input)
        results[a] = calculateLength(temp, a)

    print(results)

#partOne()
partTwo()
