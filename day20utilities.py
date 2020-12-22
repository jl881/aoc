import numpy as np


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
    return (matches, location)


getedge = {0: lambda x: x[0], 1: lambda x: x[-1], 2: lambda x: x[:, 0], 3: lambda x: x[:, -1]}


def checklegal(square, constraints):
    for i in range(len(constraints)):
        if constraints[i] is not None:
            edge = getedge[i](square)
            if not np.array_equal(edge, constraints[i]):
                return False
    return True


transform = {0: lambda x: x, 1: lambda x: np.rot90(x), 2: lambda x: rot180(x), 3: lambda x: rot270(x),
             4: lambda x: np.fliplr(x), 5: lambda x: np.flipud(x), 6: lambda x: flipLR(x), 7: lambda x: flipRL(x)}


def trysinglelocation(square, constraints):
    successes = []
    successsquare = None
    for trans in transform:
        transformed = transform[trans](square)
        if checklegal(transformed, constraints):
            successes.append(True)
            successsquare = transformed
    if len(successes) != 1:
        return None
    else:
        return successsquare
