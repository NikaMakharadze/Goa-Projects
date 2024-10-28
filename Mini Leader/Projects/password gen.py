import random  # import the random module

# Define character sets for different difficulty levels
dif_easy = 'abcdefghijklmnopqrstuvwxyz!@#$%'
dif_normal = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
dif_hard = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:",.<>?/'

# the number of symbols in the password
symbol = int(input("Enter symbols num: "))
print("Options: \nEasy, Normal, Hard")  # Display the difficulty options
difficulty = input("Enter Password's difficulty: ").lower()  # Get the user's choice and convert to lowercase

# Check the chosen difficulty and generate the password accordingly
if difficulty == "easy":
    res_dif_easy = ""

    # Generate a random password of the specified length
    for _ in range(symbol):
        res_dif_easy += random.choice(dif_easy)  # Append a random character from the easy set

    print(res_dif_easy)

elif difficulty == "normal":
    res_dif_normal = ""

    # Generate a random password of the specified length
    for _ in range(symbol):
        res_dif_normal += random.choice(dif_normal)  # Append a random character from the normal set

    print(res_dif_normal)

elif difficulty == "hard":
    res_dif_hard = ""

    # Generate a random password of the specified length
    for _ in range(symbol):
        res_dif_hard += random.choice(dif_hard)  # Append a random character from the hard set

    print(res_dif_hard)

else:
    print("You chose an invalid option")  # Inform the user of an invalid difficulty choice
