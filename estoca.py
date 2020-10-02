import Aux_module as t
from math import floor
import numpy as np

class Queen:
    '''
    Entidad creada con el fin de contener la logica detras de la ficha, ademas por simplicidad
    posee algunos metodos encargados de la transformacion de posiciones a index en la matriz, 
    por ejemplo transformar A1 a 0 y viceversa.
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.original_x = "D"
        self.original_y = 0
        self.col_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.num_to_col = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
        self.max = 7 #maximo ancho y alto del tablero
    
    def ft_0(self, pos):
        '''
        construye el vector F0 que no indica en que posicion parte la queen.
        '''
        self.move(*pos)
        f = [0]*64
        f[self.pos_to_int(pos)] = 1
        return np.array(f)

    def white(self):
        '''
        Funcion utilizada para saber si las posiciones en que se encuentra la
        reina son blancas o no.
        '''
        if (self.col_to_num[self.x] + self.y) % 2 != 0:
            return True
        return False

    def black(self):
        '''
        Funcion utilizada para saber si las posiciones en que se encuentra la
        reina son negras o no.
        '''
        if (self.col_to_num[self.x] + self.y) % 2 != 0:
            return False
        return True

    def espacio_right(self):
        '''
        nos retorna la cantidad de espacios disponibles hacia la derecha desde la posicion
        actual de la reina
        '''
        return self.max - self.col_to_num[self.x]

    def espacio_left(self):
        '''
        nos retorna la cantidad de espacios disponibles hacia la izquierda desde la posicion
        actual de la reina
        '''
        return self.col_to_num[self.x]

    def espacio_up(self):
        '''
        nos retorna la cantidad de espacios disponibles hacia arriba desde la posicion
        actual de la reina
        '''
        return self.max - self.y

    def espacio_down(self):
        '''
        nos retorna la cantidad de espacios disponibles hacia abajo desde la posicion
        actual de la reina
        '''
        return self.y
    
    def movimientos_disp(self):
        '''
        Cumple dos misiones simultaneamente, calcula la cantidad de movimientos viables como un int,
        al mismo tiempo que almacena cuales son dichas posiciones viables para moverse en un listado.
        retorna mov(int), posiciones(list).
        '''
        if self.white(): #celda blanca
            posiciones = [] # posiciones viables desde la actual
            mov = 0
            for dir_h in ["l", "r"]: #[left, right]
                for dir_v in ["d", "u"]: #[down, up]
                    if dir_h == "l" and dir_v == "d":
                        if not (3 > self.espacio_left() or 2 > self.espacio_down()):
                            pos = (self.num_to_col[self.col_to_num[self.x] - 3] ,self.y - 2)
                            posiciones.append(pos)
                            mov += 1

                    if dir_h == "l" and dir_v == "u":
                        if not (3 > self.espacio_left() or 2 > self.espacio_up()):
                            pos = (self.num_to_col[self.col_to_num[self.x] - 3] ,self.y + 2)
                            posiciones.append(pos)
                            mov += 1

                    if dir_h =="r" and dir_v == "d":
                        if not (3 > self.espacio_right() or 2 > self.espacio_down()):
                            pos = (self.num_to_col[self.col_to_num[self.x] + 3] ,self.y - 2)
                            posiciones.append(pos)
                            mov += 1

                    if dir_h == "r" and dir_v == "u":
                        if not (3 > self.espacio_right() or 2 > self.espacio_up()):
                            pos = (self.num_to_col[self.col_to_num[self.x] + 3] ,self.y + 2)
                            posiciones.append(pos)
                            mov += 1

        else: #celda negra
            posiciones = []
            mov = 0
            for dist in [3, 5, 7]: #[distancias]
                for dirr in ["l", "r", "u", "d"]: #[direcciones]
                    if dirr == "d":
                        if dist <= self.espacio_down():
                            pos = (self.x ,self.y - dist)
                            posiciones.append(pos)
                            mov += 1
                    if dirr == "u":
                        if dist <= self.espacio_up():
                            pos = (self.x ,self.y + dist)
                            posiciones.append(pos)
                            mov += 1
                    if dirr == "l":
                        if dist <= self.espacio_left():
                            pos = (self.num_to_col[self.col_to_num[self.x] - dist] ,self.y)
                            posiciones.append(pos)
                            mov += 1
                    if dirr == "r":
                        if dist <= self.espacio_right():
                            pos = (self.num_to_col[self.col_to_num[self.x] + dist] ,self.y)
                            posiciones.append(pos)
                            mov += 1
        return mov, posiciones

    def proba(self):
        '''
        calcula la probabilidad de los eventos equiprobables.
        '''
        p, _ = self.movimientos_disp()
        return float(1/p)

    def move(self, x, y):
        '''
        Desplaza a la reina a una nueva posicion 
        '''
        self.x = x
        self.y = y
    
    def int_to_pos(self, intt):
        # transforma un index de la matriz a una posicion como string
        y = intt % 8
        x = self.num_to_col[floor(intt/8)]
        return f"{x}{str(y)}"
    
    def pos_to_int(self, pos):
        # transforma una posicion en formato de tupla a un index de la matriz
        return self.col_to_num[pos[0]] * 8 + pos[1]

    def g_matrix(self):
        '''
        Crea la matriz P asociada al problema en que cada entrada es un float,
        luego es esta matriz la usada para los calculos.
        '''
        matrix = []
        for i_1 in range(8): #A,...,H
            for i_2 in range(8): #0,...,7
                self.move(self.num_to_col[i_1], i_2) #movemos la matriz atraves de todo el tablero
                row = [] #instanciamos la fila
        
                cant, posiciones = self.movimientos_disp() 
                posiciones = list(map(self.pos_to_int, posiciones)) #transformamos las posiciones
                probabilidad = float(1/cant) #calculamos la probabilidad

                for i in range(64): #iteramos sobre cada columna de la fila
                    if i in posiciones:
                        row.append(probabilidad) #insertamos las probabilidades a la fila
                    else:
                        row.append(0)
                matrix.append(row)
        self.move(self.original_x, self.original_y) #devolvemos la reina a su posicion de partida
        return matrix

    def g_matrix_print(self):
        '''
        Misma logica detras del metodo anterior, pero en este caso construimos una 
        matriz en que cada una de sus probabilidades son str, a excepcion de los 0s, 
        para una mejor visualizacion al hacer prints o al guardarla.
        '''
        matrix = []
        for i_1 in range(8): #A
            for i_2 in range(8): #0
                self.move(self.num_to_col[i_1], i_2)
                row = []
        
                cant, posiciones = self.movimientos_disp()
                posiciones = list(map(self.pos_to_int, posiciones))
                probabilidad = f"1/{cant}" #esta es la modificación
                                  
                for i in range(64):
                    if i in posiciones:
                        row.append(probabilidad)
                    else:
                        row.append(0)
                matrix.append(row)
        self.move(self.original_x, self.original_y)
        return matrix                


def P_ij(P, i, j):
    # Retorna la probabilidad P_ij asociada al problema
    return P[i][j]

def Fk(mov, P, k, i, j):
    '''
    Funcion recursiva implementada para calcular la probabilidad de que la reina vaya desde i a j
    en k movimientos, visitando por primera vez el j en la etapa k. Notar que la funcion ademas 
    recibe P y mov, los cuales se entregan con el fin de optimizar el proceso.
    P es matriz precalculada con todas las probabilidades, y mov corresponde a los movimientos
    disponibles desde cada posicion del tablero, este ultimo lo utilizamos para evitar iterar sobre
    aquellas posiciones que tienen probabilidad 0, que finalmente resultarían en 0s.
    '''
    if k == 1:
        return P_ij(P, i, j)
    else:
        suma = 0
        for r in mov[i]:
            if r != j:
                suma += P_ij(P, i, r) * Fk(mov, P, k-1, r, j)
        return suma
    
def c_no_primera_vez(Q, P, n):
    '''
    Calcula las probabilidades del item c, sin contarlo como la primera visita.
    '''
    print(f"Punto de partida ({Q.x},{Q.y}) en {n}")
    P_n = np.linalg.matrix_power(P, n)
    F_0 = Q.ft_0((Q.x, Q.y))
    resultado = np.dot(F_0, P_n)
    for r in range(len(resultado)):
        if Q.int_to_pos(r) == "H7":
            print(f"{Q.int_to_pos(r)}: {resultado[r]}")

def d(Q, P, n):
    '''
    Calcula la probabilidades del item d
    '''
    print(f"Punto de partida ({Q.x},{Q.y}) en {n}")
    P_n = np.linalg.matrix_power(P, n)
    F_0 = Q.ft_0((Q.x, Q.y))
    resultado = np.dot(F_0, P_n)
    temp = 1
    for r in range(len(resultado)):
        if Q.int_to_pos(r) == "D0":
            temp -= resultado[r]
            print(f"{Q.int_to_pos(r)}: {resultado[r]}")
    print(f"Proba de no estar en D0 tras {n} movimientos = {temp}")                  

def c_primera_vez(mov, P, n, pos_i, pos_f):
    '''
    Calcula las probabilidades del item c, contandolo como la primera visita.
    '''
    print(f"punto de partida {pos_i}, punto de llegada {pos_f} por primera vez en {n} etapas")
    print(pos_f, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f)))

def precompile_movs(Q):
    '''
    pre calcula los movimientos viables partiendo desde todas las posiciones del tablero,
    para ahorrar ramificaciones nulas en la recursión.
    '''
    mov = []
    for i in range(64):
        temp = Q.int_to_pos(i)
        Q.move(temp[0], int(temp[1]))
        _, aux = Q.movimientos_disp()
        aux = list(map(Q.pos_to_int, aux))
        mov.append(aux)
    return mov

if __name__ == "__main__":
    '''
    parametros iniciales, solo debes ajustar el n para las preguntas.
    '''
    pos_i = ("D", 0) # pos inicial
    Q = Queen(*pos_i) # instanciamos la reina
    n = 5 # Recordar ajustar este n cada vez que se pruebe el codigo
    
    P = np.array(Q.g_matrix()) # generamos P
    Q.move(*pos_i) # para asegurar que la posicion inicial sea correcta

    pos_f = ("H", 7) # pos final
    
    '''
    Para realizar una de las siguientes acciones debes descomentar solo aquellas que poseen
    los mismos numeros y comentar el resto. No olvides ajustar el n si es que quieres probar
    los items c y d. Si quisieras calcular cualquier otra probabilidad en que llegue
    por primera vez al destino, tan solo basta con llamar la funcion Fk y entregarle los 
    parametros necesarios, no olvides ajustar el n y sus puntos de partida y de 
    termino para esto!.
    '''

    #t.save_matrix(Q.g_matrix_print())      #1 guarda txt con matriz
    #Q.move(*pos_i)                         #1 es necesario tras los metodos de generar la matriz para asegurar su buena ubicación

    t.print_matrix(P)                       #2 printea la matriz              

    #c_no_primera_vez(Q, P, n)              #3 calcula item c sin pensarlo como el paso por primera vez

    #mov = precompile_movs(Q)               #4 precompila los movimientos disp, es necesario para el item c por primera vez
    #c_primera_vez(mov, P, n, pos_i, pos_f) #4 item c visitando por primera vez

    #d(Q, P, n)                             #5 calcula item d 





