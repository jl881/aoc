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

while not expanded[0]:
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

theregex = expansions[0]
print(theregex)
matches = 0
totals = 0
line = f.readline().strip()
while line:
    matchObj = re.fullmatch(rf"{theregex}", line)
    if matchObj is not None:
        matches +=1
    totals += 1
    line = f.readline().strip()
print(matches, totals)
