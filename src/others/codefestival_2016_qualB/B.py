def main():
    N, A, B = map(int, input().split())
    S = input()
    cnt_a = 0
    cnt_b = 0
    for s in S:
        if s == "a":
            if cnt_a + cnt_b < A + B:
                print("Yes")
                cnt_a += 1
            else:
                print("No")
        elif s == "b":
            if cnt_a + cnt_b < A + B and cnt_b < B:
                print("Yes")
                cnt_b += 1
            else:
                print("No")

        else:
            print("No")


if __name__ == '__main__':
    main()
