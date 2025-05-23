# Dijkstra's Algorithm

Dijkstra's algorithm is a fundamental algorithm in graph theory used for finding the shortest paths from a single source node to all other nodes in a weighted graph, provided that the edge weights are non-negative.

## Explanation of Dijkstra's Algorithm

### What it Does
Dijkstra's algorithm computes the shortest path from a specified starting node (the "source") to every other node within a graph. This means it determines the path with the minimum total weight from the source to each destination. It is widely used in network routing protocols, GPS systems for finding the shortest route, and other applications involving path optimization.

### How it Works
The algorithm maintains a set of nodes whose shortest path from the source is already known and a set of tentative distances to all other nodes. It works as follows:

1.  **Initialization**:
    *   Assign a tentative distance value to every node: set it to zero for our initial node and to infinity for all other nodes.
    *   Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
    *   Set the initial node as current.

2.  **Iteration**:
    *   For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, keep the current value.
    *   When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.

3.  **Selection**:
    *   If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete shortest path tree), then stop. The algorithm has finished.
    *   Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new "current node", and go back to step 2.

A min-priority queue is typically used to efficiently select the node with the smallest tentative distance in each step.

### Key Concepts
*   **Weighted Graph**: A graph where each edge has an associated numerical value, called a weight or cost.
*   **Non-negative Edge Weights**: Dijkstra's algorithm requires that all edge weights are non-negative. If there are negative edge weights, other algorithms like Bellman-Ford should be used.
*   **Priority Queue**: A data structure that stores elements along with their priorities. In Dijkstra's, it stores nodes and their tentative distances, allowing for efficient retrieval of the node with the smallest distance.

### Time and Space Complexity
*   **Time Complexity**:
    *   `O(V^2)` when using an adjacency matrix or a linear scan of distances in an adjacency list representation.
    *   `O((V + E) log V)` or `O(E log V)` when using an adjacency list and a binary heap (like Python's `heapq`) for the priority queue. (V = number of vertices, E = number of edges). This is the most common complexity cited.
    *   `O(E + V log V)` with a Fibonacci heap, which is theoretically faster but often more complex to implement.
*   **Space Complexity**:
    *   `O(V + E)` to store the graph representation (adjacency list), distances to each node, and the priority queue.

## Python Implementation (`index.py`)

The file `index.py` in this directory provides a generic Python implementation of Dijkstra's algorithm.

### Overview
This implementation finds the shortest paths from a given start node to all other nodes in a graph represented as an adjacency list.

### Key Features
*   Takes the graph as an adjacency list (Python dictionary where keys are nodes and values are lists of `(neighbor, weight)` tuples).
*   Accepts a `start_node` identifier.
*   Returns a dictionary mapping each node to its shortest distance from the `start_node`. Unreachable nodes will have a distance of `float('inf')`.
*   Uses Python's `heapq` module to implement the min-priority queue, which is crucial for the algorithm's efficiency.
*   Includes error handling for cases where the start node is not in the graph.

### Usage Example

```python
# Ensure you are in the parent directory of '10.DijkstraAlgorithm'
# or adjust the import path accordingly.
# For example, if running from the root of a project where '10.DijkstraAlgorithm' is a module:
# from DijkstraAlgorithm.index import dijkstra 
# If running a script directly from 10.DijkstraAlgorithm, you might need to adjust sys.path or use relative imports if structured as a package.

# The examples in index.py are self-contained and can be run directly.
# The following shows conceptual usage:

# Assuming 'dijkstra' function is available (e.g., imported)
# from index import dijkstra # If index.py is in the same directory and PYTHONPATH is set

# graph_example = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('C', 2), ('D', 5)],
#     'C': [('A', 4), ('B', 2), ('D', 1)],
#     'D': [('B', 5), ('C', 1)]
# }
# start_node_example = 'A'
# shortest_paths = dijkstra(graph_example, start_node_example)
# print(f"Shortest paths from node '{start_node_example}': {shortest_paths}")
# # Expected output:
# # Shortest paths from node 'A': {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```
To see the direct output, run the `index.py` file which includes this and other examples.

## LeetCode Problem: Network Delay Time (LeetCode 743)

The file `leetcode_problem.py` provides a solution to the LeetCode problem "Network Delay Time" (Problem 743) using Dijkstra's algorithm.

### Problem Description
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target. We send a signal from a given node `k`. The goal is to find the minimum time it takes for all `n` nodes to receive the signal. If it's impossible for all `n` nodes to receive the signal, return -1.

### Application of Dijkstra's Algorithm
Dijkstra's algorithm is a natural fit for this problem:
1.  The network can be modeled as a weighted directed graph where nodes are the network nodes and edge weights are the travel times.
2.  The problem asks for the minimum time for a signal to reach all nodes, starting from `k`. This is equivalent to finding the shortest path from `k` to all other nodes.
3.  The "time it takes for all `n` nodes to receive the signal" will be the maximum of these shortest path distances from `k`.
4.  If any node is unreachable (its shortest path distance remains infinity), then it's impossible for all nodes to receive the signal.

The `leetcode_problem.py` script implements this logic within a `Solution` class.

### Usage Example

```python
# Similar to index.py, the leetcode_problem.py file is self-contained with examples.
# Conceptual usage:

# from leetcode_problem import Solution # If leetcode_problem.py is in the same directory

# solver = Solution()
# example_times = [[2,1,1],[2,3,1],[3,4,1]]
# example_n = 4
# example_k = 2
# result = solver.networkDelayTime(example_times, example_n, example_k)
# print(f"Network delay time for example: {result}")
# # Expected output:
# # Network delay time for example: 2
```
To see the direct output, run the `leetcode_problem.py` file.

## How to Run the Code

You can run the Python files directly from your terminal, assuming you are in the root directory of this project or have navigated into the `10.DijkstraAlgorithm` directory.

1.  **To run the generic Dijkstra implementation example (`index.py`):**
    Navigate to the directory containing the file if necessary.
    ```bash
    python 10.DijkstraAlgorithm/index.py
    ```
    If you are already inside the `10.DijkstraAlgorithm` directory:
    ```bash
    python index.py
    ```

2.  **To run the LeetCode Network Delay Time solution example (`leetcode_problem.py`):**
    Navigate to the directory containing the file if necessary.
    ```bash
    python 10.DijkstraAlgorithm/leetcode_problem.py
    ```
    If you are already inside the `10.DijkstraAlgorithm` directory:
    ```bash
    python leetcode_problem.py
    ```

These scripts include example graph data and print the results of the shortest path computations to the console.
