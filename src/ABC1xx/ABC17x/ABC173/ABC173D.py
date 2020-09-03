import heapq


def main():
    _ = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    q = []
    heapq.heapify(q)
    ans = A[0]
    tmp_score = min(A[0], A[1])
    heapq.heappush(q, (-tmp_score, A[0], A[1]))
    heapq.heappush(q, (-tmp_score, A[1], A[0]))

    for a in A[2:]:
        g = heapq.heappop(q)
        ans += -g[0]
        tmp_score1 = min(a, g[1])
        tmp_push1 = (-tmp_score1, a, g[1])

        tmp_score2 = min(a, g[2])
        tmp_push2 = (-tmp_score2, a, g[2])

        heapq.heappush(q, tmp_push1)
        heapq.heappush(q, tmp_push2)

    print(ans)


if __name__ == '__main__':
    main()
