def main():
    _ = int(input())
    s = input()
    cnt = 0
    for i in range(len(s) - 2):
        if s[i:i+3] == "ABC":
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
