from collections import deque


def main():
    k = int(input())
    if k <= 9:
        print(k)
    else:
        queue = deque()
        for i in range(1, 10):
            queue.append(i)
        flag = 1
        cnt_lunlun = 9
        while flag:
            first_element = queue.popleft()
            lunlun_nums = extend_lunlun(first_element)
            for n in lunlun_nums:
                queue.append(n)
                cnt_lunlun += 1
                if cnt_lunlun == k:
                    flag -= 1
                    break
        print(queue.pop())


def extend_lunlun(num):
    lunlun_nums = []
    last_digit = num % 10
    for i in range(-1, 2):
        d = last_digit + i
        if d >= 0 and d <= 9:
            lunlun_nums.append(num*10+d)
    return lunlun_nums


if __name__ == "__main__":
    main()
