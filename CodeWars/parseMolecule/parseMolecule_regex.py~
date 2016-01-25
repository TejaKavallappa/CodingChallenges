import re
def parse_molecule(formula):
    res = {}
    #Convert square and flower brackets to parenthesis
    if(re.search(r"\[", formula)):
        formula = re.sub(r"\[",r"(",formula)
        formula = re.sub(r"\]",r")",formula)
    if(re.search(r"\{", formula)):
        formula = re.sub(r"\{",r"(",formula)
        formula = re.sub(r"\}",r")",formula)
    while(re.search(r"\(", formula)):
        formula = yes_brackets(formula)
    print formula
    res = no_brackets(formula)
    return res

def no_brackets(formula):
    res = {}
    elements = re.findall(r"([A-Z][a-z]?)(\d\d?)*", formula)
    for elem in elements:
        atm = 1
        if (elem[1] != ''):
            atm = elem[1]
        if(elem[0] not in res):
            res[elem[0]] = int(atm)
        else:
            res[elem[0]] += int(atm)
    return res

def yes_brackets(formula):
    match4 = re.search(r"\([\w\d]+\)(\d\d?)*", formula);
    newform = "" 
    if match4:
        num = ""
        if match4.group(1):
            num = match4.group(1)
            innerContent = ""
            print match4.group()
            elements = re.findall(r"([A-Z][a-z]?)(\d\d?)*", match4.group())
            for elem in elements:
                innerContent += elem[0]
                if(elem[1] == ''):
                    atm =1
                else:
                    atm = elem[1]
                innerContent += str(int(num) * int(atm))
        else:
            innerContent = re.sub(r"\(", r"", match4.group())
            innerContent = re.sub(r"\)", r"", innerContent)
        newform = re.sub(r"\([\w\d]+\)(\d)?", innerContent, formula, 1)
        match4 = re.search(r"\([\w\d]+\)(\d)?", newform);
    if newform:
        formula = newform
    return formula

if __name__=="__main__":
    molefile = open("molecules.txt","r")
    for line in molefile:
        mole = line
        print mole , " " ,parse_molecule(mole)

