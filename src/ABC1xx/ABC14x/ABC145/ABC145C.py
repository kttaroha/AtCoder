from itertools import permutations


def calc(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5


def main():
    n = int(input())
    A = [list(map(int, input().split())) for i in range(n)]
    A = list(permutations(A))
    ls = []
    for c in A:
        l = calc(c[0], c[1])
        if len(c) > 2:
            prev_idx = 1
            for a in c[2:]:
                l += calc(c[prev_idx], a)
                prev_idx += 1
        ls.append(l)
    print(sum(ls) / len(ls))


if __name__ == "__main__":
    main()
