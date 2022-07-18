import random


def main():

    while True:
        random_number = random.randint(0, 9)
        user_number = int(input("Enter the number: "))

        if user_number == random_number:
            print("You win")
        else:
            print("You lose")

        answer = input("Play more? ").lower()

        if answer == 'yes':
            continue
        elif answer == 'no':
            break


if __name__ == "__main__":
    main()
