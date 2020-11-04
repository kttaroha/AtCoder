def main():
    _ = int(input())
    K = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in A:
        if K - x < x:
            ans += 2*(K - x)
        else:
            ans += 2*x
    print(ans)


if __name__ == '__main__':
    main()
