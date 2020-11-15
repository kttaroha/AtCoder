from math import ceil


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    K = sum(B) - sum(A)
    if K < 0:
        print("No")
        return
    else:
        sum_count_1 = 0
        sum_count_2 = 0
        for i in range(N):
            if A[i] >= B[i]:
                sum_count_1 += A[i] - B[i]
            else:
                sum_count_2 += ceil((B[i] - A[i]) / 2)

    if max(sum_count_1, sum_count_2) > K:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
