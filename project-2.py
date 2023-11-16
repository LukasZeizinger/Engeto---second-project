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
x = 0
y = 0
Dict = {"1": 0,"2": 0,"3": 0,"4": 0}

# Create a random number btw 1000 to 9999
ran_num = str(random.randrange(1000,9999))
print(ran_num)
# Input from user to software


numberx = str(input(f'Enter munber: '))
print(f">>> ",numberx)

for numberx in ran_num:
    list_num.append(numberx)
    
    print(x)
    x +=1
    print("K", x)

print(list_num)

#TODO rozřezat random number do dist a přiřadit klíč k hodnotě
#TODO def zadat input a iterovat inputem přes hodnoty a zaroveň mít počítadlo a kontrolovat počítadlo a key v dictu
#TODO Pak až rozhodování 

#TODO porovnání bulls - jestli nějaké existuje udělej

#TODO porovnání cows - Jestliže číslo není bulls pak zjisti jestli není cows

#TODO jestliže je bulls = 4, tak vše ukonči

#TODO počítej čas od prvního zadání hodnoty

#TODO počítej kolikrát hráč hádal
