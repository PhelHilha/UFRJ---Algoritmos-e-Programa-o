class NumeroDecimal:

    def __init__(self, v):
        self.number = v
        self.frente = ""
        self.tras = ""
        pos = True
        for i in v:
            if i == ".": pos = False
            if pos: self.frente+= i
            elif(i != "."):
                self.tras+= i
        self.tam = len(self.tras)



    def __add__(self,other):
        max = 0
        add = ""
        new = ""
        tempself = self.tras
        tempother = other.tras
        if(self.tam > other.tam):
            max = self.tam
            for i in range(self.tam - other.tam):
                tempother += "0"
        elif(self.tam < other.tam):
            max = other.tam
            for i in range(other.tam - self.tam):
                tempself += "0"
         
        if self.frente[0] == "-":
            if int(tempother) > int(tempself):
                self.frente = int(self.frente) + 1
                tempself = "1" + tempself
                newtras = (-int(tempself) + int(tempother)) * -1
                newfrente = int(self.frente) + int(other.frente)
                return (str(str(newfrente) + "." + str(newtras)))
        else:
            newtras = int(tempself) + int(tempother)
            newtras = str(newtras)
            new = newtras[:(len(newtras) - max)]
            newtras = newtras[(len(newtras) - max):]

            newfrente = int(self.frente) + int(other.frente) + int(new)
            return (str(str(newfrente) + "." + newtras))
    def __sub__(self,other):
        new = ""
        orig = 0
        tempself = self.tras
        tempother = other.tras
        if (self.tam > other.tam):
            orig = self.tam
            for i in range(self.tam - other.tam):
                tempother += "0"
        elif (self.tam < other.tam):
            orig = other.tam
            for i in range(other.tam - self.tam):
                tempself += "0"
        newtras = int(tempself) - int(tempother)
        newtras = str(newtras)
        for i in range(orig-len(newtras)):
            newtras = "0" + newtras
        newfrente = int(self.frente) - int(other.frente)
        return (str(str(newfrente) + "." + newtras))
    def __repr__(self):
        return self.number

entrada = str(input())
n1 = ""
sinal = ""
n2 = ""
pos = 0
for a,i in enumerate(entrada):
    if i == "+" or i == "-":
        if a==0:
            n1+= i
        else:
            pos+= 1
    if pos == 0 and i != "-":
        
        n1+= i
    elif pos > 1:
        n2 += i
    elif pos == 1:
        sinal += i
        pos += 1
a = NumeroDecimal(n1)
b = NumeroDecimal(n2)
if sinal == "+": print(a+b)
else : print (a-b)
