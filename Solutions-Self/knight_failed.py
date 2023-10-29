from math import sqrt

memo = {}
traps = []
visited = []
end = None

def knight(x1, y1):
    # print(x1, y1)
    if (x1, y1) in memo:
        return memo[(x1, y1)]

    if x1 < 1 or x1 > 8:
        return 2000

    if y1 < 1 or y1 > 8:
        return 2000

    if (x1, y1) in traps:
        return 2000

    if (x1, y1) == end:
        return 0

    if (x1, y1) in visited:
        return 2000

    visited.append((x1, y1))

    points = [
        (x1 + 1, y1 + 2),
        (x1 + 2, y1 + 1),
        (x1 + 1, y1 - 2),
        (x1 + 2, y1 - 1),
        (x1 - 1, y1 + 2),
        (x1 - 2, y1 + 1),
        (x1 - 1, y1 - 2),
        (x1 - 2, y1 - 1)
    ]

    points.sort(key=lambda p: sqrt((end[0] - p[0]) ** 2 + (end[1] - p[1]) ** 2))

    res = 1 + min(knight(*p) for p in points)

    del visited[-1]

    memo[(x1, y1)] = res
    return res

def superknight(x1, y1):
    if (x1, y1) in memo:
        return memo[(x1, y1)]

    if x1 < 1 or x1 > 8:
        return 2000

    if y1 < 1 or y1 > 8:
        return 2000

    if (x1, y1) in traps:
        return 2000

    if (x1, y1) == end:
        return 0

    if (x1, y1) in visited:
        return 2000

    visited.append((x1, y1))

    points = [
        (x1 + 2, y1 + 2),
        (x1 + 1, y1 + 2),
        (x1 + 2, y1 + 1),
        (x1 + 1, y1 - 2),
        (x1 + 2, y1 - 1),
        (x1 + 2, y1 - 2),
        (x1 - 1, y1 + 2),
        (x1 - 2, y1 + 1),
        (x1 - 2, y1 + 2),
        (x1 - 1, y1 - 2),
        (x1 - 2, y1 - 1),
        (x1 - 2, y1 - 2)
    ]

    points.sort(key=lambda p: sqrt((end[0] - p[0]) ** 2 + (end[1] - p[1]) ** 2))

    res = 1 + min(superknight(*p) for p in points)

    del visited[-1]

    memo[(x1, y1)] = res
    return res

cases = int(input())
for case in range(cases):
    x1, y1 = map(int, input().split())
    end = tuple(map(int, input().split()))

    traps = []
    while True:
        trap = tuple(map(int, input().split()))
        if trap == (-1, -1):
            break
        traps.append(trap)

    memo = {}
    visited = []
    # print(x1, y1)
    # print(end)
    # print(traps)
    # print(memo)
    # raise Exception from None
    a = knight(x1, y1)
    if a >= 2000:
        a = -1
    # print(a)

    memo = {}
    visited = []
    b = superknight(x1, y1)
    if b >= 2000:
        b = -1
    # print(b)

    print(a, b)
