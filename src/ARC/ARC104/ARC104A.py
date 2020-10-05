def main():
    A, B = map(int, input().split())
    for i in range(-1000, 1000):
        for j in range(-1000, 1000):
            if i + j == A and i - j == B:
                print(i, j)


if __name__ == '__main__':
    main()
