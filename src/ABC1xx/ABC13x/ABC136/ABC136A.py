def main():
    A, B, C = map(int, input().split())
    print(max(0, C - (A - B)))


if __name__ == '__main__':
    main()
