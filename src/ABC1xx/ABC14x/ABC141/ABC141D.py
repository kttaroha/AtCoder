import heapq
from math import ceil


def main():
    N, M = map(int, input().split())

    # As heapq.heappop returns the mininum value of the sequence,
    # we need to multiply -1 in order to attain the maximum
    # value of the sequence.
    A = list(map(lambda x: (-1) * int(x), input().split()))
    heapq.heapify(A)
    for i in range(M):
        heapq.heappush(A, ceil(heapq.heappop(A) / 2))

    print(-sum(A))


if __name__ == '__main__':
    main()
