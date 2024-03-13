# coding: iso-8859-1 -*-
#-------------------------------------------------------------------DAY 1-------------------------------------------------------------------#  
'''
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("your band name could be...\n" + city + " " + pet)
#5. Make sure the input cursor shows on a new line:
'''
# Solution: https://replit.com/@appbrewery/band-name-generator-end

#-------------------------------------------------------------------DAY 2-------------------------------------------------------------------#
'''
#Data Types

#string

print("Hello"[4])

#integer

print(123 + 345)

123_456_789

#float

3.14159

#Boolean

True
False

num_char = len(input("What is your name?\n"))

new_num_char = str(num_char)  

print("your name has " + new_num_char + " characters.")


a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

#moje, sam wymyśliłem :D
two_digit_number = input()
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

3 + 5 #dodac
7 - 3 #odjac
3 * 2 #razy
6 / 3 #podzielic
2 ** 2 #do potęgi

#moje 
height = input()

weight = input()

h = float(height)
w = float(weight)
bmi = w/h**2
print(int(bmi)) #int ponieważ ma być zaokrąglone do liczby całkowitej 


score = 0
height = 1.8
isWinning = True
# litera f przed "" automatycznie zamienia na stringa każdą zmienną (zmienna musi być w nawiasach -> {})
print(f" your score is {score}, your height is {height} you are winning is {isWinning}")

print("type in your age\n")
age = input() #input jest zawsze stringiem, trzeba go zmienic -> "a = int(age)"
weeks = 4696
weeks_in_a_year = 52
a = int(age)
left = weeks - weeks_in_a_year * a 
print(f"your life expectancy is about {left} weeks")

    #projekt 2 kalkulator napiwku
print("Welcome to the tip calculator.")
bill = float(input("what was the total bill?"))
tip = int(input("what percentage tip do you want to give? 10, 12, or 15,"))
ppl = int(input("how many people to split the bill?"))
bill_and_tip = bill + (tip / 100) * bill
final = bill_and_tip / ppl
final2 = "{:.2f}".format(final)
print(f"each person should pay: {final2}$")
'''
#-------------------------------------------------------------------DAY 3-------------------------------------------------------------------#
'''
print("welcome to the rollercoaster")
height = int(input("what is your height in cm"))

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("what is your age?"))
    if   age < 12:
        bill = 5    
        print("please pay 5$")
    elif age <= 18:
        bill = 7    
        print("please pay 7$")
    elif age >= 45 and age <= 55:
        print("you go for free")
    else:
        bill = 12    
        print("please pay 12$")

    wants_photo = input("do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    
    print(f" your final bill is {bill}$")
else:
    print("you can not ride the rollercoaster")
'''

'''
number = int(input())
if number % 2 == 0: #jesli 120 to prawda jesli inne to fałsz (musi być == a nie =) # % to modulo - sprawdza reszte z dzielenia
  print("this is an even number.")
else:
  print("this is an odd number.")
'''

'''
height = float(input())
weight = int(input())
h = float(height)
w = float(weight)
bmi = w/h**2
print(int(bmi))
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
'''

'''
year = int(input())
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
     print("Leap year")
    else:
     print("Not leap year")
  else:  
     print("Leap year")
else:
  print("Not leap year")
'''

'''
print("Thank you for choosing Python Pizza Deliveries!")
size = input()
if size == "S":
    bill = 15  
    add_pepperoni = input() 
    if add_pepperoni == "Y":
        bill += 2   
if size == "M":
    bill = 20
    add_pepperoni = input() 
    if add_pepperoni == "Y":
        bill += 3   
if size == "L":
    bill = 25   
    add_pepperoni = input() 
    if add_pepperoni == "Y":
        bill += 3       
extra_cheese = input()
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
'''

'''
print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
'''

'''
print("Welcome to the treasure island. Your mission is to find the treasure.")
choice1 = input("go left or right?\n")
if choice1 == "left":
    print("you went left...")
    choice2 = input("you want to swim or wait?\n")
    if choice2 == "wait":
        print("you waited...")
        choice3 = input("You see three apear doors blue, red and yellow. Which door do you open?\n")   
        if choice3 == "yellow":
            print("you win!")
        else:
            print("game over")    
    else:
        print("game over")
else:
    print("game over")
'''

'''
import random

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")
'''
#-------------------------------------------------------------------DAY 4-------------------------------------------------------------------#

'''
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", 
"New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
"Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", 
"West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", 
"New Mexico", "Arizona", "Alaska", "Hawaii"]


#num_of_states = len(states_of_america)

#print(states_of_america[num_of_states -1])
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1]) #pierwszy nawias wybiera spośród list a drugi nawias wybiera konkretnie z listy
'''


'''
import random

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_name = random.randint(0, len(names - 1))
name = random_name
print(f"{name} is going to buy the meal today!")
'''
'''
# Tworzymy listę
lista = [1, 2, 3, 4, 5]

# Wyświetlamy listę
print("Lista przed zmianą:", lista)

# Prosimy użytkownika o podanie indeksu elementu do zmiany
indeks = int(input("Podaj indeks elementu do zmiany: "))

# Prosimy użytkownika o podanie nowej wartości
nowa_wartosc = int(input("Podaj nową wartość: "))

# Zamieniamy element w liście
if 0 <= indeks < len(lista):
    lista[indeks] = nowa_wartosc
    print("Lista po zmianie:", lista)
else:
    print("Podany indeks jest nieprawidłowy.")
'''

'''
import random
rock = '''
#    _______
#---'   ____)
#      (_____)
#      (_____)
#      (____)
#---.__(___)
'''

paper = '''
#    _______
#---'   ____)____
#          ______)
#          _______)
#         _______)
#---.__________)
'''

scissors = '''
#    _______
#---'   ____)____
#          ______)
#       __________)
#      (____)
#---.__(___)
'''
obrazki = [rock, paper, scissors]

gracz = int(input("rock - 0, paper - 1 or scissors - 2?\n"))
print(obrazki[gracz]) #pokazuje obrazki tu tego w jakis sposob

komp = random.randint(0, 2)
print(f"komputer wybral\n{komp}")
print(obrazki[komp])

if gracz >= 3 or gracz < 0:
    print("ERROR")
elif gracz == 0 and komp == 2:
    print("win")
elif komp == 0 and gracz == 2:
    print("lose")
elif komp > gracz:
    print("lose")
elif gracz > komp:
    print("win")
elif komp == gracz:
    print("draw")
else:
    print("ERROR")
'''

'''
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit + "pie")  
'''
# FIZZBUZZ
for n in range (1,101):
    if n % 3 == 0 and n % 5 ==0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)    
#
                
                
    