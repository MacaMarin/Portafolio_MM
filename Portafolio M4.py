# ==================================================================================================================
# EVALUACION DE PORTAFOLIO - MODULO 3
# ==================================================================================================================

# Liberia para el requerimiento 6
import math

# ------------------------------------------------------------------------------------------------------------------
# REQUERIMIENTO 1:
# Crear un programa que implemente variables, operadores y estructuras básicas del lenguaje Python.
# ------------------------------------------------------------------------------------------------------------------

# Dado que trabajan con un Indice de Conversion Europea, podemos reflejar la conversion de Kilos a Libras
def conversor_produccion():
    print(" Conversor de pesos: kilos a libras ===")
    print("En el área de pavos, a veces se vuelve interesante convertir los pesos de los pavos de kilos a libras para reportes.")
    
    # Solicitar al usuario que ingrese los kilos
    kilos = float(input("Ingrese el peso en kilos: "))
    # Conversión: 1 kilo ≈ 2.20462 libras
    libras = kilos * 2.20462
    # Mostrar el resultado
    print(f"{kilos:.2f} kg equivalen a {libras:.2f} libras")




# ------------------------------------------------------------------------------------------------------------------
# REQUERIMIENTO 2:
# Distinguir los tipos de datos y sentencias básicas del lenguaje
# ------------------------------------------------------------------------------------------------------------------
def formulario_registro_pavos():
    print("Registro de pesos")
    
    # Solicitar datos al usuario:
    fecha = input("Fecha del registro (AAAA-MM-DD): ")         
    nombre_colaborador = input("Nombre del colaborador: ")    
    area = input("Área (Crianza/Engorda): ")                  
    galpon = input("Galpón: ")                                
    edad_pavo = int(input("Edad del pavo en semanas: "))      
    peso_pavo = float(input("Peso del pavo en kg: "))         
    
    # Mostrar los datos ingresados
    print("\nDatos ingresados:")
    print(f"Fecha: {fecha}")
    print(f"Colaborador: {nombre_colaborador}")
    print(f"Área: {area}")
    print(f"Galpón: {galpon}")
    print(f"Edad del pavo: {edad_pavo} semanas")
    print(f"Peso del pavo: {peso_pavo} kg")




# ------------------------------------------------------------------------------------------------------------------
# REQUERIMIENTO 3:
# Utilizar sentencias condicionales para el control del flujo
# ------------------------------------------------------------------------------------------------------------------

# En mi portafolio se considera la temperatura como un factor que afecta al resultado
def control_temperatura_galpon():
    print("Control de temperatura en galpón")
    # El usuario debera ingresar las temperaturas
    temp_min = float(input("Ingresa la temperatura mínima registrada (°C): "))
    temp_max = float(input("Ingresa la temperatura máxima registrada (°C): "))
    # Calcular la diferencia
    diferencia = temp_max - temp_min

    # Condicionales
    if diferencia > 5:
        print("Diferencia de temperatura alta! Se recomienda regular la temperatura con calefacción")
    else:
        print("Diferencia de temperatura normal")
    # Mostrar la diferencia
    print(f"Diferencia registrada: {diferencia:.2f}°C")




# ------------------------------------------------------------------------------------------------------------------
# REQUERIMIENTO 4 :
# Usar while y for en conjunto
# ------------------------------------------------------------------------------------------------------------------

def registro_y_analisis_pesos():
    print("Registro y análisis de pesos de pavos")
    # Creamos una lista para almacenar los pesos
    registros = []  
    
    # Usamos WHILE para ingresar los pesos 
    continuar = "s"
    while continuar.lower() == "s":
        peso = float(input("Ingresa el peso del pavo (kg): "))
        registros.append(peso)
        continuar = input("¿Deseas ingresar otro pavo? (s/n): ")
    
    # Usamos FOR para recorrer los registros y mostrar cada peso
    print("\nPesos ingresados:")
    for i, peso in enumerate(registros, start=1):
        print(f"Pavo {i}: {peso} kg")
    
    # Calcular promedio
    if registros:
        promedio = sum(registros) / len(registros)
        print(f"El promedio de peso de los pavos es: {promedio:.2f} kg")
    else:
        print("No se ingresaron datos.")




# ------------------------------------------------------------------------------------------------------------------
# REQUERIMIENTO 5:
# Utilizar estructuras de datos apropiadas (listas, diccionarios, tuplas)
# ------------------------------------------------------------------------------------------------------------------

# Registro de galpones, responsables y cantidad de pavos

def registro_galpones():
    print("Registro de galpones")
    # Diccionario para almacenar datos
    galpones = {}  
    
    while True:
        nombre_galpon = input("Nombre del galpón (o 'salir' para terminar): ")
        if nombre_galpon.lower() == "salir":
            break
        
        #Informacion que ingresa el usuario
        estado = input("Estado del galpón (activo/liquidado): ").lower()
        jefe_sector = input("Nombre del jefe de sector: ")
        cantidad_pavos = int(input("Cantidad de pavos en el galpón: "))
        
        # Guardar en diccionario 
        galpones[nombre_galpon] = {
            "estado": estado,
            "jefe_sector": jefe_sector,
            "cantidad_pavos": cantidad_pavos
        }
    
    # Mostrar datos
    print("Galpones registrados")
    for galpon, info in galpones.items():
        print(f"{galpon}: Estado={info['estado'].capitalize()}, jefe_sector={info['jefe_sector']}, Cantidad de pavos={info['cantidad_pavos']}")




def funciones_pavos():
    print("Funciones para análisis de datos de pavos")

    # Función para calcular promedio de pesos de pavos
    def promedio_pesos(lista_pesos):
        return sum(lista_pesos) / len(lista_pesos) if lista_pesos else 0

    # Función para calcular diferencia de temperatura en galpón
    def diferencia_temperatura(temp_min, temp_max):
        return abs(temp_max - temp_min)

    # Función para calcular densidad de pavos por galpón (pavos/m²)
    def densidad_pavos(cantidad_pavos, area_m2):
        if area_m2 > 0:
            return cantidad_pavos / area_m2
        return 0

# Ingreso de datos por el usuario:

    # Pesos de los pavos
    pesos = []
    n_pesos = int(input("¿Cuántos pavos deseas registrar? "))
    for i in range(n_pesos):
        peso = float(input(f"Ingrese el peso del pavo {i+1} (kg): "))
        pesos.append(peso)

    # Temperaturas del galpón
    temp_min = float(input("Ingresa la temperatura mínima del galpón (°C): "))
    temp_max = float(input("Ingresa la temperatura máxima del galpón (°C): "))

    # Cantidad de pavos y área del galpón
    pavos_galpon = int(input("Ingresa la cantidad de pavos en el galpón: "))
    area_galpon = float(input("Ingresa el área del galpón en m²: "))

    # Resultados
    print(f"\nPromedio de pesos: {promedio_pesos(pesos):.2f} kg")
    print(f"Diferencia de temperatura: {diferencia_temperatura(temp_min, temp_max)} °C")
    print(f"Densidad de pavos por m²: {densidad_pavos(pavos_galpon, area_galpon):.2f} pavos/m²")





# ------------------------------------------------------------------------------------------------------------------
# Menú principal para elegir ejercicio
# ------------------------------------------------------------------------------------------------------------------
def menu():
    while True:
        print("\n=== Portafolio Python: Área Pavos ===")
        print("1. Conversor de pesos (Variables y operadores)")
        print("2. Formulario de registro de pavos (Tipos de datos)")
        print("3. Control de temperatura (Condicionales)")
        print("4. Registro y análisis de pesos (While + For)")
        print("5. Registro de galpones (Estructuras de datos)")
        print("6. Funciones de análisis de datos (Funciones)")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            conversor_produccion()
        elif opcion == "2":
            formulario_registro_pavos()
        elif opcion == "3":
            control_temperatura_galpon()
        elif opcion == "4":
            registro_y_analisis_pesos()
        elif opcion == "5":
            registro_galpones()
        elif opcion == "6":
            funciones_pavos()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
