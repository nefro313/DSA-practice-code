import heapq

def dijkstra(graph, start_node):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a starting node
    to all other nodes in a graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
                      Keys are nodes (e.g., strings or integers), and values are lists
                      of tuples (neighbor, weight), where 'neighbor' is the adjacent
                      node and 'weight' is the cost of the edge to that neighbor.
                      It's assumed that all nodes, including those appearing only as
                      neighbors, are keys in this dictionary. If a node is a terminal
                      node with no outgoing edges, it should be a key with an empty list
                      as its value (e.g., 'D': []).
        start_node: The node from which to calculate shortest paths. It must be a key
                    present in the 'graph' dictionary.

    Returns:
        dict: A dictionary where keys are node identifiers and values are the computed
              shortest distances from the 'start_node'. If a node is unreachable
              from 'start_node', its distance will be float('inf').

    Raises:
        KeyError: If 'start_node' is not found as a key in 'graph'.
    """
    # Validate that the start_node exists as a key in the graph.
    # This is crucial because we will try to access graph[start_node] later
    # and also initialize distances[start_node].
    if start_node not in graph:
        raise KeyError(f"Start node '{start_node}' not found in the graph keys.")

    # Initialize distances: float('inf') for all nodes defined in the graph,
    # and 0 for the start_node. float('inf') represents an infinite distance.
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    # Priority queue to store nodes to visit, ordered by their current shortest distance.
    # Each item in the priority queue is a tuple: (distance, node_identifier).
    # heapq implements a min-heap, so heapq.heappop() always returns the item
    # with the smallest distance.
    priority_queue = [(0, start_node)]  # Start with the source node, distance 0.

    while priority_queue:
        # Pop the node with the smallest tentative distance from the priority queue.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Optimization: If we have already found a shorter path to current_node
        # than the one popped from PQ, then this path is suboptimal, so skip it.
        # This is necessary because we might add multiple entries for the same node
        # to the priority queue if we find shorter paths later (as heapq doesn't
        # support a decrease-key operation directly). The first time we extract a node
        # for which current_distance == distances[current_node], it's via its true
        # shortest path.
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current_node.
        # graph[current_node] provides a list of (neighbor, weight) tuples.
        # It's assumed that if current_node is in graph, graph[current_node] is valid.
        for neighbor, weight in graph[current_node]:
            # Calculate the distance to the 'neighbor' through the 'current_node'.
            distance_through_current_node = current_distance + weight

            # If 'neighbor' is not in 'distances', it means it was in an adjacency list
            # but not as a primary key in the graph. This indicates a malformed graph
            # for this algorithm's assumptions. All nodes should be graph keys.
            if neighbor not in distances:
                # This case implies an inconsistency in graph structure.
                # For robustness, one might raise an error or log a warning.
                # However, standard Dijkstra assumes graph is well-formed.
                # print(f"Warning: Neighbor {neighbor} of node {current_node} not found as a key in graph.")
                continue # Skip this neighbor if it's not a recognized node.


            # Relaxation step: If a shorter path to the 'neighbor' is found:
            if distance_through_current_node < distances[neighbor]:
                # Update the shortest distance to 'neighbor'.
                distances[neighbor] = distance_through_current_node
                # Add the 'neighbor' to the priority queue with its new, shorter distance.
                heapq.heappush(priority_queue, (distance_through_current_node, neighbor))

    return distances

# Example Usage:
if __name__ == '__main__':
    # Example graph representation as an adjacency list
    example_graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
        # Note: All nodes ('A', 'B', 'C', 'D') are keys in the graph,
        # and their neighbors are also keys. This is a well-formed graph.
    }
    start_node_example = 'A'

    print(f"--- Main Example (from problem description) ---")
    print(f"Calculating shortest paths for graph: {example_graph}")
    print(f"Starting from node: '{start_node_example}'")
    shortest_paths = dijkstra(example_graph, start_node_example)

    print(f"\nShortest paths from node '{start_node_example}':")
    for node, distance in shortest_paths.items():
        print(f"To node '{node}': {distance}")
    # Expected output for this example:
    # Shortest paths from node 'A':
    # To node 'A': 0
    # To node 'B': 1
    # To node 'C': 3
    # To node 'D': 4

    print("\n--- Another example with a different start node ---")
    start_node_example_2 = 'D'
    print(f"Calculating shortest paths for graph: {example_graph}") # Using the same graph
    print(f"Starting from node: '{start_node_example_2}'")
    shortest_paths_2 = dijkstra(example_graph, start_node_example_2)
    print(f"\nShortest paths from node '{start_node_example_2}':")
    for node, distance in shortest_paths_2.items():
        print(f"To node '{node}': {distance}")
    # Expected output:
    # Shortest paths from node 'D':
    # To node 'A': 4
    # To node 'B': 3
    # To node 'C': 1
    # To node 'D': 0

    print("\n--- Example with a graph where not all nodes are reachable ---")
    disconnected_graph = {
        'A': [('B', 1)],
        'B': [('A', 1)],
        'C': [('D', 2)], # 'C' and 'D' are disconnected from 'A' and 'B'
        'D': [('C', 2)]
    }
    start_node_example_3 = 'A'
    print(f"Calculating shortest paths for graph: {disconnected_graph}")
    print(f"Starting from node: '{start_node_example_3}'")
    shortest_paths_3 = dijkstra(disconnected_graph, start_node_example_3)
    print(f"\nShortest paths from node '{start_node_example_3}':")
    for node, distance in shortest_paths_3.items():
        print(f"To node '{node}': {distance}")
    # Expected output:
    # Shortest paths from node 'A':
    # To node 'A': 0
    # To node 'B': 1
    # To node 'C': inf
    # To node 'D': inf

    print("\n--- Example with a graph containing a node with no outgoing edges ---")
    graph_with_terminal_node = {
        'A': [('B', 5), ('C', 3)],
        'B': [('C', 2)], # Path A->B->C has weight 5+2=7
        'C': [('D', 7)], # Path A->C has weight 3. Path A->C->D has weight 3+7=10
        'D': []          # 'D' is a terminal node
    }
    start_node_example_4 = 'A'
    print(f"Calculating shortest paths for graph: {graph_with_terminal_node}")
    print(f"Starting from node: '{start_node_example_4}'")
    shortest_paths_4 = dijkstra(graph_with_terminal_node, start_node_example_4)
    print(f"\nShortest paths from node '{start_node_example_4}':")
    for node, distance in shortest_paths_4.items():
        print(f"To node '{node}': {distance}")
    # Expected output based on trace:
    # To node 'A': 0
    # To node 'B': 5
    # To node 'C': 3 (Path A->C is shorter than A->B->C)
    # To node 'D': 10 (Path A->C->D)

    print("\n--- Example with an empty graph (should raise KeyError) ---")
    empty_graph = {}
    start_node_empty = 'A' # Start node not in empty graph
    try:
        print(f"Calculating shortest paths for graph: {empty_graph}")
        print(f"Starting from node: '{start_node_empty}'")
        shortest_paths_empty = dijkstra(empty_graph, start_node_empty)
        print(f"\nShortest paths from node '{start_node_empty}': {shortest_paths_empty}")
    except KeyError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Example with start node not in a non-empty graph (should raise KeyError) ---")
    graph_missing_start = {'X': [('Y',1)], 'Y':[]}
    start_node_missing = 'A' # 'A' is not a key in graph_missing_start
    try:
        print(f"Calculating shortest paths for graph: {graph_missing_start}")
        print(f"Starting from node: '{start_node_missing}'")
        shortest_paths_missing = dijkstra(graph_missing_start, start_node_missing)
        print(f"\nShortest paths from node '{start_node_missing}': {shortest_paths_missing}")
    except KeyError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Example with a single node graph ---")
    single_node_graph = {'Z': []}
    start_node_single = 'Z'
    print(f"Calculating shortest paths for graph: {single_node_graph}")
    print(f"Starting from node: '{start_node_single}'")
    shortest_paths_single = dijkstra(single_node_graph, start_node_single)
    print(f"\nShortest paths from node '{start_node_single}':")
    for node, distance in shortest_paths_single.items():
        print(f"To node '{node}': {distance}")
    # Expected output:
    # Shortest paths from node 'Z':
    # To node 'Z': 0

    print("\n--- Example graph where a neighbor is not a key (should be handled gracefully by skipping) ---")
    # This graph is technically "malformed" if 'C' is expected to be a full node.
    # My implementation initializes `distances` only for keys 'A' and 'B'.
    # When processing neighbors of 'A', ('C', 1) is found.
    # `distances['C']` would cause a KeyError if not handled.
    # Added a check: `if neighbor not in distances: continue`
    graph_with_hanging_neighbor = {
        'A': [('B', 1), ('C', 100)], # 'C' is a neighbor but not a key
        'B': [('A', 1)]
    }
    start_node_hanging = 'A'
    print(f"Calculating shortest paths for graph: {graph_with_hanging_neighbor}")
    print(f"Starting from node: '{start_node_hanging}'")
    shortest_paths_hanging = dijkstra(graph_with_hanging_neighbor, start_node_hanging)
    print(f"\nShortest paths from node '{start_node_hanging}':")
    for node, distance in shortest_paths_hanging.items():
        print(f"To node '{node}': {distance}")
    # Expected:
    # To node 'A': 0
    # To node 'B': 1
    # (Node 'C' is not part of the output because it was not a key in the graph's distance map)

    print("\n--- Example with negative weights (Dijkstra's not guaranteed to work) ---")
    graph_neg_weights = {
        'A': [('B', 1), ('C', -2)], # Negative weight
        'B': [('C', 3)],
        'C': []
    }
    start_node_neg = 'A'
    print(f"Calculating shortest paths for graph: {graph_neg_weights} (Dijkstra's may not be correct)")
    print(f"Starting from node: '{start_node_neg}'")
    shortest_paths_neg = dijkstra(graph_neg_weights, start_node_neg)
    print(f"\nShortest paths from node '{start_node_neg}':")
    for node, distance in shortest_paths_neg.items():
        print(f"To node '{node}': {distance}")
    # Dijkstra's algorithm is not designed for graphs with negative edge weights
    # if those weights can form negative cycles. If there are no negative cycles,
    # it might still produce correct results for some graphs, but it's not guaranteed.
    # For this specific graph: A->C is -2. A->B->C is 1+3=4. So -2 is correct.
    # Expected: A:0, B:1, C:-2. The algorithm should find this.
    # The issue arises with negative cycles, which this graph doesn't have.
```

The code has been written to `10.DijkstraAlgorithm/index.py`.
It includes:
- The Dijkstra's algorithm implementation using `heapq`.
- Comments explaining the code.
- Robustness checks:
    - `start_node` must be a key in the graph.
    - If a neighbor node encountered during path relaxation is not a key in the graph (and thus not in `distances`), it's skipped. This handles cases of "hanging edges" where a node is mentioned as a destination but not defined as a primary node in the graph.
- An extensive set of examples under `if __name__ == '__main__':` to demonstrate functionality with various graph types:
    - The problem's example graph and start node.
    - Different start node.
    - Disconnected graphs.
    - Graphs with terminal nodes.
    - Error handling for empty graphs or missing start nodes.
    - Single-node graphs.
    - A graph with a "hanging neighbor" (a neighbor that isn't a key in the graph).
    - A note and example about negative weights (highlighting Dijkstra's limitations but showing it works for simple cases without negative cycles).

The implementation aligns with the requirements of the subtask. I'll submit this.
