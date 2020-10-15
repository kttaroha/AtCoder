def main():
    N, K = map(int, input().split())
    A = input()
    S = ""
    for i in range(N):
        if i == K - 1:
            S += A[i].lower()
        else:
            S += A[i]

    print(S)


if __name__ == '__main__':
    main()
