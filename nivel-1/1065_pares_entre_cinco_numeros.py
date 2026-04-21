pairs_numbers = 0

for number in range(5):
    number = int(input())
    if number % 2 == 0:
        pairs_numbers += 1

print(f"{pairs_numbers} valores pares")
