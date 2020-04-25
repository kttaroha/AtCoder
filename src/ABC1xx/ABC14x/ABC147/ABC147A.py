def main():
    a1, a2, a3 = map(int, input().split())
    if (a1+a2+a3) <= 21:
        print("win")
    else:
        print("bust")


if __name__ == "__main__":
    main()
