def main():
    S = input()
    T = input()
    num = 0
    for i in range(3):
        if S[i] == T[i]:
            num += 1
    print(num)


if __name__ == '__main__':
    main()
