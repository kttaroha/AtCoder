def main():
    R, C = map(int, input().split()) 
    G = ["" for _ in range(C)]
    max_num_senbei = 0
    for _ in range(R):
        row = input().split()
        for i in range(len(row)):
            G[i] += row[i]

    # 0 ~ 2**Rまでの非負整数を2進数で表現した時、0と1の数の多い方の数を格納しておく
    nums = []
    for i in range(2**R):
        num_zero = 0
        num_one = 0
        bin_i = "{:010b}".format(i)[-R:]
        for j in bin_i:
            if j == "0":
                num_zero += 1
            else:
                num_one += 1
        nums.append(max(num_zero, num_one))

    for i in range(2**R):
        sum_senbei = 0
        for g in G:
            col_num = int(g, 2)
            i_col_xor = col_num ^ i
            sum_senbei += nums[i_col_xor]
        max_num_senbei = max(max_num_senbei, sum_senbei)

    print(max_num_senbei)


if __name__ == '__main__':
    main()
