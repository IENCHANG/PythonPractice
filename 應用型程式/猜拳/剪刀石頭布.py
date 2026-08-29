import random
computer1 = None
computer2 = None
running = True
options = ("paper", "scissors", "stone")
while running:
    computer1 = random.choice(options)

    computer2 = random.choice(options)
    print(f"computer1:{computer1}，computer2:{computer2}")
    if computer1 == computer2:
        print("Equalize")
    elif computer1 == "scissors" and computer2 == "paper":
        print("The computer1 wins!!")
    elif computer1 == "stone" and computer2 == "scissors":
        print("The computer1 wins!!")
    elif computer1 == "paper" and computer2 == "stone":
        print("The computer1 wins!!")
    else:
        print("The computer2 wins")
    play_again = input("Play another round?")
    if not play_again == "y":
        running = False
print("Thank you for playing!!")