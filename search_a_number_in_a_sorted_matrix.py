########################################################################################################################
#                                   Challenge 3 - Search a number in a sorted matrix
########################################################################################################################

# Given a matrix (a list of lists) of DISTINCT integers
matrix = [
    [1,4,7,12,15,1000],
    [2,5,19,31,32,1001],
    [3,8,24,33,35,1002],
    [40,41,42,44,45,1003],
    [99,100,103,106,128,1004]
]
# Print the given matrix
print("The matrix is given by : [")
for rows in matrix :
    print(rows,end='\n')
print("]")

# Get the target from user
target = int(input("Choose a target element :"))

# Iterating through the rows of the matrix
for row in range(5) :
    # Iterating through the elements in each row
    for col in range(6) :
        # Check if the element match the target
        if matrix[row][col] == target:

            # Print the row number and the column number where the element present in the given matrix
            print(f"Result = [{row},{col}]")

