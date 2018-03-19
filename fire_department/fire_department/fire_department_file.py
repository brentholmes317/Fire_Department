from sys import argv, exit
from fire_department import fire_department, convert_integer, split_input

"""
Takes a file and uses it to make the matrix for fire_department.  Asks the
user for the other information.
"""

script, filename = argv

txt = open(filename)

reading = 1 #keeps track of if the file has concluded
length = -1 #will change to the length of the first row.  If subsequent rows
            #have different lengths then we cannot make a matrix and we report
            #that back to the user
matrix = [] #this will be a list of lists as a square matrix
row_counter =0 #counts rows
while(reading == 1):
    sequence = txt.readline()
    if sequence == '':
        reading = 0
    else:
        row_counter = row_counter +1
        words = split_input(sequence)
        #checks to make sure the rows all have the same length
        if length == -1:
            length = length = words.__len__()
        elif length != words.__len__():
            print("Your rows are not the same length.")
            exit(0)
        else:
            pass
        #makes a row of the matrix
        matrix_temp = [convert_integer(words[x]) for x in range(length)]
        matrix.append(matrix_temp)

if row_counter != length:
    print("You do not have a square matrix in your text file.")
    exit(0)

#This code interacts with the user to gather all needed information
print("Please state how many rows will represent vacant locations.")
user_input = input("> ")
number = convert_integer(user_input)
if(number == None):
    print("Please give an integer.")
    exit(0)
elif number > matrix.__len__():
    print("You have more vacant lots then lots!")
    exit(0)
elif number == matrix.__len__():
    print("All your lots are vacant!")
    exit(0)

print("Do you want to ensure your fire station is at a currently vacant location? (Yes/No)")
user_input = input("> ")
vacant_lot_toggle = 0
if('YES' in user_input.upper()):
    vacant_lot_toggle = 1
elif('NO' in user_input.upper()):
    pass
else:
    print("Please give a yes or no answer.")
    exit(0)

#now we call fire_department
fire_department(matrix, number, vacant_lot_toggle)
