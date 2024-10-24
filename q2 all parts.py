# Problem-2: Fun with Numbers
odd_numbers = [1, 3, 5, 7, 9]  # a) List of 5 odd numbers
even_numbers = [2, 4, 6, 8, 10]  # b) List of 5 even numbers

# c) Combine the two lists
combined_list = odd_numbers + even_numbers

# d) Add prime numbers 11, 17, and 29 at the beginning
prime_numbers = [11, 17, 29]
combined_list = prime_numbers + combined_list

# e) Count the total number of elements
print(f"Number of elements: {len(combined_list)}")

# f) Replace the last three numbers with 100, 200, and 300
combined_list[-3:] = [100, 200, 300]

# g) Delete all the numbers in the list
combined_list.clear()

# h) Delete the list itself
del combined_list
