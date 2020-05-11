def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    prev_idx = 1
    flag = False
    num = 0
    seen = [-1] * N
    while True:
        if prev_idx == 2:
            flag = True
            break

        # if it visits the same point twice,
        # it means this graph has loop structure.
        if seen[prev_idx-1] != -1:
            break
        seen[prev_idx-1] = num
        prev_idx = A[prev_idx-1]
        num += 1

    if flag:
        print(num)
    else:
        print(-1)


if __name__ == '__main__':
    main()
