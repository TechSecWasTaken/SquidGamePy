import random

even = [2,4,6]
odd = [1,3,5]
wagerChoice = [1,2,3,4,5,6]
marbles = 10
rounds = 0

print("You are playing a marble game.")
print("You have 10 marbles, we will offer a wager.")
print("You have to guess if the wager is even or odd.")
print("If the guess is correct, you get the wager amount.")
print("If you don't answer correctly, you lose the amount of marbles that was in the wager.")
print("Get 20 marbles to win!")
print("Ready? Begin!\n")

def marbleChoice():
    global wagerChoice
    global even
    global odd
    global rounds
    global marbles

    rounds = rounds + 1
    wager = random.choice(wagerChoice)
    if rounds >= 1:
        oddOrEven = input("even or odd? (case sensitive!)")
    else: 
        oddOrEven = input("even or odd?")
    
    if oddOrEven == str("odd") or oddOrEven == str("even"):
        if wager in even:
            print("The wager was " + str(wager))
            if oddOrEven == str("even"):
                print("You won " + str(wager) + " marbles!")
                marbles = marbles + wager
            if oddOrEven == str("odd"):
                print("You lose " + str(wager) + " marbles!")
                marbles = marbles - wager
        if wager in odd:
            print("The wager was " + str(wager))
            if oddOrEven == str("odd"):
                print("You won " + str(wager) + " marbles!")
                marbles = marbles + wager
            if oddOrEven == str("even"):
                print("You lose " + str(wager) + " marbles!")
                marbles = marbles - wager
    else:
        print("That's an invalid input.")


while True:
    print("You have " + str(marbles) + " marbles!\n")
    marbleChoice()
    if marbles >= 20:
        print("You win!")
        break
    if marbles <= 0:
        print("You lose!")
        print("Time to die! :)")
        break