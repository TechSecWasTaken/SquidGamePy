import random
import time

print("literally just step on one of the panels\n")

alive = True
panels = random.randint(2,8)
panelsJumped = 0
print("There are " + str(panels) + " panels!")

def jump():
    global alive
    global panels
    global panelsJumped

    panelChoice = ["left", "right"]

    LRChoice = random.choice(panelChoice)

    if panelsJumped >= panels:
        print("You win!")
        time.sleep(3)
        exit()

    print("THE INPUT IS CASE SENSITIVE! MAKE SURE YOU TYPE left OR right AND NOT: Left OR Right!\n")
    LR = input("left or right? ")

    if LR == "left" or LR == "right":
        if LR == LRChoice:
            print("You jumped onto the correct panel!\n")
            panelsJumped = panelsJumped + 1
        else:
            print("You died.")
            alive = False

while True:
    if alive == False:
        time.sleep(3)
        exit()
    jump()
    