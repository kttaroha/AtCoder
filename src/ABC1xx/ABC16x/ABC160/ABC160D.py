'''
WARNING!
This implementation failed the supplied test cases
because of TLE (time limit exceeded) error in Python3,
while it does meet the requirements in PyPy3.
'''

# Using BFS
from collections import defaultdict, deque
import sys


def input():
    return sys.stdin.readline()


def push(v, d, dist, q, INF=1e10):
    if dist[v] != INF:
        return
    dist[v] = d
    q.append(v)


def main():
    n, x, y = map(int, input().split())
    # modify the values of x, y so that they start from zero
    x, y = x - 1, y - 1
    INF = 1e10
    ans = defaultdict(int)
    for i in range(n):
        # dist[idx]: distance between i and idx.
        dist = [INF] * n
        q = deque()
        push(i, 0, dist, q)
        while len(q) != 0:
            v = q.popleft()
            d = dist[v]
            if v - 1 >= 0:
                push(v-1, d+1, dist, q)
            if v + 1 < n:
                push(v+1, d+1, dist, q)
            if v == x:
                push(y, d+1, dist, q)
            if v == y:
                push(x, d+1, dist, q)

            ans[dist[v]] += 1

    for i in range(n):
        if i != 0:
            print(ans[i] // 2)


if __name__ == "__main__":
    main()
