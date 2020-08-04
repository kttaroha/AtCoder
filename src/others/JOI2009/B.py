def binary_search(A, x):
    ok = -1
    ng = len(A)
    while abs(ok-ng) > 1:
        mid = (ok+ng) // 2
        if A[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    d = int(input())
    n = int(input()) - 1
    m = int(input())
    D = [0]
    for _ in range(n):
        D.append(int(input()))
    D.append(d)
    D = sorted(D)
    M = sorted([int(input()) for _ in range(m)])
    sum_dist = 0

    for m in M:
        idx = binary_search(D, m)
        sum_dist += min(abs(D[idx]-m), abs(D[idx+1]-m))

    print(sum_dist)


if __name__ == '__main__':
    main()
