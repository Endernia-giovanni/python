import random
senha = ""
caracteres = "qwrtyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
i = 1

while i > 0:
    for digito in range(8):
        aleatorio = random.choice(caracteres)
        senha += aleatorio
    print(senha)
    senha = ""