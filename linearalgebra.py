#You are not allowed to use Numpy or any other modules to help write your functions
#You are only allowed to use the math module
#You may use previous defined functions to help(ex. below we used the square function to help define the cube function)
#For us, a matrix is just a nested list. 
#[[1,2,3], [4,5,6], [7,8,9]] is a 3x3 matrix
# 1 2 3
# 4 5 6
# 7 8 9

import math

#ALGEBRA
def addone(n):
  return n+1

def square(n):
  return n*n

def cube(n):
  return square(n)*n

def absolute(n):
  if n >=0:
    return n
  else:
    return n*(-1)

# Write a function that return the sum if it is even,
# return false if the sum is not even
def EvenSum(a, b):
  sum = a + b;
  if (sum % 2 == 0):
    return sum
  else:
    return False


# Write a function that returns True if n is even and False if n is odd.
def IsEven(n):
  if (n % 2 == 0):
    return True
  else:
    return False

#Write a function to solve for the solutions to the quadratic equation ax^2 + bx + c =0
#Example x^2 -5x + 6 = 0 with solutions x=2,3, 
#the function will return a list of solutions in ascending order
#Quadratic(1,-5,6) ---> [2,3]
#return false if the solution is not real. 
def Quadratic(a,b,c):
  if (b**2-4*a*c < 0):
    return False
  else:
    x1 = ((-b + math.sqrt(b**2-4*a*c))/(2*a))
    x2 = ((-b - math.sqrt(b**2-4*a*c))/(2*a))

    if (x1 > x2):
        return [int(x2), int(x1)]
    else:
        return [int(x1), int(x2)]

##LINEAR ALGEBRA FUNCTIONS

#AddMatrix will take in two matrices and return the sum of A+B 
#return false if you cannot add A and B
#Note: adding two arrays will concatinate the two arrays together, i.e return A+B will not work.
def AddMatrix(A,B):
  rowLengthA = len(A) #checking row and column length of matrices
  rowLengthB = len(B)
  colLengthA = len(A[0])
  colLengthB = len(B[0])

  if ((rowLengthA != rowLengthB) or (colLengthA != colLengthB)):
    return False

  else:
    sumMatrices = []

    for i in range (0, rowLengthA):
      newList = [] #make a list within a list
      for j in range (0, colLengthA):{
        newList.append(A[i][j] + B[i][j])}
      
      sumMatrices.append(newList) #add each list into sumMatrice
    
    return sumMatrices


#MultiplyMatrix will take in two matrices and return the product
#return false if you cannot multiply
def MultiplyMatrix(A,B):
  rowLengthA = len(A) #checking row and column length of matrices
  rowLengthB = len(B)
  colLengthA = len(A[0])
  colLengthB = len(B[0])
  multipliedList = []

  print(A)
  print(B)

  if ((colLengthA != rowLengthB)): #check conditions to multiply
    return False
  

  for i in range(0, rowLengthA):
    dotProduct = []
    for j in range(0, colLengthB):
      sumofProduct = 0
      for k in range(0, rowLengthA):
        sumofProduct += (A[i][k] * B[k][j]) 
      dotProduct.append(sumofProduct)

    multipliedList.append(dotProduct)
    
  return multipliedList

#Det will take in a matrix and compute for the determinant
#return false if you cannot take the determinant
#this should be able to handle matrix of any size.
def Det(A):
    rowLengthA = len(A) #checking row and column length of matrix
    colLengthA = len(A[0])
    detA = 0
    

    if (rowLengthA != colLengthA): #checking that this is a nxn matrix
        return False


    if (rowLengthA == 2): #for 2x2 matrix
        ad = A[0][0] * A[1][1]
        bc = A[0][1] * A[1][0]
        subDetA = ad - bc
        return subDetA

    #for all other matrices
    for i in list(range(0, rowLengthA)): #for each column
        #rewrite matrix to be a submatrix matrix multiplied by some c scalar
        scalar = A[0][i]

        Asubmatrix = A.copy() #copy matrix
        Asubmatrix = Asubmatrix[1:] #pop top row
        
        colLengthAs = len(Asubmatrix) #find height of submatrix

        for j in range(0, colLengthAs): #remove column in
            # same col as scalar
            y = i + 1
            Asubmatrix[j] = Asubmatrix[j][0:i] + Asubmatrix[j][y:]
            
        #determine sign since needs to alternate
        sign = (-1) ** (i)
        
        #repeats submatrix until 2x2
        subMatrix = Det(Asubmatrix)
        detA += sign * scalar * subMatrix

    return detA

#Take in a matrix and take the transpose
def Transpose(A):
  return

#Det will take in a matrix and determine if the columns are dependent
#return true if it is and false the columns are independent
#You can assume A is a square matrix. 
def ColDependent(A):
  return

#EigenValues will take in 2x2 matrix and compute for the real eigenvalues as a list in ascending order
#For example, EigenValues([[5,0],[0,3]]) ---> [3,5]
#return false if the dimensions is wrong or the eigenvalues are not real.
def EigenValues(A):
  return

#Rotate takes in a 2D vector in the form [a,b] and  rotate it by n degrees
#Example Rotate([1,0], 90) ---> [0,1]
#Example Rotate([1,0], -90) ---> [0,-1]
#Example Rotate([1,0], 180) ---> [-1,0]
def Rotate(v, n):
  return


