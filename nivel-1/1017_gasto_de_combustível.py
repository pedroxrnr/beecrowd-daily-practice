# beecrowd 1017 - Gasto de Combustível

tempo_gasto = float(input())
velocida_media = float(input())

calc_litros = (tempo_gasto * velocida_media) / 12

print(f"{calc_litros:.3f}")
