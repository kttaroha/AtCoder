from collections import defaultdict


def main():

    def is_in(a, b):
        return (a, b) in nums_points

    flag = 0
    mat = [
        list(map(int, input().split())),
        list(map(int, input().split())),
        list(map(int, input().split()))
    ]

    n = int(input())
    nums = [int(input()) for i in range(n)]

    combs = defaultdict(int)
    for i in range(3):
        for j in range(3):
            combs[mat[i][j]] = (i, j)

    nums_points = []
    for n in nums:
        nums_points.append(combs[n])

    if is_in(0, 0) and is_in(0, 1) and is_in(0, 2):
        flag += 1
    if is_in(1, 0) and is_in(1, 1) and is_in(1, 2):
        flag += 1
    if is_in(2, 0) and is_in(2, 1) and is_in(2, 2):
        flag += 1
    if is_in(0, 0) and is_in(1, 0) and is_in(2, 0):
        flag += 1
    if is_in(0, 1) and is_in(1, 1) and is_in(2, 1):
        flag += 1
    if is_in(0, 2) and is_in(1, 2) and is_in(2, 2):
        flag += 1
    if is_in(0, 0) and is_in(1, 1) and is_in(2, 2):
        flag += 1
    if is_in(0, 2) and is_in(1, 1) and is_in(2, 0):
        flag += 1

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
