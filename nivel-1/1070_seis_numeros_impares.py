# Beecrowd 1070 - Seis Números Ímpares

num = int(input())

if num % 2 == 0:
    num += 1

for i in range(6):
    print(num + i * 2)
