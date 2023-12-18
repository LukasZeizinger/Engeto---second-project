"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""

import random  
import time

# Intro to program
def _inputnumber():
    """Input integer and must be in range 1000-9999.
    If input is not decimal number, try new input.
    If input is out of range, try new one"""
    while True:
        try:
            numberx = int(input("Enter number: "))
        except ValueError:
            print("Please enter a number btw. 1000-9999. Try again ...")
            continue
        if numberx >= 1000 and numberx <= 9999:
            break
        else:
            print('The integer must be in the range 1000-9999')
            continue
    return numberx        
      
def word_s(slovo):
    """Mechanism for choosing if word has singular or plural"""
    if slovo > 1:
        sz = "s"
        
    else:
        sz = ""
    return sz

def generovani_cisla():
    """Generate number in correct form. It generate a random 4 digit unique number."""
    while True:

        ran_num = str(random.randrange(1000,9999))
#        print(ran_num)
        library = []
        
        for x in ran_num:
            if x in library:
                library.append(False)
            else:
                library.append(True)
            library.append(x)
#        print(library)
        
        if False in library:
            continue
        else:
            return ran_num
        
def separator_number(four_digit_unique_number):
    """ Separate number 4 digit by number and creating a list from random number. 
    Then create dictionary for unique position and value"""  

    for num in four_digit_unique_number:
        list_num.append(int(num))
    
    for i in keys:
        sep_num[i] = str(list_num[i])
        sep_num_edit[i] = str(list_num[i])
    return ()

def _bull_and_cow(mnozina):
    """Input integer and must be in range 1000-9999.
    If input is not decimal number, try new input.
    If input is out of range, try new one"""
    # Check for bull
    bull = 0
    cow = 0
    sep_num_edit = sep_num
    for k in keys:
        input_num[k] = mnozina[k]

        if str(input_num[k]) == str(sep_num[k]):
            sep_num_edit[k] = True
            bull += 1
            
    # Check for cow        
        elif str(input_num[k]) in sep_num_edit.values():
            c = str(input_num[k])
            sep_num_edit[list(sep_num_edit.values()).index(c)] = False
            cow += 1
        else:
            pass

    return (bull, cow)   

print(f"Hi there!\n","-"*48)
print(f"I've generated a random 4 digit number for you.\n","Let's play a bulls and cows game.\n","-"*48)

list_num = []
list_input_num = []
numberx = 0
hit_count = 0
sep_num = {}
input_num = {}
sep_num_edit = {}
keys = range(4)

# Create a random number btw 1000 to 9999
ran_num = generovani_cisla()
# Show the random number
print(ran_num)

# Fill sep_num by random number  
separator_number(ran_num)

# get the start time
st = time.time()

# Input from user to software

while True:
    try:
        numberx = str(_inputnumber())
        print(numberx)
    except ValueError:
        print("Please enter a number btw. 1000-9999")
        continue
# Check for correct number as input
    if int(numberx) >= 1000 and int(numberx) <= 9999:
        sep_num_edit.clear()
        sep_num_edit = sep_num.copy()
        hit_count +=1
        list_input_num.clear()
        bull = 0
        cow = 0
        cow_key = ()
        print(f">>>  {numberx}")
        print(f"Num of shots", hit_count)
# Separate 4 digit number to four 1 digit numbers
        for n in numberx:
            list_input_num.append((n))

        cislo = _bull_and_cow(list_input_num)
# Check if is comleted
        if sep_num == {0: True, 1: True, 2: True, 3: True}:
            break

        else:
            pass
# Print option for bull/s and cow/s 
        print( cislo[0],"bull" + word_s(cislo[0]), " ,", cislo[1], "cow" + word_s(cislo[1]))
        print(f"-"*48)

# Condition for break if number is in noncorrect format
    else:
        print('The integer must be in the range 1000-9999')
        continue

# get the end time
et = time.time()

# get the execution time
elapsed_time = float(et - st)
# Print option for shot/s
print(f"Execution time:", round(elapsed_time, 2), 'second'+ word_s(elapsed_time)," and ", hit_count, "shot" + word_s(hit_count))
