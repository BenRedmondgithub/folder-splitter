letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
big_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?"]

print ("welcome to the password generator!")

# These prompts must receive numbers; typing text like "a" will make int() fail.
nr_letters = str(input("How many letters would you like in your password? "))
nr_symbols = str(input("How many symbols would you like? "))
nr_numbers = str(input("How many numbers would you like? "))
nr_big_letters = str(input("How many uppercase letters would you like in your password? "))

password_list = []

for char in range(1, int(nr_letters) + 1):
    password_list.append(letters[random.randint(0, 25)])

for char in range(1, int(nr_big_letters) + 1):
    password_list.append(big_letters[random.randint(0, 25)])

for char in range(1, int(nr_numbers) + 1):
    password_list.append(numbers[random.randint(0, 9)])

for char in range(1, int(nr_symbols) + 1):
    password_list.append(symbols[random.randint(0, 29)])

# Shuffle the collected characters, then join them into one password string.
random.shuffle(password_list)

password = "".join(password_list)

for char in password_list:
    password += char
    print("char: " + char)

pwd = "".join(password_list)

print("your password is: " + password)
clear = input("press enter to clear the password")