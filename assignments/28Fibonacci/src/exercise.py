def main():
    index = int(input("Enter the index: "))
    #escribe tu código abajo de esta línea
    a=0
    b=1
    suma=0
    n=1
    while n<=index :
        n=n+1
        a=b
        b=suma
        suma=a+b
        
    print(suma)
       
if __name__ == '__main__':
    main()

