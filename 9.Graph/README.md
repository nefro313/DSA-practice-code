# Graph Data Structure and Algorithms

## Introduction to Graph Theory

A **graph** is a fundamental data structure in computer science that consists of a set of **nodes** (also called **vertices**) and a set of **edges** that connect pairs of nodes. Graphs are used to model relationships between objects and are widely applicable in various domains, such as social networks, computer networks, route planning, and more.

### Types of Graphs
There are several types of graphs, including:

*   **Undirected Graph**: Edges have no orientation; they are two-way connections. If an edge connects node A to node B, it also connects node B to node A.
*   **Directed Graph (Digraph)**: Edges have a direction. An edge from node A to node B does not necessarily imply an edge from node B to node A.
*   **Weighted Graph**: Each edge has an associated numerical value, called a weight or cost. This can represent distance, time, capacity, etc.
*   **Unweighted Graph**: Edges do not have weights. The implementation in `index.py` primarily deals with unweighted graphs, although the concept of weight is crucial for many graph algorithms like Dijkstra's.

## Graph Implementation (`index.py`)

The `index.py` file in this directory provides a Python implementation of a graph data structure.

### Representation: Adjacency List
The graph is represented using an **adjacency list**. This is a collection of lists, where each list corresponds to a node in the graph and contains all its adjacent nodes (neighbors). For an unweighted graph, this is efficient in terms of space, especially for sparse graphs (graphs with relatively few edges). Our implementation uses a Python dictionary where keys are nodes and values are lists of their neighbors (`collections.defaultdict(list)`).

### `Graph` Class Methods

*   **`__init__(self)`**:
    Initializes an empty graph. It creates a `defaultdict(list)` to store adjacency lists and a `set` (`self.nodes`) to keep track of all unique nodes added to the graph.

*   **`add_edge(self, u, v, directed=False)`**:
    Adds an edge between node `u` and node `v`.
    *   `u`: The source node.
    *   `v`: The destination node.
    *   `directed` (boolean): If `False` (default), the edge is undirected (u -- v). If `True`, the edge is directed (u -> v).
    Both `u` and `v` are added to the `self.nodes` set to ensure all nodes are tracked.

*   **`display_graph(self)`**:
    Prints the adjacency list representation of the graph. It iterates through all known nodes (from `self.nodes`, sorted for consistent output) and prints each node followed by its list of neighbors (also sorted for consistency).

### Example: Creating a Graph

```python
# Assuming the Graph class is imported from index.py
# from index import Graph # Or similar depending on execution context

# Create a graph instance
# g = Graph() # This would be how you use it if the class is imported

# Example (conceptual, as if running directly or imported):
# g.add_edge('A', 'B')         # Undirected edge A -- B
# g.add_edge('B', 'C', directed=True) # Directed edge B -> C
# g.add_edge('A', 'C')

# g.display_graph()
# Expected output (if A, B, C were added in this order and neighbors sorted):
# Graph Adjacency List:
# A: ['B', 'C']
# B: ['A', 'C']
# C: ['A'] (if A-C was undirected) or C:[] if only B->C and A-C was directed A->C
# Actual output depends on the exact sequence and directed flags.
# Refer to index.py for runnable examples.
```
To see this in action, run `python 9.Graph/index.py`. The script itself contains detailed examples.

## Graph Traversal Algorithms

Graph traversal refers to the process of visiting (checking and/or updating) each node in a graph. The `index.py` implementation includes Breadth-First Search (BFS) and Depth-First Search (DFS).

### Breadth-First Search (BFS)

*   **Explanation**:
    BFS is an algorithm for traversing or searching tree or graph data structures. It starts at a selected node (source node) and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. It explores the graph layer by layer. BFS is often used to find the shortest path in an unweighted graph.

*   **Time and Space Complexity**:
    *   Time Complexity: `O(V + E)`, where V is the number of vertices (nodes) and E is the number of edges.
    *   Space Complexity: `O(V)` in the worst case (for storing the queue and the set of visited nodes).

*   **Usage Example (from `index.py`)**:
    ```python
    # g is an instance of the Graph class, already populated with nodes and edges.
    # bfs_path = g.bfs(start_node='A') # Replace 'A' with an actual start node
    # print(f"BFS traversal from 'A': {bfs_path}")

    # Example output from index.py for g.bfs(0):
    # BFS starting from node 0: [0, 1, 2, 3, 4]
    ```

### Depth-First Search (DFS)

*   **Explanation**:
    DFS is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at a selected node (root node) and explores as far as possible along each branch before backtracking. It uses a stack (either explicitly or implicitly via recursion) to keep track of nodes to visit.

*   **Time and Space Complexity**:
    *   Time Complexity: `O(V + E)`, where V is the number of vertices and E is the number of edges.
    *   Space Complexity: `O(V)` in the worst case (for the stack depth in a skewed graph and the set of visited nodes).

*   **Usage Example (from `index.py`)**:
    ```python
    # g is an instance of the Graph class.
    # dfs_path = g.dfs(start_node='A') # Replace 'A' with an actual start node
    # print(f"DFS traversal from 'A': {dfs_path}")

    # Example output from index.py for g.dfs(0):
    # DFS starting from node 0: [0, 1, 2, 3, 4] 
    # (Note: Exact DFS path can vary based on neighbor processing order.
    # The implementation in index.py sorts neighbors to make output deterministic.)
    ```

## LeetCode Problem: Number of Islands (LeetCode 200)

The file `9.Graph/leetcode_problem.py` contains a solution for the LeetCode problem 200, "Number of Islands".

### Problem Description
Given an `m x n` 2D binary grid where `'1'` represents land and `'0'` represents water, the task is to count the number of islands. An island is formed by connecting adjacent (horizontally or vertically) land cells and is surrounded by water.

### Solution Approach using Graph Traversal
This problem can be modeled as finding connected components in a graph. Each '1' cell is a node. An edge exists between adjacent '1's.
The solution iterates through each cell of the grid:
1.  If a cell `(r, c)` contains a `'1'` (land) and hasn't been visited yet:
    *   It signifies a new island, so increment an `island_count`.
    *   Start a graph traversal (BFS or DFS) from `(r, c)`.
    *   During the traversal, visit all connected land cells (`'1's`) that are part of this island.
    *   Mark visited land cells (e.g., by changing their value from `'1'` to `'0'`, or by using an auxiliary `visited` grid) to ensure they are not processed again.
2.  Continue until all cells have been checked. The final `island_count` is the answer.
The provided solution in `leetcode_problem.py` uses BFS and modifies the grid in-place to mark visited land cells.

### Usage Example (from `leetcode_problem.py`)
```python
# from leetcode_problem import Solution # Assuming Solution class is imported

# solver = Solution()
# example_grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# num_of_islands = solver.numIslands(example_grid)
# print(f"Number of islands: {num_of_islands}") # Expected: 1
```

## How to Run the Code

You can run the Python scripts directly from your terminal. Ensure you have Python installed.

1.  **To run the graph implementation examples (`index.py`):**
    Navigate to the project's root directory or the `9.Graph` directory.
    ```bash
    python 9.Graph/index.py
    ```
    If you are already inside the `9.Graph` directory:
    ```bash
    python index.py
    ```
    This script will demonstrate graph creation, display, BFS, and DFS with sample data.

2.  **To run the LeetCode "Number of Islands" solution (`leetcode_problem.py`):**
    ```bash
    python 9.Graph/leetcode_problem.py
    ```
    If you are already inside the `9.Graph` directory:
    ```bash
    python leetcode_problem.py
    ```
    This script will run the examples defined within it and print the number of islands found.

```
