# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for each column in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
