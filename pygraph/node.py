class Node:
	"""
	Temporary representation of a node, not a mean of storing data (which is Graph's role)
	"""
	
	def __init__(self, name, predecessors, successors):
		self._name = name
		self._predecessors = predecessors
		self._successors = successors
	
	@property
	def name(self):
		return self._name
	
	@property
	def pre(self, edge_format= True):
		return self._predecessors[:]
	
	@property
	def named_pre(self):
		return [(self._name, x) for x in self._predecessors]
	
	@property
	def suc(self, edge_format= True):
		return self._successors[:]
	
	@property
	def named_suc(self, edge_format= True):
		return [(self._name, x) for x in self._successors]
	
	@property
	def deg_in(self):
		return len(self.pre)
		
	@property
	def deg_out(self):
		return len(self.suc)
	
	@property
	def deg(self):
		return self.deg_in + self.deg_out
