from knowledge import KnowledgeBase

def main():
    kb = KnowledgeBase()
    
    # Adquirir conocimiento del usuario
    kb.acquire_knowledge()

    # Mostrar todo el conocimiento almacenado
    print("\nConocimiento almacenado:")
    kb.display_knowledge()

if __name__ == "__main__":
    main()
