# Python: Double Weighted Graph
## KSAT List
This question is intended to evaluate the following topics:
- S0054: Create and destroy a Weighted Graph.
- S0063: Find item in a Weighted Graph.
- S0064: Add and remove nodes from a a Weighted Graph.
- S0379: Demonstrate ability to write object-oriented programs
- S0048: Implement a function that receives input parameters.

## Tasks
Implement a class `WeightedGraph` that applies a weighted, directional graph. 

- The class may be implemented with any method as long as the below functions have their criteria met. 
- You are free to implement any additional classes if your solution requires it.
- **YOU MAY NOT USE ANOTHER MODULE TO IMPLEMENT THE GRAPH FOR YOU**.

### Task 1
Create a default constructor with no parameters that sets up the class.

**PARAMETERS:**
- This function has no parameters

**RETURN:** None

### Task 2
Implement the function `add_node` that adds a node to a position in the graph.

**PARAMETERS:**
1. `node_id`: An index value for the node
2. `value`: Value to store within the node

**RETURN:** None

### Task 3
Implement the function `add_edge` that creates an edge FROM a source node TO a destination node in the graph, with a 
weight to travel between nodes. 

**PARAMETERS:**
1. `source`: The node where the edge begins
2. `dest`: The node where the edge ends
3. `cost`: The weight of the edge traveling from `source` to `dest`

**RETURN:** None

- Nodes must support multiple edges. 
- Edges must be one-way. 
- You may need to update your solution to accommodate this.

### Task 4
Implement the function `delete_node` that removes a node with the specified index from the graph, as well as all edges 
connected to that node. 

**PARAMETERS:**
1. `node_id`: An index value for the node

**RETURN:** None

- If a node does not exist, the function needs to handle that case and not throw an exception.

### Task 5
Implement the function `get_nodes` that returns a list of nodes in the graph.

**PARAMETERS:**
- This function has no parameters

**RETURN:** A list of tuples, each with the format (index, value)

### Task 6
Implement the function `get_edges` that returns a list of all edges in the graph.

**PARAMETERS:**
- This function has no parameters

**RETURN:** A list of tuples, each with the format (source_node_index, dest_node_index, cost)

## Task 7
Implement the function `traverse` so it uses a greedy depth first search to traverse the graph from the start node to 
the end node, choosing the shortest possible edge at each step.

**PARAMETERS:**
1. `start`: The node index where traversal begins
2. `end`: The node index to search a path towards

**RETURN:** The path taken as a list in order of traversal; return `None` if there is no valid path or either node does 
not exist.

- Assume no ties in weight.
- Only nodes along the path should be included in the traversal list.

## Testing
To test your code, follow the [Run Python and Networking instructions](https://gitlab.com/90cos/cyv/cyber-capability-developer-ccd/ccd-master-question-file/-/blob/master/performance/exam_files/compile-instructions.md).
