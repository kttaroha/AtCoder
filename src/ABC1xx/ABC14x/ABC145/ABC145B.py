def main():
    _ = input()
    s = input()
    if len(s) % 2 != 0:
        print("No")
    else:
        mid = int(len(s) / 2)
        if s[0:mid] == s[mid:]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
