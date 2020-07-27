def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = 1000
    kabu = 0
    for i in range(N-1):
        if A[i] <= A[i+1]:
            M += A[i] * kabu
            kabu = 0
            kabu += M // A[i]
            M = M % A[i]
        else:
            M += A[i] * kabu
            kabu = 0

    else:
        M += kabu * A[i+1]
    print(M)


if __name__ == '__main__':
    main()
