# 15 Definição da tupla de intervalos
intervalos = ((8, 12), (14, 18), (19, 22))

# Cálculo da quantidade total de horas
total_horas = sum(término - início for início, término in intervalos)

# Exibindo o resultado
print("Quantidade total de horas:", total_horas)