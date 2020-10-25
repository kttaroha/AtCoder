def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if sum(A) > sum(B):
        print("A")
    elif sum(A) < sum(B):
        print("B")
    else:
        print("same")


if __name__ == '__main__':
    main()
