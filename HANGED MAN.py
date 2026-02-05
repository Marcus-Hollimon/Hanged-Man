import random
from pathlib import Path
File_Path=Path(r"C:\Users\junni\My Python Projects\words.txt")
Valid_Words=[]
Difficulty= int(input("How long do you want the word to be? "))
while Difficulty <1:
    Difficulty= int(input("Please choose a word length of at least 1. "))
with open (File_Path)as file:
    for line in file:
        word=line.strip()
        if len(word)==Difficulty:
            Valid_Words.append(word)
Random_Word=random.choice(Valid_Words)
Word_To_Be_Guessed_List=[]
for char in Random_Word:
    Word_To_Be_Guessed_List.append(char)
Progress_Tracker=[]
for x in range (len(Word_To_Be_Guessed_List)):
    Progress_Tracker.append("_")
Lives= int(input("How many lives do you want to have? "))
Letter_Guessed=""
while (Lives>0) & ("_" in Progress_Tracker):
     Letter_Guessed=input("Guess a letter.")
     Index_Count=0
     if Letter_Guessed in Word_To_Be_Guessed_List:
         for x in Word_To_Be_Guessed_List:
             if Letter_Guessed==x:
                 Progress_Tracker[Index_Count]=x
             Index_Count +=1
         print("Good job")
         print("Progress, so far:", end="")
         print(Progress_Tracker)
         print(f"Lives left: {Lives}")
     else: 
        Lives-=1
        print("Incorrect!")
        print("Progress, so far:", end="")
        print(Progress_Tracker)
        print(f"Lives left: {Lives}")
if "_" in Progress_Tracker:
    print("You lost!")
    print("You win!")
    print(f"Lives left: {Lives}")