import json

# Función para registrar un trabajador
def registrar_trabajador(trabajadores):
    nombre = input("Nombre y Apellido: ")
    cargo = input("Cargo: ")
    sueldo_bruto = float(input("Sueldo Bruto: "))
    
    # Calcular descuentos y sueldo líquido
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    sueldo_liquido = sueldo_bruto - (desc_salud + desc_afp)
    
    # Crear un diccionario para el trabajador
    trabajador = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "desc_salud": desc_salud,
        "desc_afp": desc_afp,
        "sueldo_liquido": sueldo_liquido
    }
    
    # Añadir trabajador a la lista
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente!")

# Función para listar todos los trabajadores
def listar_trabajadores(trabajadores):
    for trabajador in trabajadores:
        print(trabajador)

# Función para imprimir la planilla de sueldos
def imprimir_planilla(trabajadores):
    opcion = input("¿Desea imprimir todos los trabajadores o por cargo? (todos/cargo): ")
    
    if opcion == "cargo":
        cargo_especifico = input("Ingrese el cargo específico: ")
        trabajadores_filtrados = [t for t in trabajadores if t['cargo'] == cargo_especifico]
    else:
        trabajadores_filtrados = trabajadores
    
    with open('planilla_sueldos.txt', 'w') as file:
        for trabajador in trabajadores_filtrados:
            file.write(json.dumps(trabajador) + "\n")
    
    print("Planilla de sueldos impresa exitosamente!")

# Función principal del programa
def main():
    trabajadores = []
    
    while True:
        print("\nMenú:")
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_trabajador(trabajadores)
        elif opcion == "2":
            listar_trabajadores(trabajadores)
        elif opcion == "3":
            imprimir_planilla(trabajadores)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
