def main():
    N = int(input())
    nums = [1] * (N + 1)
    s = 0
    for i in range(2, N+1):
        tmp = i
        while tmp <= N:
            nums[tmp] += 1
            tmp += i
    for i in range(1, N+1):
        s += i * nums[i]
    print(s)


if __name__ == '__main__':
    main()
