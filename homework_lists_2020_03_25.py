# Example:
# To take a slice from a list, use the list[start:end] syntax.
# Start and end are integers that refer to the position of elements.
# The endpoint is not included. An optional third integer specifies the step.

my_list = [10, 20, 30, 40, 50, 60]
print(my_list[1:4])
# => [20, 30, 40]



# Example: return a list consisting of all single-digit numbers in a list.
# Assume all numbers are positive
# single([10, 33, 4, 9, 219]) => [4, 9]

def single(numbers):
    # a temporary variable to store the result
    result = []

    for n in numbers:
        if n < 10:
            result.append(n)

    return result



# Exercise 1:
# Write a function called firstvowel(words) that prints only the words
# that begin with a vowel ("aeiou"). Use the isvowel function.
#
# Example: firstvowel(["banana", "apple", "cab", "door", "elephant", "umpire"])
# should print
#
# apple
# elephant
# umpire

def isvowel(letter):
    return letter in "aeiou"





# Exercise 2:
# Write a function called average(numbers) that returns the average of the
# list of numbers.
#
# Example: average([10, 30, 40]) => 26.666667



# Exercise 3:
# Reverse the given list
#
# Example: reverse([3, 5, 1, 2, 9]) => [9, 2, 1, 5, 3]



# Exercise 4:
# Print the left half of a list. If there are an odd number of elements,
# round down. Hint: Use math.floor or the // operator that divides
# and truncates the result
#
# Example: half([1, 5, 2, 3, 9, 2, 4]) => [1, 5, 2]




# Exercise 5:
# You played the lottery and want to know how many numbers you got right.
# Write a function that compares your numbers to the drawn numbers and
# returns the number of matches
#
# Example: lottery([10, 24, 25, 29, 32, 55], [11, 24, 25, 54, 55, 59]) => 3
# 24, 25 and 55 are matches
