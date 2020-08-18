import heapq


def main():
    _ = int(input())
    A = list(input())
    R_inds = []
    W_inds = []
    for i in range(len(A)):
        if A[i] == "R":
            R_inds.append(i*(-1))
        else:
            W_inds.append(i)

    if len(R_inds) == 0 or len(W_inds) == 0:
        print(0)
        return

    heapq.heapify(R_inds)
    heapq.heapify(W_inds)
    cnt = 0
    r_i = abs(heapq.heappop(R_inds))
    w_i = heapq.heappop(W_inds)
    while r_i > w_i:
        cnt += 1
        r_i = abs(heapq.heappushpop(R_inds, w_i*(-1)))
        w_i = heapq.heappushpop(W_inds, r_i)

    print(cnt)


if __name__ == '__main__':
    main()
