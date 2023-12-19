"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""



import random  
import time



def _inputnumber():
    """Input integer and must be in range 1000-9999.
    If input is not decimal number; try new input.
    If input is out of range; try new one"""

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
 

def generate_secret_number():
    """Generate number in correct form. It generate a random 4 digit unique number."""
    while True:

        secret_random_number = str(random.randrange(1000,9999))
#        print(ran_num)
        library = []
        
        for x in secret_random_number:
            if x in library:
                library.append(False)
            else:
                library.append(True)
            library.append(x)
#        print(library)
        
        if False in library:
            continue
        else:
            return secret_random_number
        
def separator_number(four_digit_unique_number):
    """ Separate number 4 digit by number and creating a list from random number. 
    Then create dictionary for unique position and value"""  

    for num in four_digit_unique_number:
        list_num.append(int(num))
    

    return ()


def _checkuniquenumber():
    """Generate number in correct form. It generate a random 4 digit unique number."""
    while True:

        numberx = str(_inputnumber())
        library = []
        
        for x in numberx:
            if x in library:
                library.append(False)
            else:
                library.append(True)
            library.append(x)
#        print(library)
        
        if False in library:
            continue
        else:
            return numberx


def _bull_and_cow(mnozina):
    """Check for bull - if the input number is same value and position
    Check for cow - if the input number is containt in secret number"""
    
    bull = 0
    cow = 0
    
    for k in keys:
        input_num[k] = mnozina[k]

        if str(input_num[k]) == str(separated_num_non_edit[k]):
            sep_num[k] = True
            bull += 1
            
    # Check for cow        
        elif str(input_num[k]) in separated_num_non_edit.values():
            c = str(input_num[k])
            sep_num[list(separated_num_non_edit.values()).index(c)] = False
            cow += 1
        else:
            pass

    return (bull, cow)   

     
def word_s(word):
    """Mechanism for choosing singular or plural form word"""
    if word > 1:
        sz = "s"
        
    else:
        sz = ""
    return sz



list_num = []
list_input_num = []
numberx = 0
hit_count = 0
sep_num = {}
input_num = {}
separated_num_non_edit = {}
keys = range(4)



# Intro to program
print(f"Hi there!\n","-"*48)
print(f"I've generated a random 4 digit number for you.\n","Let's play a bulls and cows game.\n","-"*48)

# Create a random number btw 1000 to 9999
ran_num = generate_secret_number()
# Show the random number - for inspection
#print(ran_num)

# Fill sep_num by random number  
separator_number(ran_num)

# Get the start time
st = time.time()

# Input from user to software

while True:
    try:
        numberx = _checkuniquenumber()
        
    except ValueError:
        print("Please enter a new number without duplicit symbol")
        continue

# Separate 4 digit number to four 1 digit numbers
    for n in numberx:
        list_input_num.append((n))
    
    for i in keys:
        sep_num[i] = str(list_num[i])
        separated_num_non_edit[i] = str(list_num[i])

    cislo = _bull_and_cow(list_input_num)
    hit_count +=1
    print(f"Num of shots", hit_count)

# Check if is comleted - 4 bulls
    if cislo ==(4,0):
        break

    else:
        sep_num.clear()
        list_input_num.clear()
# Print option for bull/s and cow/s 
        print(f"", cislo[0],"bull" + word_s(cislo[0]), " ,", cislo[1], "cow" + word_s(cislo[1]))
        print(f"-"*48)

# get the end time
et = time.time()

# get the execution time
elapsed_time = float(et - st)
# Print option for shot/s
print(f"Execution time:", round(elapsed_time, 2), 'second'+ word_s(elapsed_time)," and ", hit_count, "shot" + word_s(hit_count))
