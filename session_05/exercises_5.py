# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.

import random
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .

the_num = random.randint(1, 10)
guess = None
while guess != the_num:
    guess = int(input("Guess a whole number from 1 - 10! --> "))

print("You guessed correctly!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

width = int(input("Please enter the width of a rectangle in cm --> "))
height = int(input("Please enter the height of a rectangle in cm --> "))
area = str(round(((width*height)/10),0))
print("The area of your rectangle is " + area + " metres squared to the nearest metre squared")

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

entry = None
loop_num = 0
while entry != "qwerty123":
    entry = input("Please enter password --> ")
    if entry == "qwerty123":
        print("You have successfully logged in")
        break
    print("Password failure!")
    loop_num += 1
    if loop_num > 2:
        print("System locked!")
        break

# 5. Add up all the numbers from 1 to 500 and print the answer.

x = 0
loop_no = 1
while loop_no <= 500:
    x = x + loop_no
    loop_no += 1
print("This is x --> ", x)


# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.

num_list1 = []
numbers = ""
input_counter = 0
num_selector = 0

print("Pick a number up to 10 times. One of them must be 99")

while input_counter < 10:
    numbers = int(input("Pick a number--> "))
    num_list1.append(numbers)
    input_counter +=1

while num_selector < 10:
    if num_list1[num_selector] == 99:
        print("Number 99 is at index " + str(num_selector))
    num_selector += 1


# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36

m_count = 1
while m_count < 16:
    print(str(m_count) + " x 18 = " + str(m_count*18))
    m_count += 1

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.

count8 = 0
while count8 <= 100:
    print(count8)
    count8 += 1 

# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lessons = []
results = []
grades_input_counter = 0
pointer = 0

while grades_input_counter < 3:
    lessons.append(str(input("Tell me which lesson you want graded --> ")))
    results.append(int(input("Tell me how many marks you scored --> ")))
    grades_input_counter += 1

for score in results:
    if results[pointer] >= 80:
        print(f"You got an A in {lessons[pointer]}!")
    elif results[pointer] >= 60:
        print(f"You got an B in {lessons[pointer]}.")
    elif results[pointer] >= 50:
        print(f"You got an C in {lessons[pointer]}.")
    elif results[pointer] >= 45:
        print(f"You got an D in {lessons[pointer]}.")
    elif results[pointer] >= 25:
        print(f"You got an E in {lessons[pointer]}.")
    else:
        print(f"You got an F in {lessons[pointer]}.")
    pointer += 1

# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name

names_in = 0
names = []

while names_in < 5:
    names.append(str(input("Please enter a name into the prize draw --> ")))
    names_in += 1

print("The winner is " + names[random.randint(0,4)] + "!!!")

# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

choices = ["rock", "paper", "scissors"]
rounds = 0
comp_score = 0

while rounds < 3:
    comp_choice = choices[random.randint(0,2)]
    user_choice = (input("Pick rock, paper, or scissors --> ")).lower()
    if comp_choice == "rock" and user_choice == "scissors":
        print("The computer chose " + str(comp_choice))
        print("You lose the round!\n")
        comp_score +=1
    elif comp_choice == "rock" and user_choice == "paper":
        print("The computer chose " + str(comp_choice))
        print("You win the round!\n")
        comp_score -=1
    elif comp_choice == "paper" and user_choice == "rock":
        print("The computer chose " + str(comp_choice))
        print("You lose the round!\n")
        comp_score +=1
    elif comp_choice == "paper" and user_choice == "scissors":
        print("The computer chose " + str(comp_choice))
        print("You win the round!\n")
        comp_score -=1
    elif comp_choice == "scissors" and user_choice == "paper":
        print("The computer chose " + str(comp_choice))
        print("You lose the round!\n")
        comp_score +=1
    elif comp_choice == "scissors" and user_choice == "rock":
        print("The computer chose " + str(comp_choice))
        print("You win the round!\n")
        comp_score -=1
    elif comp_choice == user_choice:
        print("The computer chose " + str(comp_choice))
        print("This round is tied\n")
    else:
        print("Something went wrong")
    rounds += 1

if comp_score > 0:
    print("\nYou lose!")
elif comp_score < 0:
    print("\nYou win!")
else:
    print("\nIt's a draw!")