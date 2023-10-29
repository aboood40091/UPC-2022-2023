from math import sqrt


while True:
    n = int(input())
    if n == 0:
        continue

    if n < 0:
        break

    bruh = []

    for _ in range(n):
        x1, y1, x2, y2 = list(map(int, input().split()))
        # print(x1, y1, x2, y2)
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        bruh.append((dist, (x1, y1, x2, y2)))

    bruh.sort(key=lambda x: x[0])
    dist, (x1, y1, x2, y2) = bruh[-1]
    print(x1, y1, x2, y2, '%.4f' % dist)
