from collections import defaultdict


def main():
    n = int(input())
    strings = [input() for i in range(n)]
    s_dict = defaultdict(int)
    for s in strings:
        s_dict[s] -= 1
    s_sorted = sorted(s_dict.items(), key=lambda x: (x[1], x[0]))

    max_num = s_sorted[0][1]
    for t in s_sorted:
        if t[1] == max_num:
            print(t[0])
        else:
            break


if __name__ == "__main__":
    main()
