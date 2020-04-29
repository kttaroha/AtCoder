from collections import defaultdict


def main():
    d = defaultdict(int)
    nums = []
    _ = input()
    nums = list(map(int, input().split()))
    for n in nums:
        d[n] += 1

    total_combs = 0
    for k in d.keys():
        total_combs += int((d[k]*(d[k]-1))/2)

    for n in nums:
        print(total_combs - (d[n] - 1))


if __name__ == "__main__":
    main()
