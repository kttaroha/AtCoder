def main():
    N = int(input())
    nums = list(map(int, input().split()))

    if len(set(nums)) == N:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
