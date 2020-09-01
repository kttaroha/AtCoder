from collections import deque


def is_inside(x, y, W, H, G):
    return (x <= H-1 and y <= W-1 and
            x >= 0 and y >= 0 and
            G[x][y] != "#")


def main():
    H, W = map(int, input().split())
    Cx, Cy = map(int, input().split())
    Dx, Dy = map(int, input().split())

    G = [list(input()) for _ in range(H)]
    INF = int(1e9)
    q = deque()
    q.append((Cx-1, Cy-1, -INF, Cx-1, Cy-1))
    warps = [[INF] * W for _ in range(H)]
    while q:
        x, y, warp, prev_x, prev_y = q.popleft()

        if warps[x][y] != INF:
            continue

        num_warps = warps[prev_x][prev_y] + warp
        warps[x][y] = num_warps

        for step_x in range(-2, 3):
            for step_y in range(-2, 3):
                x_, y_ = x+step_x, y+step_y
                if is_inside(x_, y_, W, H, G) and warps[x_][y_] == INF:
                    if ((max(abs(step_x), abs(step_y)) == 1) and
                            (min(abs(step_x), abs(step_y)) == 0)):

                        q.appendleft((x_, y_, 0, x, y))
                    else:
                        q.append((x_, y_, 1, x, y))

    ans = warps[Dx-1][Dy-1]
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
