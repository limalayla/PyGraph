from operator import itemgetter
import numpy as np

from node import Node

def th(x):
	return str(x) + {
		1: "st",
		2: "st",
		3: "rd"
	}.get(str(x)[-1], "th")

class Graph:
	"""
	Todo:
		Nodes to be either an array of string/char or an integer (then create an array of string/char with range())
		Handle orientation mode
		Handle valuated edges
	
	Graph representation:
		- Adjacency Matrix:
			* Works for oriented/non-oriented and valued/non-valued graphs.
			* Useful feature: mat**n
			* Its simplicity and versatility is worth the memory cost.
			
	"""
	
	def __init__(self, nodes, edges):
		self._adj_mat = np.matrix(np.zeros((len(nodes), len(nodes))))
		self._names = nodes
		
		for x, y in [self._index_of(i, j) for i, j in edges]:
			self._adj_mat[x, y] = 1
	
	
	def _index_of(self, node, *args):
		is_list, have_opt_args = isinstance(node, (tuple, list)), len(args) != 0
		
		if is_list and have_opt_args:
			raise ArgumentError("Either node is a tuple/list or multiple nodes are given")
		
		if is_list or have_opt_args:
			return tuple([self._index_of(x) for x in tuple(node)+args])
		else:
			try:
				return self._names.index(node)
			except ValueError as e:
				raise IndexError("The graph doesn't contain a node labeled {}".format(node)) from e
	
	
	def _name_of(self, index, *args):
		is_list, have_opt_args = isinstance(index, (tuple, list)), len(args) != 0
		
		if is_list and have_opt_args:
			raise ArgumentError("Either index is a tuple/list or multiple indexes are given")
		
		if is_list or have_opt_args:
			return tuple([self._name_of(x) for x in tuple(index)+args])
		else:
			try:
				return self._names[node]
			except IndexError as e:
				raise IndexError("The graph doesn't have an {} node".format(th(index))) from e
	
	@property
	def nNode(self):
		return self._adj_mat.shape[0]
	
	@property
	def nEdge(self):
		return len([x for x in self._adj_mat.A1 if x != 0])
	
	
	def add(self, node):
		nNodes = self.nNode
		self._adj_mat = np.column_stack([self._adj_mat, [0]*nNodes])
		self._adj_mat = np.row_stack   ([self._adj_mat, [0]*nNodes])
	
	def del_node(self, node):
		i = self._index_of(node)
		self._adj_mat = np.delete(self._adj_mat, i, axis=0)
		self._adj_mat = np.delete(self._adj_mat, i, axis=1)
		
		del self._names[i]
	
	def del_edge(self, index):
		self[index] = 0
	
	
	def predecessor(self, node, named= True):
		i = self._index_of(node)
		
		# Extract indexes from the matrix
		indexes = [x for x, y in enumerate(self._adj_mat[:, i].A1) if y != 0]
		
		return [self._name_of(x) for x in indexes] if named else indexes
	
	
	def successor(self, node, named= True):
		i = self._index_of(node)
		
		# Extract indexes from the matrix
		indexes = [x for x, y in enumerate(self._adj_mat[i, :].A1) if y != 0]
		
		return [self._name_of(x) for x in indexes] if named else indexes
	
	
	def __getitem__(self, index):
		"""
		Return: - Representation of the node (see class Node) if index is a singleton
				- Value of the edge between index[0] and index[1] if index have two elements 
		"""
		
		if len(index) > 2:
			raise ArgumentError("Index must be at most of size 2")
			
		elif len(index) == 1:
			return Node(index, self.predecessor(index, False), self.successor(index, False))
		
		else:
			i, j = self._index_of(index)
			return self._adj_mat[i, j]
	
	def __setitem__(self, index, value):
		if len(index) != 2:
			raise ArgumentError("Index must be of size 2")
		
		i, j = self._index_of(index)
		self._adj_mat[i, j] = value
		
	def __delitem__(self, index):
		if len(index) == 1:
			self.del_node(index) 
		else:
			self.del_edge(index)
		
	def __len__(self):
		return [self.nNode, self.nEdge]
	
	def __repr__(self):
		return str(self._adj_mat)
