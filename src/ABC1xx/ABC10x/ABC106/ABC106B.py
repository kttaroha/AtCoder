def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1, 2):
        cnt_tmp = 0
        for j in range(1, N+1):
            if i % j == 0:
                cnt_tmp += 1
        if cnt_tmp == 8:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
