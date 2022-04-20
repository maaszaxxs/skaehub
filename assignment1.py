#Leap Year Function
def leap_year(age):
    if age%4==0:
        if age%400==0:
            return True
        elif age%100==0:
            return False

print(leap_year(2300))

            
#Length Last Word Function
def last_word_length(word):
    word = word.split(" ")
    lastword = word[-1]
    return len(lastword)

print(last_word_length("Hi I am Carrol"))


#Password Generator Function
import random
import string

def PasswordGen():
    len = int(input('\nEnter the length of password: '))
    all = string.ascii_letters + string.digits + string.punctuation
    temp = random.sample(all,len)
    password = "".join(temp)
    print(password)

PasswordGen()

#Reading CSV File Function
import csv

def read_csv(fileName):
    try:
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except IOError:
        print("Could not read file")

read_csv('test.csv')

#Removing duplicates from list function
def remove_duplicates(list):
    newlist=[]
    for x in list:
        if x not in newlist:
            newlist.append(x)
    return newlist

print(remove_duplicates([1,2,2,3,4,4,5,6,6]))