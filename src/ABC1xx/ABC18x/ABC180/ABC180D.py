def main():
    X, Y, A, B = map(int, input().split())
    prev = X
    cnt = 0
    now = X * (A ** (cnt + 1))
    while now - prev < B and now < Y:
        prev = now
        cnt += 1
        now = X * (A ** (cnt + 1))

    if (Y - prev) % B == 0:
        cnt += (Y - prev) // B - 1

    else:
        cnt += (Y - prev) // B
    print(cnt)


if __name__ == '__main__':
    main()
