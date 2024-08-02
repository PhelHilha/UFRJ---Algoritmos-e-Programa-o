
class Vetor(list):
    def __init__(self, numeros):
        super().__init__(self.filtro(numeros))
    def filtro(self,numeros):
        result = []
        for item in numeros:
            if isinstance(item, int) and item > 0:
                result.append(item)
            elif isinstance(item, float) and item > 0:
                result.append(int(item))
            elif isinstance(item, str) and item.isdigit() and int(item) > 0:
                result.append(int(item))
        return list(set(result))
    def mdc(self):
        if len(self) < 2:
            return ()
        mdcs = set()
        divisores = []
        for i in range(self[0]):

            if (self[0]%(i+1) == 0):
                mdcs.add(i+1)
        for i in self[1:]:
            for j in range(i):
                if (i%(j+1) == 0):
                    divisores.append(j+1)
        mdcs = mdcs.intersection(divisores)
        mdcs = tuple(mdcs)
        return mdcs
entrada = eval(input())
a = Vetor((entrada))
print(a.mdc())