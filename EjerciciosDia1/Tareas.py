class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("Tarea agregada con éxito.")

    def eliminar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print("Tarea eliminada con éxito.")
        else:
            print("La tarea no existe en la lista.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Lista de tareas pendientes:")
            for tarea in self.tareas:
                print("- " + tarea)
        else:
            print("No hay tareas pendientes.")

# Crear una instancia de la clase Tareas
lista_tareas = Tareas()

while True:
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        tarea = input("Ingrese la tarea a agregar: ")
        lista_tareas.agregar_tarea(tarea)
    elif opcion == "2":
        tarea = input("Ingrese la tarea a eliminar: ")
        lista_tareas.eliminar_tarea(tarea)
    elif opcion == "3":
        lista_tareas.mostrar_tareas()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")