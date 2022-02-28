import random

if __name__ == "__main__":
    answer = random.randint(1, 99)
    i = 0
    while True:
        attempt = input("What's your guess between 1 and 99?\n>> ")
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
            print("Congratulations, you've got it!\nYou won in", i, "attempts")
            exit()


