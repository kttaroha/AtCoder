def main():
    _ = input()
    A = list(map(int, input().split()))
    max_step = 0
    tmp = 0
    for i in range(len(A)-1):
        if A[i] >= A[i+1]:
            tmp += 1
        else:
            max_step = max(max_step, tmp)
            tmp = 0

    else:
        max_step = max(max_step, tmp)

    print(max_step)


if __name__ == '__main__':
    main()
