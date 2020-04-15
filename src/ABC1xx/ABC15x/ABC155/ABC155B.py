def main():
    n = int(input())
    A = list(map(int, input().split()))
    s = 0
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                s += 1
        else:
            s += 1
    if s == n:
        print("APPROVED")
    else:
        print("DENIED")


if __name__ == "__main__":
    main()
