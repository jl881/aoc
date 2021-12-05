from time import sleep
import re
NUMOFRULES = 134

f = open("temp.txt")
rules = [""]*NUMOFRULES
expanded = [False]*NUMOFRULES
expansions = [""]*NUMOFRULES
line = f.readline().strip()
while line:
    split = line.split(":")
    rules[int(split[0])] = split[1].strip().strip('"')
    line = f.readline().strip()

def nextrulestoexpand(expanded, rules):
    expandedlist = []
    for i in range(len(expanded)):
        if expanded[i]:
            expandedlist.append(i)
            
    returnlist = []
    for i in range(len(rules)):
        if containsonlyreferencesto(i, expandedlist, rules) and i not in expandedlist:
            returnlist.append(i)
    return returnlist

def containsonlyreferencesto(i, references, rules):
    rule = rules[i]
    cleanrule = rule.replace(" |", "")
    split = cleanrule.split(" ")
    ok = True
    for mention in split:
        if not mention.isdigit():
            ok = False
            break
        if int(mention) not in references:
            ok = False
            break
    return ok

for i in range(len(rules)):
    if rules[i].isalpha():
        expanded[i] = True
        expansions[i] = rules[i]

while not expanded[31]:
    toexpand = nextrulestoexpand(expanded,rules)
    for i in toexpand:
        rule = rules[i]
        pipesplit = rule.split("|")
        leftpipe = pipesplit[0].strip().split(" ")
        leftpiperegex = "".join([expansions[int(l)] for l in leftpipe])
        newregex = leftpiperegex
        if len(pipesplit) > 1:
            rightpipe = pipesplit[1].strip().split(" ")
            rightpiperegex = "".join([expansions[int(r)] for r in rightpipe])
            newregex = "(" + leftpiperegex + "|" + rightpiperegex + ")"
        expanded[i] = True
        expansions[i] = newregex

while line:
    line = f.readline()

listofstrings = []
line = f.readline().strip()
while line:
    listofstrings.append(line)
    line = f.readline().strip()

regex8 = expansions[42]+"+"
regex11 = expansions[42] + "("+expansions[42] +"){-1}("+ expansions[31]+"){-1}" + expansions[31]
regex0 = regex8 + regex11

matches = 0
for i in range(10):
    regex0 = regex0.replace("{"+str(i-1)+"}", "{"+str(i)+"}")
    for string in listofstrings:
        matchObj = re.fullmatch(rf"{regex0}", string)
        if matchObj is not None:
            matches +=1
print(matches)
