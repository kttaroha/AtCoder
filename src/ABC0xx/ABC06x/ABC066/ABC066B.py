def main():
    S = input()
    le = len(S) - 1
    while le > 0:
        if len(S[:le]) % 2 == 0:
            mid = le // 2
            if S[:mid] == S[mid:le]:
                break
        le -= 1

    print(le)


if __name__ == '__main__':
    main()
