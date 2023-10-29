i = 1

while True:
    m, f, s = map(int, input().split())
    if m == 0 and f == 0 and s == 0:
        break

    assert 1 <= m <= 10
    assert 1 <= f <= 10
    assert 1 <= s <= 100
    ms = input().split()
    assert(len(ms) == m)
    fs = input().split()
    assert(len(fs) == f)

    mmax = 0
    fmax = 0
    
    for case in range(s):
        inp = input().split()
        n = int(inp[0])
        actors = inp[1:]
        mn = sum((1 if actor in ms else 0) for actor in actors)
        if mn > mmax:
            mmax = mn
        fn = sum((1 if actor in fs else 0) for actor in actors)
        if fn > fmax:
            fmax = fn

    if i > 1:
        print()

    print(f"Movie #{i}")
    i += 1

    mas = "actor" if mmax == 1 else "actors"
    fas = "actress" if fmax == 1 else "actresses"
    
    print(f"You need {mmax} {mas} and {fmax} {fas}.")
