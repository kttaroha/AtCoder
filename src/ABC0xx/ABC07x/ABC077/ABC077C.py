def main():
    _ = int(input())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))

    B_ = []
    B_accum = []
    ans = 0

    for b in B:
        num = binary_search(A, b) + 1
        B_.append((b, num))

    tmp_sum = 0
    for b_ in B_:
        tmp_sum += b_[1]
        B_accum.append(tmp_sum)

    for c in C:
        b_idx = binary_search_tuple(B_, c)
        if b_idx >= 0:
            ans += B_accum[b_idx]
    print(ans)


def binary_search(A, x):
    ok = -1
    ng = len(A)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok


def binary_search_tuple(A, x):
    ok = -1
    ng = len(A)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid][0] < x:
            ok = mid
        else:
            ng = mid
    return ok


if __name__ == '__main__':
    main()
