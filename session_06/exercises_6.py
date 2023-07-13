# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".

apple = {
    "Type": "Bramley",
    "Price": 0.39,
    "Colour": "Green"
}

# 2. Add the best before date to the dictionary - print the dictionary.

apple["BBE"] = "03/08/23"

# 3. Change the price to 0.41 - print the dictionary.

apple["Price"] = 0.41

# 4. Set the apple to be on offer using a Boolean - print the dictionary.

apple["On offer"] = True

# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.

del(apple["On offer"])

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.

usr_input = input("Do you wish to enter names? Type anything for yes, or type x for exit --> ")
nameslist = []

while usr_input != "x":
    nameentry = input("Please enter a name, or press x to skip --> ")
    if nameentry == "x":
        break
    else:
        names = {
            nameentry : input("Please enter the age of this person --> ")
        }
    nameslist.append(names)

print(nameslist)

# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).

menu = [{
    "name":"steak caponata",
    "price":11.99,
    "veggie":False
},
{
    "name":"salmon bagel",
    "price":6.99,
    "veggie":False
},
{
    "name":"mushroom orzotto",
    "price":8.99,
    "veggie":True
},
{
    "name":"roasted squash & goat's cheese lentil salad",
    "price":8.99,
    "veggie":True
},
{
    "name":"hoisin beef bao",
    "price":10.99,
    "veggie":True
}]

# print("Here are the vegetarian dishes in the Menu:\n")
# for dish in menu:
#     if dish["veggie"]:
#         print(dish["name"], dish["price"])

# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

import random

beetle = {"body":0, "head": 0, "legs":0, "ant":0, "eyes":0, "mouth":0}
finished_beetle = {"body":1, "head": 1, "legs":6, "ant":2, "eyes":2, "mouth":1}
comp_beetle = {"body":0, "head": 0, "legs":0, "ant":0, "eyes":0, "mouth":0}

round_no = 1

beetle_rules = '''The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins.'''

print(f"\n{beetle_rules}\n")

def draw_beetle(roll_result, beetlechoice):
    if roll_result == 5:
        if beetlechoice["head"] < 1:
            beetlechoice["head"] += 1
    elif roll_result == 6:
        if beetlechoice["body"] < 1:
            beetlechoice["body"] += 1
    elif roll_result == 4:
        if beetlechoice["body"] == 1:
            if beetlechoice["legs"] < 6:
                beetlechoice["legs"] += 1
    elif beetlechoice["head"] > 0:
        if roll_result == 1:
            if beetlechoice["mouth"] < 1:
                beetlechoice["mouth"] += 1
        elif roll_result == 2:
            if beetlechoice["eyes"] < 2:
                beetlechoice["eyes"] += 1
        elif roll_result == 3:
            if beetlechoice["ant"] < 2:
                beetlechoice["ant"] += 1

while beetle != finished_beetle:
    print("Round: " + str(round_no))
    print("Here is your current beetle\n", beetle)
    roll_prompt = input("\nPress any key to roll the dice --> ")
    roll = random.randint(1,6)
    print("You rolled " + str(roll) +"\n")
    draw_beetle(roll, beetle)

    print("Here is the computer's beetle\n", comp_beetle)
    roll2 = random.randint(1,6)
    print("The computer rolled " + str(roll2) +"\n--------------------------------------------------------------------\n")
    draw_beetle(roll2, comp_beetle)

    if beetle == finished_beetle:
        print("You beat the computer!")
        break
    elif comp_beetle == finished_beetle:
        print("The computer has won!")
        break
    else:
        round_no += 1