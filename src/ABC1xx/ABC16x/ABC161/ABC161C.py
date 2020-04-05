def main():
    n, k = map(int, input().split())
    res = n % k
    res2 = abs(res - k)
    print(min(res, res2))


if __name__ == "__main__":
    main()
