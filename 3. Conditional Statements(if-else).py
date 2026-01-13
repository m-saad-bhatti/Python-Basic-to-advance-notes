# 3. Conditional Statements (if, else, elif)

# Example program: Checking a student's grade
# Step 1: Store a score in a variable
score = 85   # You can change this number to test different cases

# Step 2: Use if, elif, else to decide the grade
if score >= 90:
    # This block runs if the score is 90 or above
    print("Grade: A")
elif score >= 75:
    # This block runs if the score is between 75 and 89
    print("Grade: B")
elif score >= 60:
    # This block runs if the score is between 60 and 74
    print("Grade: C")
else:
    # This block runs if none of the above conditions are true (score < 60)
    print("Grade: F")

# Step 3: Program ends after printing the grade
