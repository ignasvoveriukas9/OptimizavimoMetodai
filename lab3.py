import numpy as np
import math


#def distance ( point1, point2 ):
    #return math.sqrt ( ( ( point2 [ 0 ] - point1 [ 0 ] ) ** 2 ) + ( ( point2 [ 1 ] - point1 [ 1 ] ) ** 2 ) + ( ( point2 [ 2 ] - point1 [ 2 ] ) ** 2 ) )

def distance ( point1, point2 ):
    return np.linalg.norm ( np.array ( point2 ) - np.array ( point1 ) )
    #distance = np.linalg.norm ( np.array ( point2 ) - np.array ( point1 ) )
    #print ( distance )
    #return distance

def gradientDescent ( start, lr, tol, r ):

    iteration = 0

    x, y, z = start

    grad_x = gradient_x ( x, y, z, r )
    grad_y = gradient_y ( x, y, z, r )
    grad_z = gradient_z ( x, y, z, r )

    new_x = x - ( lr * grad_x )
    new_y = y - ( lr * grad_y )
    new_z = z - ( lr * grad_z )

    #print (new_x)
    #print (new_y)
    #print (new_z)

    while distance ( ( x, y, z ), ( new_x, new_y, new_z ) ) >= tol:

        #print (grad_x)

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

    tol  = 1e-5

    functionCalls = 0

    i = 0

    while ( 1 ):

        print ( "iter: " + str ( i ) + " X = " + str ( x ) + ", " + str ( y ) + ", " + str ( z ) + " r: " + str ( r ) + " tol: " + str ( tol ) + " func calls: " + str ( functionCalls ) + " 1/r * b " + str ( ( 1 / r ) * b ( x, y, z ) ) )

        oldrb = ( 1 / r ) * b ( x, y, z )

        x, y, z, _, calls  = gradientDescent ( ( x, y, z ), lr, tol, r )

        functionCalls += calls

        r = r / rChange

        tol = tol / rChange
        #tol = 1e-5

        lr = lr / rChange

        if oldrb <= ( ( 1 / r ) * ( b ( x, y, z ) ) ):
            break

        i += 1

    return x, y, z, functionCalls


def f ( x, y, z ):
    return -( x * y * z )

def b ( x, y, z ):
    g1, g2, g3 =  0, 0, 0 

    if ( x < 0 ):
        g1 = ( -x ) ** 2

    if ( y < 0 ):
        g2 = ( -y ) ** 2

    if ( z < 0 ):
        g3 = ( -z ) ** 2

    return g1 + g2 + g3 + ( ( ( 2 * ( ( x * y ) + ( y * z ) + ( x * z ) ) ) - 1 ) ** 2 )

def B ( x, y, z, r ):
    return f (x, y, z) + ( ( 1 / r ) * b ( x, y, z ) )

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
    
rez = optimizeFunction ( ( 0.6, 0.3, 0.2 ), 1, 2 )

#rez = gradientDescent ( (0.4096861684874302, 0.4096861684874302, 0.4096861684874302 ), 1e-8, 0.000625, 0.0625 )

print ( rez ) 

