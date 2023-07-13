import random
computer_score=0
user_score=0
for i in range(1,10,1):
    user_input=int(input("Enter your guess number"))
    print("Your input is",user_input)
    computer_input=random.randint(0,9)
    print("Computer input is",computer_input)
    if user_input>computer_input:
        user_score+=10
        print("You win and your score is",computer_score)
    elif computer_input>user_input:
        computer_score+=10
        print("Computer wins and computer score is",computer_score)
    else:
        print("Invalid input try again!")
