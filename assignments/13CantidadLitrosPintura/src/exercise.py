def main():
    #escribe tu código abajo de esta línea
    import math
    area = float(input("Area a pintar en metros: "))
    rendimiento = float(input("Rendimiento (m2/1): "))
    l = math.ceil(rendimiento/area)
    print("Litros a comprar: ",l)

if __name__ == '__main__':
    main()
