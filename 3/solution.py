def partOne():
    filepath = 'input.txt'
    # first we need to figure out the grid size
    size = 10000
    grid = [[0] * size for i in range(size)]
    for i in range(size):
        grid.append([])
    with open(filepath) as fp:
        lines = fp.readlines()
        for line in lines:
            test = line.split(' ')
            x = int(test[2].split(',')[0])
            y = int(test[2].split(',')[1][:-1])
            width = int(test[3].split('x')[0])
            height = int(test[3].split('x')[1])
            for i in range(width):
                for j in range(height):
                    grid[i+x][y+j] += 1
    flat = [j for x in grid for j in x]
    count = 0
    for num in flat:
        if num > 1:
            count += 1

    return count

def partTwo():
    filepath = 'input.txt'
    # first we need to figure out the grid size
    size = 10000
    grid = [[{}] * size for i in range(size)]
    for i in range(size):
        grid.append([])
    with open(filepath) as fp:
        lines = fp.readlines()
        for line in lines:
            test = line.split(' ')
            id = test[0]
            x = int(test[2].split(',')[0])
            y = int(test[2].split(',')[1][:-1])
            width = int(test[3].split('x')[0])
            height = int(test[3].split('x')[1])
            for i in range(width):
                for j in range(height):
                    if (len(grid[i+x][y+j].values()) > 0 and grid[i+x][y+j].values()[0] >= 1):
                        grid[i+x][y+j][grid[i+x][y+j].keys()[0]].append(str(id))
                    else:
                        grid[i+x][y+j] = {str(id): [str(id)]}
    flat = [j for x in grid for j in x]
    newTest = {}
    for d in flat:
        if len(d.keys()) > 0 and d.keys()[0] in newTest.keys():
            key = d.keys()[0]
            newTest[key] += d.values()[0]
        else:
            if len(d.keys()) > 0:
                newTest[d.keys()[0]] = d[d.keys()[0]]
    duplicates = []
    for key, val in newTest.iteritems():
        if len(set(val)) > 1:
            duplicates += list(set(val))

    for key, val in newTest.iteritems():
        if len(set(val)) == 1 and val[0] not in duplicates:
            print(key, val)


partTwo()
