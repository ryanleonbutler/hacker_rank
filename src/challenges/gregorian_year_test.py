def is_leap(year):
    leap = False

    while 1900 > year > 100000:
        year = int(input())

    # Write your logic here
    if year % 4 == 0:
        leap = True
    if year % 100 == 0 and year % 400 == 0:
        leap = True
    elif year % 100 == 0 and year % 400 != 0:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
