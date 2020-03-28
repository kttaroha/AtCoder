def main():
    n = int(input())
    n = n % 26
    s = input()
    s_list = [d for d in s]
    new_s = ""
    new_ord_base = 64
    for i in s_list:
        new_ord = ord(i) + n
        if new_ord > 90:
            new_ord = new_ord % 90 + new_ord_base
        new_s += chr(new_ord)

    print(new_s)


if __name__ == "__main__":
    main()
