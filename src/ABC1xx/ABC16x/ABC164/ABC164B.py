def main():
    A, B, C, D = map(int, input().split())
    i = 0
    while True:
        if i % 2 == 0:
            C -= B
        else:
            A -= D
        if A <= 0 or C <= 0:
            break
        i += 1
    if i % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
