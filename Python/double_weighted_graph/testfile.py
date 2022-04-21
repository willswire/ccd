# Refer to README.md for the problem instructions

class WeightedGraph:

    def __init__(self):
        self.nodes = {}
        self.edges = []
        pass

    def add_node(self, node_id, value):
        self.nodes[node_id] = value
        pass

    def add_edge(self, node_id, dest_id, cost):
        self.edges.append((node_id, dest_id, cost))
        pass

    def delete_node(self, node_id):
        if node_id in self.nodes:
            self.nodes.pop(node_id)
        
        rEdges = []
        for edge in self.edges:
            if edge[0] == node_id or edge[1] == node_id:
                rEdges.append(edge)

        for rEdge in rEdges:
            self.edges.remove(rEdge)

        pass

    def get_nodes(self):
        res = []
        for key in self.nodes:
            res.append((key, self.nodes[key]))
        return res

    def get_edges(self):
        return self.edges

    def traverse(self, start, end):
        pass

