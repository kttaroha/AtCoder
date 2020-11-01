def main():
    x = int(input())
    ans = 0
    for i in range(50000+1):
        if int(i * 1.08) == x:
            ans = i
    if ans:
        print(ans)
    else:
        print(":(")


if __name__ == '__main__':
    main()
