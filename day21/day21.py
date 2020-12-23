import re

f = open("day21input.txt")
line = f.readline().strip()
uniqueallergens = []
uniqueingredients = []
lines = []

while line:
    groups = re.match(r"(.*)\(contains(.*)\)", line)
    ingredients = groups.group(1).strip().split(" ")
    allergens = groups.group(2).strip().split(", ")
    for ingredient in ingredients:
        if ingredient not in uniqueingredients:
            uniqueingredients.append(ingredient)
    for allergen in allergens:
        if allergen not in uniqueallergens:
            uniqueallergens.append(allergen)
    lines.append([ingredients,allergens])
    line = f.readline().strip()

allergens = {k:[] for k in uniqueallergens}
possiblematches= []
for allergen in uniqueallergens:
    for ingredient in uniqueingredients:
        match = True
        for i in range(len(lines)):
            if allergen in lines[i][1]:
                if ingredient not in lines[i][0]:
                    match = False
                    break
        if match and ingredient not in possiblematches:
            allergens[allergen].append(ingredient)


results = []
allfound = all(len(allergens[a]) == 1 for a in allergens)
while not allfound:
    for a in allergens:
        if len(allergens[a]) == 1:
            results.append(a + ":" + allergens[a][0])
            foundallergen = a
            foundingredient = allergens[a][0]
            break
    del allergens[foundallergen]
    for b in allergens:
                if foundingredient in allergens[b]:
                    allergens[b].remove(foundingredient)        

##knownallergens = ['cxfz', 'lxjtns', 'prxmdlz', 'qdfpq', 'clg', 'vzzz', 'knprxg', 'ncjv']
##f = open("day21input.txt")
##line = f.readline().strip()
##occurrences = 0
##while line:
##    groups = re.match(r"(.*)\(contains(.*)\)", line)
##    ingredients = groups.group(1).strip().split(" ")
##    for ingredient in ingredients:
##        if ingredient not in knownallergens:
##            occurrences += 1
##    line = f.readline().strip()
##print(occurrences)

