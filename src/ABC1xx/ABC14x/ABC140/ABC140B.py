def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    prev = -100
    s = 0
    for a in A:
        s += B[a-1]
        if a - prev == 1:
            s += C[prev-1]
        prev = a

    print(s)


if __name__ == '__main__':
    main()
