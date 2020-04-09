def main():
    colors = input().split()
    nums = list(map(int, input().split()))
    d = {
        colors[i]: nums[i] for i in range(2)
        }
    colors_rm = input()
    d[colors_rm] -= 1
    print(d[colors[0]], d[colors[1]])


if __name__ == "__main__":
    main()
