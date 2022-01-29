import unittest
import linearalgebra
import numpy as np
import math

class TestAlgebra(unittest.TestCase):

	def test_addone(self):
		self.assertEqual(linearalgebra.addone(8), 9)
		self.assertEqual(linearalgebra.addone(0), 1)
		self.assertEqual(linearalgebra.addone(-1), 0)
		self.assertEqual(linearalgebra.addone(789), 790)

	def test_square(self):
		self.assertEqual(linearalgebra.square(0), 0)
		self.assertEqual(linearalgebra.square(1), 1)
		self.assertEqual(linearalgebra.square(3), 9)
		self.assertEqual(linearalgebra.square(-4), 16)
		self.assertEqual(linearalgebra.square(5), 25)

	def test_cube(self):
		self.assertEqual(linearalgebra.cube(0), 0)
		self.assertEqual(linearalgebra.cube(1), 1)
		self.assertEqual(linearalgebra.cube(2), 8)
		self.assertEqual(linearalgebra.cube(-2), -8)
		self.assertEqual(linearalgebra.cube(3), 27)
		self.assertEqual(linearalgebra.cube(-3), -27)

	def test_absolute(self):
		self.assertEqual(linearalgebra.absolute(0), 0)
		self.assertEqual(linearalgebra.absolute(2), 2)
		self.assertEqual(linearalgebra.absolute(3), 3)
		self.assertEqual(linearalgebra.absolute(-4), 4)
		self.assertEqual(linearalgebra.absolute(-25), 25)

	def test_evensum(self):
		self.assertEqual(linearalgebra.EvenSum(0,0), 0)
		self.assertEqual(linearalgebra.EvenSum(1,1), 2)
		self.assertEqual(linearalgebra.EvenSum(4,2), 6)
		self.assertEqual(linearalgebra.EvenSum(-1,3), 2)
		self.assertEqual(linearalgebra.EvenSum(6,2), 8)
		self.assertEqual(linearalgebra.EvenSum(-6,4), -2)
		self.assertEqual(linearalgebra.EvenSum(6,8), 14)

		self.assertFalse(linearalgebra.EvenSum(3,4))
		self.assertFalse(linearalgebra.EvenSum(5,4))
		self.assertFalse(linearalgebra.EvenSum(0,7))
		self.assertFalse(linearalgebra.EvenSum(-1,4))


class TestLinearAlgebra(unittest.TestCase):

	def test_AddMatrix(self):
		self.assertEqual(linearalgebra.AddMatrix([[1,2],[3,4]],[[0,0],[0,0]]), [[1,2],[3,4]])
		self.assertEqual(linearalgebra.AddMatrix([[1,2],[3,4]],[[1,1],[2,2]]), [[2,3],[5,6]])
		self.assertEqual(linearalgebra.AddMatrix([[1,2,3],[4,5,6]],[[1,1,1],[2,2,2]]), [[2,3,4],[6,7,8]])
		self.assertFalse(linearalgebra.AddMatrix([[1,2],[3,4]],[[1,1,1],[2,2,2]]))

	def test_MultiplyMatrix(self):
		A = [[1,2],[3,4]]
		B = [[1,1],[2,2]]
		C = [[1,1,1], [2,2,2]]
		D = [[1,2],[3,4],[5,6]]
		E = [[2,3,-4], [5,-6,7], [8,-9,10]]
		self.assertEqual(linearalgebra.MultiplyMatrix([[1,2],[3,4]],[[0,0],[0,0]]), [[0,0],[0,0]])
		self.assertEqual(linearalgebra.MultiplyMatrix([[1,2],[3,4]],[[1,0],[0,1]]), [[1,2],[3,4]])
		self.assertEqual(linearalgebra.MultiplyMatrix([[1,2],[3,4]],[[1,1],[2,2]]), [[5,5],[11,11]])
		self.assertEqual(linearalgebra.MultiplyMatrix(A,B), np.matmul(A,B).tolist())
		self.assertEqual(linearalgebra.MultiplyMatrix(A,C), np.matmul(A,C).tolist())
		self.assertFalse(linearalgebra.MultiplyMatrix(D,E))
		self.assertFalse(linearalgebra.MultiplyMatrix(A,E))

	def test_Determinant(self):
		A = [[1,2],[3,4]]
		B = [[1,1],[2,2]]
		C = [[1,1,1], [2,2,2]]
		D = [[1,2],[3,4],[5,6]]
		E = [[2,3,-4], [5,-6,7], [8,-9,10]]
		F = [[6,7,8],[1,1,1],[7,8,9]]

		self.assertEqual(linearalgebra.Det(A), round(np.linalg.det(A)))
		self.assertEqual(linearalgebra.Det(B), round(np.linalg.det(B)))
		self.assertEqual(linearalgebra.Det(E), round(np.linalg.det(E)))
		self.assertEqual(linearalgebra.Det(F), 0)
		self.assertFalse(linearalgebra.Det(D))

'''	
	def test_Transpose(self):
		A = [[1,2],[3,4]]
		B = [[1,1],[2,2]]
		C = [[1,1,1], [2,2,2]]
		D = [[1,2],[3,4],[5,6]]
		E = [[2,3,-4], [5,-6,7], [8,-9,10]]
		I = [[1,0,0],[0,1,0],[0,0,1]]
		self.assertEqual(linearalgebra.Transpose(A), np.transpose(A).tolist())
		self.assertEqual(linearalgebra.Transpose(D), np.transpose(D).tolist())
		self.assertEqual(linearalgebra.Transpose(E), np.transpose(E).tolist())
		self.assertEqual(linearalgebra.Transpose(I), I)

	def test_ColDependent(self):
		A = [[1,2],[3,4]]
		B = [[1,5],[2,10]]
		C = [[1,1,1], [2,2,2], [-1,5,8]]
		D = [[1,2,3],[0,0,1],[1,0,0]]
		E = [[2,3,4], [1,1,1], [3,4,5]]
		I = [[1,0,0],[0,1,0],[0,0,1]]
		self.assertFalse(linearalgebra.ColDependent(A))
		self.assertTrue(linearalgebra.ColDependent(B))
		self.assertTrue(linearalgebra.ColDependent(C))
		self.assertFalse(linearalgebra.ColDependent(D))
		self.assertTrue(linearalgebra.ColDependent(E))
		self.assertFalse(linearalgebra.ColDependent(I))

	def test_EigenValues(self):
		A = [[3,0],[0,5]]
		B = [[-2,0],[0,3]]
		C = [[0,1],[-2,-3]]
		D = [[-5,2],[-7,4]]
		E = [[1,2,3],[4,5,6]]
		F = [[2,2],[1,3]]
		G = [[1,-1],[1,1]]
		self.assertEqual(linearalgebra.EigenValues(A), [3,5])
		self.assertEqual(linearalgebra.EigenValues(B), [-2,3])
		self.assertEqual(linearalgebra.EigenValues(C), [-2,-1])
		self.assertEqual(linearalgebra.EigenValues(D), [-3,2])
		self.assertEqual(linearalgebra.EigenValues(F), [1,4])
		self.assertFalse(linearalgebra.EigenValues(E))
		self.assertFalse(linearalgebra.EigenValues(G))

	def test_Rotate(self):
		i = [1,0]
		j = [0,1]
		v = [3,3]
		w = [-5,5]
		k = [1,1]
		z = [2,0]
		
		self.assertEqual(linearalgebra.Rotate(i, 90 ), j)
		self.assertEqual(linearalgebra.Rotate(j, 90), [-1,0])
		self.assertEqual(linearalgebra.Rotate(j, -90), i)
		self.assertEqual(linearalgebra.Rotate(v, 90), [-3,3])
		self.assertEqual(linearalgebra.Rotate(w, 180), [5,-5])
		self.assertEqual(linearalgebra.Rotate(w, -90), [5,5])
		self.assertEqual(linearalgebra.Rotate(k, 45), [0,round(math.sqrt(2),2)])
		self.assertEqual(linearalgebra.Rotate(z, 30), [round(math.sqrt(3),2), 1])
'''
if __name__ == '__main__':
    unittest.main()
