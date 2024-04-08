import random

def AI():
    you = 0
    ai = 0
    option = ["ROCK", "PAPER", "SCISSORS"]
    while True:
        get = input("ROCK PAPER SCISSORS (Press 'Q' or 'q' to EXIT): ").upper()
        if get == 'Q':
            break
        
        print("Your choice: " + get)
        AI_choice = random.choice(option)
        print("AI's choice: " + AI_choice)

        if get == AI_choice:
            print("It's a DRAW!\n")
        elif (get == "ROCK" and AI_choice == "PAPER") or \
             (get == "PAPER" and AI_choice == "SCISSORS") or \
             (get == "SCISSORS" and AI_choice == "ROCK"):
            print("AI WON THIS ROUND!\n")
            ai += 1
        else:
            print("YOU WON THIS ROUND!\n")
            you += 1

    print("Your score:", you)
    print("AI's score:", ai)

    if you < ai:
        print("AI WINS THE GAME!")
    elif you > ai:
        print("YOU WIN THE GAME!")
    else:
        print("IT'S A DRAW!")

AI()
