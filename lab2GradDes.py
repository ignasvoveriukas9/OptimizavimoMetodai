import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gradient_descent ( start, lr, tol ):

    x = np.linspace ( -0.1, 1.1, 500 )
    y = np.linspace ( -0.1, 1.1, 500 )
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

    x, y = start

    grad_x = gradient_x ( x, y )
    grad_y = gradient_y ( x, y )

    new_x = x - ( lr * grad_x )
    new_y = y - ( lr * grad_y )

    print ( f"Iteration 0: x = {x}, y = {y}, F(x, y) = {function (x,y)}" )

    while abs ( new_x - x ) >= tol and abs ( new_y - y ) >= tol:

        plt.scatter(x, y, color = 'r', s = 1)

        iteration += 1
        
        x, y = new_x, new_y

        print ( f"Iteration {iteration}: x = {x}, y = {y}, F(x, y) = { function ( x, y ) }")

        grad_x = gradient_x ( x, y )
        grad_y = gradient_y ( x, y )

        new_x = x - ( lr * grad_x )
        new_y = y - ( lr * grad_y )

    x, y = new_x, new_y
    plt.scatter(x, y, color = 'r', s = 1)

    return x, y, iteration

def function ( x, y ):
    return - ( x * y / 8 ) * ( 1 - x - y )

def gradient_x ( x, y ):
    return - ( y - ( 2 * x * y ) - ( y ** 2 ) ) / 8

def gradient_y ( x, y ):
    return - ( x - ( x ** 2 ) - ( 2 * x * y ) ) / 8

rez = gradient_descent ( ( (1), (1) ), 2.5, 1e-4 )

print ( rez ) 

plt.show()

