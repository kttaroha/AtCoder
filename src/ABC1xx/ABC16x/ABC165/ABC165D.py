from math import floor


def main():
    A, B, N = map(int, input().split())
    x = min(B - 1, N)
    print(floor(A*x/B) - A*floor(x/B))


if __name__ == "__main__":
    main()
