def main():
    L, R = map(int, input().split())
    check_point = 2019
    num_2019 = 0
    while check_point <= R:
        if check_point >= L and check_point <= R:
            num_2019 += 1
        check_point += 2019

    if num_2019 >= 1:
        print(0)
        return

    min_mod = 2018
    for i in range(L, R):
        for j in range(i+1, R+1):
            min_mod = min((i*j) % 2019, min_mod)
    print(min_mod)


if __name__ == '__main__':
    main()
