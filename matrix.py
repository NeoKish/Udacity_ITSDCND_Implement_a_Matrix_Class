import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h==1 :
            return self.g[0][0]
        elif self.h==2:
            a=self.g[0][0]
            b=self.g[0][1]
            c=self.g[1][0]
            d=self.g[1][1]
            return a*d-b*c
        
        # TODO - your code here

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        result=0    
        for i in range(self.h):
            for j in range(self.w):
                if i==j :
                    result+=self.g[i][j]
        return result            
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        det=self.determinant()  
        inverse=zeroes(self.h,self.w)  
        if self.h==1:
            inverse.g[0][0]=1/det
        elif self.h==2:
            if det==0:
                raise(ValueError,"Matrix is not invertible.")
            else:     
                a=self.g[0][0]
                b=self.g[0][1]
                c=self.g[1][0]
                d=self.g[1][1]
                inverse.g[0][0]=d
                inverse.g[0][1]=-b
                inverse.g[1][0]=-c
                inverse.g[1][1]=a
                for i in range(inverse.h):
                    for j in range(inverse.w):
                        inverse.g[i][j]=1/det*inverse.g[i][j]
        #print(inverse)                
        return inverse
        # TODO - your code here

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        
        Sum=zeroes(self.w,self.h) 
        matrix_transpose=[]
        for i in range(self.w):
            row_value=[]
            for j in range(self.h):
                row_value.append(self.g[j][i])

            matrix_transpose.append(row_value)    
        for i in range(len(matrix_transpose)):
            for j in range(len(matrix_transpose[0])):
                Sum.g[i][j]=matrix_transpose[i][j]
        return Sum
                

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
           
            
        #   
        # TODO - your code here
        #
        Sum=zeroes(self.h,self.w) 
        for i in range(self.h):
            for j in range(self.w):
                Sum[i][j]=self.g[i][j]+other.g[i][j]
                
               #matrixNew.g.append(row_V)   
      
        return Sum    

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        #matrixNew=[];
        Sum=zeroes(self.h,self.w) 
        for i in range(self.h):
            #row_V=[]
            for j in range(self.w):
                Sum[i][j]=(-1)*self.g[i][j]
                #row_V.append((-1)*self.g[i][j])
            #matrixNew.append(row_V)   
        #print(Sum)        
        return Sum

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        other=-other
        return self+other
        #
        
    def _dot_product(vector_one, vector_two):
        result=[]
        for i in range(len(vector_one)):
            result.append(vector_one[i]*vector_two[i])
        return sum(result)

    def __mul__(self, other):

        """
        Defines the behavior of * operator (matrix multiplication)
       
        """
        if self.w!=other.h:
            raise(ValueError, "Number of columns in first matrix and number of rows in second needs to be same") 
            
        other_New=other.T()
        #print(other_New)
      
        k=0
        Sum=zeroes(self.h,other.w)
        for i in range(self.h):
            row_new=[]   
            for k in range(other_New.h):
                row_v=[]
                for j in range(other.h):
                    row_v.append(self.g[i][j]*other_New[k][j])
                    #print(row_v)    
                Sum[i][k]=sum(row_v) 
     
           
        #print(Sum)
        return Sum  
            
        #   
        # TODO - your code here
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
           # matrixNew=[];
           
            for i in range(self.h):
                row_V=[]
                for j in range(self.w):
                    self.g[i][j]=(other)*self.g[i][j]
                    #row_V.append((a)*other.g[i][j])
                #matrixNew.append(row_V)   
            #print(self.g)    
        return self
            
            #   
            # TODO - your code here
            #
            