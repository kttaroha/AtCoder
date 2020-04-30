def main():
    _ = int(input())
    S = input()
    num = 0
    prev_s = ""
    for s in S:
        if s != prev_s:
            num += 1
        prev_s = s
    print(num)


if __name__ == "__main__":
    main()
