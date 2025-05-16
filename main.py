"""
Método de Newton-Raphson para encontrar raíces de funciones no lineales.
Autor: [isidro vega]
Proyecto Final - Métodos Numéricos
"""
def newton_raphson(x0, tol, max_iter):
    def f(x):
        return x ** 3 - 2 * x - 5

    def df(x):
        return 3 * x ** 2 - 2

    print("{:<10} {:<15} {:<15}".format("Iteración", "Xi", "f(Xi)"))
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print("Derivada cero. No se puede continuar.")
            return None
        x1 = x0 - fx / dfx
        print(f"{i + 1:<10} {x1:<15.6f} {f(x1):<15.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("No se encontró la raíz en el número máximo de iteraciones.")
    return None


if __name__ == "__main__":
    x0 = float(input("Introduce una estimación inicial: "))
    tol = float(input("Introduce la tolerancia: "))
    max_iter = int(input("Introduce el número máximo de iteraciones: "))
    raiz = newton_raphson(x0, tol, max_iter)
    if raiz is not None:
        print(f"\nRaíz aproximada encontrada: {raiz:.6f}")
    else:
        print("\nNo se encontró la raíz.")

    input("\nPresiona Enter para salir...")
