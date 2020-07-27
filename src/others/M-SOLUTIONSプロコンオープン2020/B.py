def main():
    A, B, C = map(int, input().split())
    K = int(input())

    while K:
        if B <= A:
            B *= 2
        else:
            if C <= B:
                C *= 2
            else:
                break
        K -= 1

    if B > A and C > B:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
