# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

r_width = 7
r_length = 10
r_area = r_width * r_length

print("Rectangle of width " + str(r_width) + " and height " + str(r_length) + " has an area of " + str(r_area) + ".")
# can also write this much more nicely as an f string but doesn't use casting which was the point of the exercise

# 2. Write code that prints the length of the string, 'python'.

print(len("python"))

# 3. Print out the first and third letter of the word 'python'.

print("python"[0], "python"[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.

name = input("Can you type your name here please? --> ")
print("Hello " + name + " :)\n ")

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

age = input(name + ", if you tell me how many years old you are, I'll tell you how many years old you'll be in 15 years time. Type here --> ")
new_age = str(int(age) + 15)
print(name + ", in 15 years' time, you will be " + new_age + " years old!\n ")

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

# skipped this one as already did it above

# 7. Ask the user to enter their hometown, print it out in uppercase letters.

hometown = input("Can you please tell me your hometown? --> ")
print("Ah, so you are " + name + " of " + str(hometown.upper()) + "!\n ")

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

fav_colour_raw = input("So " + name + ", what's your favourite colour? Mine is purple :) --> ")
fav_colour = fav_colour_raw.lower()
colour_length = len(fav_colour)

if fav_colour == "purple" or fav_colour == "lilac" or fav_colour == "violet" or fav_colour == "mauve":
    print("An excellent choice! You might find it interesting to google the history of purple dyes, especially Tyrean Purple.")
elif fav_colour == "brown":
    print("A bold choice, but I respect you for it.")
elif fav_colour == "green":
    print("I like green too! It reminds me of nature and trees :D")
elif fav_colour == "azure":
    print("It's a lovely colour, reminds me too much of my job though :')")
elif fav_colour == "turquoise":
    print("A gorgeous colour, and also the name of a gorgeous stone.")
elif fav_colour == "none" or fav_colour == "i don't know" or fav_colour == "don't know" or fav_colour == "don't have one" or fav_colour == "i don't have one" or fav_colour == "all of them" or fav_colour == "any colour" or fav_colour == "any" or fav_colour == "all":
    print("Fair enough, there are so many to choose from!")
elif fav_colour == "grey" or fav_colour == "gray":
    print(name + ", it sounds like you're allergic to fun >:p")
elif fav_colour == "red" or fav_colour == "crimson" or fav_colour == "orange" or fav_colour == "scarlet":
    print("Warm and firey.")
elif fav_colour == "yellow":
    print("The colour of sunshine and happiness and joy. Or some people might say it's the colour of fear, sickness, and decay; an interesting contradiction.")
elif fav_colour == "black":
    print("You're either a fan of keeping things simple and elegant, an edgelord, or an undertaker. Or maybe you're Batman. In any case pretty cool.")
elif fav_colour == "white":
    print("The most neutral answer, as white light is comprised of all of them. Or maybe you had a mind blank...")
elif fav_colour == "blue" or fav_colour == "indigo" or fav_colour == "periwinkle blue":
    print("A nice and calming colour, like a clear sky or a body of water.")
elif fav_colour == "pink" or fav_colour == "magenta":
    print("A highly underrated cousin to red and purple. You might consider it feminine or masculine depending on where you live.")
elif fav_colour.isalpha():
    print("An unsual choice. Or maybe you're messing with me and it's not a colour at all.")
else:
    print("That's not even a word!")
print("\n")

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

print("As a simple bot I don't have any awareness of when and where I am (or any awareness in general). " + name + ", can you tell me:")
month = input("Which month it is right now? --> ")
weather = input("Give me an adjective to describe the weather where you are right now --> ")
print("Thanks " + name + "! So it is " + month + " and it is " + weather + " today then.\n ")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

print("I can calculate for you an average temperature based on 5 temperatures for " + month + ". Please enter 5 temperatures as numbers without units.")
temp1 = int(input("Temperature 1 --> "))
temp2 = int(input("Temperature 2 --> "))
temp3 = int(input("Temperature 3 --> "))
temp4 = int(input("Temperature 4 --> "))
temp5 = int(input("Temperature 5 --> "))

av_temp = str((temp1 + temp2 + temp3 + temp4 + temp5)/5)
print("Great, thanks " + name + "! It is " + month + " and the average temperature is " + av_temp + " degrees Celcius (or whatever unit the orginal temperatures had).\n ")

# 11. Print out the above sentence but make the month upper case.

print("So just in case you forgot, this is the average temperature for " + month.upper() + ".\n")

# 12. Create a variable that holds your favourite animals and print it out. 
#   Make sure the animals are all on different lines and tabbed.

fav_animals = "cat\nsnow\nleopard\nsnake\njaguar\nlion\ntiger\nwolf\nperegrine falcon\narctic fox\ndragon\ncondor\nvulture\nblack bear\neurasian lynx\nturtle\nmanatee"
print("My favourite animals:\n" + fav_animals + "\n")

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.

user_name = str(input("Please enter a username --> "))
user_point = int(input("Give me a number and I'll pick the corresponding character from your username --> "))
print(user_name[user_point])

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".

string = "WelcometoPython"
print(string[1:14:2])