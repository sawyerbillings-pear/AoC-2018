def partOne():
    filepath = 'input.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
        threes = 0
        twos = 0
        for line in lines:
            counts = {}
            for c in list(line):
                if c in counts.keys():
                    counts[c] += 1
                else:
                    counts[c] = 1
            print(counts.values())
            if 3 in counts.values():
                threes += 1

            if 2 in counts.values():
                twos += 1
        print(twos * threes)

def partTwo():
    filepath = 'input.txt'
    with open(filepath) as fp:
        lines = fp.readlines()
        for line1 in lines:
            for line2 in lines:
                diff = 0
                charDiffs = []
                for i in range(0, len(line1)):
                    if line2[i] != line1[i]:
                        diff += 1
                        charDiffs.append(line1)
                        charDiffs.append(line2)
                if diff < 2:
                    print(charDiffs)

partTwo()

