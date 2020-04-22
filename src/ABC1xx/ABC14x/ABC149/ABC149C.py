def main():
    x = int(input())

    while True:
        flag_prime = True
        x_ = int(x**0.5) + 1

        for i in range(2, x_):
            if x % i == 0:
                flag_prime = False
                break

        if flag_prime:
            break

        x += 1

    print(x)


if __name__ == "__main__":
    main()
