
import matplotlib.pyplot as plt
import numpy as np

def newton ( f, fPrime, fDoublePrime, xi = 5, tol = 1e-4 ):

    x = np.linspace ( -1, 5, 1000 )
    y = f ( x )

    plt.title ( 'newton' )
    plt.plot ( x, y )

    plt.plot ( xi, f ( xi ), 'o' )

    iteration = 0

    while 1:

        fPrimeX = fPrime ( xi )
        fDoublePrimeX = fDoublePrime ( xi )

        if fDoublePrime == 0:
            print ("Double prime = 0")
            break

        xi1 = xi - ( fPrimeX / fDoublePrimeX )

        plt.plot ( xi, f ( xi ), 'o' )
        print ( "iteration: " + str ( iteration ) + " xi: " + str ( xi ) + ' acc: ' + str ( abs ( xi1 - xi ) ) )
        iteration += 1

        if abs ( xi1 - xi ) < tol:
            plt.plot ( xi1, f ( xi1 ), 'o' ) 
            return xi1, f ( xi1 ), iteration, iteration * 2

        xi = xi1


def f ( x ):
    return ( ( ( ( x ** 2 ) - 3 ) ** 2 ) / 2 ) - 1

def fPrime ( x ):
    return ( ( ( x ** 2 ) - 3 ) * 2 * x )

def fDoublePrime ( x ):
    return ( 6 * ( x ** 2 ) ) - 6

rez = newton ( f, fPrime, fDoublePrime )

print ( rez )

plt.show ()
