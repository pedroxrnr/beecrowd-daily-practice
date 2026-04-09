# Beecrowd 1038 - Lanche

order = input().split()
code, quantity = int(order[0]), int(order[1])
price = float()

if code == 1:
    price = 4.00
elif code == 2:
    price = 4.50
elif code == 3:
    price = 5.00
elif code == 4:
    price = 2.00
elif code == 5:
    price = 1.50

total_price = quantity * price

print(f"Total: R$ {total_price:.2f}")
