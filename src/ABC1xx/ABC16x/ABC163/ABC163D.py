def main():
    MOD = int(1e9+7)
    N, K = map(int, input().split())
    cnt = 0
    for i in range(K, N+2):
        min_sum = ((i - 1) * i) // 2
        max_sum = ((2 * N - i + 1) * i) // 2
        cnt += (max_sum - min_sum + 1) % MOD

    print(cnt % MOD)


if __name__ == '__main__':
    main()
