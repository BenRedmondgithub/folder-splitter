user_input = input("Press Enter to continue...")
while True:
    if user_input == "!quote":
        print (randomQuote)
    else:
        print ("try again!")



        myQuote = ["Fuck me dude", "Thanks to God, Jesus, and the bear conductor.", "dickballs", "Fuck yeah dude", "CLUNKLES, USE YOUR FISTS.", "Am I fucking over", "what a mark", "This shit pulls no punches at all.", "This has one job and it is to ruin my day"]
        import random
        randomQuote = random.choice(myQuote)
        print (randomQuote)