def main():
    _ = int(input())
    A = list(map(int, input().split()))
    prev_a = A[0]
    max_a = A[0]
    for a in A[1:]:
        if a + 1 < prev_a or a + 1 < max_a:
            print("No")
            break
        elif prev_a == a:
            prev_a = a
            max_a = max(max_a, a)
        else:
            prev_a = a - 1
            max_a = max(max_a, a)
    else:
        print("Yes")


if __name__ == '__main__':
    main()
