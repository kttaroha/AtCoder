def main():
    N = list(input())
    flag = True
    for i in range(len(N)-1):
        if N[i] == N[i+1]:
            flag = False

    if flag:
        print("Good")
    else:
        print("Bad")


if __name__ == '__main__':
    main()
