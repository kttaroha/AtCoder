def main():
    _ = int(input())
    A = list(map(int, input().split()))

    m_dist = 0
    e_dist = 0
    c_dist = 0

    for a in A:
        m_dist += abs(a)
        e_dist += a ** 2
        c_dist = max(c_dist, abs(a))

    print(m_dist)
    print(e_dist**0.5)
    print(c_dist)


if __name__ == '__main__':
    main()
