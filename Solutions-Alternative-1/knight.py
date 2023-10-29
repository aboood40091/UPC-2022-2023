import sys
from math import dist


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solve():
    cases = int(sys.stdin.readline())
    for cur_case in range(cases):
        xs, ys = [int(x) for x in sys.stdin.readline().split()]
        xt, yt = [int(x) for x in sys.stdin.readline().split()]
        forbs = []
        cur_x, cur_y = [int(x) for x in sys.stdin.readline().split()]
        while cur_x != -1:
            forbs.append([cur_x, cur_y])
            cur_x, cur_y = [int(x) for x in sys.stdin.readline().split()]
        visited = []
        min_steps = [[10_000 for x in range(8)] for y in range(8)]
        x, y = [xs, ys]
        visit(xs, ys, forbs, visited, xt, yt, min_steps)
        vis_n = (min_steps[xt - 1][yt - 1])
        if(vis_n==10_000):
            vis_n = -1

        visited = []
        min_steps = [[10_000 for x in range(8)] for y in range(8)]
        x, y = [xs, ys]
        super_visit(xs, ys, forbs, visited, xt, yt, min_steps)
        super_vis_n = min_steps[xt - 1][yt - 1]
        if (super_vis_n == 10_000):
            super_vis_n = -1
        print(vis_n, super_vis_n)

def get_super_possibles(x, y, forbs):
    poss = []
    poss.append([x + 1, y + 2])
    poss.append([x + 1, y - 2])
    poss.append([x + 2, y + 1])
    poss.append([x + 2, y - 1])
    poss.append([x - 1, y + 2])
    poss.append([x - 1, y - 2])
    poss.append([x - 2, y + 1])
    poss.append([x - 2, y - 1])
    poss.append([x - 2, y - 2])
    poss.append([x - 2, y + 2])
    poss.append([x + 2, y - 2])
    poss.append([x + 2, y + 2])
    poss = [x for x in poss if x not in forbs]
    poss = [[x, y] for x, y in poss if (x >= 1) and (x <= 8) and  (y>=1) and (y <= 8)]
    return poss


def get_possibles(x, y, forbs):
    poss = []
    poss.append([x + 1, y + 2])
    poss.append([x + 1, y - 2])
    poss.append([x + 2, y + 1])
    poss.append([x + 2, y - 1])
    poss.append([x - 1, y + 2])
    poss.append([x - 1, y - 2])
    poss.append([x - 2, y + 1])
    poss.append([x - 2, y - 1])
    poss = [x for x in poss if x not in forbs]
    poss = [[x, y] for x, y in poss if (x >= 1) and (x <= 8) and 1 <= y <= 8]
    return poss


def super_visit(x, y, forbs, visited, xt, yt, min_steps):
    if x == xt and x == yt:
        pass
    visited.append([x, y])
    for poss_x, poss_y in get_super_possibles(x, y, forbs):
        if len(visited) < min_steps[poss_x - 1][poss_y - 1]:
            min_steps[poss_x - 1][poss_y - 1] = int(len(visited))
            super_visit(poss_x, poss_y, forbs, visited, xt, yt, min_steps)
    visited.remove([x, y])
    return


def visit(x, y, forbs, visited, xt, yt, min_steps):
    if x == xt and x == yt:
        pass
    visited.append([x, y])
    for poss_x, poss_y in get_possibles(x, y, forbs):
        if len(visited) < min_steps[poss_x - 1][poss_y - 1]:
            min_steps[poss_x - 1][poss_y - 1] = int(len(visited))
            visit(poss_x, poss_y, forbs, visited, xt, yt, min_steps)
    visited.remove([x, y])
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
