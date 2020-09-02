def main():
    M = int(input())
    n, r = M // 1000, M % 1000

    if r == 0:
        print(0)
        return

    print((n+1)*1000-M)


if __name__ == '__main__':
    main()
