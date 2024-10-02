import random

# Inicializa el inventario con valores aleatorios entre 0 y 20
def inicializar_inventario():
    return [[random.randint(0, 20) for _ in range(10)] for _ in range(3)]

# Función para procesar el pedido
def procesar_pedido(inventario, codigos, cantidades):
    pedido_exitoso = True

    # Verificamos si el pedido se puede cumplir
    for i in range(len(codigos)):
        linea = codigos[i] // 100   # Calculamos la línea a partir del código
        indice = codigos[i] % 10    # Calculamos el índice dentro de la línea

        # Verificamos si hay existencias suficientes
        if inventario[linea][indice] < cantidades[i]:
            pedido_exitoso = False
            break

    # Si el pedido es exitoso, actualizamos el inventario
    if pedido_exitoso:
        for i in range(len(codigos)):
            linea = codigos[i] // 100
            indice = codigos[i] % 10
            inventario[linea][indice] -= cantidades[i]  # Actualizamos el inventario

        print("Compra exitosa. Inventario actualizado:")
        for i, linea in enumerate(inventario):
            print(f"Línea {i}: {linea}")
    else:
        print("No se puede suplir el pedido. Existencias insuficientes.")

# Genera un código de modelo aleatorio (entre 0 y 299)
def generar_codigo_modelo():
    return random.randint(0, 2) * 100 + random.randint(0, 9)

# Main
def main():
    inventario = inicializar_inventario()  # Inicializa el inventario

    num_modelos = int(input("Ingrese la cantidad de modelos que desea pedir (máx 10): "))

    codigos = []
    cantidades = []

    # Leer los códigos de los modelos y las cantidades
    for i in range(num_modelos):
        codigo = generar_codigo_modelo()  # Generar código aleatorio
        print(f"El código del modelo {i + 1} es: {codigo}")
        cantidad = int(input(f"Ingrese la cantidad de piezas para el modelo {i + 1} (entre 1 y 5): "))
        codigos.append(codigo)
        cantidades.append(cantidad)

    # Procesar el pedido
    procesar_pedido(inventario, codigos, cantidades)

if __name__ == "__main__":
    main()