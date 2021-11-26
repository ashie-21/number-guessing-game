import random
number = random.randint(1, 9)
print ("Number Guessing Game")
guess = input("Guess a no. (between 1 and 9):")
# Compare the user entered number with the number to be guessed
if guess == number:
    # if number entered by user is same as the generated
    # number by randint function then break from loop using loop
    # control statement "break"
    print ("Congratulation YOU WON!!!")
    break
# Check whether the user guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)
# While loop to count the number of chances
while chances < 5: