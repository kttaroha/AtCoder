def main():
    A, B = map(int, input().split())
    cnt = 1
    num = 0
    while cnt < B:
        cnt += A - 1
        num += 1

    print(num)


if __name__ == '__main__':
    main()
