from textos import documentacion # Importa el diccionario desde textos.py

# Menu interactivo
while True:
    print("\nMenú de Documentación")
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia")
    print("3. Estructura por tabla")
    print("4. Escalas de medición")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Salir")
    
# El usuario selecciona una opción
    opcion = input("Seleccioná una opción (1-6): ")
    # Analiza la opción y realiza la acción correspondiente
    if opcion in documentacion:
        print("\n" + documentacion[opcion])
        if opcion == "6":
            break
    else:
        print("Opción inválida. Por favor, elegí un número del 1 al 6.")
