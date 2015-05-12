# arrays können später nicht mehr verändert weden,
# außerdem mmüssen alle Werte denselben Typ haben
import numpy as np
arr = np.array( ((1,1,1,1,1),(1,2,1,1,1), (1,1,3,1,1),(1,1,1,4,1)) )
# also possible: np.zeros(dimension1,dimesnion2) or np.ones(dimension1,dimension2)
print arr
print arr.ndim #gibt dimension des arrays zurück, also hier 2
print np.cumsum(arr,axis=0)#spalte
print np.cumsum(arr,axis=1)#zeile

#slicing und indexing (starts at 0!!)
#a) integer indexes
print "a"
arr1 = arr[[[1],[2]],[1,3]]# integer indexes?? Official doc:
# array indexing refers to any use of brackets[] to index array values
#source: stackoverflow.com/questions4257394/slicing-of-a-numpy-2d-array-or-how-di-i-extract-an-mxn-submatrix-from-an-nxn-ar
print arr1
#b) slices (basic slicing with start:stop:step parameters???)
print "b"
arr2 = arr[1:3:1, 1::2]
print arr2
#c) boolean arrays
print "arr3"
arr3 = [(arr == 2) | (arr == 1) | (arr == 1) | (arr == 4)]
print arr3

print arr *5 # jedes Element wir dmit dem vektor (5) multipliziert
print "---"
print arr.shape[1]
print arr * np.arange(arr.shape[1]) #arr.shape[1] ergibt 5(Zahl der Spalten), np.arange(5) ergibt einen vektor
# mit dne Werten von 0 bis 4, also eine matrix-vektor-multiplikation
#print arr * np.arange(arr.shape[0]) # funktioniert nicht, da inkompatible Dimensionen
# arr.shape[0] gibt die dimension von arr hinsichtlich zeilen zurück (4)
# in order to broadcast, the size of the trailing axis for both arrays in 
# an operation must either be the same size or one of them must be 1
print arr.T * np.arange(arr.shape[0]) # funkitoniert, da arr transponiert wird
# und somit dimensionsgleichheit auf der trailing axis herrscht

v = (0,1,2,3,4)
print arr * v
print np.multiply(arr, v)# multiplies arguments elementwise