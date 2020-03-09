"""
Text-based version of the program.

Done:
sort with the closest to current date the the top of array
overwrite the text file
sort the array
add to the file

Still need to:
edit a certain item in the file

Additional Goals:
implement GUI
have reminders x days in advance
"""

import datetime  
# https://www.journaldev.com/23270/python-current-date-time
# https://kite.com/python/examples/5639/datetime-get-the-year,-month,-and-day-of-a-%60datetime%60


date = datetime.datetime.today()
MONTH_ARRAY = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec" ]
DAY_ARRAY = [31,29,31,30,31,30,31,31,30,31,30,31]
current_month_num = date.month
current_month = MONTH_ARRAY[date.month-1]
current_day = date.day

TEXT_NAME = "birthdays.txt"
birthday_arr = []

print("Welcome to Birthday Reminder")
print (current_month, current_day)


def setup_array(arr:list)->list:
    # https://stackoverflow.com/questions/6213063/python-read-next
    """
    Returns an array with all of the saved birthdays from the text file.
    """
    arr=[]
    file = open(TEXT_NAME, 'r')
    lines = file.readlines()
    i=0
    count = 1
    while i < len(lines):
        num = i # saved as an integer (instead of a string)
        name = lines[i].replace("\n","")
        month = lines[i+1].replace("\n","")
        day = lines[i+2].replace("\n","")
        relation = lines[i+3].replace("\n","")
        # next is a blank line for readablilty in the file
        arr.append([count, name, month, day, relation])
        i+=5
        count+=1
    file.close()    
    return arr

def update_file(arr:list)->None:
    """
    Overwrites the old file with the updated information.
    """
    file = open(TEXT_NAME, 'w') 
    i=0
    while i< len(arr): # only saves first line?
        file.write(arr[i][1]+"\n")
        file.write(arr[i][2]+"\n")
        file.write(arr[i][3]+"\n")
        file.write(arr[i][4]+"\n")
        file.write("\n")
        i+=1
    file.close() 

def display_person(num:int, item:list):
    """
    Turns the data from the list into a more readable output.
    """
    item[0] = num # reassigns number in array
    name = item[1]
    month = MONTH_ARRAY[ int(item[2])-1 ]
    day = item[3]
    relation = item[4]
    print (num, "Name:",name,", Birthday:", month, day, ", Relation:",relation)
  
def add_item(arr:list)->list:
    """
    Asks the user for the new birthday and returns the updated array including the new input.
    """
    name = input("Enter the name:")
    while True:
        month = input("Enter the month as a integer (Ex, Jan = 1, Feb=2, Dec=12): ")
        try: 
            month = int(month)  
            if not(1<=month<=12):
                print("Month must be between 1 and 12")
            else:
                break
        except ValueError: # https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
            print("Error, not integer input.")
    while True:
        day = input("Enter the day: ")
        try:
            day = int(day)
            if not(1<=day<=DAY_ARRAY[month-1]):
                print("Day must be between 1 and",DAY_ARRAY[month-1],"for the month of", MONTH_ARRAY[month-1])
            else:
                break
        except ValueError:
            print("Error, not integer input.")      
    month = str(month) # both month and day will be saved in the file and array as strings
    day = str(day)
    relation = input("Enter the relation:")
    num=len(arr)
    arr.append([num, name, month, day, relation])
    
    return arr

def sort_array(arr:list)->list: # bubble sort is used, which is very slow
    """
    Returns an array sorted in order of date.
    """
    unsorted = True
    while unsorted: # sorts by month
        count = 0 # resets to zero at the begining of each run
        for i in range(len(arr)-1): # len - 1 since we do i+1
            if (int(arr[i][2]) > int(arr[i+1][2])): # ex. June is before Feb
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
                arr[i][0] , arr[i+1][0] = arr[i+1][0] , arr[i][0] # switches back the number
            elif (int(arr[i][2]) == int(arr[i+1][2])) and (int(arr[i][3]) > int(arr[i+1][3])): # ex. Mar 27 is before Mar 3
                arr[i] , arr[i+1] = arr[i+1] , arr[i]
                arr[i][0] , arr[i+1][0] = arr[i+1][0] , arr[i][0] # switches back the number
            else:
                count +=1
        if count == (len(arr)-1): # fully sorted when each item in the array is in the right spot for the whole for loop
            unsorted = False # or just break
    return arr

def view(arr:list)->None:
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
        else: # birthday already passed
            break
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
    
# will update and sort the birthday array and text file at the begining of the program
birthday_arr = setup_array(birthday_arr)
birthday_arr = sort_array(birthday_arr)
update_file(birthday_arr)


while True:
    print("Do you want to: add a birthday (A), view birthdays (V), edit a birthday (E), or quit (Q)? ")
    choice = input()
    if choice == "A":
        print ("Add")
        birthday_arr = add_item(birthday_arr)
        birthday_arr = sort_array(birthday_arr)
        update_file(birthday_arr)
        # overwrite the file with the sorted array
    elif choice == "V":
        view(birthday_arr)
    elif choice == "E":
        print ("Edit")
        
    elif choice == "Q":
        break
    else:
        print ("Invalid Input")

print ("Goodbye")
