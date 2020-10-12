def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    cnt = 0
    for i in range(H-1):
        for j in range(W-1):
            if A[i][j] == "." and A[i+1][j] == ".":
                cnt += 1
            if A[i][j] == "." and A[i][j+1] == ".":
                cnt += 1

    for i in range(W-1):
        if A[H-1][i] == "." and A[H-1][i+1] == ".":
            cnt += 1

    for i in range(H-1):
        if A[i][W-1] == "." and A[i+1][W-1] == ".":
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()