#Program to check positive integer is a power of four
def power4(num):
    x = abs(num)
    if (x == 0):
        return False
    while (x != 1):
            if (x % 4 != 0):
                return False
            x = x // 4

    return True

print(power4(60))

#Program to find perfect root
import math

def perfect_root(num):
    number = int(num)
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False

print(perfect_root(16))

#Program to guess a random number
import random

def random_game():
  x = random.randint(1, 10)
  num = None
  while x != num:
     num = input ("Enter a number between 1 and 10 ")
     if num == x:
       print("Congratulations")
       break
     else:
        print("Try again")

random_game()

#Program to return web page text, content and api
import requests

url = None

def getwebpage ():
   url = input("Enter website name: ")
   #Response text
   print(requests.get(f'https://{url}.com').text)
   #Content
   print(requests.get(f'\nhttps://{url}.com').content)
   #Raw data of API
   print(requests.get(f'\nhttps://api.{url}.com/events', stream = True).raw)
   print(requests.get(f'\nhttps://api.{url}.com/events', stream = True).raw.read(15))

getwebpage()

