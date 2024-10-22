
import matplotlib.pyplot as plt
import numpy as np

def goldenCut ( f, l, r, tol = 1e-4 ):

    t = 0.618

    x = np.linspace ( -1, 6.5, 1000 )
    y = f ( x )

    plt.title ( 'Golden cut' )
    plt.xlabel ( 'x' )
    plt.ylabel ( 'y' )
    plt.plot ( x, y )

    iteration = 0

    L = r - l

    x1 = r - ( t * L )
    x2 = l + ( t * L )

    fx1 = f ( x1 )
    fx2 = f ( x2 )

    plt.plot ( x1, fx1, 'o' )
    plt.plot ( x2, fx2, 'o' )

    print ( 'iteration ' + str ( iteration ) + ': x1: ' + str ( x1 ) + ' x2: ' + str ( x2 ) )

    while L > tol:

        if ( fx2 < fx1 ):
            l = x1
            L = r - l

            x1 = x2
            fx1 = fx2

            x2 = l + ( t * L )
            fx2 = f ( x2 )

            plt.plot ( x2, fx2, 'o' )
        else:
            r = x2
            L = r - l

            x2 = x1
            fx2 = fx1

            x1 = r - ( t * L )
            fx1 = f ( x1 )

            plt.plot ( x1, fx1, 'o' )

        iteration += 1
        
        print ( 'iteration ' + str ( iteration ) + ': x1: ' + str ( x1 ) + ' x2: ' + str ( x2 ) + ' L: ' + str(L) )

    xMin = ( r + l ) / 2
    return xMin, f ( xMin ), iteration, iteration + 2 

def f ( x ):
    return ( ( ( ( x ** 2 ) - 3 ) ** 2 ) / 2 ) - 1

rez = goldenCut ( f, 0, 10 )

print ( rez )

plt.show ()
