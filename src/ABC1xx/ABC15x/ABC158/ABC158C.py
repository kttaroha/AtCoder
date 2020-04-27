def main():
    A, B = map(int, input().split())
    for i in range(1, 10000):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            print(i)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
