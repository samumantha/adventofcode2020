import sys
"""
def find_biggest(index):
    biggestf = 0
    biggestl = 0
    for i,line in enumerate(input):
        firstf = line.find('F') #the bigger the index, the higher the number
        firstl = line.find('L') #same here
        if firstf >= biggestf and firstl >= biggestl:
            biggestf = firstf
            biggestl = firstl
            indexofbiggest = i 

    print(input[indexofbiggest])
"""

# with a hint from shuuby :)
def binary_check(input):
    # F or L gives 0
    highestid = 0
    seatlist = []
    for line in input:
        line = line.replace('F','0')
        line = line.replace('B','1')
        line = line.replace('R','1')
        line = line.replace('L','0')
        seatid = int(line,2)
        seatlist.append(seatid)
        if seatid >= highestid:
            highestid = seatid
    return highestid, seatlist

def find_my_seat(seatlist):
    # max 1023
    seatlist.sort()
    fulllist = list(range(0,1023))
    mismatches = [x for x in fulllist if not x in seatlist]
    myseat = 0
    for mismatch in mismatches:
        if mismatch-1 in seatlist and mismatch+1 in seatlist:
            #print(mismatch)
            myseat = mismatch
    return myseat


if __name__ == "__main__":

    inputtxt = sys.argv[1]
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    input_wo_newline = [line.strip() for line in input] 

#Part1
    seatid,seatlist = binary_check(input_wo_newline)
    print(seatid)

#Part2
    print(find_my_seat(seatlist))

