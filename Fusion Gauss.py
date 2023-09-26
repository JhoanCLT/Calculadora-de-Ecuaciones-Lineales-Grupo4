#OFICIAL HASTA AHORA 4AM
from numpy import *
import numpy as np

def metodo_gauss(matriz, vector):
    try:
        dimension = len(matriz)-1
        #dimension= 1
        col = 0
        for j in range(0, dimension):#se repite por num de ecuaciones
            f = 0
            print('')
            print('     Columna:  ', col+1)
            for i in range(0, dimension-j):
            # L(colum act), fil(fila act)
                num1 = matriz[dimension-1-f, 0+col]
                num2 = matriz[dimension-f, 0+col]
                #print(num1, num2)
                fila1 = matriz[dimension-1-f]*num2
                fila2 = matriz[dimension-f]*num1
                fila_corregida = fila2-fila1
                fila1_v=vector[dimension-1-f]*num2
                fila2_v=vector[dimension-f]*num1
                # matriz[dimension-2-fil]=fila1
                vector[dimension-f] = (fila2_v-fila1_v)
                matriz[dimension-f] = fila_corregida
                # print(i)
                # print(fila1,fila2,fila2-fila1)
                print('Matriz:  ')
                print(matriz)
                print('Vector:  ')
                print(vector)
                if col == dimension-1 and f == 0:
                    break
                #print('el fil:   ', fil)
                f += 1
            col += 1
    except Exception as e:
        #return None
        return ''
def solucion(matriz,vector):
    try:    
        C = (matriz**-1)*vector
        print('')
        print('Resultado de las variables:  ')
        print((C))
    except Exception as e:
        #return None
        return ''

    

def main():
    print('--------------SISTEMA DE ECUACIONES POR METODO GAUSS JORDAN-----------------')
#Datos de Ingreso
    incognits = int(input('Ingrese el numero de incognitas: '))
    ecuaciones= int(input('Ingrese el numero de Ecuaciones del Sistema: '))
#Establecer dimensiones de cada matriz
    A=np.empty((ecuaciones,incognits))
    B=np.empty((ecuaciones,1))
    print()
# Lee valores de Matriz
    print(f'                   Ingrese la Matriz {ecuaciones}x{incognits}:')

# Lee la matriz principal
    for i in range(ecuaciones):
        print('ECUACION', i+1)
        for j in range(incognits):
            dato=float(input("Valor A["+str(i+1)+"]["+str(j+1)+"]: "))
            A[i][j]=dato

# Lee resultados de la Matriz
#B = list(map(float, input('Ingrese los resultados de cada FILA separada con ESPACIOS: ').split()))
    print()
    print('Ingrese los resultados de cada fila')
    for i in range(ecuaciones):
        for j in range(1):
            dato=float(input("Resultado de fila ["+str(i+1)+"]: "))
            B[i][j]=dato

# Mostrar la Matriz y Vectores creados
    print('\nComprueba si el sistema es correcto:\n')
    print('MATRIZ PRINCIPAL:')
    for i in range(ecuaciones):
        for j in range(incognits):
            print(A[i][j], end="  ")
        print()
    
    print('RESULTADOS DE CADA ECUACION:   ')
    for i in range(ecuaciones):
        for j in range(1):
            print(B[i][j], end="  ")
        print()

    # Validar los valores de la Matriz
    reset = input('\nPon (Y) para YES o (N) para NO. (YES is default): ').lower()
    if reset == 'n':
        print(), main()
    else:
        if incognits > ecuaciones:
            print()
            print('EL SISTEMA DE ECUACIONES TIENE SOLUCIONES INFINITAS ')
        else:
            A=matrix(A)
            B=matrix(B)
            metodo_gauss(A, B)
            solucion(A,B)
            if np.any(A[:, incognits-1] == 0) and np.any(B[:, 0] != 0):
                print("Sistema sin solución")
            if np.any(A[:,:] == 0) and np.any(B[:, 0] == 0):
                print('hay filas de ceros')
main()