from time import sleep
import numpy as np

nvectors = [[-1, 0], [0, -1], [0, 1], [1, 0]]
neighbourvectors = [np.array(nvector) for nvector in nvectors]
validrange = range(0,12)

def rot180(square):
    return np.rot90(np.rot90(square))

def rot270(square):
    return np.rot90(np.rot90(np.rot90(square)))

def flipRL(square):
    return np.fliplr(np.rot90(square))

def flipLR(square):
    return np.flipud(np.rot90(square))

def pprint(square):
    for row in square:
        print(row)

def findmatches(strings1, strings2):
    global currentmatches
    matches = False
    location = -1
    for i in range(len(strings1)):
        for j in range(len(strings2)):
            if strings1[i] == strings2[j]:
                matches = True
                location = i
                break
        if matches:
            break
    return (matches,location)

def populate(tileno, sharedsides):
    coords = [tilelocations[tileno] for tileno in sharedsides]
    if len(coords) == 1:
        coord = coords[0]
        npcoord = np.array(coord)
        shift = lambda vector : list(vector + coord)
        potentialspaces= list(map(shift, neighbourvectors))
        okspaces= [space for space in potentialspaces if space[0] in validrange and space[1] in validrange]
        success= trytwolocations(tileno,coord, okspaces)
    else:
        coord1 = tilelocations[sharedsides[0]]
        coord2 = tilelocations[sharedsides[1]]
        side1 = np.array(coord1) if coord1[0] < coord2[0] else np.array(coord2)
        side2 = np.array(coord2) if np.array_equal(side1, coord1) else np.array(coord1)
        diff = side2 - side1
        constraints = [None, None, None, None]

        if np.array_equal(diff, np.array([1,1])):
            okspaces = [side1 + np.array([0,1]), side1 + np.array([1,0])]
            oks = [space for space in okspaces if not np.any(populated[tuple(space)])]
        elif np.array_equal(diff, np.array([1,-1])):
            okspaces = [side1 + np.array([0,-1]), side1 + np.array([1,0])]
            oks = [space for space in okspaces if not np.any(populated[tuple(space)])] 
        if len(oks) == 1:
            newspace = oks[0]
        else:
            print("epic fail")
        if np.array_equal(diff, np.array([1,1])):
            if np.array_equal(side1-newspace, np.array([0,-1])):
                constraints[1] = populated[tuple(side2)][0]
                constraints[2] = populated[tuple(side1)][:,-1]
            elif np.array_equal(side1-newspace, np.array([-1,0])):
                constraints[0] = populated[tuple(side1)][-1]
                constraints[3] = populated[tuple(side2)][:,0]
        elif np.array_equal(diff, np.array([1,-1])):
            if np.array_equal(side1-newspace, np.array([-1,0])):
                constraints[0] = populated[tuple(side1)][-1]
                constraints[2] = populated[tuple(side2)][:,-1]
            elif np.array_equal(side1-newspace, np.array([0,1])):
                constraints[3] = populated[tuple(side1)][:,0]
                constraints[1] = populated[tuple(side2)][0]
            
        attempt = trysinglelocation(tileno, constraints)
        success = attempt is not None
        if not success:
            print("AAAAAAAAGH!!!!")
        else:
            populated[tuple(newspace)] = attempt
            tilelocations[tileno] = list(newspace)

def trytwolocations(tileno, coord,okspaces):
    success = []
    successsquare = None
    correctspace = None
    placedtile = np.array(coord)
    edge = [0, 11]
    for i in range(len(okspaces)):
        if okspaces[i][0] in edge or okspaces[i][1] in edge:
            constraints = [None, None, None, None]
            okspace = np.array(okspaces[i])
            diff = placedtile - okspace
            if np.array_equal(diff,np.array([1,0])):
                okspace= placedtile + np.array([-1, 0])
                constraints[1] = populated[tuple(placedtile)][0]
            elif np.array_equal(diff,np.array([0,1])):
                okspace= placedtile + np.array([0, -1])
                constraints[3] = populated[tuple(placedtile)][:,0]
            elif np.array_equal(diff,np.array([-1,0])):
                okspace= placedtile + np.array([1, 0])
                constraints[0] = populated[tuple(placedtile)][-1]
            elif np.array_equal(diff, np.array([0,-1])):
                okspace= placedtile + np.array([0, 1])
                constraints[2] = populated[tuple(placedtile)][:,-1]
            attempt = trysinglelocation(tileno, constraints)
            if attempt is not None:
                successsquare = attempt
                correctspace = okspace
                success.append(True)
    if len(success) != 1:
        return False
    else:
        populated[tuple(correctspace)] = successsquare
        tilelocations[tileno] = list(correctspace)
        return True

transform = {0: lambda x: x, 1: lambda x: np.rot90(x), 2: lambda x: rot180(x), 3: lambda x: rot270(x), 4: lambda x: np.fliplr(x), 5: lambda x: np.flipud(x), 6: lambda x: flipLR(x), 7: lambda x: flipRL(x)}
def trysinglelocation(tileno, constraints):
    square = nptilesquare[tileno]
    successes = []
    successsquare = None
    for trans in transform:
        transformed = transform[trans](square)
        if checklegal(transformed,constraints):
            successes.append(True)
            successsquare = transformed
    if len(successes) != 1:
        return None
    else:
        return successsquare

getedge = {0: lambda x: x[0], 1: lambda x: x[-1], 2: lambda x: x[:,0], 3: lambda x: x[:,-1]}
def checklegal(square, constraints):
    for i in range(len(constraints)):
        if constraints[i] is not None:
            edge = getedge[i](square)
            if not np.array_equal(edge, constraints[i]):
                return False
    return True
    

f = open("day20input.txt")
line = f.readline().strip()
tilesquare = {}
while line:
    tileno = int(line.strip(":").strip("Tile "))
    tilesquare[tileno] = []
    for i in range(10):
        line = list(f.readline().strip())
        toints = lambda symbol : 1 if symbol == "#" else 0
        line = list(map(toints,line))
        tilesquare[tileno].append(line)
    f.readline()
    line = f.readline().strip()
        
tileedges = {}
for tile in tilesquare:
    square = tilesquare[tile]
    tileedges[tile] = []
    tileedges[tile].append(square[0])
    tileedges[tile].append(square[-1])
    leftedge = [row[0] for row in square]
    rightedge = [row[-1] for row in square]
    tileedges[tile].append(leftedge)
    tileedges[tile].append(rightedge)

for tile in tileedges:
    reverseedges = []
    for edge in tileedges[tile]:
        reverseedges.append(list(reversed(edge)))
    tileedges[tile] = tileedges[tile] + reverseedges


corners = [1453, 1459, 2543, 3181]

populated = np.zeros((12,12,10,10))
nptilesquare = {k:np.array(v) for (k,v) in tilesquare.items()}
nptileedges = {k:np.array(v) for (k,v) in tileedges.items()}

neighbours = {k:[] for k in tilesquare.keys()}
relevantsides = {k:[False, False, False, False] for k in tilesquare.keys()}

for tile1 in tileedges:
    for tile2 in tileedges:
        if tile2 != tile1:
            matches = findmatches(tileedges[tile1], tileedges[tile2])
            if matches[0]:
                neighbours[tile1].append(tile2)
                relevantsides[tile1][matches[1]] = True

tilelocations = {}
corners = [1453, 1459, 2543, 3181]

populated[0,0] = nptilesquare[1453]
tilelocations[1453] = [0,0]
populated[0,11] = flipLR(nptilesquare[3181])
tilelocations[3181] = [0,11]
populated[11,0] = nptilesquare[2543]
tilelocations[2543] = [11,0]
populated[11,11] = nptilesquare[1459]
tilelocations[1459] = [11,11]

numsides = 0
while len(tilelocations) < 144:
    locationsthispass = list(tilelocations.keys())
    for tile1 in tileedges:
        if tile1 not in tilelocations:
            sharedsides = [item for item in neighbours[tile1] if item in locationsthispass]
            if len(sharedsides) > numsides:
                populate(tile1, sharedsides)
    numsides = 1 if numsides == 0 else 0

            
modpopulated = np.zeros((12,12,8,8))
for i in range(12):
    for j in range(12):
        modpopulated[i,j] = populated[i,j,1:9,1:9]

bigpopulated = np.zeros([96,96])
for i in range(12):
    for j in range(12):
        bigpopulated[i*8:(i+1)*8,j*8:(j+1)*8] = modpopulated[i,j]

bigpopulated = np.fliplr(bigpopulated)

monster = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
       [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
inversemonster = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
       [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]])

endingpopulated = np.copy(bigpopulated)
for i in range(93):
    for j in range(76):
        searcharea = bigpopulated[i:i+3,j:j+20]
        masked = np.multiply(searcharea,monster)
        if np.array_equal(masked,monster):

            removemonster = np.multiply(searcharea,inversemonster)

            endingpopulated[i:i+3,j:j+20] = removemonster

print(np.sum(bigpopulated))
print(np.sum(endingpopulated))
