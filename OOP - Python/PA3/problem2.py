"""
Amandeep Singh
Ruid 145003464
"""

def dimension(M):
    '''returns dimension of matrix M'''
    return (len(M),len(M[0])) #use len to send dimenskikons

def row(M,i):
    '''returns row i of matrix M'''
    return M[i-1] #i is i-1 in notation starting from0

def column(M,i):
    '''returns coli from matrix M'''
    column = []
    for j in range (0, len(M)):
        column.append(M[j][i-1]) #traverse row and append column element
    return column

def matrix_sum(A,B):
    '''sum of matrix A and B'''
    add_list=[]
    if(dimension(A)==dimension(B)): #dimension must match
        for i in range(0,len(A)):
            temp_row=[]
            for j in range(0,dimension(B)[1]):
                temp_row.append(A[i][j]+B[i][j]) #access and add rows
            add_list.append(temp_row)
    else:
        print('Error Dimensions dont match')
    return add_list


def matrix_difference(A,B):
    '''difference of matrices'''
    add_list=[]
    if(dimension(A)==dimension(B)): #dimension checking
        for i in range(0,len(A)):
            temp_row=[]
            for j in range(0,dimension(B)[1]):
                temp_row.append(A[i][j]-B[i][j]) #access row and subtract
            add_list.append(temp_row)
    else:
        print('Error Dimensions dont match')
    return add_list

def matrix_product(A,B):
    '''product of matrices'''
    (n_rows_A,n_cols_A)=dimension(A)
    (n_rows_B,n_cols_B)=dimension(B)
    out_mat=[]
    if n_cols_A==n_rows_B: #dimensions must match
        out_mat=[]
        for i in range(0,n_rows_A):
            temp=[]
            for j in range(0,n_cols_B):
                Arow=row(A,i+1) #access required col,row and then multiply
                Bcol=column(B,j+1)
                prod_val=sum(a * b for a, b in zip(Arow, Bcol))
                temp.append(prod_val)
            out_mat.append(temp)
    else:
        print('Error Dimensions dont match')
    return out_mat
                           

def reduce_matrix(M,i,j):
    '''removes i and j row and col resp from M'''
    N=M.copy()
    N.pop(i-1) #row removed
    out_mat=[]
    for ii in range(0,len(N)):
        temp=[]
        for jj in range(0,dimension(N)[1]):
            if jj!=j-1:
                temp.append(N[ii][jj]) #col removed
        out_mat.append(temp)
    return out_mat

def determinant(M):
    '''recursively give dimension'''
    size=dimension(M)
    n_rows=size[0]
    n_cols=size[1]
    det=0
    
    if(n_rows!=n_cols):
        print('Error ! Not square matrix')
        return -1
    
    if n_rows==2:
        det=M[0][0] * M[1][1] - M[1][0] * M[0][1]
    else:
        for p in range(0,n_rows):
            c=reduce_matrix(M,1,p+1)
            det=det+M[0][p]*((-1)**p)*determinant(c)
    
    return det

def pretty_print(M):
    '''print matrix'''
    s = [[str(e) for e in row] for row in M]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print ('\n'.join(table))
    
                    
                
        
            
## USE THE FOLLOWING TEST CODE TO TEST YOUR CODE 
## FOR PROBLEM #2 

if __name__ == "__main__":
    print("Testing module problem2 (Assignment #3): ")
    A = [[5, 3, -1], [9, 4, 12]]
    B = [[6, 9, 12], [-8, 6, -4], [7, 11, 13]]
    C = [[0, -21, -1], [11, 13, 17]]

    print("Three matrices have been created.")
    print("\nMatrix A equals \n")
    pretty_print(A)
    print("\nMatrix B equals \n")
    pretty_print(B)
    print("\nMatrix C equals \n")
    pretty_print(C)

    print("Matrix A has dimension ", dimension(A))
    print("Matrix B has dimension ", dimension(B))
    print("Matrix C has dimension ", dimension(C))

    print()
    print("The second row of matrix A is: ", row(A, 2))
    print("The third column of matrix B is: ", column(B, 3))
    print("The second column of matrix C is: ", column(C, 2))

    print()
    D = matrix_sum(A, C)
    print("The sum of matrices A and C is: \n")
    pretty_print(D)

    D = matrix_difference(C, A)
    print("The difference of matrices C and A is: \n")
    pretty_print(D)

    D = matrix_product(A, B)
    print("The product of  matrices A and B is: \n")
    pretty_print(D)

    D = matrix_product(A, C)
    print()

    D = reduce_matrix(A, 1, 1)
    print("Matrix obtained by removing row 1, column 1 of matrix A: \n")
    pretty_print(D)

    D = reduce_matrix(B, 3, 2)
    print("Matrix obtained by removing row 3, column 2 of matrix B: \n")
    pretty_print(D)

    D = determinant(B)
    print("The determinant of matrix B is: ", D)

    print("\nGoodbye!")
