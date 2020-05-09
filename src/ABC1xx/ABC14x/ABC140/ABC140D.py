def main():
    N, K = map(int, input().split())
    S = input()
    num = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            num += 1
    print(min(num + 2*K, N - 1))


if __name__ == '__main__':
    main()
