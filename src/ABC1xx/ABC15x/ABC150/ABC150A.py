def main():
    a = list(map(int, input().split()))
    if 500 * a[0] >= a[1]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
