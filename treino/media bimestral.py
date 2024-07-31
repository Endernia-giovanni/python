num1 = (int(input("escreva sua nota do 1° bimestre    ")))
num2 = (int(input("escreva sua nota do 2° bimestre    ")))
num3 = (int(input("escreva sua nota do 3° bimestre    ")))
num4 = (int(input("escreva sua nota do 4° bimestre    ")))

sum = num1 + num2 + num3 + num4
div = sum/4
total = 100 - sum
print(f"sua media é {div}")
print(f"seu resutado total é {total}")