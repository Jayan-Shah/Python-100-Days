import random
from draw_art import logo3,logo2,stages
import os

#Print Hangman Logo
print(logo3,"\n\n\n")
length_of_stage = len(stages) 

# Random Word Choice
word_list = ["baboon", "ardvark", "camel", "horse", "lifespan"]
random_word_choice = random.choice(word_list)

# Creating blanks of same length

list_of_blanks = []
length_of_word = len(random_word_choice)

def display():
    for i in range (len(random_word_choice)):
        list_of_blanks.append('_')
        print(list_of_blanks[i],end=" ") 




display()
while (length_of_word !=0 and length_of_stage !=0 ):
    
    # Guessing a letter....
 
    user_guess = input("\n\nGuess a letter: ").lower()

    #Validating the Guess
    i=0
    flag=0
    for char in random_word_choice:
        if user_guess == char:
            list_of_blanks[i]=char
            length_of_word = length_of_word -1
            flag=1
        i+=1   
    
    if(flag==0):
        os.system('clear')
        print(stages[length_of_stage-1])
        length_of_stage =length_of_stage - 1
        display()

    else:
        os.system('clear')
        display()

if(length_of_word==0):
    os.system('clear')
    print(f"\nYou won!!!...\n{logo2}")

else:
    print("\nOopppssss.....You Lost!!\n")
 

        