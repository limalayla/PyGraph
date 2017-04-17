# PyGraph

Yet another Graph's Theory implementation for Python, this time aimed at readability and ease of use.

_(On a side note, this library is educational in the first place. Feel free to point out improvements, I'll gladly take them into acount :simple_smile:)_

## Features
- [x] Oriented Graph
- [ ] Non-Oriented Graph
- [ ] Valued Graph
- [ ] Paths
- [ ] Algorithms
- [ ] Visualization

## Use
```Python
from graph import Graph

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
```

See `demo.py` for complete up-to-date exemples. 

## Todo
- [ ] Documentation
