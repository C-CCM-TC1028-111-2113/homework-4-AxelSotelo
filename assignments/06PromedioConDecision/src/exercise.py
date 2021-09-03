def main():
  #escribe tu código abajo de esta línea
    
    suma=0
    nm=0
    n=0
    while n >= 0:
        n=float(input("Dame un numero positivo, dame uno negativo para terminar: "))
        if n>=0:
            suma=suma+n
            nm=nm+1
        else:
            break
        
    prom=suma/nm
    print("El promedio es ", prom)
    
if __name__ == '__main__':
    main()
