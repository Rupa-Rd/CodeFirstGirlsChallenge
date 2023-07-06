########################################################################################################################
#                                   Challenge 4 - Factorials
########################################################################################################################

# Define factorial function
def factorial( num ) :
   # Define fact = 1
    fact = 1
    for i in range(1,num+1) : # Iterating i to 1,2,3,....n
        # Calculating fact = fact * i
        fact *= i
        # Return 1 if num = 0 else return fact
    return 1 if num == 0 else fact

# Get the value of number from user
number = int(input("Enter a Number : "))

# Print the factorial value
print(f"The Factorial of {number} is {factorial(number)}")

