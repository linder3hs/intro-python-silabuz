# x -> Es el parametro que vamos recibir
# y despues de los : vamos a ejecutar una intruccion

# ! Para usar este lambda debemos guardarlo en una variable
# En n lambda el return es implicito es decir esta ahi

# Beneficios
# Es solo una linea
# Para instrucciones simples es mas que suficiente
# Su uso es dinamico

calcular_cubo = lambda x: x ** 3 

print(calcular_cubo(10))

calcular_area_rectangulo = lambda b, h=10 : b * h / 2

print(calcular_area_rectangulo(8, 10))
print(calcular_area_rectangulo(*[12, 14]))
