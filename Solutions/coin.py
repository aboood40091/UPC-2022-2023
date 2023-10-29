cases = int(input())
for case in range(cases):
    countx = 0
    county = 0
    won = False
    while True:
        x, y = map(int, input().split())
        if x == -1 and y == -1:
            break

        if won:
            continue

        countx += x
        if countx >= 100:
            print("The winner is the husband.")
            won = True

        county += y
        if county >= 100:
            print("The winner is the wife.")
            won = True
