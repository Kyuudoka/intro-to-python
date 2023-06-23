# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

name = input("What is your name? --> ")
if name == "Bob":
    print("Welcome Bob")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

if name != "Alice":
    print("You are not Alice!")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".

password = input("Please enter password --> ")
if password == "querty123":
    print("You have successfully logged in.")
else:
    print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

number = int(input("Please enter a number --> "))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

num1 = int(input("Enter your first number --> "))
num2 = int(input("Enter your second number --> "))
total = num1 + num2
if total > 21:
    print("Bust")
else:
    print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

length = int(input("Tell me the length of your rectangle --> "))
width = int(input("Tell me the width of your rectangle ---> "))
if length == width:
    print("Your rectangle is obviously a square")
else:
    print("Your rectangle is obviously not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary = int(input("Tell me your current yearly salary (as a plain number without units)--> "))
yos = int(input("Tell me how many years you have worked at oour company --> "))
if yos >= 3:
    print(f"Your bonus will be £{salary/10}!")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

num = int(input("Give me a whole number --> "))
if num > 0:
    print(f"{num} cubed is {num*num*num}")
else:
    print(f"Half of {num} is {num/2}")


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

name = input("Tell me your name --> ")
if name == "Alice":
    print("Hello, Alice")
elif name == "Bob":
    print("You're not Bob! I'M Bob!")
else:
    print("You are probably actually Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

age = int(input("I can check if you can go to this secondary school. How many years old are you? --> "))
if age <= 0:
    print("You're not born yet!")
elif age < 11:
    print("You're too young to go to this school!")
elif age >= 11 and age <= 16:
    print("You can can come to this school!")
elif age > 16:
    print("You're too old for this school!")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

month = input("Enter a month and I'll tell you what season it is in the UK --> ")
if month == "March" or month == "April" or month == "May":
    print(f"{month} is in Spring.")
elif month == "June" or month == "July" or month == "August":
    print(f"{month} is in Summer.")
elif month == "September" or month == "October" or month == "November":
    print(f"{month} is in Autumn.")
elif month == "December" or month == "January" or month == "February":
    print(f"{month} is in Winter.")
else:
    print("I don't know. Either that's not a month or you didn't capitalize it or spell it correctly so I couldn't read it.")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

num3 = int(input("Give me your first number --> "))
num4 = int(input("Give me your second number --> "))
if num3 % 2 != 0 and num4 % 2 != 0:
    print("Both of these are odd numbers.")
else:
    print(f"{num3} x {num4} = {num3 * num4}")

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

num5 = int(input("Give me your first number --> "))
num6 = int(input("Give me your second number --> "))

if num5 > num6:
    print(f"{num5} is the greater number")
elif num6 > num5:
    print(f"{num6} is the greater number")
else:
    print("Those numbers are equal")

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary2 = int(input("Tell me your current yearly salary (as a plain number without units)--> "))
yos2 = int(input("Tell me how many years you have worked at oour company --> "))
if yos2 >= 3 and yos2 <= 5:
    print(f"Your bonus will be £{salary2/10}!")
elif yos2 >= 7:
    print(f"Your bonus will be £{salary2/5}!")
else:
    print("You will not recieve a bonus this time.")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.

age1 = int(input("Give me the age of the first person. --> "))
age2 = int(input("Give me the age of the second person. --> "))
age3 = int(input("Give me the age of the third person. --> "))

if age1 > age2 and age1 > age3:
    print("The first person is the eldest")
elif age2 > age1 and age2 > age3:
    print("The second person is the eldest")
elif age3 > age1 and age3 > age2:
    print("The third person is the eldest")
elif age1 == age2 == age3:
    print("All three are the same age")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson = input("Tell me which lesson you want graded --> ")
score = int(input("Tell me how many marks you scored --> "))
if score >= 80:
    print(f"You got an A in {lesson}!")
elif score >= 60:
    print(f"You got an B in {lesson}.")
elif score >= 50:
    print(f"You got an C in {lesson}.")
elif score >= 45:
    print(f"You got an D in {lesson}.")
elif score >= 25:
    print(f"You got an E in {lesson}.")
else:
    print(f"You got an F in {lesson}.")
