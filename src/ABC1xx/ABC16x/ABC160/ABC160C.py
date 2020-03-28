def main():
    length, num = map(int, input().split())
    a = list(map(int, input().split()))
    max_dis = 0
    first_h = a[0]
    prev_h = a[0]
    for h in a[1:]:
        dis = h - prev_h
        max_dis = max(max_dis, dis)
        prev_h = h

    dis = (length - prev_h) + first_h
    max_dis = max(max_dis, dis)
    print(length - max_dis)


if __name__ == "__main__":
    main()
