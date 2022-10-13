# Python program to add two binary numbers.

# Driver code
# Declaring the variables
a = "1010"
b = "1011"

# Calculating binary value using function
sum = bin(int(a, 2) + int(b, 2))

# Printing result
print(sum[2:])
