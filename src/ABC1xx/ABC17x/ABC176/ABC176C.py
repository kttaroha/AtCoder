def main():
    _ = int(input())
    A = list(map(int, input().split()))

    mi = A[0]
    s = 0

    for a in A[1:]:
        if a <= mi:
            s += mi - a
        else:
            mi = a

    print(s)


if __name__ == '__main__':
    main()
