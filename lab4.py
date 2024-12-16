import numpy as np
import math

def simplex( matrix ):
    
    base = [ 5, 6, 7]

    while True:

        #print ( matrix )
        print("Matrix:")
        for row in matrix:
            print ( row )
        print ( "Base" )
        print ( base )

        addToBase = whichToAdd ( matrix [0] )

        print ( "Add to base collum:")
        print ( addToBase )

        if addToBase == -1:
            x1, x2, x3, x4 = 0, 0, 0, 0
            for i, value in enumerate ( base ):
                if value == 1:
                    x1 = matrix [ i + 1 ] [ 0 ]
                elif value == 2:
                    x2 = matrix [ i + 1 ] [ 0 ]
                elif value == 3:
                    x3 = matrix [ i + 1 ] [ 0 ]
                elif value == 4:
                    x4 = matrix [ i + 1 ] [ 0 ]

            return -matrix [0][0], x1, x2, x3, x4

        removeFromBase = whichToRemove ( matrix, base, addToBase )

        print ( "Remove from base (index of base)" )
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

myMatrix = [
        [ 0.0,  2.0, -3.0,  0.0, -5.0, 0.0, 0.0, 0.0],
        [ 6.0, -1.0,  1.0, -1.0, -1.0, 1.0, 0.0, 0.0],
        [3.0,  2.0,  4.0,  0.0,  0.0, 0.0, 1.0, 0.0],
        [ 2.0,  0.0,  0.0,  1.0,  1.0, 0.0, 0.0, 1.0]
        ]


#print ( whichToRemove (orgMatrix, [5, 6, 7], whichToAdd (orgMatrix[0]) ) )
#print ( switchBase ( orgMatrix, [5, 6, 7], 2, 1 ) )
print ( simplex ( myMatrix ) )

