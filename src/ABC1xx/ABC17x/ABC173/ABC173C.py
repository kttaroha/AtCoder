def main():
    H, W, K = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    combs = []
    total_blacks = 0
    ans = 0
    for a in A:
        for a_ in a:
            if a_ == "#":
                total_blacks += 1

    for i in range(2**(H+W)):
        tmp_combs = []
        for j in range(H+W):
            if (i >> j) & 1:
                tmp_combs.append(1)
            else:
                tmp_combs.append(0)
        combs.append(tmp_combs)

    for c in combs:
        num_black = total_blacks
        for i in range(H):
            for j in range(W):
                h, w = c[i], c[H+j]
                if (h == 1 or w == 1) and A[i][j] == "#":
                    num_black -= 1

        if num_black == K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
