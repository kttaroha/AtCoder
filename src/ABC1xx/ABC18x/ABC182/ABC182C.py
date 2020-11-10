def main():
    N = input()
    cnt = 0
    for i in range(2**len(N)):
        num = ""
        for j in range(len(N)):
            if ((i >> j) & 1):
                num += N[j]

        if num != "":
            if int(num) % 3 == 0:
                cnt = max(cnt, len(num))

    if cnt == 0:
        print(-1)
    else:
        print(len(N) - cnt)


if __name__ == '__main__':
    main()
