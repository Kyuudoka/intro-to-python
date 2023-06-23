# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruits)

# 2. Add "Grapes" to the list and print the list.

fruits.append("Grapes")
print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.

fruits[2] = "Strawberries"
print(fruits)

# 4. Remove "Apples" from the list and print the list.

del(fruits[0])
print(fruits)

# 5. Print out the current length of the list.

print(len(fruits))

# 6. Order the list alphabetically.

fruits.sort()

# 7. Print out the list again.

print(fruits)


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.

for fruit in fruits:
    print(fruit)

# 2. Print the numbers 1 to 100 (including the number 100).

for number_list in range(1, 101):
    print(number_list)

# 3. Print all odd numbers from 1 to 100.

for number_list2 in range(1, 101, 2):
    print(number_list2)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).

skipped_games = [1916, 1940, 1944, 2020]

for games in range(1896, 2024, 4):
    if games not in skipped_games:
        print(games)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.

num_list = [7, 3, 45, 32, 5, 56, 92, 4, 8, 38]
evens = []
odds = []

for num in num_list:
    if (num % 2) == 0:
        evens.append(num)
    else:
        odds.append(num)

print("Number of even numbers --> ", len(evens))
print("Numer of odd numbers --> ", len(odds))

print("evens: ", evens)
print("odds: ", odds)

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

names = ["Ella", "Jonathan", "Dave", "Nymeria", "Gordon"]

for name in names:
    print("Hello", name)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".

letter_list = []
for letter in "supercalifragilisticexpialidocious":
    letter_list.append(letter)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

num_list2 = [5, 3, 7, 2, 8]
new_nums = []
for num in num_list2:
    new_nums.append(num*num)

# print(new_nums)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
dr_names = []
names2 = ["Ella", "Jonathan", "Dave", "Nymeria", "Gordon"]
for name in names2:
    dr_names.append("Dr. " + name)

print(dr_names)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)