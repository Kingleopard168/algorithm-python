number=int(input("Enter number:"))
num = number
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    print(remainder, "x")
    reverse = (reverse * 10) + remainder
    print(reverse, "y")
    temp = temp // 10
    print(temp, "z")
if num == reverse:
  print('PalinDrome')
else:
  print("Not Palindrome")