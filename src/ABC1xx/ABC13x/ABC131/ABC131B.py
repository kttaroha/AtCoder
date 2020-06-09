def main():
    N, L = map(int, input().split())
    min_abs = 1e10
    s = 0
    for i in range(N):
        if abs(L + i) < min_abs:
            min_abs = abs(L+i)

    for i in range(N):
        if abs(L+i) != min_abs:
            s += L+i
    print(s)


if __name__ == '__main__':
    main()
