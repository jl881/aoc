#chinese remainder theorem

def findinverse(A,C):
	for B in range(C):
		if (A*B)%C == 1:
			return B

f = open("temp.txt")
f.readline()
rawlist = f.readline().strip().split(",")
posvalue = []
for i in range(len(rawlist)):
    if rawlist[i] != "x":
        posvalue.append((i, int(rawlist[i])))

N = 1
for pair in posvalue:
    modulo = pair[1]
    N *= modulo

x = 0
for pair in posvalue:
    offset = pair[0]
    busno= pair[1]
    bi = (busno - offset)%busno
    Ni = N// busno
    xi = findinverse(Ni, busno)
    x += bi*Ni*xi
print(x%N)
