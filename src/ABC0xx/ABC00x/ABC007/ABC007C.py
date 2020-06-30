from collections import deque


def main():
    R, C = map(int, input().split())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    m = [list(input()) for _ in range(R)]
    g = [[[] for _ in range(C)] for _ in range(R)]
    seen = [[0] * C for _ in range(R)]
    q = deque()

    for r in range(R):
        for c in range(C):
            r_idx = r - 1
            c_idx = c - 1

            if c_idx > 0 and m[r_idx][c_idx-1] != "#":
                g[r_idx][c_idx].append((r_idx, c_idx-1))
            if r_idx > 0 and m[r_idx-1][c_idx] != "#":
                g[r_idx][c_idx].append((r_idx-1, c_idx))
            if r_idx < R-1 and m[r_idx+1][c_idx] != "#":
                g[r_idx][c_idx].append((r_idx+1, c_idx))
            if c_idx < C-1 and m[r_idx][c_idx+1] != "#":
                g[r_idx][c_idx].append((r_idx, c_idx+1))

    q.append((sx-1, sy-1))
    while q:
        v = q.popleft()
        for i in g[v[0]][v[1]]:
            if seen[i[0]][i[1]]:
                continue
            seen[i[0]][i[1]] = seen[v[0]][v[1]] + 1
            q.append(i)

    print(seen[gx-1][gy-1])


if __name__ == '__main__':
    main()
