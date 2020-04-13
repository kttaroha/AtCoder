from collections import defaultdict


def main():
    _ = int(input())
    S = input()

    # stores the number of each letter appears in the string.
    color_num = defaultdict(int)

    # the number of the combinations of letters which satifies
    # S[i] == S[j] == S[k] and j - i == k -j.
    num_subst = 0

    for i in range(len(S) - 1):
        color_num[S[i]] += 1
        for j in range(i + 1, len(S)):
            if S[i] != S[j]:
                diff = j - i
                idx = j + diff
                if idx < len(S) and S[idx] != S[i] and S[idx] != S[j]:
                    num_subst += 1
    color_num[S[len(S) - 1]] += 1
    total_num_comb = color_num["R"] * color_num["G"] * color_num["B"]
    print(total_num_comb - num_subst)


if __name__ == "__main__":
    main()
