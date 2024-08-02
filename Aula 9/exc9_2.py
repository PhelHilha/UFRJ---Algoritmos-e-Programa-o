class Polinomio:

    def __init__(self, coeficientes=[]):

        "Construtor, onde a lista coeficientes contem os coeficientes para os termos de grau 0, grau 1, etc."
        self.coeficientes = coeficientes

    def __setitem__(self, grau, coeficiente):

        "Altera o coeficiente para o termo do grau dado"

        if grau < len(self.coeficientes):
            self.coeficientes[grau] = coeficiente
        else:
            for i in range(grau - len(self.coeficientes)):
                self.coeficientes.append(0)
            self.coeficientes.append(coeficiente)

    def __getitem__(self, grau):

        "Retorna o coeficiente para o grau dado"
        if grau > len(self.coeficientes):
            return 0
        else:
            return self.coeficientes[grau]

    def grau(self):

        "Retorna o grau do polinomio"
        return len(self.coeficientes)

    def __mul__(self, p):

        "Retorna o polinomio dado pela multiplicacao deste polinomio por p (tambem um polinomio)"

        result = [0] * (self.grau() + p.grau() + 1)
        for i, a in enumerate(self.coeficientes):
            for j, b in enumerate(p.coeficientes):
                result[i + j] += a * b
        return Polinomio(result)

    def __add__(self, p):

        "Retorna o polinomio dado pela soma deste polinomio com p (tambem um polinomio)"
        newpolinomio = []
        dist = max([len(self.coeficientes), len(p.coeficientes)])

        for i in range(dist):
            if (i < len(self.coeficientes) and i < len(p.coeficientes)):
                newpolinomio.append(self.coeficientes[i] + p.coeficientes[i])
            elif (i < len(self.coeficientes) and i >= len(p.coeficientes)):
                newpolinomio.append(self.coeficientes[i])
            elif (i >= len(self.coeficientes) and i < len(p.coeficientes)):
                newpolinomio.append(p.coeficientes[i])
        return Polinomio(newpolinomio)

    def __sub__(self, p):

        "retorna o polinomio dado pela diferenca entre este polinomio e p (tambem um polinomio)"
        newpolinomio = []
        dist = max([len(self.coeficientes), len(p.coeficientes)])

        for i in range(dist):
            if (i < len(self.coeficientes) and i < len(p.coeficientes)):
                newpolinomio.append(self.coeficientes[i] - p.coeficientes[i])
            elif (i < len(self.coeficientes) and i >= len(p.coeficientes)):
                newpolinomio.append(self.coeficientes[i])
            elif (i >= len(self.coeficientes) and i < len(p.coeficientes)):
                newpolinomio.append(p.coeficientes[i])
        return Polinomio(newpolinomio)

    def avalia(self, x):
        "Retorna a avaliacao do polinomio avaliado em x."
        result = 0
        for i in range(len(self.coeficientes)):
            result += self.coeficientes[i] * (x ** i)
        return result

    def derivada(self):
        "Retorna um polinomio com a sua derivada"
        result = []

        for i in range(self.grau()):
            if i == 0:
                continue
            else:
                result.append(self.coeficientes[i] * i)
        return Polinomio(result)
    def newton(self, x0, n):
        x = x0
        for i in range(n):
            try:
                x = x - (self.avalia(x)/self.derivada().avalia(x))
            except ZeroDivisionError:
                return "Abortado"
        return ((f"{self.avalia(x):.2f}",f"{x:.2f}"))

p1 = eval(input())
x0 = int(input())
n = int(input())
p = Polinomio(p1)

print(p.newton(x0,n))