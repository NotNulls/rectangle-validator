import numpy as np
import math
import sys

def cordinates_from_file(filename):
    with open('filename','r') as file:
        lines = file.readline()
        coordinates = [list(map(float, line.strip().split(','))) for line in lines]
    return coordinates

def check_rectagle(A,B,C):
    """
    Firstly we shall calculate the vectors formded by those points given and find out about point D coordinates.
    """

    AB = np.array(B) - np.array(A)
    BC = np.array(C) - np.array(B)
    
    

    if AB @ BC == 0:
        print ('Točke obrazuju pravokut.')
    else:
        print ('Točke ne obrazuju pravokut. ')
        


def fourthPointCoordiantes(A,B,C):

    """
    Pronalazi koordinate nedostajuće točke.
    """
    

    mid_point = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
    print ('Mid Point: ',mid_point)

    D = (float(2 * mid_point[0] - B[0]), float(2 * mid_point[1] - B[1]))

    print (f'Točka D je kordinata: {D}')
    return (D)

    

A = (1,1)
B = (1,3)
C = (5,5)



def findDiagonalLenght(A,C):
    diagonal = math.sqrt((C[0]-A[0])**2 + (C[1]-A[1])**2)
    print (f'Dujina diagonale je: {diagonal}')





def isPointInRectangle(A,C,X=None):
    if (X[0]>A[0] and X[0]<C[0] and X[1]<C[1] and X[1]<C[1]):
        print ('Točka je unutar datog pravokuta.')
    else:
        print ('Točka je van datog pravokuta.')



if __name__ == '__main__':

    # if check_rectagle(A,B,C) == True:
    #     fourthPointCoordiantes(A,B,C)
    #     isPointInRectangle(A,C,X=(0,4))
    #     findDiagonalLenght(A,C)


   

    

    if check_rectagle(A,B,C) == True:
        isPointInRectangle(A,C,X=(0,4))
    elif fourthPointCoordiantes(A,B,C):
        
        

        d = findDiagonalLenght(A,C)