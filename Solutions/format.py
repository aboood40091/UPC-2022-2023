def read(s):
    s = s.strip()
    if s[0] != '"':
        a = s.split()[0]
        return a, s[len(a):]

    o = []
    for c in s[1:]:
        if c == '"':
            break
        o.append(c)

    return ''.join(o), s[len(o) + 2:].strip()

i = 1

while True:
    inp = input().split()
    if int(inp[0]) == 0:
        break

    r, n = map(int, inp[:2])
    rest = ' '.join(inp[2:])
    p1, p2s = read(rest)
    p2, _ = read(p2s)
    first = (r // n) % 2 != 0
    print(f"{i}. {p1 if first else p2}")
    i += 1
    
