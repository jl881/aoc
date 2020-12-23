numofrows = 0
numofcols = 0
zrange = None
yrange = None
xrange = None

neighbours = []
for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1, 0, 1]:
            neighbours.append((x,y,z))
neighbours.remove((0,0,0))

def makeplane():
    global numofrows
    global numofcols
    world = []
    
    f = open("temp.txt")
    line = f.readline().strip()
    rowlen = len(line)
    numofcols = rowlen
    for i in range(6):
        world.append(["."]*(12+rowlen))
    while line:
        numofrows += 1
        extendline = "......" + line + "......"
        world.append(list(extendline))
        line = f.readline().strip()
    for i in range(6):
        world.append(["."]*(12+rowlen))
    return world

def makeworld(plane):
    numofrows = len(plane)
    numofcols = len(plane[0])
    blankplane = []
    for i in range(numofrows):
        blankplane.append(["."]*numofcols)

    world = []
    for i in range(6,0,-1):
        world.append(blankplane)
    world.append(plane)
    for i in range(6,0,-1):
        world.append(blankplane)
    return world

def getstate(xyz, world):
    zmod = xyz[2] + 6
    ymod = xyz[1] + 6 + (numofrows-1)//2
    xmod = xyz[0] + 6 + (numofcols-1)//2
    return(world[zmod][ymod][xmod])

def getneighbours(xyz,world):
    nbcoords = []
    for nb in neighbours:
        nbcoord = tuple(map(sum, zip(xyz,nb)))
        if validcoord(nbcoord):
            nbcoords.append(nbcoord)
    return nbcoords

def defineranges():
    global zrange
    global yrange
    global xrange
    zrange = range(-6, 7)
    yrange = range(-(6 + (numofrows-1)//2), 6 + numofrows//2 +1)
    xrange = range(-(6 + (numofcols-1)//2), 6 + numofcols//2 +1)

def validcoord(coord):
    validx = coord[0] in xrange
    validy = coord[1] in yrange
    validz = coord[2] in zrange
    validornot = validx and validy and validz
    return validornot
    
def indextocoord(i0, i1, i2):
    z = i0-6
    y = i1-(6+(numofrows-1)//2)
    x = i2-(6+(numofcols-1)//2)
    return (x,y,z)

def nextstate(xyz, world):
    currentstate = getstate(xyz,world)
    neighbours = getneighbours(xyz,world)
    neighbourstates = []
    for neighbour in neighbours:
        neighbourstates.append(getstate(neighbour,world))
    if currentstate == "#":
        if neighbourstates.count("#") not in range(2,4):
            return "."
        else:
            return "#"
    elif currentstate == ".":
        if neighbourstates.count("#") == 3:
            return "#"
        else:
            return "."

world = makeworld(makeplane())
defineranges()

for i in range(6):
    newworld = []
    for depth1 in range(len(world)):
        newplane = []
        for depth2 in range(len(world[0])):
            newrow = []
            for depth3 in range(len(world[0][0])):
                newrow.append(nextstate(indextocoord(depth1,depth2,depth3),world))
            newplane.append(newrow)
        newworld.append(newplane)
    world = newworld[::]

count = 0
for depth1 in range(len(world)):
    for depth2 in range(len(world[0])):
        for depth3 in range(len(world[0][0])):
            if world[depth1][depth2][depth3] == "#":
                count += 1
print(count)
    
