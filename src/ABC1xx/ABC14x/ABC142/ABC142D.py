def main():
    a, b = map(int, input().split())
    x = gcd(a, b)
    ans = prime_factorize(x)
    print(len(set(ans)) + 1)


def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


if __name__ == '__main__':
    main()
