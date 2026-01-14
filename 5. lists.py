# 5. lists

# -------------------------------
# 1. Creating a List
# -------------------------------
marks = ['saad', 'hassan', 'owais', 'bilal', 'hafsa']
print(marks)                 # ['saad', 'hassan', 'owais', 'bilal', 'hafsa']
print(type(marks))           # <class 'list'>
print(len(marks))            # 5


# -------------------------------
# 2. Mutability (List can change)
# -------------------------------
marks[0] = 'ali'             # changing value at index 0
print(marks)                 # ['ali', 'hassan', 'owais', 'bilal', 'hafsa']


# -------------------------------
# 3. Indexing & Slicing
# -------------------------------
print(marks[1:3])   #print elements from index 1 to 2            
                    # ['hassan', 'owais']
print(marks[-3:-1]) #print elements from index -3 to -2          
                    # ['owais', 'bilal']


# -------------------------------
# 4. Common List Methods
# -------------------------------
nums = [2, 1, 3, 4, 5]

nums.sort()                  # sorts the list in ascending order
print(nums)                  # [1, 2, 3, 4, 5]

nums.append(6)               # adds 6 at the end of the list
print(nums)                  # [1, 2, 3, 4, 5, 6]

nums.insert(0, 0)            # inserts 0 at index 0
print(nums)                  # [0, 1, 2, 3, 4, 5, 6]

nums.remove(3)               # removes the first occurrence of 3
print(nums)                  # [0, 1, 2, 4, 5, 6]

nums.pop()                   # removes and returns the last item
print(nums)                  # [0, 1, 2, 4, 5]

nums.reverse()               # reverses the list
print(nums)                  # [5, 4, 2, 1, 0]


# -------------------------------
# 5. Built-in List Functions
# -------------------------------
print(len(nums))             # 5
print(max(nums))             # 5
print(min(nums))             # 0
print(sum(nums))             # 12


# -------------------------------
# 6. Copying a List
# -------------------------------
copy_nums = nums.copy()
print(copy_nums)             # same values, different memory location