
inputtxt = 'd1_input.txt'

##Part 1

with open(inputtxt,'r') as inp:
    input = inp.readlines()


for aline in input:
    for secondline in input:
        aline = int(aline)
        secondline = int(secondline)
        #print(aline)
        if aline + secondline == 2020:
            print(aline * secondline) 
            break
        
## PArt 2

for aline in input:
    for secondline in input:
        for thirdline in input:
            aline = int(aline)
            secondline = int(secondline)
            thirdline = int(thirdline)
            if aline + secondline + thirdline == 2020:
                print(aline * secondline * thirdline) 
                break

