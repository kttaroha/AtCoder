def main():
    a, b = map(int, input().split())
    s = ""
    if a > b:
        for i in range(a):
            s += str(b)
    else:
        for i in range(b):
            s += str(a)
    print(s)


if __name__ == "__main__":
    main()