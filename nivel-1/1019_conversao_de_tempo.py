# beecrowd 1019 - Coversão de Tempo

tempo = 140153

tempo_horas = (tempo // 60) //60

tempo_minutos = (tempo // 60) % 60

tempo_segundos = tempo % 60

print(f"{tempo_horas}:{tempo_minutos}:{tempo_segundos}")
