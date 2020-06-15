import random
lit = []
for i in range(6):
    b = random.randint(0,10)
    if b<4:
        num1 = random.randint(65,91)
        lit.append(chr(num1))
    else:
        num2 = random.randint(0,10)
        lit.append(str(num2))
s = "".join(lit)
print(s)
