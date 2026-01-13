#4. Loop (For loop and While loop)
# For loop to iterate over a range of numbers
for i in range(1, 6):
     # i takes one value at a time from the range
    print(i)  # prints current value of i

# While loop to print a message until a condition is met
# initialize variable
i = 1
while i <= 5:
    print(i)      # prints current value of i
    i += 1        # increases i by 1 (VERY IMPORTANT)
# Without i += 1, the loop would run infinitely since i would always be 1