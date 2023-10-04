import readchar
def main():
    print("El programa está en ejecución. Presiona la tecla ↑ (flecha hacia arriba) para salir.")
    while True:
        key = readchar.readkey()
        if key == readchar.key.UP:
            break
        print(f"Tecla presionada (en bruto): {key}")
if __name__ == "__main__":
    main()





