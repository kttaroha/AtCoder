def main():
    S = input()
    combs = set()
    max_len = 0
    for i in range(len(S)):
        for j in range(len(S), i - 1, -1):
            S_tmp = S[i:j]
            for s in S_tmp:
                if s not in ["A", "C", "G", "T"]:
                    break
            else:
                combs.add(S_tmp)

    for s in combs:
        max_len = max(max_len, len(s))

    print(max_len)


if __name__ == '__main__':
    main()
