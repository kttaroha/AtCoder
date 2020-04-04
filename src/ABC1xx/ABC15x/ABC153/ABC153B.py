def main():
    hp, num = map(int, input().split())
    a = list(map(int, input().split()))
    attack = sum(a)

    if hp > attack:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
