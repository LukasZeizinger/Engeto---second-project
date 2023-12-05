"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""

import random  
import time

# Intro to program

print(f"Hi there!")
print(f"-"*50)
print(f"I've generated a random 4 digit number for you.")
print(f"Let's play a bulls and cows game.")
print(f"-"*50)
print(f"-"*50)

list_num = []
list_input_num = []
numberx = 0
hit_count = 0
sep_num = {}
input_num = {}
sep_num_edit = {}
keys = range(4)




# Create a random number btw 1000 to 9999
ran_num = str(random.randrange(1000,9999))
print(ran_num)
# Fill sep_num by random number  

for num in ran_num:
    list_num.append(int(num))
    
for i in keys:
    sep_num[i] = str(list_num[i])
    sep_num_edit[i] = str(list_num[i])
print(sep_num)

# get the start time
st = time.time()

#TODO def zadat input a iterovat inputem přes hodnoty a zaroveň mít počítadlo a kontrolovat počítadlo a key v dictu


# Input from user to software

 
while True:
    try:
        numberx = str(input("Enter number: "))
    except ValueError:
        print("Please enter a number btw. 1000-9999")
        continue
    if int(numberx) >= 1000 and int(numberx) <= 9999:
        sep_num_edit.clear
        sep_num_edit = sep_num.copy()
        hit_count +=1
        list_input_num.clear()
        bull = 0
        print(f">>>  {numberx}")
        print(f"Num of shots", hit_count)
        for n in numberx:
            list_input_num.append((n))

        for k in keys:
            input_num[k] = list_input_num[k]

            if str(input_num[k]) == str(sep_num[k]):
                input_num[k] = True
                sep_num_edit[k] = False

                bull +=1
            else:
                pass

        if input_num == {0: True, 1: True, 2: True, 3: True}:
            break

        else:
            
            cow = 0
            for m in keys:
                if input_num[m] in sep_num_edit.values():

                    sep_num_edit[k] = False
                    cow +=1
                else:
                    pass

        if bull < 1 and cow < 1:
            print(bull," bull ",cow, "cow")
        elif bull < 1:
            print(bull," bull ",cow, "cows")
        else:
            print(bull," bulls ",cow, "cows") 
    else:
        print('The integer must be in the range 1000-9999')
        break

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st

if hit_count == int(1):
    print(f'Execution time:', round(elapsed_time, 2), 'seconds and ', hit_count, "shot")
else:
    print(f'Execution time:', round(elapsed_time, 2), 'seconds and ', hit_count, "shots")


#TODO Rozhodovaní 

#TODO porovnání bulls - jestli nějaké existuje udělej

#TODO porovnání cows - Jestliže číslo není bulls pak zjisti jestli není cows

#TODO jestliže je bulls = 4, tak vše ukonči

#TODO počítej čas od prvního zadání hodnoty

#TODO počítej kolikrát hráč hádal

