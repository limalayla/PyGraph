from node import Node

class MarkNode(Node):
	def __init__(self, name, mark, predecessors, successors):
		Node.__init__(self, name, predecessors, successors)
		
		self._mark = mark
	
	@property
	def mark(self):
		return self._mark
