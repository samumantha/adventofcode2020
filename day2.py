"""

Advent of Code, Day 2

input: list of strings with a policy (in beginning, see d2_test.txt), 

todo: 
part1: policy: the lowest and highest number of times the character must appear in string; check strings for validity
part2: policy: character must appear at either first or second index given (indexing starts with 1); check strings for validity

results on testset:
part1: 2
part2: 1

"""

import sys

##Part 1

def decode_line(line):
    
    low = line.split('-')[0]
    high = line.split('-')[1].split(' ')[0]
    letter = line.split(':')[0][-1]
    pw = line.split(':')[1][1:]
    count = pw.count(letter)

    return low,high,letter,pw,count

def run_part1(input):
    thecount = 0
    for line in input:
        low,high,letter,pw,count = decode_line(line)
        if count >= int(low) and count <= int(high):
            thecount += 1
    print(thecount)

## PArt 2

def run_part2(input):
    thecount = 0
    for line in input:
        low,high,letter,pw,count = decode_line(line)
        if pw[int(low)-1] == letter and pw[int(high)-1] != letter:
            thecount += 1
        elif pw[int(low)-1] != letter and pw[int(high)-1] == letter:
            thecount += 1
    print(thecount)


if __name__ == "__main__":

    inputtxt = sys.argv[1]
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    
    run_part1(input)
    run_part2(input)