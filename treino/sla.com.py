import time as t
numb1 = 1
numb2 = numb1 +1

sequencia = [1]

print(sequencia)

while True:
    numb2 = numb1 +1
    sequencia.append(numb1)
    sequencia.append(numb2)
    sequencia.pop(numb1)
    print (sequencia)
    numb1 = numb2
    if sequencia.__len__() > 15:
        t.sleep(0.5)