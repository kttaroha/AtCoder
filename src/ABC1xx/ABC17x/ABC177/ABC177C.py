def main():
    _ = int(input())
    A = list(map(int, input().split()))
    total_sum = 0
    inv_cum_sum = []
    ans = 0
    for i in range(len(A)):
        total_sum += int(A[i] % int(1e9+7))
        total_sum = int(total_sum % int(1e9+7))
    tmp_cum_sum = 0
    for i in range(len(A)):
        tmp_cum_sum += int(A[i] % int(1e9+7))
        tmp_cum_sum = int(tmp_cum_sum % int(1e9+7))
        inv_cum_sum.append(total_sum - tmp_cum_sum)
    for i in range(len(inv_cum_sum)):
        ans += int((A[i] * inv_cum_sum[i]) % int(1e9+7))
    print(int(ans % int(1e9+7)))


if __name__ == '__main__':
    main()