import collections

class Graph:
    """
    Represents a graph data structure using an adjacency list.
    Nodes can be any hashable type (e.g., integers, strings).
    """

    def __init__(self):
        """
        Initializes an empty graph.
        The graph is stored as a dictionary where keys are nodes and values are
        lists of their adjacent nodes.
        Using collections.defaultdict(list) simplifies adding edges.
        A separate set self.nodes tracks all nodes ever added to the graph,
        ensuring that even isolated nodes or nodes that are only destinations
        are accounted for.
        """
        self.graph = collections.defaultdict(list)
        self.nodes = set() # Keep track of all nodes explicitly

    def add_edge(self, u, v, directed=False):
        """
        Adds an edge between node u and node v.
        Also ensures that both u and v are registered as nodes in the graph.

        Args:
            u: The source node.
            v: The destination node.
            directed (bool): If True, the edge is directed (u -> v).
                             If False (default), the edge is undirected (u <-> v).
        """
        # Add u and v to the set of all nodes.
        self.nodes.add(u)
        self.nodes.add(v)
        
        # Add the edge from u to v.
        self.graph[u].append(v)

        if not directed:
            # If undirected, also add the reverse edge from v to u.
            self.graph[v].append(u)

    def display_graph(self):
        """
        Prints the adjacency list representation of the graph.
        It lists all nodes that have been added (even if isolated or only destinations),
        followed by their adjacency list. Neighbors are sorted for consistent display.
        """
        print("Graph Adjacency List:")
        if not self.nodes:
            print("Graph is empty.")
            return

        # Sort all known nodes for consistent display order.
        sorted_all_nodes = sorted(list(self.nodes))

        for node in sorted_all_nodes:
            # Accessing self.graph[node] for a node that might only be a destination
            # (and thus not a key in self.graph if it has no outgoing edges) is safe
            # with defaultdict(list) as it will return an empty list.
            # Sorting neighbors ensures the display is deterministic.
            print(f"{node}: {sorted(self.graph[node])}")

    def bfs(self, start_node):
        """
        Performs a Breadth-First Search (BFS) traversal starting from start_node.

        Args:
            start_node: The node from which to start the BFS traversal.

        Returns:
            A list of nodes in the order they were visited by BFS.
            Returns an empty list if the start_node is not in the graph's known nodes.
        """
        if start_node not in self.nodes:
            print(f"Warning: Start node '{start_node}' not found in the graph for BFS.")
            return []
        
        visited_nodes_ordered_list = []
        queue = collections.deque()
        
        # visited_in_queue_set tracks nodes that have been added to the queue,
        # to prevent adding them multiple times and avoid cycles.
        visited_in_queue_set = set() 

        queue.append(start_node)
        visited_in_queue_set.add(start_node)

        while queue:
            current_node = queue.popleft()
            visited_nodes_ordered_list.append(current_node)

            # Sort neighbors for deterministic BFS output. This is primarily for
            # consistent testing and examples. The inherent properties of BFS
            # (like finding shortest paths in unweighted graphs) do not depend
            # on this specific neighbor processing order.
            sorted_neighbors = sorted(self.graph[current_node])

            for neighbor in sorted_neighbors:
                if neighbor not in visited_in_queue_set:
                    visited_in_queue_set.add(neighbor)
                    queue.append(neighbor)
        
        return visited_nodes_ordered_list

    def dfs(self, start_node):
        """
        Performs a Depth-First Search (DFS) traversal starting from start_node.
        Implemented iteratively using a stack.

        Args:
            start_node: The node from which to start the DFS traversal.

        Returns:
            A list of nodes in the order they were visited by DFS.
            Returns an empty list if the start_node is not in the graph's known nodes.
        """
        if start_node not in self.nodes:
            print(f"Warning: Start node '{start_node}' not found in the graph for DFS.")
            return []

        visited_nodes_ordered_list = []
        stack = []  # Using a Python list as a stack.
        
        # processed_nodes_set tracks nodes whose processing has been completed
        # (i.e., they have been popped from stack and their neighbors explored).
        processed_nodes_set = set()

        stack.append(start_node)
        
        while stack:
            current_node = stack.pop()

            # If this node has already been processed, skip it.
            # This is crucial because a node might be added to the stack multiple times
            # by different paths before it's actually processed.
            if current_node in processed_nodes_set:
                continue
            
            # Mark node as processed and add to the result list.
            processed_nodes_set.add(current_node)
            visited_nodes_ordered_list.append(current_node)

            # Add unvisited neighbors to the stack.
            # To achieve a typical DFS exploration pattern (exploring one branch deeply),
            # neighbors are pushed onto the stack in reverse order of how one might
            # want to visit them if they were listed (e.g., sorted).
            # If neighbors are [N1, N2, N3] (sorted), pushing N3, then N2, then N1
            # means N1 will be popped and explored first.
            
            # Sort neighbors first (e.g., numerically or alphabetically), then reverse
            # for deterministic stack processing.
            sorted_neighbors_for_stack = sorted(self.graph[current_node], reverse=True)

            for neighbor in sorted_neighbors_for_stack:
                if neighbor not in processed_nodes_set:
                    stack.append(neighbor)
        
        return visited_nodes_ordered_list

# Example Usage:
if __name__ == '__main__':
    # Create a graph instance
    g = Graph()

    print("--- Building Graph ---")
    # Add edges: (source, destination, directed_flag)
    g.add_edge(0, 1)  # Undirected: 0 -- 1
    g.add_edge(0, 2)  # Undirected: 0 -- 2
    g.add_edge(1, 2)  # Undirected: 1 -- 2
    g.add_edge(2, 3, directed=True) # Directed: 2 -> 3
    g.add_edge(3, 4)  # Undirected: 3 -- 4
    g.add_edge(4, 0, directed=True) # Directed: 4 -> 0 (edge from 4 to 0)

    # Add a disconnected component
    g.add_edge(5, 6)  # Undirected: 5 -- 6
    g.add_edge(5, 7, directed=True) # Directed: 5 -> 7

    # Add an isolated node (will be known to the graph via self.nodes)
    g.nodes.add(8)

    # Display the graph (neighbors will be sorted in the display)
    g.display_graph()
    # Expected graph structure (adjacencies sorted):
    # 0: [1, 2]       (Edge 4->0 is incoming to 0, not outgoing from 0)
    # 1: [0, 2]
    # 2: [0, 1, 3]
    # 3: [4]          (Edge 2->3 is incoming to 3. Edge 3--4 means 3 is connected to 4)
    # 4: [0, 3]       (Edge 3--4 means 4 is connected to 3. Edge 4->0 means 0 is a neighbor of 4)
    # 5: [6, 7]
    # 6: [5]
    # 7: []           (Node 7 is a destination from 5, has no outgoing edges)
    # 8: []           (Isolated node)

    print("\n--- BFS Traversal ---")
    # BFS from node 0
    bfs_result_0 = g.bfs(0)
    print(f"BFS starting from node 0: {bfs_result_0}") 
    # Expected (with sorted neighbors): [0, 1, 2, 3, 4]

    # BFS from node 5 (disconnected component)
    bfs_result_5 = g.bfs(5)
    print(f"BFS starting from node 5: {bfs_result_5}")
    # Expected (with sorted neighbors): [5, 6, 7]
    
    # BFS from isolated node 8
    bfs_result_8 = g.bfs(8)
    print(f"BFS starting from node 8 (isolated): {bfs_result_8}") # Expected: [8]

    # BFS from non-existent node 99
    bfs_result_99 = g.bfs(99)
    print(f"BFS starting from node 99 (non-existent): {bfs_result_99}") # Expected: []

    print("\n--- DFS Traversal ---")
    # DFS from node 0
    dfs_result_0 = g.dfs(0)
    print(f"DFS starting from node 0: {dfs_result_0}") 
    # Expected (iterative, pushing sorted_reversed neighbors): [0, 1, 2, 3, 4] (Path 0->1->2->3->4)
    # Manual trace for DFS(0):
    # S=[0]
    # Pop 0. res=[0], PSet={0}. Nbrs(0) sorted=[1,2]. rev_N(0)=[2,1]. Push 2, Push 1. S=[2,1]
    # Pop 1. res=[0,1], PSet={0,1}. Nbrs(1) sorted=[0,2]. rev_N(1)=[2,0]. 0 in PSet. Push 2 (not in PSet). S=[2,2]
    # Pop 2. res=[0,1,2], PSet={0,1,2}. Nbrs(2) sorted=[0,1,3]. rev_N(2)=[3,1,0]. 0,1 in PSet. Push 3. S=[2,3]
    # Pop 3. res=[0,1,2,3], PSet={0,1,2,3}. Nbrs(3) sorted=[4]. rev_N(3)=[4]. Push 4. S=[2,4]
    # Pop 4. res=[0,1,2,3,4], PSet={0,1,2,3,4}. Nbrs(4) sorted=[0,3]. rev_N(4)=[3,0]. 0,3 in PSet. S=[2]
    # Pop 2. 2 in PSet. Skip. S=[]
    # Output: [0, 1, 2, 3, 4] - This is correct.

    # DFS from node 5 (disconnected component)
    dfs_result_5 = g.dfs(5)
    print(f"DFS starting from node 5: {dfs_result_5}")
    # Expected (iterative, pushing sorted_reversed neighbors): [5, 6, 7] (Path 5->6, then 5->7)
    # Manual trace for DFS(5):
    # S=[5]
    # Pop 5. res=[5], PSet={5}. Nbrs(5) sorted=[6,7]. rev_N(5)=[7,6]. Push 7, Push 6. S=[7,6]
    # Pop 6. res=[5,6], PSet={5,6}. Nbrs(6) sorted=[5]. rev_N(6)=[5]. 5 in PSet. S=[7]
    # Pop 7. res=[5,6,7], PSet={5,6,7}. Nbrs(7) []. S=[]
    # Output: [5, 6, 7] - This is correct.
                                                       
    # DFS from isolated node 8
    dfs_result_8 = g.dfs(8)
    print(f"DFS starting from node 8 (isolated): {dfs_result_8}") # Expected: [8]

    # DFS from non-existent node 99
    dfs_result_99 = g.dfs(99)
    print(f"DFS starting from node 99 (non-existent): {dfs_result_99}") # Expected: []

    print("\n--- Testing graph with no edges (only nodes) ---")
    g_no_edges = Graph()
    g_no_edges.nodes.add('A') # Add node 'A'
    g_no_edges.nodes.add('B') # Add node 'B'
    g_no_edges.display_graph() # Expected: A: [], B: []
    print(f"BFS from 'A' in no-edge graph: {g_no_edges.bfs('A')}") # Expected: ['A']
    print(f"DFS from 'B' in no-edge graph: {g_no_edges.dfs('B')}") # Expected: ['B']
    print(f"BFS from 'C' (non-existent node): {g_no_edges.bfs('C')}") # Expected: []

    print("\n--- Testing empty graph ---")
    g_empty = Graph()
    g_empty.display_graph() # Expected: Graph is empty.
    print(f"BFS from 'A' in empty graph: {g_empty.bfs('A')}") # Expected: []
    print(f"DFS from 'A' in empty graph: {g_empty.dfs('A')}") # Expected: []
```
The file `9.Graph/index.py` has been updated with the complete Graph class implementation, including BFS, DFS, comments, and example usage as specified.

Key changes and confirmations:
-   **`__init__`**: Uses `collections.defaultdict(list)` for `self.graph` and `self.nodes = set()` to track all nodes.
-   **`add_edge`**: Correctly adds edges and updates `self.nodes`.
-   **`display_graph`**: Iterates over `sorted(list(self.nodes))` and prints sorted adjacency lists for consistent output.
-   **`bfs`**:
    -   Checks if `start_node` is in `self.nodes`.
    -   Uses `collections.deque` and a `visited_in_queue_set` (renamed for clarity from `visited_set` in my internal plan to distinguish its role).
    -   Sorts neighbors before adding to queue for deterministic example output.
-   **`dfs`**:
    -   Checks if `start_node` is in `self.nodes`.
    -   Uses a list as a stack and `processed_nodes_set` (renamed for clarity). A node is added to `processed_nodes_set` when it's popped and its neighbors are about to be explored.
    -   Sorts neighbors (reversed) before pushing to stack for deterministic example output.
-   **Example Usage**: Comprehensive examples are in place, covering various scenarios including disconnected graphs, isolated nodes, non-existent start nodes, and empty/no-edge graphs. The manual traces in the comments confirm the expected behavior of BFS and DFS given the neighbor sorting strategy.

The implementation addresses all points from the subtask description.I have successfully implemented the `Graph` class in `9.Graph/index.py` as per the requirements.

Here's a summary of the implementation:

1.  **`Graph` Class**:
    *   **`__init__(self)`**: Initializes `self.graph = collections.defaultdict(list)` to store the adjacency list and `self.nodes = set()` to keep an explicit record of all nodes added to the graph (either as source or destination of an edge, or as an isolated node).
    *   **`add_edge(self, u, v, directed=False)`**:
        *   Adds `u` and `v` to the `self.nodes` set.
        *   Appends `v` to `self.graph[u]`'s list of neighbors.
        *   If `directed` is `False`, it also appends `u` to `self.graph[v]`'s list.
    *   **`display_graph(self)`**:
        *   Prints a header "Graph Adjacency List:".
        *   If `self.nodes` is empty, it prints "Graph is empty.".
        *   Otherwise, it iterates through `sorted(list(self.nodes))` to display all nodes in a consistent order. For each node, it prints the node and its sorted list of neighbors (from `self.graph[node]`).

2.  **Breadth-First Search (BFS) - `bfs(self, start_node)`**:
    *   Checks if `start_node` is in `self.nodes`. If not, prints a warning and returns an empty list.
    *   Initializes an empty list `visited_nodes_ordered_list` to store the traversal order.
    *   Uses `collections.deque` for the `queue` and a `visited_in_queue_set` to keep track of nodes that have been added to the queue (to prevent cycles and redundant processing).
    *   Starts by adding `start_node` to the queue and `visited_in_queue_set`.
    *   In the main loop, it dequeues `current_node`, appends it to `visited_nodes_ordered_list`.
    *   It then iterates through `sorted(self.graph[current_node])` (neighbors sorted for deterministic output in examples) and adds any neighbor not in `visited_in_queue_set` to both the set and the queue.
    *   Returns `visited_nodes_ordered_list`.

3.  **Depth-First Search (DFS) - `dfs(self, start_node)`**:
    *   Implemented iteratively.
    *   Checks if `start_node` is in `self.nodes`. If not, prints a warning and returns an empty list.
    *   Initializes an empty list `visited_nodes_ordered_list`.
    *   Uses a Python list as a `stack` and a `processed_nodes_set` to keep track of nodes that have been popped from the stack and fully processed.
    *   Pushes `start_node` onto the stack initially.
    *   In the main loop, it pops `current_node` from the stack.
    *   If `current_node` is already in `processed_nodes_set`, it continues (skips).
    *   Otherwise, it adds `current_node` to `processed_nodes_set` and appends it to `visited_nodes_ordered_list`.
    *   It then iterates through `sorted(self.graph[current_node], reverse=True)` (neighbors sorted and reversed to ensure that when pushed to stack, they are processed in a standard sorted order, e.g., smaller/alphabetically first) and adds any neighbor not in `processed_nodes_set` to the stack.
    *   Returns `visited_nodes_ordered_list`.

4.  **Well-commented Code**: Docstrings and inline comments explain the purpose and logic of classes, methods, and important code sections.

5.  **Example Usage (`if __name__ == '__main__':`)**:
    *   An instance of `Graph` is created.
    *   Several edges (directed and undirected) are added, forming a graph with a main component, a disconnected component, and an explicitly added isolated node.
    *   `display_graph()` is called to show the graph structure.
    *   BFS and DFS traversals are demonstrated from:
        *   A node in the main component (node 0).
        *   A node in the disconnected component (node 5).
        *   The isolated node (node 8).
        *   A non-existent node (node 99).
    *   Additional test cases for an empty graph and a graph with nodes but no edges are included.
    *   Comments in the example section include expected outputs and brief traces to verify correctness.

The solution fulfills all the requirements of the subtask.
