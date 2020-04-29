def main():
    n = int(input())
    a = 1
    b = n
    a_r = int(n**0.5) + 1
    for i in range(1, a_r):
        if n % i == 0:
            b_tmp = n // i
            if i + b_tmp < a + b:
                a = i
                b = b_tmp
    print(a+b-2)


if __name__ == "__main__":
    main()
