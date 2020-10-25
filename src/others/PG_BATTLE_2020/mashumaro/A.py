def main():
    N, X, A, B = map(int, input().split())

    if N >= X:
        print(N*B)
    else:
        print(N*A)


if __name__ == '__main__':
    main()
