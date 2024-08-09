# PROJECT 1: Rock, Paper,  Scissors
'''
Rock  =     1
Paper =     0
Scissors = -1
'''

#Giving instructions

import random
print('''
Welcome to the Rock-Paper-Scissors game!\n
Please follow these instructions:\n
    1) Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors.\n
    2) The computer will make a selection.\n
    3) The winner will be determined based on the following rules: 
        Rock defeats Scissors, Scissors defeat Paper, and Paper defeats Rock.\n
    Best of luck, and enjoy the game! ''')


#Taking input
computer = random.choice([1,0,-1])
you_in = input("Enter your choice: ")
YourDict={'r':1,'p':0,'s':-1}
you=YourDict[you_in.lower()]
revdict={1:'Rock',0:'Paper',-1:'Scissors'}

#Now we have 2 values
print(f'You Chose {revdict[you]}\nComputer Chose {revdict[computer]}')

'''
if(computer==you):
    print("It is a Draw!")
else:
    if(computer==1 and you==-1): #(computer-you)=2
        print("You Lose!")
    elif(computer==-1 and you==1): #(computer-you)=-2
        print("You Win!")
    elif(computer==0 and you==1): #(computer-you)=-1
        print("You Lose!")
    elif(computer==1 and you==0): #(computer-you)=1
        print("You win!")
    elif(computer==-1 and you==0): #(computer-you)=-1
        print("You Lose!")
    elif(computer==0 and you==-1): #(computer-you)=1
        print("You Win!")
    else:
        print("Something Went wrong!")
'''
if(computer==you):
    print("It is a Draw!")
else:
    if(computer-you==-1 or computer-you==2):
        print("You Lose!")
    else:
        print("You Win!")



