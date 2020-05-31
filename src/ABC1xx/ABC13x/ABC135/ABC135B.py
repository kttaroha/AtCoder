def main():
    _ = int(input())
    A = list(map(int, input().split()))
    A_ = sorted(A)
    cnt = 0
    for i in range(len(A)):
        a = A[i]
        a_ = A_[i]
        if a != a_:
            cnt += 1

    if cnt <= 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
