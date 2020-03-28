def main():
    day = input()
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    days_dict = {days[i]: 7-i for i in range(len(days))}
    print(days_dict[day])


if __name__ == "__main__":
    main()
