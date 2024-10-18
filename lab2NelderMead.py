import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance ( point1, point2 ):
    return math.sqrt ( ( ( point2 [ 0 ] - point1 [ 0 ] ) ** 2 ) + ( ( point2 [ 1 ] - point1 [ 1 ] ) ** 2 ) )

def nelder_Mead ( start, lr, tol ):

    x = np.linspace ( -0.1, 1, 100 )
    y = np.linspace ( -0.1, 1, 100 )
    X, Y = np.meshgrid(x, y)

    Z = function ( X, Y )

    fig = plt.figure()
    ax = fig.add_subplot ( 111, projection = '3d' )

    ax.plot_surface ( X, Y, Z, cmap = 'viridis', alpha = 0.5 )

    ax.set_xlabel ( 'X' )
    ax.set_ylabel ( 'Y' )
    ax.set_zlabel ( 'f(X, Y)' )
    ax.set_title ( 'grad des' )

    iteration = 0

    x0, y0 = start

    s1 = ( ( ( math.sqrt ( 3 ) + 1 ) / ( 2 * math.sqrt ( 2 ) ) ) * lr )
    s2 = ( ( ( math.sqrt ( 3 ) - 1 ) / ( 2 * math.sqrt ( 2 ) ) ) * lr )

    #X1
    x1 = x0 + s2
    y1 = y0 + s1
    #X2
    x2 = x0 + s1
    y2 = y0 + s2

    points = [
            ( x0, y0, function ( x0, y0 ) ),
            ( x1, y1, function ( x1, y1 ) ),
            ( x2, y2, function ( x2, y2 ) ) 
            ]

    while distance ( points [ 0 ], points [ 1 ] ) > tol and iteration < 50:

        iteration += 1

        points = sorted ( points, key = lambda point: point [ 2 ] ) # sort by f ( x, y )

        print ( f"Iteration {iteration}:" )
        print ( f"xl: ({points[0][0]}, {points[0][1]}) f: {points[0][2]}" )
        print ( f"xg: ({points[1][0]}, {points[1][1]}) f: {points[1][2]}" )
        print ( f"xh: ({points[2][0]}, {points[2][1]}) f: {points[2][2]}" )

        xc = 0.5 * ( points [ 0 ] [ 0 ] + points [ 1 ] [ 0 ] )
        yc = 0.5 * ( points [ 0 ] [ 1 ] + points [ 1 ] [ 1 ] )

        xNew = ( 2 * xc ) - points [ 2 ] [ 0 ]
        yNew = ( 2 * yc ) - points [ 2 ] [ 1 ]

        fNew = function ( xNew, yNew )

        if fNew < points [ 0 ] [ 2 ]:
            xz = ( 3 * xc ) - ( 2 * points [ 2 ] [ 0 ] )
            yz = ( 3 * yc ) - ( 2 * points [ 2 ] [ 1 ] )
            fz = function ( xz, yz )
            points [ 2 ] = ( xz, yz, fz )
            print ( "expanded" )
        elif fNew > points [ 0 ] [ 2 ] and fNew < points [ 1 ] [ 2 ]:
            points [ 2 ] = ( xNew, yNew, fNew )
            print ( "normal" )
        elif fNew > points [ 1 ] [ 2 ] and fNew < points [ 2 ] [ 2 ]:
            xz = ( 1.5 * xc ) - ( 0.5 * points [ 2 ] [ 0 ] )
            yz = ( 1.5 * yc ) - ( 0.5 * points [ 2 ] [ 1 ] )
            fz = function ( xz, yz )
            points [ 2 ] = ( xz, yz, fz )
            print ( "smaller" )
        elif fNew > points [ 2 ] [ 2 ]:
            xz = ( 0.5 * xc ) + ( 0.5 * points [ 2 ] [ 0 ] )
            yz = ( 0.5 * yc ) + ( 0.5 * points [ 2 ] [ 1 ] )
            fz = function ( xz, yz )
            points [ 2 ] = ( xz, yz, fz )
            print ( "change direction" )




    return points [ 0 ] [ 0 ], points [ 0 ] [ 1 ], iteration

def function ( x, y ):
    return - ( x * y / 8 ) * ( 1 - x - y )

rez = nelder_Mead ( ( (0), (0) ), 0.4, 1e-4 )

print ( rez )    

plt.show()
