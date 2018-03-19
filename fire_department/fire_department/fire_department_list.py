from fire_department import fire_department, convert_integer

#This code interacts with the user to gather all needed information
print("How many rows will represent vacant locations.")
user_input = input("> ")
number = convert_integer(user_input)
if(number == None):
    print("Please give an integer.")
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

print("Please enter the entries of your cost matrix in the following format:")
print("E00, E01,...,E0n,E10,E11,E12,...,E1n,...Enn")
sequence = input("> ")

#this code will turn the input list into a matrix
words = sequence.split(',')

#a variable that indicates the splitting by commas failed.  We will use this
#to see if splitting by spaces also fails at which point we give up
strike = 0

#checks if splitting by spaces worked if not we assign a strike
for word in words:
    if(convert_integer(word) == None):
        strike = 1

if strike == 1:
    words = sequence.split()

    #checks if splitting by commas works.  Either will do but we demand consistency
    for word in words:
        if(convert_integer(word) == None):
            print("Your input is improperly formatted.")
            exit(0)

#now we check to make sure we can make a square matrix
length = words.__len__()
matrix_size = convert_integer(math.sqrt(length))
if convert_integer(length) % matrix_size != 0:
    print("You need to give a perfect square number of integers for it to be a cost matrix.")
    exit(0)
elif number > matrix_size:
    print("You have more vacant locations than total locations.")
elif number == matrix_size:
    print("You don't need a fire station!  You're whole town is vacant lots!")
#right now I do not check that the numbers make a reasonable cost matrix
#finally we make that matrix
else:
    matrix = [[convert_integer(words[y*matrix_size+x]) for x in range(matrix_size)] for y in range(matrix_size)]
    print(matrix)
#now we call fire_department
fire_department(matrix, number, vacant_lot_toggle)
