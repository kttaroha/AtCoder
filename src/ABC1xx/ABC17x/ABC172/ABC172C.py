def main():
    N, M, K = map(int, input().split())
    ns = list(map(int, input().split()))
    ms = list(map(int, input().split()))
    ns_accum, ms_accum = [0], [0]
    n_accum_tmp, m_accum_tmp, num_books = 0, 0, 0
    for i in range(len(ns)):
        n_accum_tmp += ns[i]
        ns_accum.append(n_accum_tmp)

    for i in range(len(ms)):
        m_accum_tmp += ms[i]
        ms_accum.append(m_accum_tmp)

    for i in range(len(ns_accum)):
        time_left = K - ns_accum[i]
        if time_left >= 0:
            num_book_m = max(0, binary_search(ms_accum, time_left))
            num_books = max(num_books, i+num_book_m)

    print(num_books)


def binary_search(A, x):
    ok = -1
    ng = len(A)
    while (abs(ok - ng) > 1):
        mid = (ng+ok) // 2
        if A[mid] <= x:
            ok = mid
        else:
            ng = mid

    return ok


if __name__ == '__main__':
    main()
