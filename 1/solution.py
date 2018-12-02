
filepath = 'input.txt'
with open(filepath) as fp:  
    lines = fp.readlines()
    cnt = 0
    currFreq = [0]
    i = 0
    found = False
    while i < len(lines) and found is False:
        cnt += int(lines[i].strip())
        print(cnt)
        if cnt in currFreq:
            print("FOUND: ", cnt)
            found = True
        else:
            currFreq.append(cnt)
            if i == len(lines)-1:
                i = 0
            else:
                i += 1
