def main():
    W, H, x, y = map(int, input().split())
    diff = 1e-5
    mid_W, mid_H = W / 2, H / 2
    if abs(x - mid_W) < diff and abs(y - mid_H) < diff:
        t = 1
    else:
        t = 0

    print(W*H/2, t)


if __name__ == '__main__':
    main()
