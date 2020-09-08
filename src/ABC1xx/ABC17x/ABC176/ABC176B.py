def main():
    A = list(input())
    s = 0
    for a in A:
        s += int(a)
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
