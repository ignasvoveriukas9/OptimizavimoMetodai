import numpy as np
import math

def distance ( point1, point2 ):
    return np.linalg.norm ( np.array ( point2 ) - np.array ( point1 ) )

def gradientDescent ( start, lr, tol, r ):

    iteration = 0

    x, y, z = start

    grad_x = gradient_x ( x, y, z, r )
    print ("gardx: " + str (grad_x) )
    grad_y = gradient_y ( x, y, z, r )
    grad_z = gradient_z ( x, y, z, r )

    new_x = x - ( lr * grad_x )
    new_y = y - ( lr * grad_y )
    new_z = z - ( lr * grad_z )

    while distance ( ( x, y, z ), ( new_x, new_y, new_z ) ) >= tol:

        iteration += 1
        
        x, y, z = new_x, new_y, new_z

        grad_x = gradient_x ( x, y, z, r )
        grad_y = gradient_y ( x, y, z, r )
        grad_z = gradient_z ( x, y, z, r )

        new_x = x - ( lr * grad_x )
        new_y = y - ( lr * grad_y )
        new_z = z - ( lr * grad_z )

    x, y, z = new_x, new_y, new_z

    return x, y, z, iteration, ( iteration * 3 ) + 3

def optimizeFunction ( start, r, rChange):

    x, y, z = start

    lr = 0.01

    tol  = 1e-6

    functionCalls = 0

    i = 0

    while ( 1 ):

        oldrb = ( 1 / r ) * b ( x, y, z )


        print ( "iter: " + str ( i ) + " X = " + str ( x ) + ", " + str ( y ) + ", " + str ( z ) + " r: " + str ( r ) + " tol: " + str ( tol ) + " lr: " + str ( lr ) + " func calls: " + str ( functionCalls ) + " 1/r * b " + str ( oldrb ) )

        x, y, z, _, calls  = gradientDescent ( ( x, y, z ), lr, tol, r )

        functionCalls += calls

        r = r / rChange

        tol = tol / rChange

        lr = lr / rChange

        if oldrb <= ( ( 1 / r ) * ( b ( x, y, z ) ) ):
            break

        functionCalls += 2;

        i += 1

    return x, y, z, functionCalls

def b ( x, y, z ):
    g1, g2, g3 =  0, 0, 0 

    if ( x < 0 ):
        g1 = ( -x ) ** 2
    if ( y < 0 ):
        g2 = ( -y ) ** 2
    if ( z < 0 ):
        g3 = ( -z ) ** 2

    return g1 + g2 + g3 + ( ( ( 2 * ( ( x * y ) + ( y * z ) + ( x * z ) ) ) - 1 ) ** 2 )

def gradient_x ( x, y, z, r ):
    g = 0

    if ( x < 0 ):
        g = 2 * x
    return ( - ( y * z ) ) + ( ( 1 / r ) * ( g + ( ( 4 * ( ( 2 * ( ( x * y ) + ( y * z ) + ( x * z ) ) ) - 1 ) ) * ( y + z ) ) ) )
    
def gradient_y ( x, y, z, r ):
    g = 0

    if ( y < 0 ):
        g = 2 * y
    return ( - ( x * z ) ) + ( ( 1 / r ) * ( g + ( ( 4 * ( ( 2 * ( ( x * y ) + ( y * z ) + ( x * z ) ) ) - 1 ) ) * ( x + z ) ) ) )


def gradient_z ( x, y, z, r ):
    g = 0

    if ( z < 0 ):
        g = 2 * z

    return ( - ( x * y ) ) + ( ( 1 / r ) * ( g + ( ( 4 * ( ( 2 * ( ( x * y ) + ( y * z ) + ( x * z ) ) ) - 1 ) ) * ( x + y ) ) ) )
    
rez = optimizeFunction ( ( 1, 1, 1 ), 1, 5 )

print ( rez ) 

