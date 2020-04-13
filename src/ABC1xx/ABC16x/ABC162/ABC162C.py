def main():
    s = 0
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, n+1):
            gcd_tmp = gcd(i, j)
            for k in range(1, n+1):
                s += gcd(gcd_tmp, k)
    print(s)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()
