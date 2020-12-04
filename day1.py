"""

Advent of Code, Day 1

input: list of numbers

todo: 
part 1: find the two numbers, that sum up to 2020, multiply them and submit the result
part 2: find the three numbers from the list that sum up to 2020, multiply them and submit the result

testresults:
part 1: 514579
part 2: 241861950


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

