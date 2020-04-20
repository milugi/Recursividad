# Ejercicio 1

def  fibonacciI ( numero ):
    fib1  =  0
    fib2  =  1
    for  i  in  range ( 2 , numero + 1 ):
        aux  =  fib1  +  fib2
        fib1  =  fib2
        fib2  =  aux
    return  aux

def  fibonacci (num):
    if ( num == 0  or num == 1 ):
        return  num
    else:
        return  fibonacci ( num - 1 ) +  fibonacci ( num - 2 )

# Ejercicio 2
def suma (n):
        if n == 1:
            return (n)
        else:
            return (n + suma(n-1))

print (suma(4))

#Ejercicio 3

def  producto ( numero1 , numero2 ):
    if ( numero2 == 1 ):
        return  numero1
    else:
        return  numero1  +  producto ( numero1 , numero2 - 1 )
 
print (producto (8, 2))

#Ejercicio 4

def  potencia ( base , exponente ):
    if (exponente == 1 ):
        return base
    else:
        return base * potencia ( base , exponente -1 )

print (potencia(3,4)

#Ejercicio 5
def caracteres (sec):
    if ( len (sec) == 1):
        return  sec
    else:
        return sec[-1] + caracteres (sec[:-1])
print (caracteres("hola"))

#Ejercicio 6

def serie (n):
    if n == 1:
            return n
        else:
            return 1/n + (serie(n-1)) 
 
 #Ejercicio 7 

def  binario ( numero ):
    if ( numero  <=  1 ):
        return  str ( numero )
    else :
        return  binario ( numero // 2 ) +  str ( numero  %  2 )
print (binario(3))


#ejercicio 8
def  logaritmo ( base , numero ):
    if ( base  ==  numero ):
        return  1
    else :
        return  1  +  logaritmo ( base , numero / base )
#Ejercicio 9

def cantidad (num):
    if (num == 0):
        return 0
    else:
        return 1 + cantidad (num//10)

print(cantidad (454))

#Ejercicio 11
def  mcd ( n1 , n2 ):
    if  n2 == 0 :
    return  n1
    else :
        return  mcd ( n2 , n1  %  n2 )

#Ejercicio 12
def  mcm ( n , m ):
    if ( n  %  m  ==  0 ):
        return  n
    else :
        return  mcm ( n , m  *  n )

#Ejercicio 13
def  suma_dig ( n ):
    if  n < 10 :
        return  n
    else:
        return ( n % 10 ) +  suma_dig ( n // 10 )

# Ejercicio14

def  raíz ( n , x ):
    if x*x == n:
        return x
    elif x*x > n:
        return x-1
    else:
        return raiz(n,x+1)

#Ejercicio 15

def sucesion(num):
    if(num == 1):
        return 2
    else:
        return -3 * sucesion(num-1)

#Ejercicio 16

def barrido(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])
        barrido(vec[0:-1])

#Ejercicio 17

def barrido_matriz(m, i, j):
    if (i<len(m) and j<len(m[i])):
        print(m[i][j])
        if(j==len(m[i][j])):
            j+=1
            j=-1
        barrido_matriz(m,i,j+1)

#Ejercicio 18

def suc(n):
    if n==1:
        return 2
    else:
        return n+1/suc(n-1)

#Ejercicio 19
i=0
def busq_secuencial(buscado, v):
    global i
    if buscado==v[i]:
        return "El elemento se encuentra en la posicion ",i," de la lista"
    else:
        i+=1
        return busq_secuencial(buscado,v)

#Ejercicio 20
def bbin(buscado,v,pri,ult):
    if pri>ult:
        return "El elemento no se encuentra"
    med=(pri+ult)//2
    if buscado==v[med]:
        return med
    elif buscado>v[med]:
        return bbin(buscado,v,med+1,ult)
    else:
        return bbin(buscado,v,pri,med-1)


#Ejercicio 21
def contar_naves(vec):
    if(len(vec)==0):
        return 0
    else:
        if(vec[-1][2]):
            return 1 + contar_naves(vec[0:-1])
        else:
            return 0 + contar_naves(vec[0:-1])

#Ejercicio 25
def sucesion2(n):
    if n==1:
        return 3
    elif n>=2:
         sucesión de retorno ( n - 1 ) + 2 * n