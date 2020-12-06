import sys


if __name__ == "__main__":

    inputtxt = sys.argv[1]
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    input_wo_newline = [line.strip() for line in input] 

    #rows 0 to 127
    for line in input_wo_newline:
        total = 128
        for i,letter in enumerate(line):
            if i < 7:
                #F keeps lower
                total = total / 2
                if letter == 'F':
                    up = total
                    
            else:

