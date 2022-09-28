'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
z=0
print("Video Game Trivia")

print()

print("Question 1")
print("A. The Leviathan")
print("B. Mjolnir")
print("C. Godslayer")
print("D. Bone Reaver")

print()

user_input = input("What is Kratos's axe called? ")

print()

if user_input.upper() == "A":
    x=1
elif user_input.upper().strip() == "B":
    x=2
elif user_input.upper() == "C":
    x=2
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was The Leviathan")

print()

print("Question 2")
print("A. 3 stone, 5 iron")
print("B. 4 stone, 2 iron")
print("C. 4 wood, 2 iron")
print("D. 3 wood, 5 iron")

print()

user_input = input("What materials are needed to make a smithing table in Minecraft? ")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper() == "B":
    x=2
elif user_input.upper().strip() == "C":
    x=1
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 4 wood, 2 iron")

print()

print("Question 3")
print("A. Cursed Captain")
print("B. Gold Hoarder")
print("C. Pirate King")
print("D. Pirate Lord")

print()

user_input = input("What is the name of the final boss in Sea of Thieves, Tall Tales? ")

print()

if user_input.upper() == "A":
    x=2
elif user_input.upper().strip() == "B":
    x=1
elif user_input.upper() == "C":
    x=2
elif user_input.upper() == "D":
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was the Gold Hoarder")

print()

print("Question 4")
user_input = input("How much boost does a small boost pad give you in Rocket League? ")

print()

if user_input.upper() == "12":
    x=1
else:
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 12")

print()

print("Question 5")
user_input = input("How long does it take for a large boost pad to respawn in Rocket League? ")

print()

if user_input.upper() == "10":
    x=1
else:
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 10")

print()

print("Question 6")
user_input = input("How many generators are needed to open the escape doors in Dead by Daylight? ")

print()

if user_input.upper() == "5":
    x=1
else:
    x=2

if x==1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 5")

print()

print("Question 7")
user_input = input("How many Call of Duty games are there? ")

print()

if user_input.upper() == "19":
    x = 1
else:
    x=2

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 19")

print()

print("Question 8")
print("A. The Black Lotus")
print("B. Company of Onyx")
print("C. Trevor and Kids")
print("D. The Black Hand")

print()

user_input = input("What is the name of the enemies in Just Cause 4? ")

print()

if user_input.upper() == "A":
    x = 2
elif user_input.upper() == "B":
    x = 2
elif user_input.upper() == "C":
    x = 2
elif user_input.upper().strip() == "D":
    x = 1

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was The Black Hand")

print()

print("Question 9")
print("A. 24 Story Levels")
print("B. 36 Story Levels")
print("C. 43 Story Levels")
print("D. 52 Story Levels")

print()

user_input = input("How many levels are there in Lego Star Wars, The Complete Saga? ")

print()

if user_input.upper() == "A":
    x = 2
elif user_input.upper().strip() == "B":
    x = 1
elif user_input.upper() == "C":
    x = 2
elif user_input.upper() == "D":
    x = 2

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was 36")

print()

print("Question 10")
user_input = input("What is the name of the first dragon introduced in Skylanders? ")

print()

if user_input.upper().strip() == "SPYRO":
    x = 1
else:
    x=2

if x == 1:
    print("Correct")
    z+=1
else:
    print("Wrong, the answer was Spyro")

print()

print("Your score is",z/10*100,"%")
y=float(z/10*100)

if y<60:
    print("You failed")
elif y>=90:
    print("You got an A")
elif y<90 and y>=80:
    print("You got an B")
elif y<80 and y>=70:
    print("You got an C")
elif y<70 and y>=60:
    print("You got a D")