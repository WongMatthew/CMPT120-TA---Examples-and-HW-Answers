import random

yeses = ["yes", "y", "of course", "certainly yes", "sure"]
noses = ["no", "n", "no way", "of course not", "never"]
byes = ["Goodbye!", "See you!", "ciao", "Have a good day"]

while True:
    response = input("How can I assist you? ")
    response = response.lower()

    if response in yeses:
        print("Great! You can ask me 2 yes/no questions.")
        for i in range(2):
            answer = random.choice([True, False])
            if answer:
                print("Yes, definitely.")
            else:
                print("No, definitely not.")

    elif response in noses:
        print("Sorry to hear that. Maybe I can help you with something else.")

    else:
        print("I'm sorry, I didn't understand what you said.")

    bye = random.choice(byes)
    print(bye)

    if bye == "Goodbye!":
        break