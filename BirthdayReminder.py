"""
Text-based version of the program.

Done:
sort with the closest to current date the the top of array

Still need to:
add to the file
edit a certain item in the file
sort the file by date when a new birthday is added, editted or removed
"""

import datetime  
# https://www.journaldev.com/23270/python-current-date-time
# https://kite.com/python/examples/5639/datetime-get-the-year,-month,-and-day-of-a-%60datetime%60


print("Welcome to Birthday Reminder")


date = datetime.datetime.today()
MONTH_ARRAY = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec" ]
current_month_num = date.month
current_month = MONTH_ARRAY[date.month-1]
current_day = date.day
print (current_month, current_day)

birthday_arr = []

def setup(arr):
    # https://stackoverflow.com/questions/6213063/python-read-next
    """
    Returns an updated list with all of the saved birthdays from the text file.
    """
    arr=[]
    file = open('birthdays.txt', 'r')
    lines = file.readlines()
    i=0
    while i < len(lines):
        num = i # saved as an integer (instead of a string)
        name = lines[i].replace("\n","")
        month = lines[i+1].replace("\n","")
        day = lines[i+2].replace("\n","")
        relation = lines[i+3].replace("\n","")
        arr.append([num, name, month, day, relation])
        i+=5
    file.close()    
    return arr

def display_person(num, item:list):
    """
    Turns the data from the list into a more readable output.
    """
    item[0] = num # reassigns number in array
    name = item[1]
    month = MONTH_ARRAY[ int(item[2]) ]
    day = item[3]
    relation = item[4]
    print (num, "Name:",name,", Birthday", month, day, ", Relation:",relation)
    

def view(arr):
    """
    Prints out each birthday from the list.
    """
    start = 0 # currently the first item in the list
    x=0
    while x< len(arr):
        month = int(arr[x][2])
        day = int(arr[x][3])
        if month<current_month_num: # if the month of this birthday is before the current month
            start+=1
        elif month==current_month_num and day<current_day:
            start+=1
        x+=1
    count = 1
    x=0
    while x < (len(arr)-start): #prints birthdays after after current month and day
        display_person(count, arr[x+start])
        x+=1
        count+=1
    x=0
    while x < (start): #prints birthdays after after current month and day
        display_person(count, arr[x])
        x+=1
        count+=1
    

while True:
    birthday_arr = setup(birthday_arr)
    print("Do you want to: add a birthday (A), view birthdays (V), edit a birthday (E), or quit (Q)")
    choice = input()
    if choice == "A":
        print ("Add")
    elif choice == "V":
        print ("View")
        view(birthday_arr)
    elif choice == "E":
        print ("Edit")
    elif choice == "Q":
        print ("Quit")   
        break
    else:
        print ("invalid input")

print ("thanks")