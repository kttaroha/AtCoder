def main():
    A, B = list(input().split())
    n = int(A+B)

    tmp_float = n ** 0.5
    tmp_int = int(n ** 0.5)
    if tmp_int == tmp_float:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
