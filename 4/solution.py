from collections import Counter
import numpy as np
from datetime import datetime, date, time

class Guard:
    def __init__(self, id, shifts, minutesAsleep, totalSleep):
        self.id = id
        self.shifts = {}
        self.minutesAsleep = []
        self.totalSleep = totalSleep

    def calculateSleepHours(self):
        for key, val in self.shifts.iteritems():
            for i in range(len(val[0])):
                self.minutesAsleep += range(val[0][i], val[1][i])
                self.totalSleep += ((val[1][i] - 1) - val[0][i])


class NightAction:
    def __init__(self, date, action):
        self.date = date
        self.action = action

def partOne():
    filepath = 'input.txt'
    shifts = []
    guards = []
    test = []

    with open(filepath) as fp:
        lines = fp.readlines()
        for line in lines:
            timeStr = str(line.split(']')[0].split(' ')[1])
            testDate = str(line.split(']')[0].split(' ')[0].split('-')[1]) + '/' + str(line.split(']')[0].split(' ')[0].split('-')[2] + " " + timeStr)
            datetime_object = datetime.strptime(testDate, '%m/%d %H:%M')
            action = str(line.split(']')[1])

            test.append(NightAction(datetime_object, action))

    final = {}
    actions = sorted(test, key=lambda x: x.date, reverse=False)
    for t in actions:
        if 'Guard' in t.action:
            guard = t.action.split(' ')[2]
            final[guard] = []

    currGuard = ''
    for t in actions:
        if 'Guard' in t.action:
            currGuard = t.action.split(' ')[2]
        else:
            final[currGuard].append(t.date.minute)

    fullData = {}
    for key, val in final.iteritems():
        i = 0
        if key not in fullData.keys():
            fullData[key] = []
        while i < len(val) - 2:
            fullData[key] += list(range(val[i], val[i + 1]))
            i += 2

    print(sorted(fullData['#2663']), Counter(fullData['#2663']))
    partTwo(fullData)


def partTwo(guardData):
    minTracker = {}

    for key, val in guardData.iteritems():
        minTracker[key] = [0] * 60

    for k, v in guardData.iteritems():
        for _ in v:
            minTracker[k][_] += 1

    maxSleeper = 0
    maxSleeperGuard = None

    for k, v in minTracker.iteritems():
        print(k, max(v))
        if max(v) > maxSleeper:
            maxSleeper = max(v)
            maxSleeperGuard = k

    print(minTracker[maxSleeperGuard])
    print(minTracker[maxSleeperGuard].index(maxSleeper))
    print(maxSleeperGuard)


partOne()
