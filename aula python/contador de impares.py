import verificador_imparoupar as vr

#pedir um numero
numero = int(input("digite o numero total para a soma   "))
#listas para uso futuro
impar = []
par = []

i = 0
while i < numero:
#verificar se é impar
    new = vr.verification(i) #feito em outro arquivo, para poupar linhas de codigo e para usar em futuros trabalhos onde eu possa precisar de um verificador
#guardar numa lita
    if new == "impar":
        impar.append(i)
    elif new == "par":
        par.append(i)
    i += 1

#somar
impar_somado = sum(impar)
par_somado = sum(par)

#mostrar ao usuario o resultado
print(f"a soma dos impares são: {impar_somado}")
print(f"a soma dos pares é : {par_somado} ")