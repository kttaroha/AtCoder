def main():
    N = int(input())
    N_sqrt = int(N ** 0.5) + 1
    cnt_tmp = 0
    ans = []
    for i in range(1, N_sqrt):
        if N % i == 0:
            cnt_tmp += 1
            ans.append(i)

    for i in range(cnt_tmp-1, -1, -1):
        a = ans[i]
        div = int(N/a)
        if div != a:
            ans.append(div)

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
