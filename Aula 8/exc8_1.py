class Matriz:
    def __init__(self, n,m,v):
        self.linha = n
        self.coluna = m
        self.matrizes = []
        for i in range(n):
            lin = []
            for j in range(m):
                lin.append(v[i * m + j])
            self.matrizes.append(lin)
    def __add__(self,other):
        result = [[0 for a in range(self.coluna)] for a in range(self.linha)]
        for i in range(self.linha):
            for j in range(self.coluna):
                result[i][j] = self.matrizes[i][j] + other.matrizes[i][j]
        return result
    def __sub__(self,other):
        result = [[0 for a in range(self.coluna)] for a in range(self.linha)]
        for i in range(self.linha):
            for j in range(self.coluna):
                result[i][j] = self.matrizes[i][j] - other.matrizes[i][j]
        return result
    def __mul__(self,other):
        result = [[0 for a in range(other.coluna)] for a in range(self.linha)]

        for i in range(self.linha):
            for j in range(other.coluna):
                for k in range(other.linha):
                    result[i][j] += self.matrizes[i][k] * other.matrizes[k][j]
        return result
    def __repr__(self):
        return str(self.matrizes)

input = str(input())
add = False
cont = 0
X = ""
Z = ""
C = ""
for i in input:
    if i == "(": add= True
    if i == ")"and cont==0:
        add= False
        cont +=1
        X+= i
    elif i == ")" and cont==1:
        C+=i
        add= False

    if add and cont==0:
        X+= i
    elif add and cont==1:
        C+= i
    elif(i!=")"): Z+= i
n1 = eval(X)
n2 = eval(C)
a = Matriz(n1[0],n1[1],n1[2])
b = Matriz(n2[0],n2[1],n2[2])
if Z=="+":
    print(a+b)
if Z=="-":
    print(a-b)
if Z=="*":
    print(a*b)
