def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    
    for i in range(1,height+1):
        s=height-i        
        print(" "*s+"*"*i)    
    
if __name__ == '__main__':
    main()

