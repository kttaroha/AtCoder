def main():
    n = int(input())
    A, B = input().split()
    s = ""
    for i in range(n):
        s += A[i]
        s += B[i]
    print(s)


if __name__ == "__main__":
    main()
