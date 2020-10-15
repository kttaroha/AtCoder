def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        points = i
        cnt = 0
        while points < K:
            points *= 2
            cnt += 1
        ans += (0.5) ** cnt / N

    print(ans)


if __name__ == '__main__':
    main()
