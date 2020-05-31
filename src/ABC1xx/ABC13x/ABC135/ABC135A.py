def main():
    A, B = map(int, input().split())
    mi = min(A, B)
    ma = max(A, B)
    if (ma - mi) % 2 == 0:
        print((ma + mi) // 2)
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
