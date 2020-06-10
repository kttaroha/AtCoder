def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    D = 0
    bounds = [D]
    for a in A:
        D += a
        bounds.append(D)

    for b in bounds:
        if b <= X:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
