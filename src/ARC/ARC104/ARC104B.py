def main():
    N, S = list(input().split())
    N = int(N)
    ans = 0

    for i in range(N-1):
        num_t = 0
        num_c = 0 
        num_a = 0
        num_g = 0

        if S[i] == "A":
            num_a += 1
        elif S[i] == "T":
            num_t += 1
        elif S[i] == "C":
            num_c += 1
        else:
            num_g += 1

        for j in range(i+1, N):
            if S[j] == "A":
                num_a += 1
            elif S[j] == "T":
                num_t += 1
            elif S[j] == "C":
                num_c += 1
            else:
                num_g += 1

            if num_t == num_a and num_c == num_g:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
