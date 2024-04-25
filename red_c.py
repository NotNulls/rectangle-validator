import math
import numpy as np


def fourth_point_coordinates(a, b, c):
    """
    Pronalaženje četvrte točke.
    """
    ac = np.array(c) - np.array(a)
    d = tuple(np.array(b) + ac)
    return d


def find_diagonal_length(a, c, d):
    """
    Pronalaženje dujina diagonala.
    """
    diagonal_ad = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)
    diagonal_cb = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
    return diagonal_ad, diagonal_cb


def mid_point(a, b, c, d):
    """
    Pronalaženje središnjih točaka.
    """
    midpoint_bc = ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2)
    midpoint_ad = ((a[0] + d[0]) / 2, (a[1] + d[1]) / 2)
    return midpoint_ad, midpoint_bc


def is_point_in_rectangle(a, d, x):
    """
    Provera da li je točka unutar pravokuta.
    """
    if (x[0] > a[0] and x[0] < d[0] and x[1] > a[1] and x[1] < d[1]):
        print('Točka je unutar pravokuta.')
    else:
        print('Točka je van pravokuta.')


def is_rectangle(midpoint_ad, midpoint_bc, diagonal_ad, diagonal_cb):
    """
    Proveravanje da li točke formiraju pravokut na osnovu središnjih točaka i diagonala.
    """
    if midpoint_ad == midpoint_bc and diagonal_ad == diagonal_cb:
        return True
    else:
        return False

def read_coordinates_from_file(filename):
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            # Pretvoriti svaku liniju ponaosob u tuple koji sadrži float članove
            cleaned_line = line.strip().replace("(", "").replace(")", "")
            coord_tuple = tuple(map(float, cleaned_line.split(',')))
            coordinates.append(coord_tuple)
    return coordinates

if __name__ == '__main__':
    
    coordinates = read_coordinates_from_file('dummydata.csv')
    for coord in coordinates:
        a = tuple(coord[0:2])  
        b = tuple(coord[2:4])  
        c = tuple(coord[4:6])  
        x = tuple(coord[6:8])

        d = fourth_point_coordinates(a, b, c)

        ad = np.array(d) - np.array(a)  
        bc = np.array(c) - np.array(b)

        dot_product = np.dot(ad, bc)
        
        is_perpendicular = dot_product == 0

        diagonal_ad, diagonal_cb = find_diagonal_length(a, c, d)

        mid_ad, mid_bc = mid_point(a, b, c, d)

        is_rectangle_result = is_rectangle(mid_ad, mid_bc, diagonal_ad, diagonal_cb)

        if is_rectangle_result:
            print('True')
            print('Date točke formiraju pravokut.')
            if is_perpendicular == 0:
                print ('Dobijena figura je kvadrat.')
            else:
                print ('Dobijena figura nije kvadrat.')
        else:
            break
            # print('False')
            # print('Date točke ne formiraju pravokut.')

        is_point_in_rectangle(a, d, x)
        print(diagonal_ad)
        print ('__________________________________________')
