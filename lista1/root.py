class exercise:
    def __init__(self, f, df, x0: float, tol: float):
        self.f = f
        self.df = df
        self.x0 = x0
        self.tol = tol

    def get_root(self) -> float:
        '''
        Get a root of a given function

        args:
        -------------------------------------
        f <- function\n
        df <- derivative of f\n
        x0 <- inicial guess\n
        tol <- error tolerance\n

        '''
        f = self.f
        df = self.df
        x0 = self.x0
        tol = self.tol
        if abs(f(x0)) < tol:
            return x0

        else:
            self.x0 = x0 - f(x0)/df(x0)
            return exercise.get_root(self)


x0 = 18729729872981
tol = 1e-10
f = lambda x: x -2
df = lambda x: 1
print(
    exercise(f, df, x0, tol).get_root()
)

##