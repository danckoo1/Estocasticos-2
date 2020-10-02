import tablero as t
from math import floor
import numpy as np
import time




class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.original_x = "D"
        self.original_y = 0
        self.col_to_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        self.num_to_col = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
        self.max = 7
    
    def ft_0(self, pos):
        self.move(*pos)
        f = []
        for i in range(64):
            if i == self.pos_to_int(pos):
                f.append(1)
            else:
                f.append(0)
        return np.array(f)

    def white(self):
        if (self.col_to_num[self.x] + self.y) % 2 != 0:
            return True
        return False

    def black(self):
        if (self.col_to_num[self.x] + self.y) % 2 != 0:
            return False
        return True

    def espacio_right(self):
        return self.max - self.col_to_num[self.x]
    def espacio_left(self):
        return self.col_to_num[self.x]
    def espacio_up(self):
        return self.max - self.y
    def espacio_down(self):
        return self.y
    
    def movimientos_disp(self):
        if self.white(): #white cell
            posiciones = []
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

        else: #black cell
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
        p, _ = self.movimientos_disp()
        return float(1/p)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def int_to_pos(self, intt):
        y = intt % 8
        x = self.num_to_col[floor(intt/8)]
        return f"{x}{str(y)}"
    
    def pos_to_int(self, pos):
        return self.col_to_num[pos[0]] * 8 + pos[1]
    
    def pos_to_list(self, pos):
        l = []
        for p in pos:
            l.append(self.pos_to_int(p))
        return l

    def g_matrix(self): #fila i columna j
        matrix = []
        for i_1 in range(8): #A
            for i_2 in range(8): #0
                self.move(self.num_to_col[i_1], i_2)
                row = []
        
                cant, posiciones = self.movimientos_disp()
                posiciones = self.pos_to_list(posiciones)
                probabilidad = float(1/cant)

                for i in range(64):
                    if i in posiciones:
                        row.append(probabilidad)
                    else:
                        row.append(0)
                matrix.append(row)
        self.move(self.original_x, self.original_y)
        return matrix

    def g_matrix_print(self):
        matrix = []
        for i_1 in range(8): #A
            for i_2 in range(8): #0
                self.move(self.num_to_col[i_1], i_2)
                row = []
        
                cant, posiciones = self.movimientos_disp()
                posiciones = self.pos_to_list(posiciones)
                probabilidad = f"1/{cant}"
                                  
                for i in range(64):
                    if i in posiciones:
                        row.append(probabilidad)
                    else:
                        row.append(0)
                matrix.append(row)
        self.move(self.original_x, self.original_y)
        return matrix
    
def item_c(Q, resultado):
    a=0
    for r in range(len(resultado)):
        if resultado[r] != 0:
            a+= resultado[r]
            print(f"{Q.int_to_pos(r)}: {resultado[r]}")
        else:
            print(f"-------{Q.int_to_pos(r)}: {resultado[r]}")
    print(a)

def item_d(Q, resultado):
    a=0
    temp = 1
    for r in range(len(resultado)):
        if Q.int_to_pos(r) == "D0":
            temp -= resultado[r]
            print(f"{Q.int_to_pos(r)}: {resultado[r]}")
        else:
            print(f"-------{Q.int_to_pos(r)}: {resultado[r]}")
        a+= resultado[r]
    print(f"proba buscada = {temp}")
    print(a)                   

def P_ij(P, i, j):
    return P[i][j]


def Fk(mov, P, k, i, j):
    print(f"este k {k} y este {i}")
    if k == 1:
        return P_ij(P, i, j)
    else:
        suma = 0
        for r in mov[i]:
            if r != j:
                suma += P_ij(P, i, r) * Fk(mov, P, k-1, r, j)
        return suma
    


if __name__ == "__main__":

    start = time.time()
    pos_i = ("D", 0) # pos inicial
    pos_f1 = ("H", 7) # pos final
    #pos_f2 = ("A", 2) # pos final
    #pos_f3 = ("A", 0) # pos final
    #pos_f4 = ("D", 3) # pos final
    #pos_f5 = ("D", 7) # pos final
    #pos_f6 = ("G", 2) # pos final
    #pos_f7 = ("G", 0) # pos final
    #pos_f8 = ("G", 4) # pos final
    

    n = 15 # etapas
    Q = Queen(*pos_i)
    t.save_matrix(Q.g_matrix_print()) #print
    P = np.array(Q.g_matrix())
    #P_n = np.linalg.matrix_power(P, n)
    #F_0 = Q.ft_0(pos)
    #resultado = np.dot(F_0, P_n)
    #item_c(Q, resultado)
    #item_d(Q, resultado)
    mov = []
    for i in range(64):
        temp = Q.int_to_pos(i)
        Q.move(temp[0], int(temp[1]))
        _, aux = Q.movimientos_disp()
        aux = list(map(Q.pos_to_int, aux))
        mov.append(aux)
    #print(pos_f1, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f1)))
    #print(pos_f2, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f2)))
    #print(pos_f3, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f3)))
    #print(pos_f4, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f4)))
    #print(pos_f5, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f5)))
    #print(pos_f6, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f6)))
    #print(pos_f7, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f7)))
    #print(pos_f8, " :", Fk(mov, P, n, Q.pos_to_int(pos_i), Q.pos_to_int(pos_f8)))
    
    end = time.time()
    print(end - start)





