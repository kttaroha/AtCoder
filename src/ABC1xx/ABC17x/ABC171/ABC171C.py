def main():
    N = int(input())
    s = ""
    d = N
    while d:
        if d % 26 == 0:
            d, r = d // 26 - 1, 26
        else:
            d, r = d // 26, d % 26
        s += chr(r+64).lower()

    print("".join(list(reversed(s))))


if __name__ == '__main__':
    main()