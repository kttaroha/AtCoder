def main():
    _ = int(input())
    a = list(map(int, input().split()))
    total = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            total += a[i]*a[j]
    print(total)


if __name__ == "__main__":
    main()
