def keta(num):
    cnt = 0
    while num >= 1:
        num /= 10
        cnt += 1
    return cnt


def main():
    a = list(map(int, input().split()))
    # 探索範囲s
    beg = 0
    end = 10**9 + 1
    while (end - beg > 1):
        mid = (beg + end) // 2
        if a[0] * mid + a[1] * keta(mid) <= a[2]:
            beg = mid
        else:
            end = mid

    print(int(beg))


if __name__ == "__main__":
    main()
