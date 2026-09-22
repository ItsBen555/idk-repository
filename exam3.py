year_num = int(input('please enter the year you want to know if its leap : '))

print(year_num%4)
print(year_num%100)

print('-'*98)


if year_num%4==0 and year_num%100!=0 or year_num%400==0:
    print(f'{year_num} is a leap year')
else:
    print(f"{year_num} is not a leap year")

