setup = ["Hey man, you're a real... ", "get out of here, you... ", "You're such an... ", "What the hell were you thinking, you... "]

curse = ["fuck ", "shit ", "bitch ", "asshole ", "dick ", "pussy ", "cunt ", "ass "]

curseafter = ["weasel ", "bastard ", "cock ", "twat ", "prick ", "goblin ", "merchant ", "waffle ", "Frog ", "motherfucker ", "sniffer"]

import random

randomSetup = random.choice(setup)
randomCurse = random.choice(curse)
randomCurseAfter = random.choice(curseafter)

print(randomSetup + randomCurse + " " + randomCurseAfter)   