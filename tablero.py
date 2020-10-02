def print_matrix(matrix):

    # Se obtienen las dimensiones del tablero
    n = len(matrix)
    m = len(matrix[0])

    # Se generan los nuevos tableros en forma de listas de listas con los nuevos caracteres
    matrix = [map(str, x) for x in matrix]

    # Se imprimen las letras representando cada columna
    num_to_col = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
    columnas = ' ' * 5
    cols = []
    for i_1 in range(8): #A
        for i_2 in range(8): #0
            cols.append(f'{num_to_col[i_1] + str(i_2)}')

    for indice in cols:
        columnas += f'  {indice}'

    print(columnas)
    print(' ' * 4 + '┌' + '─' * (4 * m + 2) + '┐')
    # Se generan las filas del mapa rival con sus respectivas celdas
    indice = 0 
    for i_1 in range(8): #A
        for i_2 in range(8): #0
            fila = ''
            
            fila += f' {num_to_col[i_1] + str(i_2)} │'
            temp = ''
            for element in matrix[indice]:
                if element == '0':
                    temp = temp + ' ' + ' 0 '
                else:
                    temp = temp + ' ' +element

            fila += ' ' + temp + ' │'
            print(fila)
            indice += 1
    print(' ' * 4 + '└' + '─' * (4 * m + 2) + '┘')


def save_matrix(matrix):

    # Se obtienen las dimensiones del tablero
    n = len(matrix)
    m = len(matrix[0])

    # Se generan los nuevos tableros en forma de listas de listas con los nuevos caracteres
    matrix = [map(str, x) for x in matrix]

    # Se imprimen las letras representando cada columna
    num_to_col = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
    columnas = ' ' * 5
    cols = []
    for i_1 in range(8): #A
        for i_2 in range(8): #0
            cols.append(f'{num_to_col[i_1] + str(i_2)}')

    for indice in cols:
        columnas += f'  {indice}'
    
    with open("matrix.txt", "w", encoding="utf-8") as file:


        file.write(columnas+"\n")
        file.write(' ' * 4 + '┌' + '─' * (4 * m + 2) + '┐'+"\n")
        # Se generan las filas del mapa rival con sus respectivas celdas
        indice = 0 
        for i_1 in range(8): #A
            for i_2 in range(8): #0
                fila = ''

                fila += f' {num_to_col[i_1] + str(i_2)} │'
                temp = ''
                for element in matrix[indice]:
                    if element == '0':
                        temp = temp + ' ' + ' 0 '
                    else:
                        temp = temp + ' ' +element

                fila += ' ' + temp + ' │'
                file.write(fila+"\n")
                indice += 1
        file.write(' ' * 4 + '└' + '─' * (4 * m + 2) + '┘'+"\n")