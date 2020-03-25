def main():
    a = int(input())
    n = list(map(int, input().split()))
    sum_dists = []
    for i in range(1, 101):
        sum_dists.append(sum([(d - i)**2 for d in n]))

    print(min(sum_dists))


if __name__ == "__main__":
    main()
