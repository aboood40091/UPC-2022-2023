from math import sqrt

cases = int(input())
for case in range(cases):
    s = input()
    n = len(s) // 8
    cnum = round(sqrt(n) + 0.0001)
    assert cnum ** 2 == n
    mat = [[0 for oof1 in range(cnum)] for oof2 in range(cnum)]
    y = 0
    x = 0
    for i in range(0, len(s), 8):
        c = s[i:i+8]
        n = int(c, 2)

        mat[y][x] = (n).to_bytes().decode()
        y += 1
        if y >= cnum:
            y = 0
            x += 1
            
    print(''.join(''.join(row) for row in mat))
        
