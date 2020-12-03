"""

Advent of Code, Day 1

"""
import sys


##Part 1

def run_part1(input):
    for aline in input:
        for secondline in input:
            aline = int(aline)
            secondline = int(secondline)
            #print(aline)
            if aline + secondline == 2020:
                print(aline * secondline) 
            
        
## PArt 2

def run_part2(input):
    for aline in input:
        for secondline in input:
            for thirdline in input:
                aline = int(aline)
                secondline = int(secondline)
                thirdline = int(thirdline)
                if aline + secondline + thirdline == 2020:
                    print(aline * secondline * thirdline) 


if __name__ == "__main__":

    inputtxt = sys.argv[1]
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    run_part1(input)
    run_part2(input)

