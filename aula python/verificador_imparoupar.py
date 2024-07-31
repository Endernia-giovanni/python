'''
verificar se um numero é impar ou par
'''
impar = "impar"
par = "par"

def verification(number):
    verificado = number % 2
    if verificado == 1:
        return  impar
    elif verificado == 0:
        return par