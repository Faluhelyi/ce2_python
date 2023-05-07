class lista1_3:
    def __init__(self, n: int):
        self.n = n
    def factorial(self):
        n = self.n
        if n < 0:
            raise Exception('parameter n must not be negative')
        if (n == 1) or (n == 0):
            return 1
        else:
            return n*lista1_3(n-1).factorial()
        
    def pascal_triangle(self):
        n = self.n
        linha = 0
        pos = 0
        triangle_lines = {}
        while linha <= n:
            l = [None]*(linha+1)
            for pos in range(len(l)):
                # nCr = n!/((n-r)!*r!)
                l[pos] = lista1_3(linha).factorial()/(lista1_3(linha-pos).factorial()*lista1_3(pos).factorial())
            triangle_lines[linha] = l
            linha = linha +1

        return triangle_lines[n]
            

print(lista1_3(10).pascal_triangle())
