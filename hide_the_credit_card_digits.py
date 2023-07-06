########################################################################################################################
#                                   Challenge 5 - Hide the credit card digits.
########################################################################################################################
import random
# Importing the random library to generate random credit card number
from random import *
# Generating a 16 digits credit card number using randint function
credit_card_number = str(randint(1000000000000000,10000000000000000))
# Defining a credit_card variable to format the card number
credit_card = ""
# Defining a result variable to hide the first 12 digits of a card number
result = ""
# Declare number_count = 1
number_count = 1
# Iterating through the randomly generated credit card number
for i in credit_card_number :
    # Check if the number_count greater than or equal to 13
    if number_count >= 13:
        # Make the last four digits of the card number visible
        result += i
        # Format the card details and save it in credit_card variable
        credit_card += i
    else :
        # Hide the first 12 digits using "X"
        result += "X"
        # Format the card details and save it in credit_card variable
        credit_card += i
        # Check if the number_count is divisible by 4
        if number_count % 4 == 0 :
            # Then add a space to format the credit card number
            credit_card += " "
            result += " "
    # Increase the number_count by 1
    number_count += 1
# Print the formatted randomly generated card number
print(f"Randomly generated credit card number: {credit_card}")
# Print the card number after hiding the first 12 digits
print(f"After hiding the first 12 digits, it would be: {result}")

