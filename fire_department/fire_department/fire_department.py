from sys import exit
import math

"""
The idea behind the fire_department function is to answer the following:
If a town wishes to place a fire department so that the time for the
firetrucks to get to any location in the town is minimized, where should
they put the fire station? I wish to add to this problem that unoccupied
lots may be added as potential locations but will not be considered as a
place that the fire truck needs to be able to get to.
I also will give the option to only place the fire
department somewhere that is currently unoccupied.
The input will be a cost matrix and an integer that tells me how many of the
locations given are vacant and an integer that tells me if we are restricted
to vacant lots (0 for restricted to vacant lots).  The cost matrix will be set up
so that the first k rows are vacant lots with the remaining rows being occupied
spaces.  This function is to be called by interactive programs one of which
asks the user for to input the cost matrix as a list, the other of which will
take the cost matrix as a file as input in the command line.
"""

def convert_integer(s):
  try:
      return int(s)
  except ValueError:
      return None

def fire_department(matrix, number, vacant):
    rows = matrix[0].__len__()
    #this variable will tell us which locations we need to consider for the fire
    #department.  We start by assuming we must consider all locations
    last_row = rows
    if vacant == 1:
        #we only consider vacant locations
        last_row = number
    else:
        pass
    #now we will find the distance from the first possible location to
    #the furthest non-empty property
    largest_distance = matrix[0][number] #initialize as the distance to the first-nonempty property
    answer = 0 #we start with the first lot as our answer.  it may change.
    for j in range(number+1,rows):
        if(matrix[0][j] > largest_distance):
            largest_distance = matrix[0][j]
    for i in range(1,last_row):
        temp = matrix[i][number] #a variable that keeps track of row i's largest_distance
        for k in range(number, rows): #going through the matrix one row at a time
            if(matrix[i][k] > temp):
                temp = matrix[i][k]
        if(temp < largest_distance):
            largest_distance = temp
            answer = i
    print(f"The fire department should be placed in lot {answer}.")
    print(f"This location is no further than {largest_distance} from any occupied lot.")
    exit(0)

def split_input(sequence):
    #this code will turn the line into a row of the matrix
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

    return words
