import numpy as np

class Matrix:

    def __init__(self, rows, cols, data = []):
        if type(rows) != int or type(cols) != int:
            print('O valor passado não é um número!')
            return
        if rows < 0 or cols < 0:
            print('Numero de linhas ou colunas inválido, deve ser positivo.')
            return
        self.rows = rows
        self.cols = cols
        
        if data:
            self.data = data
        else:
            self.data = [0] * (self.rows * self.cols)
        

    def __getitem__(self, key):
        try:
            i, j = key
            if self.rows < 0:
                raise Exception('Numero de linhas não é compatível')
            if self.cols < 0:
                raise Exception('Numero de colunas não é compatível')
            #print(key)
            return self.data[(j-1) + (i-1) * self.cols]
        except IndexError:
            print('Não existe a linha/coluna nessa matriz')
        

    #Método para definir um dos valores da matriz
    def __setitem__(self, key, value):
        try:
            i, j = key
            self.data[(j-1) + (i-1) * self.cols] = value
        except IndexError:
            print("Não existe a linha/coluna nessa matriz")


    def __repr__(self):
        print('')
        for i in range(1, self.rows+1):
            for j in range(1,self.cols+1):
                print("{0:.4f}".format(self[i,j]),end="   ")
            print('')

        return ''


    def __radd__(self,other):

        return self.__add__(other)
        

    #usar 'type()' para adicionar opção elemento a elemento

    def __add__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] + other[i,j]

            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] + other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 
                
    def __sub__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] - other[i,j]

            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] - other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 

        return res

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] * other[i,j]

            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    res[i,j] = self[i,j] * other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 

    def __rmul__(self, other):
        return self.__mul__(other)        

    def __truediv__(self,other):
        if type(other) == Matrix:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    if other[i,j] == 0:
                        print('Valor não pode divir por 0!')
                        return
                    else:
                        res[i,j] = self[i,j] / other[i,j]
            return res

        elif type(other) == int or type(other) == float:
            res = Matrix(self.rows, self.cols)
            for i in range(1, self.rows + 1):
                for j in range(1, self.cols + 1):
                    if other == 0:
                        print('Valor não pode divir por 0!')
                        return
                    else: 
                        res[i,j] = self[i,j] / other
            return res

        else:
            print('Elemento não compatível para operação!')

            return 

    def __rtruediv__(self, other):
        return self.__truediv__(other)


    def dot(self,other):
        try:
            if self.cols != other.rows:
                raise Exception('Número de linhas e colunas é incompatível para multiplicação!')
        except Exception:
            raise

        else:
            res = Matrix(self.rows,other.cols)

            for k in range(1,self.cols + 1):
                for i in range(1, self.rows + 1):
                    for j in range(1,other.cols + 1):
                        res[i,j] += self[i,k] * other[k,j]
            return res

    def transpose(self):

        res = Matrix(self.cols,self.rows)

        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                res[j,i] = self[i,j]

        return res


    def LU(self):
        L = Matrix(self.rows,self.cols,self.data)
        L = self.get_diagonal_principal(L.rows, L.cols)
        U = Matrix(self.rows,self.cols,self.data)

        print("L")
        self.print(L)
        print("\nU")
        self.print(U)
        pivots = U.definirU()
        print("\nU triangulo inferior zerado")
        self.print(U)
        print("\npivots = " + str(pivots))
        L.definirL(pivots)
        print("\nL triangulo inferior com pivots")
        self.print(L)

    def definirU(self):
        pivots = []
        for i in range(1, self.rows+1):
            for j in range(1, self.cols+1):
                if i > j:
                    print("\natualizando: " + str(i) + "," + str(j))
                    pivots.append(self.atualizarLinha(i, j))

        return pivots

    def definirL(self, pivots):
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                if i > j:
                    self[i,j] = pivots[0]
                    pivots.pop(0)

    def atualizarLinha(self, atuali, atualj):

        pivot = self[atuali, atualj] / self[atualj, atualj]

        for j in range(1, self.cols+1):
            print(str(self[atuali,j]) + " = " + str(self[atuali,j]) + " - (" +str(pivot)+"*"+ str(self[atuali,j]) + ") =" + str(self[atuali,j]))
            self[atuali,j] -= (pivot*self[atualj,j])
            print("a["+str(atuali)+","+str(j)+"] = a["+str(atuali)+","+str(j)+"] - " +str(pivot)+"*"+" a["+str(atualj)+","+str(atuali)+"] =" + str(self[atuali,j]))
            print()

        return pivot

    def get_diagonal_principal(self, rows,cols):
        res = Matrix(rows, cols)

        for i in range(1, res.rows+1):
            for j in range(1, res.cols+1):
                if i == j:
                    res[i,j] = 1
                else:
                    res[i, j] = 0

        return res


    def print(self, matrix):
        for i in range(1, matrix.rows + 1):
            for j in range(1, matrix.cols + 1):
                print(str(matrix[i, j]), end='\t')
            print("", )