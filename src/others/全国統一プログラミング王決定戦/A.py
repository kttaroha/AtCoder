def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = [0]
    s.append(A[0])
    s_max = [0]*(N+1)

    for i in range(1, len(A)):
        s.append(s[i]+A[i])

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            s_max[j-i] = max(s_max[j-i], s[j]-s[i])

    for sm in s_max[1:]:
        print(sm)


if __name__ == '__main__':
    main()
