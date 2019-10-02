def suma(m1, m2):
    r1 = m1[0] + m2[0]
    r2 = m1[1] + m2[1]
    r = [r1, r2]
    return r

def prod(m1, m2):
    r1 = m1[0] * m2[0] - m1[1] * m2[1]
    r2 = m1[0] * m2[1] + m2[0] * m1[1]
    r = [r1, r2]
    return r

def columna(j, W):
    Z = [0]*len(W)
    k = 0
    for i in W:
        Z[k] = [i[j]]
        k = k+1
    return Z

def modul(a1, b1):
    r1 = math.sqrt(a1 ** 2 + b1 ** 2)
    r = round(r1,2)
    return [r, 0]


def fila_por_columna(V, W):
    t = [0, 0]
    for i in range(len(V)):
        t = suma(t, prod(V[i], W[i][0]))
    return t

def producto_de_matrices(A, B):
    f = len(A)
    c = len(B[0])
    C = [[0]*c for fila in range(f)]
    for i in range(f):
        for j in range(c):
            C[i][j] = fila_por_columna(A[i], columna(j, B))
    return C

def producto_tensorial(A, B):
    f_A = len(A)
    c_A = len(A[0])
    f_B = len(B)
    c_B = len(B[0])
    f_T = f_A * f_B
    c_T = c_A * c_B
    T = [[0]*c_T for fila in range(f_T)]
    for i in range(f_T):
        for j in range(c_T):
            T[i][j] = prod(A[i // f_B][j // c_B], B[i % f_B][j % c_B])
    return T

def vec(complejo):
    if "+" in complejo[1:] or "-" in complejo[1:] :
        if complejo[0] == "-":
            L = 1
            oper = complejo[1:]
        else:
            L = 0
            oper = complejo[:]
        for letra in oper:
            if letra == "+" or letra == "-":
                a1 = complejo[:L]
                b1 = complejo[L:]
                b1 = b1[1:-1]
                if b1 == '':
                    b1 = 1
                
                if letra == "-":
                    r = [round(float(a1), 2),-round(float(b1), 2)]
                else:
                    r = [round(float(a1), 2),round(float(b1), 2)]
            L += 1
            
    else:
        if "i" in complejo:
            if complejo == "i" or complejo == "-i":
                if complejo == "i":
                    r = [0, 1]
                else:
                    r = [0,-1]
            else:
                r = [0, round(float(complejo[:-1]), 2)]
        else:
            r = [round(float(complejo), 2), 0]
    return r

def compl(v):
    if v[0] != 0 and v[1] != 0:
        if v[1] < 0:
            r = str(v[0]) + " " + str(v[1]) +"i"
        else:
            r = str(v[0]) + " + " + str(v[1]) +"i"
    elif v[0] == 0 and v[1] != 0:
        r = str(v[1]) + "i"
    elif v[0] != 0 and v[1] == 0:
        r =  str(v[0])
    elif v[0] == 0 and v[1] == 0:
        r = str(0)
    return r

def M_u(M1):
    if M1 == []:
        r = []
        return False
    else:
        x1 = len(M1)
        y1 = len(M1[0])
        if y1 == x1:
            r = Mult_M(M1, M1)
            zero = 0
            one = 0
            for i in range(x1):
                for x in range(y1):
                    if r[i][x] == "0":
                        zero += 1
                    elif r[i][x] == "1.0i":
                        one += 1
            if zero == x1**2 - x1 and one == x1:
                return True
            else:
                return False
        else:
            return False
