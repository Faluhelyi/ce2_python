class lista1_1:
    def __init__(self, x0: float, tol: float = None, epsilon: float = None, delta: float = None):
        """
        Get hyperparams
        """
        self.x0 = x0
        self.tol = tol
        self.epsilon = epsilon
        self.delta = delta

    def get_root(self, f, df) -> float:
        '''
        Get a root of a given function by Newthon-Raphson method

        args:
        -------------------------------------
        f <- function\n
        df <- derivative of f\n
        x0 <- inicial guess\n
        tol <- error tolerance for |f(x)-0|\n
        '''
        x0 = self.x0
        tol = self.tol
        if abs(f(x0)) < tol:
            return x0

        else:
            self.x0 = x0 - (f(x0)/df(x0)) if df(x0) != 0 else None
            x0 = self.x0
            return lista1_1.get_root(self, f, df) if x0 != None else None
        
    def get_root2(self, f, df):
        '''
        Get a root of a given function by Newthon-Raphson method

        args:
        -------------------------------------
        f <- function\n
        df <- derivative of f\n
        x0 <- inicial guess\n
        epsilon <- error tolerance for |x-x0|\n
        delta <- error tolerance for |f(x)-f(x0)|\n
        '''
        x0 = self.x0
        epsilon = self.epsilon
        delta = self.delta
        x = x0 - (f(x0)/df(x0)) if df(x0) != 0 else None
        if x == None:
            return x
        else:
            c = 0
            while not (abs(x - x0)<delta) | (abs(f(x) - f(x0))<epsilon):
                x0 = x
                x = x0 - (f(x0)/df(x0)) if df(x0) != 0 else None
                if x ==None:
                    break
                c = c+1
                if c ==50:
                    break
                
            return x
        
print("------------- solucao algoritmo 1 (sqrt(2)) ---------------------------------------")
############################################
## sqrt(2) pelo metodo de Newthon-Raphson ##
############################################
r11 = lista1_1(x0= 1, tol= 1e-3).get_root(f = lambda x: (x**2) -2, df= lambda x: 2*x)
r12 = lista1_1(x0= 1, tol= 1e-10).get_root(f = lambda x: (x**2) -2, df= lambda x: 2*x)

print(f"sqrt(2) por Newthon-Raphson (tol = 1e-3):\n x0 = 1: sqrt(2)~={round(r11, 9)}")
print(f"sqrt(2) por Newthon-Raphson (tol = 1e-10):\n x0 = 1: sqrt(2)~={round(r12, 9)}")

print("------------- solucao algoritmo 1 (Roots) ---------------------------------------")
###############################################################
## Raizes de f(x) = (x**2) - 9 pelo metodo de Newton-Raphson ##
###############################################################
r21 = lista1_1(x0= -4, tol= 1e-3).get_root(f = lambda x: (x**2) -9, df= lambda x: 2*x)
r22 = lista1_1(x0= 0, tol= 1e-3).get_root(f = lambda x: (x**2) -9, df= lambda x: 2*x)
r23 = lista1_1(x0= 4, tol= 1e-3).get_root(f = lambda x: (x**2) -9, df= lambda x: 2*x)

r24 = lista1_1(x0= -4, tol= 1e-10).get_root(f = lambda x: (x**2) -9, df= lambda x: 2*x)
r25 = lista1_1(x0= 0, tol= 1e-10).get_root(f = lambda x: (x**2) -9, df= lambda x: 2*x)
r26 = lista1_1(x0= 4, tol= 1e-10).get_root(f = lambda x: (x**2) -9, df= lambda x: 2*x)

print(f"Raizes pelo metodo de Newton-Raphson (tol = 1e-3):\n x0 = -4: root_1 ~={r21}\n x0 = 0: root = {r22}\n x0 = 4: root_2 ~={r23}")
print(f"Raizes pelo metodo de Newton-Raphson (tol = 1e-10):\n x0 = -4: root_1 ~={r24}\n x0 = 0: root = {r25}\n x0 = 4: root_2 ~={r26}")


print("------------- solucao algoritmo 2 (sqrt(2)) ---------------------------------------")
############################################
## sqrt(2) pelo metodo de Newthon-Raphson ##
############################################
r11 = lista1_1(x0= 1, epsilon= 1e-3, delta = 1e-3).get_root2(f = lambda x: (x**2) -2, df= lambda x: 2*x)


print(f"sqrt(2) por Newthon-Raphson (epsilon = delta = 1e-3):\n x0 = 1: sqrt(2)~={round(r11, 9)}")

print("------------- solucao algoritmo 2 (Roots) ---------------------------------------")
###############################################################
## Raizes de f(x) = (x**2) - 9 pelo metodo de Newton-Raphson ##
###############################################################
r21 = lista1_1(x0= -4, epsilon= 1e-3, delta = 1e-3).get_root2(f = lambda x: (x**2) -9, df= lambda x: 2*x)
r22 = lista1_1(x0= 0, epsilon= 1e-3, delta = 1e-3).get_root2(f = lambda x: (x**2) -9, df= lambda x: 2*x)
r23 = lista1_1(x0= 4, epsilon= 1e-3, delta = 1e-3).get_root2(f = lambda x: (x**2) -9, df= lambda x: 2*x)

print(f"Raizes pelo metodo de Newton-Raphson (epsilon = delta = 1e-3):\n x0 = -4: root_1 ~={r21}\n x0 = 0: root = {r22}\n x0 = 4: root_2 ~={r23}")



