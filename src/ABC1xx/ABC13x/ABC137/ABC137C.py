from collections import defaultdict


def main():
    N = int(input())
    d = defaultdict(int)
    s = 0
    for i in range(N):
        d["".join(sorted(input()))] += 1

    for k in d.keys():
        s += d[k]*(d[k]-1)/2

    print(int(s))


if __name__ == '__main__':
    main()
