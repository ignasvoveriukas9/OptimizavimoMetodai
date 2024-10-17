import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gradient_descent ( start, lr, tol ):

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

    x, y = start

    grad_x = gradient_x ( x, y )
    grad_y = gradient_y ( x, y )

    new_x = x - ( lr * grad_x )
    new_y = y - ( lr * grad_y )

    while abs ( new_x - x ) >= tol and abs ( new_y - y ) >= tol:

        ax.scatter(x, y, function (x, y), color = 'r', s = 1)

        iteration += 1
        
        x, y = new_x, new_y

        print ( f"Iteration {iteration}: x = {x}, y = {y}, F(x, y) = { function ( x, y ) }")

        grad_x = gradient_x ( x, y )
        grad_y = gradient_y ( x, y )

        new_x = x - ( lr * grad_x )
        new_y = y - ( lr * grad_y )

    plt.show()

    return x, y, iteration

def function ( x, y ):
    return - ( x * y / 8 ) * ( 1 - x - y )

def gradient_x ( x, y ):
    return - ( y - ( 2 * x * y ) - ( y ** 2 ) ) / 8

def gradient_y ( x, y ):
    return - ( x - ( x ** 2 ) - ( 2 * x * y ) ) / 8

rez = gradient_descent ( ( (1), (1) ), 0.5, 1e-4 )

print ( rez )    

