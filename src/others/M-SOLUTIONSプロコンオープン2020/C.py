def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    div_i = 0
    for i in range(N):
        if i <= K - 1:
            pass
        else:
            if A[i] > A[div_i]:
                print("Yes")
            else:
                print("No")
            div_i += 1


if __name__ == '__main__':
    main()
