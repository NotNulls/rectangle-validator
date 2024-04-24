import numpy as np
import math
import sys

def cordinates_from_file(filename):
    with open('filename','r') as file:
        lines = file.readline()
        coordinates = [list(map(float, line.strip().split(','))) for line in lines]
    return coordinates

def fourthPointCoordiantes(A,B,C):
    """
    Pronalazi koordinate nedostajuće točke.
    """

    AC = np.array(C) - np.array(A)
    D = (tuple(np.array(B) + AC))
    
    print (f'Točka D je kordinata: {D}')
    return (D)


def findDiagonalLenght(A,C):

    A = np.array(A)
    C = np.array(C)

    diagonal_ad = math.sqrt((D[0]-A[0])**2 + (D[1]-A[1])**2)
    diagonal_cb = math.sqrt((C[0]-B[0])**2 + (C[1]-B[1])**2)
    
    print(f'Diagonala AD: {diagonal_ad}, diagonala CB: {diagonal_cb}')
    return diagonal_ad,diagonal_cb
    
def midPoint(A,B,C,D):
    mid_point_BC = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    mid_point_AD = ((A[0] + D[0]) / 2, (A[1] + D[1]) / 2)

    return mid_point_AD, mid_point_BC


def isPointInRectangle(A,C,X=None):
    if (X[0]>A[0] and X[0]<D[0] and X[1]<C[1] and X[1]<D[1]):
        print ('Točka je unutar datog pravokuta.')
    else:
        print ('Točka je van datog pravokuta.')

def is_rectangle(mid_point_AD, mid_point_BC):
        if mid_point_AD == mid_point_BC and diagonal_ad == diagonal_cb:
            print ('Postavljene tačke obrazuju pravokut.')
            return True
        else:
            print ('Postavljene tačke ne obrazuju pravokut.')
            return False
             


if __name__ == '__main__':


    
    A = (1,1)
    B = (6,1)
    C = (1,6)
    X = (2,2)

    D = fourthPointCoordiantes(A,B,C)
    
    diagonal_ad,diagonal_cb = findDiagonalLenght(A,C)
    
    mid_BC, mid_AD = midPoint(A,B,C,D)

    is_rectangle(mid_BC, mid_AD)
        
    
    in_rectangle = isPointInRectangle(A,D,X)
    
    

    
        
