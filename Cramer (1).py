# Calculadora de sistemas matriciales de reglas de Cramer y teorema de Laplace
#-------------------------------------------------------------------
# Regla de Cramer | Xi = det(Ai) / det(A)
# Laplace         | Sum cof(A)i*j * A(i*j)
# Cofactor        | (-1)^i+j * det(A)i*j
#--------------------------------------------------------------------
# LAPLACE:  METODO PARA SACAR DETERMINANTE DE UNA MATRIZ
# COFACTOR: COMPLEMENTO QUE AYUDA A RESOLVER AL METODO LAPLACE
#--------------------------------------------------------------------

# ALGORITMO DE LAPLACE (para sacar determinante de una matriz)
def laplace(matrix, val=1):
    #Establecer longitud de matriz
    n = len(matrix)
    # N vale segun n de filas
    # Retorna Det si longitud de matriz es 1
    if n == 1:
        return val * matrix[0][0]
    else:
        sign = -1
        det = 0
        for i in range(n):
            mtx = []
            for j in range(1, n):
                buff = []
                for k in range(n):
                    if k != i:
                        buff.append(matrix[j][k])
                mtx.append(buff)
            sign *= -1
            #Funcion laplace
            det += val * laplace(mtx, sign * matrix[0][i])
        return det

# ALGORITMO DE CRAMER
def cramer(matrix, results, order):
    # Calcular y Mostrar Det de Matriz Principal
    # Llamar funcion laplace
    main_det = laplace(matrix)
    print(f'\nDeterminante de la matriz principal: {main_det}')

    # Construir New Matriz con Sustituciones
    if main_det != 0:
        resolution = []
        for r in range(order):
            matrix_sub = []
            for i in range(order):
                matrix_sub.append([])
                for j in range(order):
                    if j == r:
                        matrix_sub[i].append(results[i])
                    else:
                        matrix_sub[i].append(matrix[i][j])

            # Mostrar Matriz Actual con Sustitucion
            print(f'\nMatriz con reemplazo en COLUMNA {r + 1}:')
            for line in matrix_sub:
                for val in line:
                    print(f'{val:^8}', end=' ')
                print()

            # Calcula Det con Sustitucion
            # Llamar funcion laplace
            sub_det = laplace(matrix_sub)
            print(f'Determinante de esta matriz: {sub_det}')

            # Calcula y Guarda Solucion Final
            resolution.append(sub_det / main_det)

    # Devuelve Solucion para Mostrar en Pantalla
        return resolution

    # Display Resolution if Main Det is 0
    # Mostrar solucion si la Det principal es 0
    else:
        return 0
#-----------------------------INICIO DE CALCULO POR METODO CRAMER------------------------------

#FUNCION PRINCIPAL
def main():
    print('--------------SISTEMA DE ECUACIONES CON METODO CRAMER-----------------------------')
    order = int(input('Ingrese el numero de incognitas: '))

    # Lee valores de Matriz
    print(f'Ingres la Matriz {order}x{order} separada con ESPACIOS (para columnas) y ENTERS (para lineas):')
    matrix = [list(map(float, input().split())) for i in range(order)]

    # Lee resultados de la Matriz
    results = list(map(float, input('Ingrese los resultados de cada FILA separada con ESPACIOS: ').split()))

    # Mostrar la Matriz creada
    print('\nComprueba si el sistema es correcto:\n')
    for l, line in enumerate(matrix):
        for val in line:
            print(f'{val:^8}', end=' ')
        print(f'= {results[l]:^8}', end='\n')

    # Validar los valores de la Matriz
    reset = input('\nPon (Y) para YES o (N) para NO. (YES is default): ').lower()
    if reset == 'n':
        print(), main()
    else:
        # Mostrar Resultados Finales
        # Llamar funcion Cramer
        resolution = cramer(matrix, results, order)
        if resolution != 0:
            print('\nSoluciones:')
            for r in range(order):
                print(f'A{r + 1} = {resolution[r]}')
        else:
            print('\nImpossible terminar el algoritmo.\nEl determinante de la matriz principal es IGUAL a 0.')


main()
