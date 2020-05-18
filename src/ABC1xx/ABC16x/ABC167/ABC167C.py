def main():
    N, M, X = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    total_cost = 1e10
    possible = False
    for i in range(2**N):
        tmp_cost = 0
        rikai = [0]*M
        for j in range(N):
            if ((i >> j) & 1):
                tmp_cost += A[j][0]
                for k in range(M):
                    rikai[k] += A[j][k+1]

        if min(rikai) >= X:
            possible = True
            total_cost = min(total_cost, tmp_cost)

    if possible:
        print(total_cost)
    else:
        print(-1)


if __name__ == '__main__':
    main()
