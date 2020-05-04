def main():
    _ = input()
    A = list(map(int, input().split()))
    d = dict()
    for i in range(len(A)):
        d[i+1] = A[i]
    d = sorted(d.items(), key=lambda x: x[1])
    print(*[l[0] for l in d])


if __name__ == "__main__":
    main()
