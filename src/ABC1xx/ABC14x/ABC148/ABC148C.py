def main():
    a, b = map(int, input().split())
    print(lcm(a, b))


def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    main()
