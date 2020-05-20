from collections import deque, defaultdict
from sys import stdin

input = stdin.readline


def main():
    N, M = map(int, input().split())
    route = defaultdict(list)
    for i in range(M):
        a, b = map(int, input().split())
        route[a-1].append(b-1)
        route[b-1].append(a-1)

    arrive_time = [0] + [-1] * (N - 1)
    arrive_route = [0] + [-1] * (N - 1)
    q = deque()
    q.append(0)
    while len(q):
        idx = q.popleft()  # using BFS
        for c in route[idx]:
            if arrive_time[c] >= 0 and arrive_time[c] <= arrive_time[idx]+1:
                continue
            arrive_time[c] = arrive_time[idx]+1
            arrive_route[c] = idx
            q.append(c)
    if min(arrive_time) < 0:
        print("No")
    else:
        print("Yes")
        for r in arrive_route[1:]:
            print(r+1)


if __name__ == '__main__':
    main()
