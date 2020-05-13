def main():
    A = list(input())
    cnt = 0
    nums_right = []
    nums_left = []
    current_right = 0
    current_left = 0
    for a in A:
        nums_right.append(current_right)
        if a == "<":
            current_right += 1
        else:
            current_right = 0
    else:
        nums_right.append(current_right)

    for a_ in A[::-1]:
        nums_left.append(current_left)
        if a_ == ">":
            current_left += 1
        else:
            current_left = 0
    else:
        nums_left.append(current_left)

    nums_left = nums_left[::-1]

    for nr, nl in zip(nums_right, nums_left):
        cnt += max(nr, nl)
    print(cnt)


if __name__ == '__main__':
    main()
