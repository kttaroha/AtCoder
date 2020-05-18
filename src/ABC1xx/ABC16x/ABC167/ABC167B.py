def main():
    A, B, C, K = map(int, input().split())
    if K <= A:
        print(K)
    else:
        if (B - K + A) >= 0:
            print(A)
        else:
            print(A-(K-A-B))


if __name__ == '__main__':
    main()
