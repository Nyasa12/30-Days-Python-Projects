import random

computer_choice = random.randint(1,100)
your_choice = int(input("Enter your guess: "))

while computer_choice != your_choice :

   if (computer_choice >= your_choice) :
     print("a little higher, Try Again")
   elif (computer_choice <= your_choice):
     print("a little lower, Try Again")
   else :
       print("Invalid, Try Again")
       
   your_choice = int(input("Enter your guess: "))

print("Congratulation! You Won")
