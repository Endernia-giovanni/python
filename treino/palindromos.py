print('vamos verificar se algumas palavras sao  palíndromo?')
palavra_input = input("digite uma palavra aqui: ") 
palavra_verificada = palavra_input[::-1] # inverte a ordem da palavra q pedi

if palavra_verificada == palavra_input:
    print("essa palavra é um  palíndromo :)")
else:
    print("essa palavra não é um  palíndromo :(")
    print("essa palavra fica assim de traz pra frente")
    print(palavra_input[::-1])
