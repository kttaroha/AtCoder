def main():
    A, B, C, D = map(int, input().split())
    num_C_div = B // C - (A - 1) // C
    num_D_div = B // D - (A - 1) // D
    CD_lcm = lcm(C, D)
    num_CandD_div = B // (CD_lcm) - (A - 1) // (CD_lcm)
    num_CorD_div = num_C_div + num_D_div - num_CandD_div
    print((B - A + 1) - num_CorD_div)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == '__main__':
    main()
