from math import ceil

def main():
    S = list(input())
    num_r = 0
    num_l = 0
    agg = []
    pos = [0 for _ in range(len(S))]
    for i in range(len(S)-1):

        if S[i] == "R":
            num_r += 1

        elif S[i] == "L":
            num_l += 1

        if S[i] == "R" and S[i+1] == "L":
            agg.append((i, num_r))
            num_r = 0
        elif S[i] == "L" and S[i+1] == "R":
            agg.append((i, num_l))
            num_l = 0

        if i == len(S) - 2:
            num_l += 1
            agg.append((i, num_l))
            num_l = 0

    # length of agg is always even number
    for i in range(0, len(agg)-1, 2):
        idx = agg[i][0]
        r_num = ceil(agg[i][1] / 2) + agg[i+1][1] // 2
        l_num = agg[i][1] - ceil(agg[i][1] / 2) + agg[i+1][1] - agg[i+1][1] // 2
        pos[idx] = r_num
        pos[idx+1] = l_num
    print(*pos)


if __name__ == '__main__':
    main()

