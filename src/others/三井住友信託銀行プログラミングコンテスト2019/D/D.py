from collections import defaultdict


def main():
    _ = input()
    S = input()
    S_idx = defaultdict(list)
    num_combs = 0
    for i in range(len(S)):
        S_idx[S[i]].append(i)

    for i in range(10):
        for j in range(10):
            for k in range(10):
                if not ((len(S_idx[str(i)]) == 0) or (len(S_idx[str(j)]) == 0) or (len(S_idx[str(k)]) == 0)):
                    s1_idx = S_idx[str(i)][0]
                    if not s1_idx >= S_idx[str(j)][-1]:
                        s2_idx = binary_search(S_idx[str(j)], s1_idx)
                        if not (s2_idx == -1 or s2_idx >= S_idx[str(k)][-1]):
                            num_combs += 1
    print(num_combs)


def binary_search(A, x):
    ok = len(A)
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] > x:
            ok = mid
        else:
            ng = mid
    if ok < len(A):
        return A[ok]
    else:
        return -1


if __name__ == '__main__':
    main()
