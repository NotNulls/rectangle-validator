import math
import numpy as np


def fourth_point_coordinates(a, b, c):
    """
    Find coordinates of the fourth point for a given three points of a rectangle.
    """
    ac = np.array(c) - np.array(a)
    d = tuple(np.array(b) + ac)
    return d


def find_diagonal_length(a, c, d):
    """
    Find the lengths of diagonals.
    """
    diagonal_ad = math.sqrt((d[0] - a[0]) ** 2 + (d[1] - a[1]) ** 2)
    diagonal_cb = math.sqrt((c[0] - b[0]) ** 2 + (c[1] - b[1]) ** 2)
    return diagonal_ad, diagonal_cb


def mid_point(a, b, c, d):
    """
    Find the midpoints of diagonals.
    """
    midpoint_bc = ((b[0] + c[0]) / 2, (b[1] + c[1]) / 2)
    midpoint_ad = ((a[0] + d[0]) / 2, (a[1] + d[1]) / 2)
    return midpoint_ad, midpoint_bc


def is_point_in_rectangle(a, d, x):
    """
    Check if a point is within a rectangle defined by given points.
    """
    if (x[0] > a[0] and x[0] < d[0] and x[1] > a[1] and x[1] < d[1]):
        print('Točka je unutar pravokuta.')
    else:
        print('Točka je van pravokuta.')


def is_rectangle(midpoint_ad, midpoint_bc, diagonal_ad, diagonal_cb):
    """
    Check if points form a rectangle based on midpoints and diagonal lengths.
    """
    if midpoint_ad == midpoint_bc and diagonal_ad == diagonal_cb:
        return True
    else:
        return False


if __name__ == '__main__':
    a = (1, 1)
    b = (6, 1)
    c = (1, 6)
    x = (2, 2)

    d = fourth_point_coordinates(a, b, c)

    diagonal_ad, diagonal_cb = find_diagonal_length(a, c, d)

    mid_ad, mid_bc = mid_point(a, b, c, d)

    is_rectangle_result = is_rectangle(mid_ad, mid_bc, diagonal_ad, diagonal_cb)

    if is_rectangle_result:
        print('True')
        print('Date točke formiraju pravokut.')
    else:
        print('False')
        print('Date točke ne formiraju pravokut.')

    is_point_in_rectangle(a, d, x)
    print(diagonal_ad)
