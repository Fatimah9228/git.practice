#random number gessing user 
import random
num = (random.randint(0,10))
guess = int(input("enter number between 0 and 10 "))
def guess_numb(guess,num):


    
  while num != guess:
    if(guess < num):
      print("guess too low")
      guess = int(input("enter number between 0 and 10 "))
    else:
      print("guess to high")
      guess = int(input("enter number between 0 and 10 "))

  if (guess == num):
    print("guess correct")    
      
    
guess_numb(guess,num)
