cases = int(input())
hall = 360 / 12
mall = 360 / 60
for case in range(cases):
    h, m = map(int, input().split())
    assert 1 <= h <= 12
    assert 0 <= m <= 59
    if h == 12:
        h = 0
    ha = h * hall
    ma = m * mall
    # print(h, ha, m, ma)
    a = abs(ha - ma)
    if a > 180:
        a -= 180
    print('%0.3f' % a)
