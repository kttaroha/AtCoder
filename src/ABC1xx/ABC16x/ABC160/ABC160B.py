def main():
    m = int(input())
    num_500 = m // 500
    res = m % 500
    num_5 = res // 5
    print(num_500 * 1000 + num_5 * 5)


if __name__ == "__main__":
    main()
