
import matplotlib.pyplot as plt
import numpy as np

def bisection ( f, rangeMin, rangeMax, tol = 1e-4 ):
    
    x = np.linspace ( -1, 5, 1000 )
    y = f ( x )

    plt.title ( 'bisection' )
    plt.plot ( x, y )

    acc = abs ( rangeMax - rangeMin )
    iterations = 0

    while acc > tol:
        mid = ( rangeMin + rangeMax ) / 2
        fM = f ( mid )

        left = ( rangeMin + mid ) / 2
        right = ( mid + rangeMax ) / 2

        fL = f ( left )
        fR = f ( right )

        if ( fL < fM ):
            rangeMax = mid
        elif ( fR < fM ):
            rangeMin = mid
        else:
            rangeMin = left
            rangeMax = right

        acc = abs ( rangeMax - rangeMin )

        plt.plot ( mid, fM, 'o' )
        print ( 'mid point for iteration ' + str ( iterations ) + ': x: ' + str ( mid ) + ' y: ' + str ( fM ) )
        # print ( 'Left: ' + str ( rangeMin ) + ' right: ' + str ( rangeMax ) + '\r\n' )
        iterations += 1

    x_min = ( rangeMin + rangeMax ) / 2
    return x_min, f ( x_min ), iterations



def f ( x ):
    return ( ( ( ( x ** 2 ) - 3 ) ** 2 ) / 2 ) - 1

rez = bisection ( f, 0, 10 )

print ( rez )

plt.show ()
