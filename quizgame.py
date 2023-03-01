

print("Welcome to my computer Quiz")

playing = input("Do you want to play? ")
if playing != "Yes":
    quit()
print("Okay ! Let's play:) ")
score = 0

answer = input("What does CPU stand for? ")
if answer == "Central processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect !")
answer = input("What does GPU stand for? ")
if answer == "Graphic processing unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect !")

answer = input("What does Ram stand for? ")
if answer == "Random access memory":
    print("Correct! ")
    score += 1
else:
    print("Incorrect !")

answer = input("What does PSU stand for? ")
if answer == "Power Supply  unit":
    print("Correct! ")
    score += 1
else:
    print("Incorrect !")

print("you got " + str(score) + " questions Correct")
print("you got " + str((score / 4) * 100) + " %")


