"""

Advent of Code, Day 3

"""
import sys
import math

##Part 1

#3 right 1 down
# load data
def input_to_list(inputtxt):
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    #input has one string per line with /n in the end
    print(input)
    input_wo_newline = [line.strip() for line in input] 
    # one string per row
    print(input_wo_newline)
    return input_wo_newline

def move_to_next(position, map, to_right, down):
    #map is list of strings, each string is one row, each char is column
    # 3 to right
    position = (position[0],position[1] + to_right)
    position = (position[0] + down, position[1])
    return position


def count_trees(map):
    position = (0,0)
    treecount = 0

    #as long as there is rows in the map..
    for line in range(0,len(map)):
        
        #update position
        position = move_to_next(position,map,3,1)

        if position[0] <= len(map)-1:

            # adding line n amounts of times depending on how often needed
            if position[1]/len(map[position[0]]) >= 1:
                map[position[0]] = (1 + int(position[1]/len(map[position[0]]))) * map[position[0]]

            # if the end poistion of one move is a 'tree', count it
            if map[position[0]][position[1]] == '#': 
                treecount = treecount + 1

    return treecount
    

##Part 2



if __name__ =="__main__":
    inputtxt = sys.argv[1]

    onemap = input_to_list(inputtxt)
    print(count_trees(onemap))