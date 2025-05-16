
"""
Método de Newton-Raphson para encontrar raíces de funciones no lineales.
Autor: [Tu Nombre]
Proyecto Final - Métodos Numéricos
"""

# Definición de la función original f(x)
def f(x):
    return x**3 - 2*x - 5

# Definición de la derivada de la función f'(x)
def df(x):
    return 3*x**2 - 2

# Implementación del método de Newton-Raphson
def newton_raphson(x0, tolerancia, max_iter):
    print("Iteración\tXi\t\tf(Xi)")
    for i in range(max_iter):
        fxi = f(x0)
        dfxi = df(x0)

        if dfxi == 0:
            print("Error: Derivada igual a cero. Método falla.")
            return None

        # Cálculo del siguiente valor de x usando la fórmula de Newton-Raphson
        x1 = x0 - fxi / dfxi

        # Muestra resultados paso a paso
        print(f"{i + 1}\t\t{x1:.6f}\t{fxi:.6f}")

        # Verifica si se alcanzó la tolerancia
        if abs(x1 - x0) < tolerancia:
            print("\nRaíz aproximada encontrada:", round(x1, 6))
            return x1

        x0 = x1

    print("\nNo se encontró la raíz con la tolerancia y número de iteraciones dados.")
    return None

# Función principal
if __name__ == "__main__":
    print("Método de Newton-Raphson\n")
    try:
        # Solicita datos de entrada al usuario
        x0 = float(input("Ingrese la estimación inicial (x0): "))
        tolerancia = float(input("Ingrese la tolerancia (por ejemplo, 0.0001): "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))

        # Llama a la función con los datos ingresados
        newton_raphson(x0, tolerancia, max_iter)

    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar valores numéricos.")
