class lista1_4:
    def __init__(self, n: int):
        self.n = n
    def factorial(self) -> int:
        n = self.n
        if n < 0:
            raise Exception('parameter n must not be negative')
        if (n == 1) or (n == 0):
            return 1
        else:
            return n*lista1_4(n-1).factorial()
        
    def pascal_triangle(self):
        pass
