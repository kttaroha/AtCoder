def main():
    N, D = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for a in A:
        if (a[0]**2 + a[1]**2)**0.5 <= D:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
