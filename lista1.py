class lista1:
    def __init__(self, x0: float = None, tol: float = None):
        """
        Get the hyperparams
        """
        self.x0 = x0
        self.tol = tol

    def get_root(self, f, df) -> float:
        '''
        Get a root of a given function

        args:
        -------------------------------------
        f <- function\n
        df <- derivative of f\n
        x0 <- inicial guess\n
        tol <- error tolerance\n

        '''
        if (self.x0 == None) | (self.tol ==None):
            return None
 
        x0 = self.x0
        tol = self.tol
        if abs(f(x0)) < tol:
            return x0

        else:
            self.x0 = x0 - f(x0)/df(x0)
            x0 = self.x0
            return lista1.get_root(self, f, df)


print(lista1().get_root(lambda x: x -2, lambda x: 1))



