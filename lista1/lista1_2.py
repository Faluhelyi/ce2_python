# Igor, 180122207
class lista1_2:
    def __init__(self, n: int):
        """
        Get hyperparams
        """
        self.n = n

    def estimate_area_unit_circ(self):
        """
        function to estimate the area of an unit circle by Monte Carlo
        using random.uniform(-1, 1)
        """
        import random
        num_inside = 0
        for i in range(self.n):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                num_inside = num_inside + 1
        return 4*(num_inside/self.n)
    
    def estimate_area_unit_circ2(self):
        """
        function to estimate the area of an unit circle by Monte Carlo
        using random.randint(-1 ,1)
        """
        import random
        num_inside = 0
        for i in range(self.n):
            x =  random.randint(-1 ,1)
            y =  random.randint(-1 ,1)
            if x**2 + y**2 <= 1:
                num_inside = num_inside + 1
        return 4*(num_inside/self.n)
    

import numpy as np

print("------------------------------ solucao algoritmo 1 ------------------------------")
r11 = lista1_2(1_000).estimate_area_unit_circ()
r12 = lista1_2(500_000).estimate_area_unit_circ()
print(f"Estimativa da area do circulo unitario por Monte Carlo: \n1_000 repeticoes: Area ~= {r11},\
      Abs. error ~={abs(r11-np.pi)} \n500_000 repeticoes: Area ~= {r12},\
      Abs. error ~={abs(r12-np.pi)}")
print("------------------------------ solucao algoritmo 2 ------------------------------")
r11 = lista1_2(n= 1_000).estimate_area_unit_circ2()
r12 = lista1_2(n= 500_000).estimate_area_unit_circ2()
print(f"Estimativa da area do circulo unitario por Monte Carlo: \n1_000 repeticoes: Area ~= {r11},\
      Abs. error ~={abs(r11-np.pi)} \n500_000 repeticoes: Area ~= {r12},\
      Abs. error ~={abs(r12-np.pi)}")

