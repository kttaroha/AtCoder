from collections import deque


def main():
    side = 0
    S = input()
    len_s = len(S)

    d = deque()
    for s in S:
        d.append(s)

    n = int(input())
    for i in range(n):
        q = input().split()
        if len(q) == 1:
            side += 1
        elif len(q) == 3:
            len_s += 1
            if side % 2 == 0:
                if q[1] == "1":
                    d.appendleft(q[2])
                else:
                    d.append(q[2])
            else:
                if q[1] == "1":
                    d.append(q[2])
                else:
                    d.appendleft(q[2])
    S = ""
    if side % 2 == 0:
        for i in range(len_s):
            S += d.popleft()
    else:
        for i in range(len_s):
            S += d.pop()

    print(S)


if __name__ == "__main__":
    main()
