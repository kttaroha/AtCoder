import sys
input = sys.stdin.readline


def main():
    num = 0
    _ = input()
    A = sorted(list(map(int, input().split())))
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            a = A[i]
            b = A[j]
            thresh = a + b
            ok = j
            ng = len(A)
            idx = binary_search(A, ok, ng, thresh)
            num += idx - j

    print(num)


def binary_search(li, ok, ng, value):
    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2
        if li[mid] < value:
            ok = mid
        else:
            ng = mid

    return ok


if __name__ == "__main__":
    main()
