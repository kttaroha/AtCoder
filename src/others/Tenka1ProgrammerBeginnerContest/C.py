def main():
    N = int(input())
    A = sorted([int(input()) for _ in range(N)])
    A_rev = sorted(A, reverse=True)

    # 端に大きな数がくるパターン
    ans1 = 0
    large_num_inside1 = (N - 2) // 2
    small_num_inside1 = (N - 2) - large_num_inside1

    for i in range(large_num_inside1):
        ans1 += 2 * A_rev[i]

    for i in range(small_num_inside1):
        ans1 -= 2 * A[i]
    
    if N % 2 == 0:
        ans1 += A_rev[large_num_inside1]
        ans1 -= A_rev[large_num_inside1+1]
    
    else:
        ans1 += A_rev[large_num_inside1]
        ans1 += A_rev[large_num_inside1+1]
            
    # 端に小さな数がくるパターン
    ans2 = 0
    small_num_inside2 = (N - 2) // 2
    large_num_inside2 = (N - 2) - small_num_inside2

    for i in range(large_num_inside2):
        ans2 += 2 * A_rev[i]

    for i in range(small_num_inside2):
        ans2 -= 2 * A[i]

    if N % 2 == 0:
        ans2 -= A[small_num_inside2]
        ans2 += A[small_num_inside2+1]

    else:
        ans2 -= A[small_num_inside2]
        ans2 -= A[small_num_inside2+1]

    print(max(ans1, ans2))


if __name__ == '__main__':
    main()
