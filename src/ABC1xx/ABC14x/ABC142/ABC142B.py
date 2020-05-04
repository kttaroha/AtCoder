def main():
    N, k = map(int, input().split())
    M = list(map(int, input().split()))
    num = 0
    for m in M:
        if m >= k:
            num += 1
    print(num)


if __name__ == "__main__":
    main()
