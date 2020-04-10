def main():
    a = list(map(int, input().split()))
    if len(set(a)) == 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
