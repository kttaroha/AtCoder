def main():
    _ = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum_prev = sum(A)

    for i in range(len(A)-1):
        b = B[i]
        b = max(0, b - A[i])
        A[i] = max(0, A[i] - B[i])
        A[i+1] = max(0, A[i+1] - b)

    print(sum_prev - sum(A))


if __name__ == '__main__':
    main()
