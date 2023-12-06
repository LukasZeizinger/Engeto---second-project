"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukas Zeizinger
email: zeizingerlukas@gmail.com
discord: Lukáš Zeizinger _nantuko
"""

import random  
import time

# Intro to program

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
ran_num = str(7349)
#(random.randrange(1000,9999))
# Show the random number
print(ran_num)

# Fill sep_num by random number  

for num in ran_num:
    list_num.append(int(num))
    
for i in keys:
    sep_num[i] = str(list_num[i])
    sep_num_edit[i] = str(list_num[i])


# get the start time
st = time.time()



# Input from user to software

 
while True:
    try:
        numberx = str(input("Enter number: "))
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
# Check for bull
        for k in keys:
            input_num[k] = list_input_num[k]

            if str(input_num[k]) == str(sep_num[k]):
                input_num[k] = True
                sep_num_edit[k] = False

                bull +=1
            
# Check for cow   / nefunguje zatím         
            elif str(input_num[k]) in sep_num_edit.values():
#                c = str(input_num[k])
#                co = list(sep_num_edit.keys())[int(c)]
                cow_key = sep_num_edit.get(c)
                sep_num_edit[cow_key] = False
                cow +=1
            else:
                    pass
# Check if is comleted
        if input_num == {0: True, 1: True, 2: True, 3: True}:
            break

        else:
            pass
# Print option for bull/s and cow/s 
        if bull < 2 and cow < 2:
            print(bull," bull ",cow, "cow")
        elif bull < 2 and cow >= 2:
            print(bull," bull ",cow, "cows")
        elif bull >= 2 and cow < 2:
            print(bull," bulls ",cow, "cow")
        else:
            print(bull," bulls ",cow, "cows") 
        print(f"-"*48)
# Condition for break if number is in noncorrect format
    else:
        print('The integer must be in the range 1000-9999')
        break

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
# Print option for shot/s
if hit_count == int(1):
    print(f'Execution time:', round(elapsed_time, 2), 'seconds and ', hit_count, "shot")
else:
    print(f'Execution time:', round(elapsed_time, 2), 'seconds and ', hit_count, "shots")
