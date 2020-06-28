def main():
    S = input()
    T = input()
    cnt = 0 
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1 

    print(cnt)

   
if __name__ == '__main__':
    main()