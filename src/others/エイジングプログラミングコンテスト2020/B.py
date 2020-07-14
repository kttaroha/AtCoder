def main():
    _ = input()
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(len(A)):
        if (i+1) % 2 != 0:
            if A[i] % 2 != 0:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
