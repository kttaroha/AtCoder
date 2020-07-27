def main():
    s = int(input())
    if s <= 599:
        print(8)
    else:
        print(10 - s//200)


if __name__ == '__main__':
    main()
