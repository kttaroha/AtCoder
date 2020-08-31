def main():
    S = input()
    T = input()

    min_change = 1e5
    for i in range(len(S)-len(T)+1):
        tmp_change = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                tmp_change += 1
        min_change = min(min_change, tmp_change)

    if len(S) == len(T):
        min_change = 0
        for i in range(len(T)):
            if S[i] != T[i]:
                min_change += 1

    print(min_change)


if __name__ == '__main__':
    main()
