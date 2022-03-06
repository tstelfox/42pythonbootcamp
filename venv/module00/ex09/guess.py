import random

if __name__ == "__main__":
    answer = random.randint(1, 99)
    # answer = 42
    i = 0
    print("Guessin game.\nType exit to quit")
    while True:
        attempt = input("What's your guess between 1 and 99?\n>> ")
        if attempt == 'exit':
            print("Bye bitch")
            exit()
        i += 1
        try:
            num = int(attempt)
        except ValueError:
            print("That's not a number.")
            continue
        if int(attempt) < answer:
            print("Too low!")
        elif int(attempt) > answer:
            print("Too high!")
        else:
            if answer == 42:
                print("Stupid book reference")
            if i == 1:
                print("Got it on the first go!")
            elif i > 1:
                print("Congratulations, you've got it!\nYou won in", i, "attempts")
            exit()


