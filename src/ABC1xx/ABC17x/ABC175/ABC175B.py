from itertools import combinations

def main():
    _ = int(input())
    A = list(map(int, input().split()))
    if len(set(A)) < 3:
        print(0)
        return
    C = combinations(A, 3)
    ans = 0
    for c in C:
        c = sorted(c)
        if c[0] != c[1] and c[0] != c[1] and c[1] != c[2]:
            if c[2] < c[1] + c[0]:
                ans += 1
    print(ans)
    
    
if __name__ == '__main__':
    main()