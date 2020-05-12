def main():
    cnt = 0
    num_w = 0
    A = list(input())
    for i in range(len(A)):
        if A[i] == "W":
            cnt += i - num_w
            num_w += 1
    print(cnt)


if __name__ == "__main__":
    main()
