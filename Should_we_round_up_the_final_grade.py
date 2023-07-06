########################################################################################################################
#                                   Challenge 1 - Grading problem
########################################################################################################################

# Getting grade as a input.
grade = int(input("Enter your grade :"))

# Rounding off to the next multiple of 5
round_off = ((grade // 5) + 1)*5

# Finding the difference between the grade and the next multiple of 5
diff =  round_off - grade

# Assigning grade is equal to next multiple of 5 if the difference is less than 3 or else no change
grade = round_off if diff < 3 else grade

# If grade is less than 40 report 'Failed'
if grade < 40 :
    print(f"Sorry, You've \'Failed' and your grade is {grade}")

# If grade is greater than 80 report 'Distinction'
elif grade > 80 :
    print(f"You secured \'Distinction' and your grade is {grade}")

# Else report 'Passed'
else :
    print(f"You \'Passed' and your grade is {grade}")
