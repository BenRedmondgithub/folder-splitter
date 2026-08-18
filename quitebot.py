import random

myQuote = ["Fuck me dude", "Thanks to God, Jesus, and the bear conductor.", "dickballs", "Fuck yeah dude", "CLUNKLES, USE YOUR FISTS.", "Am I fucking over", "what a mark", "This shit pulls no punches at all.", "This has one job and it is to ruin my day"]

while True:

    user_input = input("Type !quote to get a random quote: ")
    if user_input == "!quote":
        randomQuote = random.choice(myQuote)
        print(randomQuote)
    else:
        print("try again!")