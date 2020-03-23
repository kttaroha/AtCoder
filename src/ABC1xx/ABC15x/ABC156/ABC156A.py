a, b = list(map(int, input().split()))
if a <= 10:
    print(b + 100*(10 - a))
else:
    print(b)