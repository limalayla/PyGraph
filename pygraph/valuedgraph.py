from graph import Graph

class ValuedGraph(Graph):
	"""
	Same as graph but:
		- Absence of edge is None, not 0
		- Edges are a 3-uplets (in, out[, value]). If no value is given, then 0 is assumed
	"""
	@Graph._no_edge.getter
	def _no_edge(self):
		return None
	
	def __init__(self, nodes, valued_edges):
		Graph.__init__(self, nodes, [])
		
		for i, j, value in [self._index_of(x[0], x[1]) + (x[2] if len(x) == 3 else 0,) for x in valued_edges]:
			self._adj_mat[i, j] = value
