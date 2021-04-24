#A program that gets a number from the user and prints out, from 1 to that number:
user_num = int(input("Enter a number: \n"))
def fizz_buzz(user_num_local):
    if(user_num_local % 3 == 0 and user_num_local % 5 == 0):
        print("Fizz Buzz")
    elif(user_num_local % 5 == 0):
        print("Buzz")
    elif(user_num_local % 3 == 0):
        print("Fizz")
    else:
        print("The number is: " + str(user_num_local))
fizz_buzz(user_num)

    
