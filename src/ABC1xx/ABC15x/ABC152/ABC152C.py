def main():
    _ = int(input())
    A = list(map(int, input().split()))
    min_value = 1e10
    cnt = 0
    for a in A:
        if a <= min_value:
            min_value = a 
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
