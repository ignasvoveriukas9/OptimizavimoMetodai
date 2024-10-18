import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Nelder_Mead ( start, lr, tol ):

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
            ( x0, y0, function ( x0, y0 ),
            ( x1, y1, function ( x1, y1 ),
            ( x2, y2, function ( x2, y2 ) 
            ]

    points = sorted ( points, key = lambda point: point [ 2 ] ) # sort by f ( x, y )

    xc = 0.5 * ( points [ 0 ] [ 0 ] + points [ 1 ] [ 0 ] )
    yc = 0.5 * ( points [ 0 ] [ 1 ] + points [ 1 ] [ 1 ] )

    xNew = ( 2 * xc ) - points [ 2 ] [ 0 ]
    yNew = ( 2 * yc ) - points [ 2 ] [ 1 ]

    fNew = function ( xNew, yNew )

    if fNew < points [ 0 ] [ 2 ]:
        points [ 2 ] [ 0 ] = ( 3 * xc ) - ( 2 * points [ 2 ] [ 0 ] )
        points [ 2 ] [ 1 ] = ( 3 * yc ) - ( 2 * points [ 2 ] [ 1 ] )
        points [ 2 ] [ 2 ] = function ( points [ 2 ] [ 0 ], points [ 2 ] [ 1 ] ) 
    elif fNew > points [ 0 ] [ 2 ] and fNew < points [ 1 ] [ 2 ]:
        points [ 2 ] [ 0 ] = xNew
        points [ 2 ] [ 1 ] = yNew
        points [ 2 ] [ 2 ] = fNew
    elif fNew > points [ 1 ] [ 2 ] and fNew < points [ 2 ] [ 2 ]:
        points [ 2 ] [ 0 ] = ( 1.5 * xc ) - ( 0.5 * points [ 2 ] [ 0 ] )
        points [ 2 ] [ 1 ] = ( 1.5 * yc ) - ( 0.5 * points [ 2 ] [ 1 ] )
        points [ 2 ] [ 2 ] = function ( points [ 2 ] [ 0 ], points [ 2 ] [ 1 ] )
    elif fNew > points [ 2 ] [ 2 ]:
        points [ 2 ] [ 0 ] = ( 0.5 * xc ) + ( 0.5 * points [ 2 ] [ 0 ] )
        points [ 2 ] [ 1 ] = ( 0.5 * yc ) + ( 0.5 * points [ 2 ] [ 1 ] )
        points [ 2 ] [ 2 ] = function ( points [ 2 ] [ 0 ], points [ 2 ] [ 1 ] )



    return x, y, iteration

def function ( x, y ):
    return - ( x * y / 8 ) * ( 1 - x - y )

rez = gradient_descent ( ( (1), (1) ), 0.5, 1e-4 )

print ( rez )    

plt.show()
