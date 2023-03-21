# --------->> PROGRAMA CONVERSOR MONEDA - CURSO PYTHON
# -->> VARIABLES GLOBALES
ARS = 202.91
COL = 4849.99
MEX = 18.74
nombre: str = input("Ingresar su nombre: ")

# -->> MENU DE OPCIONES
print(f"Hola {nombre} bienvenido al conversor de monedas")
print("1 - Dolares estadounidenses a pesos argentinos")
print("2 - Dolares estadounidenses a pesos colombianos")
print("3 - Dolares estadounidenses a pesos mexicanos")
opcion = int(input("Cual es la opcion que deseas: "))


# -->> FUNCION CONVERSOR MONEDA
def conversor_moneda(val: float) -> float:
    dolares = int(input("Cuantos dolares tienes: "))
    pesos = val * dolares
    return pesos


if opcion == 1:
    print(f"Tienes {conversor_moneda(ARS)} pesos argentinos.")
elif opcion == 2:
    print(f"Tienes {conversor_moneda(COL)} pesos colombianos.")
elif opcion == 3:
    print(f"Tienes {conversor_moneda(MEX)} pesos mexicanos.")
else:
    print("Ingrese una opcion correcta")
