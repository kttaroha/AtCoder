from collections import defaultdict


def main():
    N = int(input())
    a = list(map(int, input().split()))

    boss_dict = defaultdict(int)
    for i in a:
        boss_dict[i] += 1

    for i in range(1, N + 1):
        print(boss_dict[i])


if __name__ == "__main__":
    main()
