
import random
user_wins=0
computer_wins=0
while True:
    user_input= input("Type Roclk/Paper/Scissors or Q to Quit").lower()
    if user_input=="q":
        quit()
        
        #creating list where we have rock ,paper and scissor
    if user_input in ["rock","paper","scissors"]: