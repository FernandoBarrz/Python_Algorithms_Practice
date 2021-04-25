# A program that gets a number from the user and prints out a list of factorials up to that number:
# Using Recursive Code
def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num - 1)



user_num = int(input("Enter a number: "))

print(factorial(user_num))
