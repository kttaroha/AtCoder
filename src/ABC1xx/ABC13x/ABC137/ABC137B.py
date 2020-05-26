def main():
    K, X = map(int, input().split())
    mi = int(max(X-K+1, -1e6))
    ma = int(min(X+K, 1e6+1))
    black = [i for i in range(mi, ma)]
    print(*black)


if __name__ == '__main__':
    main()
