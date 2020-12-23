from time import sleep

def unbracket(expression):
    searchpointer = 0
    cleanexpression = ""
    oldlocation2 = -1
    while searchpointer < len(expression):
        allbracketsfound = True
        location1 = -1 #location of bracket1
        for pos in range(searchpointer,len(expression)):
            if expression[pos] == "(":
                location1 = pos
                allbracketsfound = False
                break
        if location1 > -1: #bracket found
            otheropens = 0
            for pos in range(location1+1,len(expression)):
                if expression[pos] == ")" and otheropens == 0:
                    location2 = pos #location of bracket2
                    break
                elif expression[pos] == ")" and otheropens > 0:
                    otheropens -= 1
                elif expression[pos] == "(":
                    otheropens += 1
            inside =expression[location1+1:location2]
            if location1 > oldlocation2:
                cleanexpression = cleanexpression + expression[oldlocation2+1:location1]
            cleanexpression = cleanexpression + unbracket(inside)
            searchpointer = location2
            oldlocation2 = location2
        if allbracketsfound:
            if cleanexpression == "":
                cleanexpression = expression
            else:
                cleanexpression = cleanexpression +expression[oldlocation2+1:]
            break
        searchpointer += 1
    result = evaluate(cleanexpression)
    return result

def evaluate(expression):
    tokens = expression.split(" ")
    accumulator = int(tokens[0])
    for i in range(1,len(tokens), 2):
        operation = tokens[i]
        argument = int(tokens[i+1])
        if operation == "*":
            accumulator *= argument
        elif operation == "+":
            accumulator += argument
    return str(accumulator)

        
f = open("temp.txt")
results = []
line = f.readline().strip()
while line:
    calculate = int(unbracket(line))
    results.append(calculate)
    line = f.readline().strip()
print(sum(results))
