def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    max_value = 0
    for i in range(2 ** N):
        value = 0
        for j in range(N):
            if ((i >> j) & 1):
                value += V[j] - C[j]

        max_value = max(max_value, value)

    print(max_value)


if __name__ == '__main__':
    main()
