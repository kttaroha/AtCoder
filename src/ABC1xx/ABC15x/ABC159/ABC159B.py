def main():
    S = input()
    idx1 = int((len(S) - 1)/2)
    idx2 = int((len(S) + 3)/2) - 1
    flag1 = check(S)
    flag2 = check(S[:idx1])
    flag3 = check(S[idx2:])
    if flag1 and flag2 and flag3:
        print("Yes")
    else:
        print("No")


def check(s):
    if s == s[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
