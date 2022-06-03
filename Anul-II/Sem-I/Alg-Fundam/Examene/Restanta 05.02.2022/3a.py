f = open("graf.in", "r")
listaInscrieri = []
visited = []

line = f.readline()
nProjects = int(line.split()[0])
mStudents = int(line.split()[1])
# flowStudent = [[0] * (nProjects + 1) for i in range(nProjects + 1)]
# flowProiect = [[0] * (nProjects + 1) for i in range(nProjects + 1)]
proiectPerStudent = 1
studentPerProiect = 1

listaAdiacentaProiect = [[] * mStudents]

line = f.readline()
while line:
    proiect = int(line.split()[0])
    student = int(line.split()[1])
    # listaInscrieri.append((int(line.split()[0]), int(line.split()[1])))
    listaAdiacentaProiect[proiect - 1].append(student)
    line = f.readline()
f.close()

k = 2

print("pentru k=" + str(k))
print("asocieri proiect-student")


rest = [[0] * (nProjects + mStudents + 1) for i in range(nProjects + mStudents + 1)]



