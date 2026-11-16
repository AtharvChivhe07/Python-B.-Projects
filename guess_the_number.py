import random

print("Welcome to the Guess the number game !!")

number = random.randint(1,100)
count = 0

while True:
    guess = input("Guess a number between 1 to 100 (or type 'exit' to quit): ")

    #Exit condition..

    if guess.lower() == "exit":
        print("Thanks for playing ! Goodbye...") 
        break

    # Convert Input into int

    if not guess.isdigit():
        continue

    guess = int(guess)
    count +=1


    if number > guess:
        print("Grater value please !!")

    elif number < guess:
        print("Lower value please !!")

    else :
        print(f"Congratulations you won !! You guessed the number in {count} guesses.")

        #generate new number automatically 

        number = random.randint(1,100)
        count = 0

        print("\n New number generated let's play again...!!")