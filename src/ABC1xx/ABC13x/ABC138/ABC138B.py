def main():
    _ = input()
    A = list(map(int, input().split()))
    d = 0
    for a in A:
        d += 1/a
    print(1/d)


if __name__ == '__main__':
    main()
