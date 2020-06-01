def main():
    _ = input()
    A = list(map(int, input().split()))
    cnt = 1
    mi = min(A)
    if mi == 0:
        print(0)
    else:
        for a in A:
            cnt *= a
            if cnt > 1e18 and mi > 0:
                print(-1)
                break
        else:
            if cnt < 0:
                print(-1)
            else:
                print(cnt)


if __name__ == '__main__':
    main()
