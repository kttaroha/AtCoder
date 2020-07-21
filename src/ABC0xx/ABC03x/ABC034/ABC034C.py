def modinv(a, m):
    b, u, v = m, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u

    u %= m
    if u < 0:
        u += m
    return u


def main():
    mod = 1000000007
    W, H = map(int, input().split())
    W -= 1
    H -= 1
    fac = []
    fac.append(1)
    fac.append(1)
    for i in range(2, W+H+1):
        fac.append((fac[i-1] * i))
    print((fac[W+H]//(fac[W]*fac[H])) % mod)


if __name__ == '__main__':
    main()
