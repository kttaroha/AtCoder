import itertools


def main():
    _ = input()
    b = input().split()
    c = input().split()

    b_comb = sorted(list(itertools.permutations(b)))
    c_comb = sorted(list(itertools.permutations(c)))
    for i in range(len(b_comb)):
        if b_comb[i] == tuple(b):
            p = i + 1
            break
    for i in range(len(c_comb)):
        if c_comb[i] == tuple(c):
            q = i + 1
            break
    print(abs(p - q))


if __name__ == "__main__":
    main()
