from collections import defaultdict


def main():
    N, K, Q = map(int, input().split())
    d = defaultdict(int)
    for i in range(Q):
        a = int(input())
        d[a-1] += 1

    for i in range(N):
        if Q - d[i] < K:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
