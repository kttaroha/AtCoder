def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    max_h = sorted(A, reverse=True, key=lambda x: x[0])[0][0]
    max_s = sorted(A, reverse=True, key=lambda x: x[1])[0][1]

    left = max_h - 1
    right = max_h + max_s*N + 1
    while abs(left-right) > 1:
        mid = (left + right) // 2
        cond = is_satisfied(A, mid)
        if cond:
            right = mid
        else:
            left = mid

    print(right)


def is_satisfied(A, x):
    time_req = []
    for a in A:
        time_req.append(((x-a[0])/a[1]))

    time_req = sorted(time_req)
    time_curr = 0
    for t in time_req:
        if t >= time_curr:
            time_curr += 1
        else:
            return False
    return True


if __name__ == '__main__':
    main()
