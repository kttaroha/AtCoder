from collections import defaultdict


def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(1, N):
        left_s = S[:i]
        right_s = S[i:]
        d_left = defaultdict(int)
        d_right = defaultdict(int)
        tmp_ans = 0
        for j in range(len(left_s)):
            d_left[left_s[j]] += 1

        for k in range(len(right_s)):
            d_right[right_s[k]] += 1

        for ke in d_left.keys():
            if d_left[ke] and d_right[ke]:
                tmp_ans += 1

        ans = max(ans, tmp_ans)

    print(ans)


if __name__ == '__main__':
    main()
