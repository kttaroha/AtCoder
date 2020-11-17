import heapq


def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    heapq.heapify(A)
    B = [list(map(int, input().split())) for _ in range(M)]
    B = sorted(B, key=lambda x: x[1], reverse=True)

    for b, c in B:
        cnt = b
        while cnt:
            v = heapq.heappop(A)
            if v >= c:
                heapq.heappush(A, v)
                break
            else:
                heapq.heappush(A, c)
                cnt -= 1

    print(sum(A))


if __name__ == '__main__':
    main()
