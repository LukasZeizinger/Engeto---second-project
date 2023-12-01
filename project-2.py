"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""

import random


# Intro to program

print(f"Hi there!")
print(f"-"*50)
print(f"I've generated a random 4 digit number for you.")
print(f"Let's play a bulls and cows game.")
print(f"-"*50)
print(f"-"*50)

list_num = []
numberx = 0
hit_count = 0
sep_num = {}
keys = range(4)

# Create a random number btw 1000 to 9999
ran_num = str(random.randrange(1000,9999))
print(ran_num)
# Fill sep_num by random number  

for num in ran_num:
    list_num.append(numberx)

for i in keys:
    sep_num[i] = list_num[i]
print(sep_num)


#TODO def zadat input a iterovat inputem přes hodnoty a zaroveň mít počítadlo a kontrolovat počítadlo a key v dictu


# Input from user to software

 
while True:
    try:
        numberx = int(input("Enter number: "))
    except ValueError:
        print("Please enter a number btw. 1000-9999")
        continue
    if numberx >= 1000 and numberx <= 9999:
        hit_count +=1
        print(f">>>  {numberx}")
        print(f"Num of shots", hit_count)
    else:
        print('The integer must be in the range 1000-9999')
        break


#TODO Rozhodovaní 

#TODO porovnání bulls - jestli nějaké existuje udělej

#TODO porovnání cows - Jestliže číslo není bulls pak zjisti jestli není cows

#TODO jestliže je bulls = 4, tak vše ukonči

#TODO počítej čas od prvního zadání hodnoty

#TODO počítej kolikrát hráč hádal

