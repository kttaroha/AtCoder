import heapq


def main():
    _ = input()
    A = list(map(int, input().split()))
    heapq.heapify(A)

    while len(A) > 1:
        n1 = heapq.heappop(A)
        n2 = heapq.heappop(A)
        n = (n1 + n2) / 2
        heapq.heappush(A, n)

    print(sum(A))


if __name__ == '__main__':
    main()
