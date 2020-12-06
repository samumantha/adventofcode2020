import sys

#any
def get_group_lists(input):
    #grouplist = []
    groupset = set()
    fulllist = []
    for i,line in enumerate(input):
        if not line == '':
            #print(line)
            #grouplist.append(line)
            for char in list(line):
                groupset.add(char)
        elif line == '':
            fulllist.append(list(groupset))
            groupset = set()
        if i == len(input)-1:
            fulllist.append(list(groupset))
    return fulllist

#all
def get_group_lists2(input):
    grouplist = []
    #groupset = set()
    fulllist = []
    groupline = 0
    for i,line in enumerate(input):
        
        if not line == '':
            #print(line)
            #grouplist.append(line)
            for char in list(line):
                #groupset.add(char)
                grouplist.append(char)
            groupline = groupline + 1
        elif line == '':
            #fulllist.append(list(groupset))
            #print(groupline)
            #print(grouplist)
            newgrouplist = set()
            for answer in grouplist:
                for char in answer:
                    if grouplist.count(char) == groupline :  
                        newgrouplist.add(char)
                        break    
            fulllist.append(list(newgrouplist))
                        
            #groupset = set()
            grouplist = []
            groupline = 0
        if i == len(input)-1:
            newgrouplist = set()
            for answer in grouplist:
                for char in answer:
                    if grouplist.count(char) == groupline :  
                        newgrouplist.add(char)
                        break
            #fulllist.append(list(groupset))
            fulllist.append(list(newgrouplist))
    return fulllist


if __name__ == "__main__":

    inputtxt = sys.argv[1]
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    input_wo_newline = [line.strip() for line in input] 

#Part 1
    fulllist = get_group_lists(input_wo_newline)

    flattenedlist = [item for sublist in fulllist for item in sublist]

    print(len(flattenedlist))

#Part 2
    thelist = get_group_lists2(input_wo_newline)
    #print(thelist)
    
    theflattenedlist = [item for sublist in thelist for item in sublist]

    print(len(theflattenedlist))