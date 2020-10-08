def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # 実装を簡単にするためにAの長さを2倍にしておく
    A += A
    dp = [[0] * 2 * N for _ in range(2 * N)]

    if N % 2 == 1:
        for i in range(N):
            dp[i][i] = A[i]

    for diff in range(1, 2*N):  # 差分が1, 2N-1までを探索
        for i in range(2*N-diff):
            j = i + diff
            if (diff+1) % 2 == N % 2:
                dp[i][j] = max(dp[i+1][j]+A[i], dp[i][j-1]+A[j])
            else:
                if A[i] > A[j]:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    max_value = 0
    # 最初のどの部分でケーキを切り取るのが良いかを計算している
    for i in range(N):
        j = i + N - 1
        max_value = max(max_value, dp[i][j])
    print(max_value)


if __name__ == '__main__':
    main()
