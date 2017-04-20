from graph import Graph
from markgraph import MarkGraph
from valuedgraph import ValuedGraph

if __name__ == "__main__":
	a, b, c, d = 'a', 'b', 'c', 'd'

	def oriented_graph():
		graph = Graph([a, b, c, d], [(a, b), (a, c), (a, d), (c, b), (d, b), (d, c)])

		print("Graph: n={}, m={}".format(graph.nNode, graph.nEdge))
		
		node = graph[c]
		print("Node {}: {} = {}({}) + {}({})".format(node.name, node.deg, node.deg_in, node.pre, node.deg_out, node.suc))
		
		print("[a-b]={}".format(graph[a, b]))
		
		print("\n{}".format(graph))
		del graph[c]
		print("\n{}".format(graph))
		del graph[a, b]
		print("\n{}".format(graph))

	def mark_graph():
		graph = MarkGraph([a, b, c, d], [(a, b), (a, c), (a, d), (c, b), (d, b), (d, c)])

		print("MarkGraph: n={}, m={}".format(graph.nNode, graph.nEdge))
		
		node = graph[c]
		print("Node {} ({}): {} = {}({}) + {}({})".format(node.name, node.mark, node.deg, node.deg_in, node.pre, node.deg_out, node.suc))
		
		print("[a-b]={}".format(graph[a, b]))
		
		print("\n{}".format(graph))
		del graph[c]
		print("\n{}".format(graph))
		del graph[a, b]
		print("\n{}".format(graph))

	def valued_graph():
		graph = ValuedGraph([a, b, c, d], [(a, b, 6), (a, c), (a, d, 0), (c, b, -12), (d, b, "str"), (d, c, "a")])
		
		print("ValuedGraph: n={}, m={}".format(graph.nNode, graph.nEdge))
		
		node = graph[c]
		print("Node {}: {} = {}({}) + {}({})".format(node.name, node.deg, node.deg_in, node.pre, node.deg_out, node.suc))
		
		print("[a-b]={}".format(graph[a, b]))
		
		print("\n{}".format(graph))
		del graph[c]
		print("\n{}".format(graph))
		del graph[a, b]
		print("\n{}".format(graph)) 

	
	oriented_graph()
	print("\n")
	mark_graph()
	print("\n")
	valued_graph()
