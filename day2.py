inputtxt = 'd2_input.txt'

##Part 1

with open(inputtxt,'r') as inp:
    input = inp.readlines()

def decode_line(line):
    
    low = line.split('-')[0]
    high = line.split('-')[1].split(' ')[0]
    letter = line.split(':')[0][-1]
    pw = line.split(':')[1][1:]
    count = pw.count(letter)

    return low,high,letter,pw,count

thecount = 0
for line in input:
    low,high,letter,pw,count = decode_line(line)
    if count >= int(low) and count <= int(high):
        thecount += 1
print(thecount)

## PArt 2

thecount = 0
for line in input:
    low,high,letter,pw,count = decode_line(line)
    if pw[int(low)-1] == letter and pw[int(high)-1] != letter:
        thecount += 1
    elif pw[int(low)-1] != letter and pw[int(high)-1] == letter:
        thecount += 1
print(thecount)