import numpy as np
import math

def simplex( matrix ):
    
    base = [ 5, 6, 7]

    while True:

        print ( matrix )
        print ( base )

        addToBase = whichToAdd ( matrix [0] )

        print ( addToBase )

        if addToBase == -1:
            return matrix [0]

        removeFromBase = whichToRemove ( matrix, base, addToBase )

        print ( removeFromBase )

        matrix, base = switchBase ( matrix, base, addToBase, removeFromBase )



def whichToAdd ( row ):

    for i, value in enumerate ( row ):
        if value < 0 and i != 0:
            return i 
                
    return -1

def whichToRemove ( matrix, base, addToBase ):

    #remove = ( 0, matrix [1][0] / matrix [1][addToBase]  )
    remove = ( -1, math.inf )

    for i, baseValue in enumerate ( base ):
        if matrix [ i + 1 ] [ addToBase ] > 0:
            if matrix [ i + 1 ] [ 0 ] / matrix [ i + 1 ] [ addToBase ] < remove [ 1 ]:
                remove = ( i, matrix [ i + 1 ] [ 0 ] / matrix [ i + 1 ] [ addToBase ] )

    return remove[0]

def switchBase ( matrix, base, addToBase, removeFromBase ):

    divisor = matrix [ removeFromBase + 1 ][ addToBase ]

    newRow = []

    for x in matrix [ removeFromBase + 1 ]:
        newRow.append ( x / divisor )

    matrix [ removeFromBase + 1 ] = newRow

    for i, row in enumerate ( matrix ):
        newRow = []
        if i != ( removeFromBase + 1 ):
            rowMultiplier = row [ addToBase ]
            for j, value in enumerate ( row ):
                newRow.append ( value - ( matrix [ removeFromBase + 1 ] [ j ] * rowMultiplier ) )
            matrix [ i ] = newRow

    base [ removeFromBase ] = addToBase

    return matrix, base


orgMatrix = [
        [ 0.0,  2.0, -3.0,  0.0, -5.0, 0.0, 0.0, 0.0],
        [ 8.0, -1.0,  1.0, -1.0, -1.0, 1.0, 0.0, 0.0],
        [10.0,  2.0,  4.0,  0.0,  0.0, 0.0, 1.0, 0.0],
        [ 3.0,  0.0,  0.0,  1.0,  1.0, 0.0, 0.0, 1.0]
        ]

#print ( whichToRemove (orgMatrix, [5, 6, 7], whichToAdd (orgMatrix[0]) ) )
#print ( switchBase ( orgMatrix, [5, 6, 7], 2, 1 ) )
print ( simplex ( orgMatrix ) )

