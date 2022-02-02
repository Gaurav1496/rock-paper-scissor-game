# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:33:00 2022

@author: gpanc
"""
import random 
print("ROCK-PAPER-SCISSOR GAME")
print("""
      THIS GAME IS CREATED USING PYTHON
      RULES OF GAME ARE:
          1.SELECT ANY OPTION FROM ROCK,PAPER,SCISSORS
          2.ONCE SELECTED OPTION CANNOT BE CANCELLED
 WINNING RULES ARE AS FOLLOWS:
     ROCK VS PAPER -> PAPER WINS
     ROCK VS SCISSORS -> ROCK WINS
     PAPER VS SCISSORS -> SCISSOR WINS
        TO QUIT THE GAME PRESS CTRL + C
        HOPE YOU ENJOY THE GAME    """)
        
print("Options are as follows \n 1:Rock \n 2:Paper \n 3:Scissor")
User_choice = int(input("Enter your Choice : "))

if User_choice == 1 :
    User_choice = "Rock"
elif User_choice == 2 :
    User_choice = "Paper"
elif User_choice == 3 :
    User_choice = "Scissor"    
        
print("Option You choose is : ",User_choice)  
        
print("Now is Computer's turn......")

computer_choice = random.randint(1, 3) 
if computer_choice == 1 :
    computer_choice = "Rock"
elif computer_choice == 2 :
    computer_choice = "Paper"
elif computer_choice == 3 :
    computer_choice = "Scissor" 
print ("Computer choice is : ",computer_choice)

#condition for Result
if (User_choice == "Rock" and computer_choice == "Paper"): #paper
    print("Computer wins!")
elif (User_choice == "Paper" and computer_choice == "Rock"): #paper
    print("<<User Wins!!!>>")
elif (User_choice == "Paper" and computer_choice == "Scissor") : #scissor
    print("Computer Wins!!")
elif (User_choice == "Scissor" and computer_choice == "Paper") : #scissor
    print("<<User Wins!!>>") 
elif (User_choice == "Rock" and computer_choice == "Scissor") : #rock     
    print("<<User Wins!!>>")
elif (User_choice == "Scissor" and computer_choice == "Rock") : #rock
    print("Computer Wins!!")
else:
    print("GAME DRAWN")    

print("Thank You for Playing ")    
       
        
        
        
        
        