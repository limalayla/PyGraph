from graph import Graph

if __name__ == "__main__":
	a, b, c, d = 'a', 'b', 'c', 'd'
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
