# mat = [
#     [0, 1, 2, 3, 4],
#     [9, 8, 7, 6, 5],
#     [4, 7, 8, 5, 1],
#     [2, 3, 4, 2, 9],
#     [1, 2, 5, 9, 7]
# ]
mat = [list(map(int, input().split())) for _ in range(5)]
# print(mat)

mat_trans = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
for y, row in enumerate(mat):
    for x, col in enumerate(row):
        mat_trans[x][y] = col

# print(mat_trans)

empty = 'null'

cases = int(input())
for case in range(cases):
    num = list(map(int, input().split()))
    assert len(num) == 2
    y, x = num
    west = ' '.join(map(str, mat[y][:x]))
    east = ' '.join(map(str, mat[y][x+1:]))
    north = ' '.join(map(str, mat_trans[x][:y]))
    south = ' '.join(map(str, mat_trans[x][y+1:]))
    # print(west)
    # print(east)
    # print(north)
    # print(south)
    print(f"The west neighbours of element {mat[y][x]} at position [{y}][{x}] are: {west if west else empty} end of list")
    print(f"The east neighbours of element {mat[y][x]} at position [{y}][{x}] are: {east if east else empty} end of list")
    print(f"The north neighbours of element {mat[y][x]} at position [{y}][{x}] are: {north if north else empty} end of list")
    print(f"The south neighbours of element {mat[y][x]} at position [{y}][{x}] are: {south if south else empty} end of list")
