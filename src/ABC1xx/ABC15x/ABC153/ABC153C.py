def main():
    num, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    sum_attack = sum(a[k:])
    print(sum_attack)


if __name__ == "__main__":
    main()
