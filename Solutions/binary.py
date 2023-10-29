getw = lambda n: bin(n).count('1')

cases = int(input())
for case in range(cases):
    n = int(input())
    w = getw(n)
    m = n + 1
    while True:
        if getw(m) == w:
            break
        m += 1
    print(m)
