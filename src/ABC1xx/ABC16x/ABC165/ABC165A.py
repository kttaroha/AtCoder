def main():
    k = int(input())
    A, B = map(int, input().split())
    for i in range(A, B+1):
        if i % k == 0:
            print("OK")
            break
    else:
        print("NG")


if __name__ == "__main__":
    main()
