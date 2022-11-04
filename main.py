#random number gessing user 
import random

def guess_numb():
  num = (random.randint(0,10))
  guess = int(input("enter number between 0 and 10 "))
  while num != guess:
    if(guess < num):
      print("guess too low")
      guess = int(input("enter number between 0 and 10 "))
    elif(guess>num):
      print("guess to high")
      guess = int(input("enter number between 0 and 10 "))
    else:
      print("guess correct")
      
    
guess_numb()
