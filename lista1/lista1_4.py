# Igor, 180122207

#############################################
## Calculate Pascal's triangle Recursively ##
#############################################
def pascal_triangle(n):
    """
    Produce n-th row of the Pascal's triangle
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        linha = [None]*(n+1)
        linha[0] = 1
        linha[-1] = 1
        pos = 1
        while pos < n:
            linha[pos] = pascal_triangle(n-1)[pos-1]+\
                pascal_triangle(n-1)[pos]
            pos += 1
        return linha
    
###########
## Usage ##
###########
for i in range(11):
    print(pascal_triangle(i))


