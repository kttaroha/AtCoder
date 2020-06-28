def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    for i in range(M-1):
        for j in range(i+1, M):
            score_sum = 0
            for k in range(N):
                score_sum += max(A[k][i], A[k][j])
            max_score = max(max_score, score_sum)
    print(max_score)


if __name__ == '__main__':
    main()
