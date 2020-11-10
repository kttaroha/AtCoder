def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []
    ans_tmp = 0
    for i in range(K):
        ans_tmp += A[i]
    ans.append(ans_tmp)

    for i in range(N-K):
        ans.append(ans[i]+A[i+K]-A[i])

    print(sum(ans))


if __name__ == '__main__':
    main()
