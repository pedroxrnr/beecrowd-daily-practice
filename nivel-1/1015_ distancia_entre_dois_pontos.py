# beecrowd 1015 -  Distância Entre Dois Pontos

X1, Y1 = map(float, input().split())
X2, Y2 = map(float, input().split())

calc_distancia = ((X2 - X1)**2 + (Y2 - Y1)**2)**0.5

print(f"{calc_distancia:.4f}")