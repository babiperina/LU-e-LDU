from matrix import Matrix

m = Matrix(3,3,[1,1,1,2,1,-1,2,-1,1])
b = [-2,1,3]

m.LU(b)