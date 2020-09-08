from collections import deque


def BFS(start_h, start_w, end, time_total, W, H, G):
    INF = float("inf")
    steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.append((start_h, start_w))
    g = [[INF] * W for _ in range(H)]
    g[start_h][start_w] = 0

    while q:
        h, w = q.popleft()
        if G[h][w] == end:
            time_total += g[h][w]
            return time_total, h, w

        for s in steps:
            h_, w_ = h + s[0], w + s[1]
            if (h_ >= 0 and w_ >= 0
                    and h_ < H and w_ < W
                    and G[h_][w_] != "X" and g[h_][w_] == INF):
                q.append((h_, w_))
                g[h_][w_] = g[h][w] + 1


def main():
    H, W, N = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    time_total = 0

    for i in range(H):
        for j in range(W):
            if G[i][j] == "S":
                h, w = i, j

    for num in range(1, N+1):
        time_total, h, w = BFS(h, w, str(num), time_total, W, H, G)

    print(time_total)


if __name__ == '__main__':
    main()
