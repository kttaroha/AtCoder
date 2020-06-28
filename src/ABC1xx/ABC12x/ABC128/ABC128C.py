def main():
    N, M = map(int, input().split())
    lights = []
    for i in range(M):
        lights.append(set(list(map(int, input().split()))[1:]))
    P = list(map(int, input().split()))
    switch_combs = []

    # enumerate all the possible combinations of the on/off of the switches.
    for i in range(2**N):
        tmp_comb = set()
        for j in range(N):
            if (i >> j) & 1:
                tmp_comb.add(j+1)
        switch_combs.append(tmp_comb)
    num_sum = 0

    for comb in switch_combs:
        for i in range(len(lights)):
            num_match = len(lights[i] & comb)
            if not num_match % 2 == P[i]:
                break
        else:
            num_sum += 1
    print(num_sum)


if __name__ == '__main__':
    main()
