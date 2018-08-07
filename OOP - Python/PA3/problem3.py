#Amandeep Singh 145003464 



class Matrix:
    '''Matrix Class'''
    M=[]
    def __init__(self,mat):
        '''initilaizes with 2d list'''
        self.M=mat
    
    def dimension(self):
        '''teturn dimension'''
        return (len(self.M),len(self.M[0]))

    def row(self,i):
        '''return row i'''
        return self.M[i-1]

    def column(self,i):
        '''return col i'''
        column = []
        for j in range (0, len(self.M)):
            column.append(self.M[j][i-1])
        return column
    
    def __add__(self,other):
        '''overload add(+) operator and add 2 matrices'''
        add_list=[]
        A=self.M
        B=other.M
        if(self.dimension()==other.dimension()):
            for i in range(0,len(A)):
                temp_row=[]
                for j in range(0,other.dimension()[1]):
                    temp_row.append(A[i][j]+B[i][j])
                add_list.append(temp_row)
        else:
            print('Error Dimensions dont match')
        return Matrix(add_list)


    def __sub__(self,other):
        '''subtract and overload -'''
        add_list=[]
        A=self.M
        B=other.M
        if(self.dimension()==other.dimension()):
            for i in range(0,len(A)):
                temp_row=[]
                for j in range(0,other.dimension()[1]):
                    temp_row.append(A[i][j]-B[i][j])
                add_list.append(temp_row)
        else:
            print('Error Dimensions dont match')
        return Matrix(add_list)
    
    def __mul__(self,other):
        '''multiply two matrcies and oberload *'''
        A=self.M
        B=other.M
        (n_rows_A,n_cols_A)=self.dimension()
        (n_rows_B,n_cols_B)=other.dimension()
        out_mat=[]
        if n_cols_A==n_rows_B:
            out_mat=[]
            for i in range(0,n_rows_A):
                temp=[]
                for j in range(0,n_cols_B):
                    Arow=self.row(i+1)
                    Bcol=other.column(j+1)
                    prod_val=sum(a * b for a, b in zip(Arow, Bcol))
                    temp.append(prod_val)
                out_mat.append(temp)
        else:
            print('Error Dimensions dont match')
        return Matrix(out_mat)

        
    def reduce_matrix(self,i,j):
        '''Reduce matrix'''
        N=self.M.copy()
        N.pop(i-1)
        out_mat=[]
        for ii in range(0,len(N)):
            temp=[]
            for jj in range(0,Matrix(N).dimension()[1]):
                if jj!=j-1:
                    temp.append(N[ii][jj])
            out_mat.append(temp)
        return Matrix(out_mat)

    
    def determinant(self):
        '''calculate detrminant'''
        size=self.dimension()
        n_rows=size[0]
        n_cols=size[1]
        det=0
        if(n_rows!=n_cols):
            print('Error ! Not square matrix')
            return -1
        if n_rows==2:
            M=self.M
            det=M[0][0] * M[1][1] - M[1][0] * M[0][1]
        else:
            for p in range(0,n_rows):
                M=self.M
                c=self.reduce_matrix(1,p+1)
                det=det+M[0][p]*((-1)**p)*c.determinant()
        
        return det

    def __str__(self):
        '''convert to string or pretty print'''
        M=self.M
        s = [[str(e) for e in row] for row in M]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        return ('\n'.join(table))

if __name__ == "__main__":
    '''Call all routines'''
    print("Testing module problem3 (Assignment #3): ")
    A = Matrix([[5, 3, -1], [9, 4, 12]])
    B = Matrix([[6, 9, 12], [-8, 6, -4], [7, 11, 13]])
    C = Matrix([[0, -21, -1], [11, 13, 17]])

    print("Three matrices have been created.")
    print("\nMatrix A equals \n")
    pA=str(A)
    print(pA)
    print("\nMatrix B equals \n")
    pB=str(B)
    print(pB)
    print("\nMatrix C equals \n")
    pC=str(C)
    print(pC)

    print("Matrix A has dimension ", A.dimension())
    print("Matrix B has dimension ", B.dimension())
    print("Matrix C has dimension ", C.dimension())

    print()
    print("The second row of matrix A is: ", A.row( 2))
    print("The third column of matrix B is: ", B.column( 3))
    print("The second column of matrix C is: ", C.column( 2))

    print()
    D = A+C
    print("The sum of matrices A and C is: \n")
    print(str(D))

    D = C-A
    print("The difference of matrices C and A is: \n")
    print(str(D))

    D =A-B
    print("The product of  matrices A and B is: \n")
    print(str(D))

    D = A*C
    print()

    D = A.reduce_matrix(1, 1)
    print("Matrix obtained by removing row 1, column 1 of matrix A: \n")
    print(str(D))

    D = B.reduce_matrix(3, 2)
    print("Matrix obtained by removing row 3, column 2 of matrix B: \n")
    print(str(D))

    D = B.determinant()
    print("The determinant of matrix B is: ", D)

    print("\nGoodbye!")

        
                    
