# Types of graph
# Directed and undirected - directions of one node to the next
# Weighted and unweighted - measurements of the edge (e.g. distance from one node to the next)

# Descriptions of directed graphs
# Cyclic and acyclic - describes the flow of the overall graph (i.e. once we move to the next node is it possible to go back?)

# Edge list
# Each element in the array represents an edge, and each subarray represents the nodes connected by that edge
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]


# Adjacent list
# The index (or key of a dict) is a node and the elements in the subarray (or values of a dict) are the nodes connected to that node
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent matrix
# The index (of key of a dict) is a node and the index of the elements in the subarray (or values of a dict of the same subarray) represent the nodes that the node is connected to, "1" (or weighted value), or not, "0".
graph = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
]
