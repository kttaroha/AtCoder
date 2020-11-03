def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    inf = int(1e9) + 7
    sum_template = ((K-1)*K) % inf * pow(2, -1, inf)
    ans = 0
    # table[i][0]に最初に与えられた数列（繰り返し前)の転倒数
    # table[i][1]に最初に与えられた数列（繰り返し前)でA[i]より小さい数
    table = [[0, 0] for _ in range(N)]

    for i in range(N):
        tmp = A[i]
        for j in range(N):
            if tmp > A[j]:
                table[i][1] += 1
                if i < j:
                    table[i][0] += 1

    for t in table:
        ans += K*t[0] + t[1]*sum_template
        ans = ans % inf

    print(ans)


if __name__ == '__main__':
    main()
