import sys
import re

#(Birth Year) - four digits; at least 1920 and at most 2002.
def byr_valid(s):
    return 1920 <= int(s) <= 2002  

#(Issue Year) - four digits; at least 2010 and at most 2020.
def iyr_valid(s):
    return 2010 <= int(s) <= 2020  

#(Expiration Year) - four digits; at least 2020 and at most 2030.
def eyr_valid(s):
    return 2020 <= int(s) <= 2030  

#(Height) - a number followed by either cm or in:
        #If cm, the number must be at least 150 and at most 193.
        #If in, the number must be at least 59 and at most 76.
def hgt_valid(s):
    if s[-2:] == "cm":
        return 150 <= int(s[:-2]) <= 193
    return 59 <= int(s[:-2]) <= 76

#(Hair Color) - a # followed by exactly six characters 0-9 or a-f. 
def hcl_valid(s):
    return re.match(r"^#[0-9a-f]{6}$",s)

#(Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def ecl_valid(s):
    return s in  ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

#(Passport ID) - a nine-digit number, including leading zeroes.
def pid_valid(s):
    return re.match(r"^\d{9}$",s)

validation_rules = {
    "byr": byr_valid,
    "iyr": iyr_valid,
    "eyr": eyr_valid,
    "hgt": hgt_valid,    
    "hcl": hcl_valid,
    "ecl": ecl_valid,
    "pid": pid_valid,
}

def parse_raw_passports(raw_pp):
    kvs = [x.split(':') for x in raw_pp.split()]
    return {k:v for k,v in kvs}

def validate_passorts(pp):
    for header, validator in validation_rules.items():
        if header not in pp.keys():
            return False
        if not validator(pp[header]):
            return False
    return True

def main():
    passport_raw = ''.join([x for x in sys.stdin]).split('\n\n')
    passports = [parse_raw_passports(pp) for pp in passport_raw]    
    
    valid_passports = [pp for pp in passports if validate_passorts(pp)]

    print(len(valid_passports))


main()
