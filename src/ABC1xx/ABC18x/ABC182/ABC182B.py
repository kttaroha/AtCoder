def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    max_int = 0
    for i in range(2, 1001):
        tmp_cnt = 0
        for a in A:
            if a % i == 0:
                tmp_cnt += 1
        if tmp_cnt >= cnt:
            max_int = i
            cnt = max(cnt, tmp_cnt)

    print(max_int)


if __name__ == '__main__':
    main()
