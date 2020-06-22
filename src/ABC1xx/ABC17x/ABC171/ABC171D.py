from collections import defaultdict


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    d = defaultdict(int)
    s = sum(A)
    for a in A:
        d[a] += 1

    for i in range(Q):
        B, C = map(int, input().split())
        num = d[B]
        d[B] = 0
        d[C] += num
        s += num * (C - B)
        print(s)


if __name__ == '__main__':
    main()
