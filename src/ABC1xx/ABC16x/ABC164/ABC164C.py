def main():
    n = int(input())
    a = [input() for i in range(n)]
    print(len(set(a)))


if __name__ == "__main__":
    main()
