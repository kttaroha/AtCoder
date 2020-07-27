from collections import defaultdict


def main():
    N, M = map(int, input().split())
    d = defaultdict(set)
    num_mem = 1
    for _ in range(M):
        a, b = map(int, input().split())
        d[a].add(b)
        d[b].add(a)

    for i in range(2**N):
        tmp_mem = set()
        for j in range(N):
            if (i >> j) & 1:
                tmp_mem.add(j+1)
        for t in tmp_mem:
            tmp_mem_ = tmp_mem - {t}
            if not tmp_mem_.issubset(d[t]):
                break
        else:
            num_mem = max(num_mem, len(tmp_mem))

    print(num_mem)


if __name__ == '__main__':
    main()
