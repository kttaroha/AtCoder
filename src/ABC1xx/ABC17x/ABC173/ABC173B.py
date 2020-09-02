from collections import defaultdict


def main():
    N = int(input())
    d = defaultdict(int)
    results = ["AC", "WA", "TLE", "RE"]
    for _ in range(N):
        d[input()] += 1

    for r in results:
        print(f"{r} x {d[r]}")


if __name__ == '__main__':
    main()
