from graph import Graph
from marknode import MarkNode

class MarkGraph(Graph):
	__no_mark = None
	
	def __init__(self, nodes, edges, marks= []):
		Graph.__init__(self, nodes, edges)
		
		if len(marks) == 0:
			marks = [self.__no_mark] * self.nNode
		
		if len(marks) != self.nNode:
			raise ArgumentError("Lengths of nodes and marks differ")
		
		self._marks = marks
	
	def add(self, node):
		Graph.add(node)
		self._marks.append(self.__no_mark)
	
	def del_node(self, node):
		i = self._index_of(node)
		del self._marks[i]
		Graph.del_node(self, node)
	
	def __getitem__(self, node):
		if len(node) == 1:
			i = self._index_of(node)
			return MarkNode(node, self._marks[i], self.predecessor(node, False), self.successor(node, False))
		else:
			return Graph.__getitem__(self, node)


	def mark(self, node, mark):
		i = self._index_of(node)
		self._marks[i] = mark

	def unmark(self, node):
		self.mark(node, self.__no_mark)
