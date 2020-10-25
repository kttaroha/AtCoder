from math import ceil


def main():
    S = input()
    num_R = 0
    num_L = 0
    pos_rl = [0] * len(S)
    # R->Lとなっている場所の特定
    # R->Lとなっている場所のLの座標を格納するようにする
    for i in range(len(S)-1):
        if S[i] == "R" and S[i+1] == "L":
            pos_rl[i+1] += 1

    # R->Lとなっている場所から左方向にRが連続して何個存在しているかカウント
    cnt_R = [0] * len(S)
    for i in range(len(S)):
        if S[i] == "R":
            num_R += 1

        if pos_rl[i]:
            cnt_R[i] += num_R
            num_R = 0

    # R->Lとなっている場所から右方向にLが連続して何個存在しているかカウント
    cnt_L = [0] * len(S)
    for i in range(len(S)-1, -1, -1):
        if S[i] == "L":
            num_L += 1

        if pos_rl[i]:
            cnt_L[i] += num_L
            num_L = 0

    # 答えの集計
    ans = [0] * len(S)
    for i in range(len(S)):
        if pos_rl[i]:
            ans[i] += ceil(cnt_L[i] / 2) + cnt_R[i] // 2
            ans[i-1] += cnt_L[i] // 2 + ceil(cnt_R[i] / 2)

    print(*ans)


if __name__ == '__main__':
    main()
