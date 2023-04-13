from random import randint

if __name__ == "__main__":
    secret = randint(1, 99)
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!\n")
    count = 0
    while 42:
        try:
            r = input("What's your guess between 1 and 99?\n>> ")
            count += 1
        except EOFError:
            print("\nGoodbye!")
            break
        try:
            r = int(r)
        except:
            if r == "exit":
                print("Goodbye!")
                break
            print("That's not a number.")
        else:
            if r == secret:
                if secret == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                if count != 1:
                    print("Congratulations, you've got it!")
                    print("You won in %i attempts!"%count)
                else:
                    print("Congratulations! You got it on your first try!")
                break
            elif r < secret:
                print("Too low!")
            elif r > secret:
                print("Too high!")
