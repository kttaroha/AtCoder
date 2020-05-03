from itertools import combinations_with_replacement


def main():
    N, M, Q = map(int, input().split())
    conds = [list(map(int, input().split())) for i in range(Q)]
    combs = combinations_with_replacement([i for i in range(1, M+1)], N)
    ans = 0
    for comb in combs:
        ans_ = 0
        for c in conds:
            if comb[c[1]-1] - comb[c[0]-1] == c[2]:
                ans_ += c[3]
        ans = max(ans, ans_)
    print(ans)


if __name__ == "__main__":
    main()
