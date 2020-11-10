def main():
    N = int(input())
    A = list(map(int, input().split()))
    cum = [A[0]]
    cums = [cum[0]]
    cums_max = []
    cum_max = -1e10
    ans = 0

    for i in range(1, len(A)):
        cum.append(cum[i-1]+A[i])

    for c in cum:
        cum_max = max(c, cum_max)
        cums_max.append(cum_max)

    for i in range(1, len(cum)):
        cums.append(cums[i-1]+cum[i])

    if len(A) == 1:
        print(max(0, A[0]))
    else:
        for i in range(1, len(cums)):
            ans = max(ans, cums[i-1]+cums_max[i])
        print(ans)


if __name__ == '__main__':
    main()
