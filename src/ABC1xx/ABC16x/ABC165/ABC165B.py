def main():
    x = int(input())
    i = 1
    m_prev = 100
    while True:
        m_now = int(m_prev * (1.01))
        if m_now >= x:
            print(i)
            break
        m_prev = m_now
        i += 1


if __name__ == "__main__":
    main()