from collections import deque


def main():
    N, Q = map(int, input().split())
    g = [[] for _ in range(N)]

    # for storing the value of the each node
    cnt = [0]*N

    # for DFS
    stack = deque()
    stack.append(0)
    seen = [0] * N

    # store the structure of the graph
    for i in range(N-1):
        a, b = map(int, input().split())
        g[b-1].append(a-1)
        g[a-1].append(b-1)

    # add values to parent nodes
    for i in range(Q):
        p, x = map(int, input().split())
        cnt[p-1] += x

    # DFS
    while len(stack):
        idx = stack.pop()
        seen[idx] += 1
        for c in g[idx]:
            if seen[c]:
                continue
            cnt[c] += cnt[idx]
            stack.append(c)

    print(*cnt)


if __name__ == '__main__':
    main()
