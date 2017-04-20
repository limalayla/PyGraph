from operator import itemgetter
import numpy as np

from node import Node

def th(x):
	return str(x) + {
		1: "st",
		2: "st",
		3: "rd"
	}.get(str(x)[-1], "th")

class Graph(object):
	"""
	Todo:
		Nodes to be either an array of string/char or an integer (then create an array of string/char with range())
		Handle orientation mode
		Handle valuated edges
	
	Graph representation:
		- Adjacency Matrix:
			* Works for oriented/non-oriented and valued/non-valued graphs.
			* Useful feature: mat**n computes paths from node_i to node_j of length n at most
			* Its simplicity and versatility is worth the memory cost.
			
	"""
	
	@property
	def _no_edge(self):
		return 0
	
	def __init__(self, nodes, edges):
		n = len(nodes)
				
		self._adj_mat = np.matrix([[self._no_edge]*n ]*n)
		self._names = nodes
		
		for i, j in [self._index_of(x, y) for x, y in edges]:
			self._adj_mat[i, j] = 1
	
	
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
		return len([x for x in self._adj_mat.A1 if x != self._no_edge])
	
	
	def add(self, node):
		nNodes = self.nNode
		self._adj_mat = np.column_stack([self._adj_mat, [self._no_edge]*nNodes])
		self._adj_mat = np.row_stack   ([self._adj_mat, [self._no_edge]*nNodes])
		self._names.append(node)
		self._names.append(node)
	
	def del_node(self, node):
		i = self._index_of(node)
		self._adj_mat = np.delete(self._adj_mat, i, axis=0)
		self._adj_mat = np.delete(self._adj_mat, i, axis=1)
		
		del self._names[i]
	
	def del_edge(self, index):
		self[index] = self._no_edge
	
	
	def predecessor(self, node, named= True):
		i = self._index_of(node)
		
		# Extract indexes from the matrix
		indexes = [x for x, y in enumerate(self._adj_mat[:, i].A1) if y != self._no_edge]
		
		return [self._name_of(x) for x in indexes] if named else indexes
	
	
	def successor(self, node, named= True):
		i = self._index_of(node)
		
		# Extract indexes from the matrix
		indexes = [x for x, y in enumerate(self._adj_mat[i, :].A1) if y != self._no_edge]
		
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
	
	
	def __pow__(self, other):
		# Will raise a TypeError if other isn't an integer, numpy's matrices handles this behavior
		self._adj_mat **= other
		
	def __len__(self):
		return [self.nNode, self.nEdge]
	
	def __repr__(self):
		return str(self._adj_mat)
