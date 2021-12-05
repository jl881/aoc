numofplanes = 0
numofrows = 0
numofcols = 0
wrange = None
zrange = None
yrange = None
xrange = None

neighbours = []
for x in [-1,0,1]:
    for y in [-1,0,1]:
        for z in [-1, 0, 1]:
            for w in [-1,0,1]:
                neighbours.append((x,y,z,w))
neighbours.remove((0,0,0,0))

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

def makeworld3d(plane):
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

def makeworld4d(world3d):
    numofplanes = len(world3d)
    numofrows = len(world3d[0])
    numofcols = len(world3d[0][0])
    blankworld3d = []
    for i in range(numofplanes):
        blankplane = []
        for j in range(numofrows):
            blankplane.append(["."]*numofcols)
        blankworld3d.append(blankplane)
    
    world = []
    for i in range(6,0,-1):
        world.append(blankworld3d)
    world.append(world3d)
    for i in range(6,0,-1):
        world.append(blankworld3d)
    return world

def getstate(xyzw, world):
    wmod = xyzw[3] + 6
    zmod = xyzw[2] + 6
    ymod = xyzw[1] + 6 + (numofrows-1)//2
    xmod = xyzw[0] + 6 + (numofcols-1)//2
    return(world[wmod][zmod][ymod][xmod])

def getneighbours(xyzw,world):
    nbcoords = []
    for nb in neighbours:
        nbcoord = tuple(map(sum, zip(xyzw,nb)))
        if validcoord(nbcoord):
            nbcoords.append(nbcoord)
    return nbcoords

def defineranges():
    global wrange
    global zrange
    global yrange
    global xrange
    wrange = range(-6,7)
    zrange = range(-6, 7)
    yrange = range(-(6 + (numofrows-1)//2), 6 + numofrows//2 +1)
    xrange = range(-(6 + (numofcols-1)//2), 6 + numofcols//2 +1)

def validcoord(coord):
    validx = coord[0] in xrange
    validy = coord[1] in yrange
    validz = coord[2] in zrange
    validw = coord[3] in wrange
    validornot = validx and validy and validz and validw
    return validornot

def indextocoord(i0, i1, i2, i3):
    w = i0-6
    z = i1-6
    y = i2-(6+(numofrows-1)//2)
    x = i3-(6+(numofcols-1)//2)
    return (x,y,z,w)

def nextstate(xyzw, world):
    currentstate = getstate(xyzw,world)
    neighbours = getneighbours(xyzw,world)
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

world = makeworld4d(makeworld3d(makeplane()))
defineranges()


for i in range(6):
    newworld4d = []
    for depth1 in range(len(world)):
        newworld3d = []
        for depth2 in range(len(world[0])):
            newplane = []
            for depth3 in range(len(world[0][0])):
                newrow = []
                for depth4 in range(len(world[0][0][0])):
                    newrow.append(nextstate(indextocoord(depth1,depth2,depth3,depth4),world))
                newplane.append(newrow)
            newworld3d.append(newplane)
        newworld4d.append(newworld3d)
    world = newworld4d[::]
    

count = 0
for depth1 in range(len(world)):
    for depth2 in range(len(world[0])):
        for depth3 in range(len(world[0][0])):
            for depth4 in range(len(world[0][0][0])):
                if world[depth1][depth2][depth3][depth4] == "#":
                    count += 1
print(count)
    

