def main():
    N = int(input())
    ans = [0] * 100000

    for i in range(1, 100):
        for j in range(1, 100):
            for k in range(1, 100):
                tmp = i ** 2 + j ** 2 + k ** 2 + i*j + j*k + k*i
                ans[tmp] += 1
    for i in range(N):
        print(ans[i+1])


if __name__ == '__main__':
    main()
