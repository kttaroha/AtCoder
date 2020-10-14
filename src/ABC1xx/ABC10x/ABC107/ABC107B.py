def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    row_drop = []
    col_drop = []
    for i in range(H):
        cnt_white = 0
        for j in range(W):
            if G[i][j] == ".":
                cnt_white += 1
        if cnt_white == W:
            row_drop.append(i)

    for i in range(W):
        cnt_white = 0
        for j in range(H):
            if G[j][i] == ".":
                cnt_white += 1
        if cnt_white == H:
            col_drop.append(i)

    G_new = []
    for i in range(H):
        if i in row_drop:
            continue
        row = []
        for j in range(W):
            if j in col_drop:
                continue
            row.append(G[i][j])
        G_new.append(row)

    for g in G_new:
        print("".join(g))


if __name__ == '__main__':
    main()
