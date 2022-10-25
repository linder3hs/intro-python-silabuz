x = 10
y = 0

try:
    print("Aca se ejecutando cuando todo esta ok")
    print(x/y)
except Exception as ex:
    print("Cuando detecta un error en el try entra a except")
    print(ex)
