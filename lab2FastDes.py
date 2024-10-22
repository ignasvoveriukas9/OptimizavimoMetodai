import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance ( point1, point2 ):
    return math.sqrt ( ( ( point2 [ 0 ] - point1 [ 0 ] ) ** 2 ) + ( ( point2 [ 1 ] - point1 [ 1 ] ) ** 2 ) )

def goldenCut ( f, l, r, tol = 1e-4 ):

    t = 0.618

    iters = 0

    L = r - l

    x1 = r - ( t * L )
    x2 = l + ( t * L )

    fx1 = f ( x1 )
    fx2 = f ( x2 )

    while L > tol:

        if ( fx2 < fx1 ):
            l = x1
            L = r - l

            x1 = x2
            fx1 = fx2

            x2 = l + ( t * L )
            fx2 = f ( x2 )

        else:
            r = x2
            L = r - l

            x2 = x1
            fx2 = fx1

            x1 = r - ( t * L )
            fx1 = f ( x1 )

        iters += 1

    xMin = ( r + l ) / 2
    return xMin, iters + 2

def fastest_descent ( start, tol ):

    x = np.linspace ( -0.1, 1.2, 500 )
    y = np.linspace ( -0.1, 1.2, 500 )
    X, Y = np.meshgrid(x, y)

    Z = function ( X, Y )

    z_min = np.min ( Z )
    z_max = np.max ( Z )

    neg_levels1 = np.linspace ( 4.2e-3, abs ( z_min ), 8 )
    neg_levels2 = np.linspace ( 2e-3, 4e-3, 6 )
    neg_levels3 = np.linspace ( 1e-4, 1.5e-3, 2)
    neg_levels = ( - np.concatenate ( ( neg_levels3, neg_levels2, neg_levels1 ) ) ) [::-1]
    pos_levels = np.geomspace ( 1e-3, 0.8, 8 )

    levels = np.concatenate ( ( neg_levels, pos_levels ) )

    plt.figure ( figsize = ( 8, 6 ) )

    contour = plt.contour ( X, Y, Z, levels = levels, cmap = 'viridis' )
    plt.clabel ( contour, inline = True, fontsize = 8 )
    plt.title ( 'grad des' )
    plt.xlabel ( 'X' )
    plt.ylabel ( 'Y' )
    plt.colorbar ( contour )

    iteration = 0
    funcCalls = 0

    x, y = start

    grad_x = gradient_x ( x, y )
    grad_y = gradient_y ( x, y )

    
    def f_alpha ( alpha ):
        return function ( x - alpha * grad_x, y - alpha * grad_y )

    alpha_opt, funcCall = goldenCut ( f_alpha, 0 ,3 )

    funcCalls += funcCall

    new_x = x - ( alpha_opt * grad_x )
    new_y = y - ( alpha_opt * grad_y )

    print ( f"Iteration 0: lr = {alpha_opt}, x = {x}, y = {y}, F(x, y) = { function ( x, y )}" )

    while distance ( ( x, y ), ( new_x, new_y ) ) >= tol:

        plt.scatter(x, y, color = 'r', s = 1)

        iteration += 1
        
        x, y = new_x, new_y

        print ( f"Iteration {iteration}: lr = {alpha_opt}, x = {x}, y = {y}, F(x, y) = { function ( x, y ) }")

        grad_x = gradient_x ( x, y )
        grad_y = gradient_y ( x, y )

        alpha_opt, funcCall = goldenCut ( f_alpha, 0 ,3 )

        funcCalls += funcCall

        new_x = x - ( alpha_opt * grad_x )
        new_y = y - ( alpha_opt * grad_y )

    #plt.show()

    x, y = new_x, new_y

    plt.scatter ( x, y, color = 'r', s = 1 )

    return x, y, iteration, ( ( iteration * 2 ) + 2 ) + funcCalls

def function ( x, y ):
    return - ( x * y / 8 ) * ( 1 - x - y )

def gradient_x ( x, y ):
    return - ( y - ( 2 * x * y ) - ( y ** 2 ) ) / 8

def gradient_y ( x, y ):
    return - ( x - ( x ** 2 ) - ( 2 * x * y ) ) / 8

rez = fastest_descent ( ( (1), (1) ), 1e-4 )

print ( rez )    

plt.show()

