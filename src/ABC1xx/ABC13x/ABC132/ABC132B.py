def main():
    _ = input()
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(len(A)-2):
        A_sub = sorted(A[i:i+3])
        a = A[i+1]
        if a == A_sub[1]:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
