def main():
    s = input()
    flag = True
    for i in range(len(s)):
        if ((i + 1) % 2 == 0 and s[i] == "R"):
            flag = False
        elif ((i + 1) % 2 != 0 and s[i] == "L"):
            flag = False

    if flag:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
