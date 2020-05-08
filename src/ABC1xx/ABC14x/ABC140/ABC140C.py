def main():
    _ = int(input())
    B = list(map(int, input().split()))
    A = []
    A.append(B[0])
    A.append(min(B[0:2]))
    
    for i in range(1, len(B[:-1])):
        A.append(min(B[i], B[i+1]))
    if len(B) > 1:
        A.append(B[-1])

    print(sum(A))

    
if __name__ == '__main__':
    main()