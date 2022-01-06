import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import unittest

from pathfind.pathfind import *


class GridMap5x5Test(unittest.TestCase):
	"""
	Test methods inside GridMap class.
	"""

	def setUp(self):
		"""
		Set up GridMap for testing.
		"""
		A = [[1, 1, 1, 1, 1, 1],
			 [0, 0, 0, 0, 1, 1],
			 [1, 1, 1, 1, 1, 1],
			 [1, 1, 1, 1, 0, 0],
			 [1, 1, 1, 1, 1, 1],
			 [1, 1, 0, 0, 0, 1]]

		self.gridmap5x5 = GridMap(A)

		B = [[1, 1, 1, 1, 1, 1],
			 [1, 1, 1, 1, 1, 1],
			 [0, 0, 0, 0, 0, 0],
			 [1, 1, 1, 1, 1, 1],
			 [1, 1, 1, 1, 1, 1],
			 [1, 1, 1, 1, 1, 1]]

		self.bisected_gridmap = GridMap(B)


	def test_is_valid_node(self):
		"""
		Test that is_valid_node returns expected values for various
		cases.
		"""
		
		# Traversable nodes -> True
		self.assertTrue(self.gridmap5x5.is_valid_node(Node([0, 0])))
		self.assertTrue(self.gridmap5x5.is_valid_node(Node([2, 2])))
		
		# Untraversable nodes -> False
		self.assertFalse(self.gridmap5x5.is_valid_node(Node([0, 1])))
		self.assertFalse(self.gridmap5x5.is_valid_node(Node([3, 5])))
		
		# Off grid nodes -> False
		self.assertFalse(self.gridmap5x5.is_valid_node(Node([0, -1])))
		self.assertFalse(self.gridmap5x5.is_valid_node(Node([6, 6])))

	
	def test_get_neighbours(self):
		"""
		Test that get_neighbours returns expected values for various
		cases.
		"""
		
		# Next to obstacle
		expected1 = sorted([node.pos for node in [Node([1, 2]), Node([3, 2]), Node([2, 3])]])
		output1 = sorted([node.pos for node in self.gridmap5x5.get_neighbours(Node([2, 2]))])
		
		self.assertEqual(expected1, output1)

		# Edge of grid, next to obstacle
		expected2 = [Node([5, 4])]
		output2 = self.gridmap5x5.get_neighbours(Node([5, 5]))
		
		self.assertEqual(expected1, output1)


	def test_find_shortest_path(self):
		"""
		Tests that find_shortest_path returns expected values for various cases.
		"""
		
		# Test "normal" findable paths
		self.assertEqual(PathFind.find_shortest_path(self.gridmap5x5, [0, 0], [5, 5]), 12)
		self.assertEqual(PathFind.find_shortest_path(self.gridmap5x5, [1, 5], [5, 5]), 6)

		# Test where P, Q are the same -> 0
		self.assertEqual(PathFind.find_shortest_path(self.gridmap5x5, [0, 0], [0, 0]), 0)
		
		# Test exception raised if input nodes are untraversable
		with self.assertRaises(AssertionError):
			self.assertRaises(PathFind.find_shortest_path(self.gridmap5x5, [0, 1], [1, 2]))
			self.assertRaises(PathFind.find_shortest_path(self.gridmap5x5, [1, 2], [0, 1]))

		# Test output is correct for unreachable nodes
		self.assertEqual(PathFind.find_shortest_path(self.bisected_gridmap, [0, 0], [5, 5]), "<node unreachable>")


# Run tests
def run():
	unittest.main(verbosity=2)

run()
