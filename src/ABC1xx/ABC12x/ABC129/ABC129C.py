def main():
    N, M = map(int, input().split())
    A = set([int(input()) for _ in range(M)])
    ways = [0] * (N+1)
    ways[0] = 1
    for i in range(1, N+1):
        if i not in A:
            ways[i] = ways[i-1] + ways[i-2]

    print(ways[N] % 1000000007)


if __name__ == '__main__':
    main()
