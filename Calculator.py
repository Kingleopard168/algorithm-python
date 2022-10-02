number=int(input("Enter number:"))
originnum = number
temp = 12
while temp > 0:
    number = number * 0.3
    number = number + originnum
    originnum = number
    temp = temp -1
    print(number)

   