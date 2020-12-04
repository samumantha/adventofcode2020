"""

Advent of Code, Day 4

"""
import sys
import re


# start reading first line into dict, when next line is '', start next dict 
def get_pp_dicts(input):
    alldictlist = []
    adict= {}
    for i,line in enumerate(input):
        if not line == '':
            print(line)
            pairs = line.split(' ')
            for pair in pairs:
                key, value = pair.split(':')
                adict[key] = value
        elif line == '':
            alldictlist.append(adict)
            adict = {}
        if i == len(input)-1:
            alldictlist.append(adict)
    return alldictlist

def count_valid_pp(pplist, needed):
    valid_counter= 0
    for passport in pplist:
        all_there = all(field in passport for field in needed)
        if all_there:
            valid_counter = valid_counter + 1
    return valid_counter

def get_valid_pp(pplist, needed):
    valid_passports = []
    for passport in pplist:
        all_there = all(field in passport for field in needed)
        if all_there:
            valid_passports.append(passport)
    return valid_passports

def check_val_year(value,digits,min,max):
    valid = False
    if len(str(value)) == digits and value >= min and value <= max:
        #print('valid')
        valid = True
    return valid

def check_val_height(value,cmmin,cmmax,inmin,inmax):
    valid = False
    #could be only 2 digit number
    if len(value) >= 4:
        value_int = int(value[:-2])
        if value.endswith('cm'):
            if value_int >= cmmin and value_int <= cmmax:
                valid = True
        elif value.endswith('in'):
            if value_int >= inmin and value_int <= inmax:
                valid = True
    return valid

def check_val_haircolor(value):
    valid = False
    # a # followed by exactly six characters 0-9 or a-f.
    if value.startswith('#') and len(value)== 7:
        regex1 = re.compile('[a-z]')
        regex2 = re.compile('[0-9]')
        if regex1.search(value) or regex2.search(value): 
            #print('valid')
            valid = True
    return valid

def check_val_eyecolor(value):
    valid = False
    validlist = ['amb' ,'blu', 'brn', 'gry', 'grn','hzl','oth']
    if value in validlist:
        #print('valid')
        valid = True
    return valid

def check_val_pid(value):
    valid = False
    if len(value) == 9:
        #print('valid')
        valid = True
    return valid


def check_validity(valid_pp):
    valid = True
    valid_count = 0
    for passport in valid_pp:
        print('next')
        checklist = [check_val_year(int(passport['byr']),4, 1920,2002),check_val_year(int(passport['iyr']),4, 2010,2020), check_val_year(int(passport['eyr']),4, 2020,2030), check_val_height(passport['hgt'],150,193,59,76), check_val_haircolor(passport['hcl']),check_val_eyecolor(passport['ecl']), check_val_pid(passport['pid'])]
        
        if all(checklist):
            valid_count = valid_count +1 
    return valid_count
  
"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
"""

if __name__ =="__main__":

    
    inputtxt = sys.argv[1]
    with open(inputtxt,'r') as inp:
        input = inp.readlines()
    input_wo_newline = [line.strip() for line in input]
    print(input_wo_newline)
    
    pp_dictlist = get_pp_dicts(input_wo_newline)

    needed = ['byr', 'iyr','eyr', 'hgt', 'hcl','ecl', 'pid']
    #optional = 'cid'

    valid_pp_number = count_valid_pp(pp_dictlist, needed)
   
    #PArt 1

    print(valid_pp_number)

    #Part 2

    valid_passports = get_valid_pp(pp_dictlist, needed)

    print(check_validity(valid_passports))
