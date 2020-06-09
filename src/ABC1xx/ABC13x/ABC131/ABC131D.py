def main():
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    time = 0
    jobs = sorted(jobs, key=lambda x: x[1])
    for j in jobs:
        time += j[0]
        if time > j[1]:
            print("No")
            return

    else:
        print("Yes")


if __name__ == '__main__':
    main()
