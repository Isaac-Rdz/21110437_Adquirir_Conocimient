from database import create_table, add_knowledge, display_knowledge

class KnowledgeBase:
    def __init__(self):
        create_table()  # Crear la tabla al inicializar la clase

    def acquire_knowledge(self):
        """Método para adquirir conocimiento del usuario."""
        while True:
            key = input("Ingrese la clave del conocimiento (o 'salir' para terminar): ")
            if key.lower() == 'salir':
                break
            value = input("Ingrese el valor del conocimiento: ")
            add_knowledge(key, value)
            print(f"Conocimiento añadido: {key} -> {value}")

    def display_knowledge(self):
        """Mostrar todo el conocimiento almacenado."""
        
        display_knowledge()  # Llama a la función para mostrar el conocimiento
