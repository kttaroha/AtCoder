def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 1e10
    for i in range(len(A)+1):
        sum_diff = abs(sum(A[:i]) - sum(A[i:]))
        ans = min(ans, sum_diff)

    print(ans)


if __name__ == '__main__':
    main()
