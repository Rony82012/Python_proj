#rotation of matrix by 90 degrees

def rotate(matrix):
	if matrix is None or len(matrix) < 1:
		return None
	else:
		if len(matrix) == 1:
			return matrix
		else:
			matsol = [row[:] for row in matrix]
			m = len(matrix[0])

			for x in range(0,m):
				for j in range(0,m):
					matsol[j][m-1-x] = matrix[x][j]
			return matsol


'''
__main.py__ example
from matrixshift import rotate

threem = [['a','b','c'],
		[1,2,3],
		['x','y','z']]
print('%s' % rotate(threem))

expected answer:
[['x',1,'a'],['y',2,'b'],['z',3,'c']]
'''