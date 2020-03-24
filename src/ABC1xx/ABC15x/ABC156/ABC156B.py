def main():
    a, b = list(map(int, input().split()))
    d = 1
    while True:
        if b**d > a:
            break
        else:
            d += 1
    print(d)


if __name__ == "__main__":
    main()
