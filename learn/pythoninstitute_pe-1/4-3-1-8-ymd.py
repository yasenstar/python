def is_year_leap(year):
    # 能被4整除、但不能被100整除，或能被400整除的年份为闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]
    if month in month31:
        return 31
    elif month in month30:
        return 30
    elif is_year_leap(year):
        return 29
    else:
        return 28

def day_of_year(year, month, day):
    if days_in_month(year, month) >= day:
        return day
    else:
        return None

print(day_of_year(2000, 12, 31))
