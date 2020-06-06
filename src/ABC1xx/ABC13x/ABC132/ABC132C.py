def main():
    _ = input()
    A = sorted(list(map(int, input().split())))
    print(A[len(A)//2] - A[len(A)//2-1])


if __name__ == '__main__':
    main()
