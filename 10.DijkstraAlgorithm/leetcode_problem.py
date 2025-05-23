"""
LeetCode Problem 743: Network Delay Time

Problem Statement:
You are given a network of n nodes, labeled from 1 to n. You are also given times,
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is
the source node, vi is the target node, and wi is the time it takes for a signal
to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for
all n nodes to receive the signal. If it is impossible for all n nodes to receive
the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Calculates the minimum time for a signal starting from node k to reach all n nodes.

        Args:
            times: A list of lists, where each inner list [u, v, w] represents a directed
                   edge from node u to node v with travel time w.
            n: The total number of nodes in the network, labeled 1 to n.
            k: The starting node from which the signal is sent.

        Returns:
            The minimum time required for the signal to reach all nodes. If any node
            is unreachable, returns -1.
        """

        # Step 1: Build the graph (adjacency list).
        # Keys are source nodes, values are lists of (target_node, time_taken) tuples.
        # Nodes are 1-indexed, so the graph can be represented using a dictionary
        # or a list of lists if we adjust indices.
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize distances (signal received times).
        # `signal_received_time[node]` stores the minimum time for the signal to reach `node`.
        # Initialize all times to infinity, as nodes are initially unreached.
        # Nodes are 1 to n. We can use a dictionary or an array of size n+1.
        signal_received_time = {i: float('inf') for i in range(1, n + 1)}
        signal_received_time[k] = 0  # Time to reach the starting node k is 0.

        # Step 3: Initialize the priority queue (min-heap).
        # Stores tuples of (time_to_reach_node, node_itself).
        # Start with the source node k.
        priority_queue = [(0, k)]  # (time, node)

        while priority_queue:
            # Pop the node that can be reached in the shortest time found so far.
            time_to_current_node, current_node = heapq.heappop(priority_queue)

            # If we've already found a shorter path to current_node, skip this one.
            # This happens if current_node was added to PQ multiple times with decreasing costs.
            if time_to_current_node > signal_received_time[current_node]:
                continue

            # Explore neighbors of the current_node.
            if current_node in graph: # Check if current_node has outgoing edges
                for target_node, travel_time in graph[current_node]:
                    # Calculate time to reach target_node through current_node.
                    new_time_to_target = time_to_current_node + travel_time

                    # If this path is shorter than any previously found path to target_node:
                    if new_time_to_target < signal_received_time[target_node]:
                        signal_received_time[target_node] = new_time_to_target
                        heapq.heappush(priority_queue, (new_time_to_target, target_node))
        
        # Step 4: Determine the result.
        # Find the maximum time in signal_received_time. This is the time when the last node
        # receives the signal.
        max_time = 0
        for node_id in range(1, n + 1):
            time_val = signal_received_time[node_id]
            if time_val == float('inf'):
                return -1  # A node is unreachable.
            max_time = max(max_time, time_val)
            
        return max_time

if __name__ == '__main__':
    solver = Solution()

    # Example 1
    times1 = [[2,1,1],[2,3,1],[3,4,1]]
    n1 = 4
    k1 = 2
    print(f"Input: times = {times1}, n = {n1}, k = {k1}")
    output1 = solver.networkDelayTime(times1, n1, k1)
    print(f"Output: {output1}") # Expected: 2

    # Example 2
    times2 = [[1,2,1]]
    n2 = 2
    k2 = 1
    print(f"\nInput: times = {times2}, n = {n2}, k = {k2}")
    output2 = solver.networkDelayTime(times2, n2, k2)
    print(f"Output: {output2}") # Expected: 1

    # Example 3
    times3 = [[1,2,1]]
    n3 = 2
    k3 = 2
    print(f"\nInput: times = {times3}, n = {n3}, k = {k3}")
    output3 = solver.networkDelayTime(times3, n3, k3)
    print(f"Output: {output3}") # Expected: -1 (Node 1 is unreachable from Node 2)

    # Custom Example: All nodes reachable, more complex
    times4 = [[1,2,1],[1,3,4],[2,3,1],[3,4,1],[4,1,2]] # Contains a cycle, but Dijkstra handles it
    n4 = 4
    k4 = 1
    print(f"\nInput: times = {times4}, n = {n4}, k = {k4}")
    output4 = solver.networkDelayTime(times4, n4, k4)
    # Trace for times4, n4=4, k4=1:
    # graph = {1:[(2,1),(3,4)], 2:[(3,1)], 3:[(4,1)], 4:[(1,2)]}
    # sig_time = {1:0, 2:inf, 3:inf, 4:inf}
    # pq = [(0,1)]
    # 1. pop (0,1). current_node=1, time_to_current_node=0.
    #    neighbor 2: new_time = 0+1=1. sig_time[2]=1. pq.push((1,2))
    #    neighbor 3: new_time = 0+4=4. sig_time[3]=4. pq.push((4,3))
    #    pq = [(1,2), (4,3)]
    # 2. pop (1,2). current_node=2, time_to_current_node=1.
    #    neighbor 3: new_time = 1+1=2. sig_time[3]=2 (was 4). pq.push((2,3))
    #    pq = [(2,3), (4,3)]
    # 3. pop (2,3). current_node=3, time_to_current_node=2.
    #    neighbor 4: new_time = 2+1=3. sig_time[4]=3. pq.push((3,4))
    #    pq = [(3,4), (4,3)]
    # 4. pop (3,4). current_node=4, time_to_current_node=3.
    #    neighbor 1: new_time = 3+2=5. 5 is not < sig_time[1] (0). No update.
    #    pq = [(4,3)]
    # 5. pop (4,3). time_to_current_node=4. This is > sig_time[3] (2). Continue.
    # pq is empty.
    # Final sig_time: {1:0, 2:1, 3:2, 4:3}
    # max_time = max(0,1,2,3) = 3
    print(f"Output: {output4}") # Expected: 3

    # Custom Example: Node unreachable
    times5 = [[1,2,1], [1,3,1], [2,4,1]] # Node 5 is not defined / part of edges
    n5 = 5 # Node 5 is expected to be reached
    k5 = 1
    print(f"\nInput: times = {times5}, n = {n5}, k = {k5}")
    output5 = solver.networkDelayTime(times5, n5, k5)
    # sig_time for node 5 will remain 'inf'
    print(f"Output: {output5}") # Expected: -1

    # Custom Example: Start node has no outgoing edges, n > 1
    times6 = [[2,1,1]]
    n6 = 3
    k6 = 1 # Node 1 has no outgoing edges specified in times6
    print(f"\nInput: times = {times6}, n = {n6}, k = {k6}")
    output6 = solver.networkDelayTime(times6, n6, k6)
    # sig_time = {1:0, 2:inf, 3:inf}. Node 1 is in graph from k.
    # max_time will try to get sig_time[2] or sig_time[3] -> inf.
    print(f"Output: {output6}") # Expected: -1
    
    # Custom Example: n=1
    times7 = []
    n7 = 1
    k7 = 1
    print(f"\nInput: times = {times7}, n = {n7}, k = {k7}")
    output7 = solver.networkDelayTime(times7, n7, k7)
    # sig_time = {1:0}. max_time = 0.
    print(f"Output: {output7}") # Expected: 0
```
I have written the solution for LeetCode 743 "Network Delay Time" in `10.DijkstraAlgorithm/leetcode_problem.py`.

Here's a summary of what I did:
1.  **Added Problem Statement**: Included the full problem description, examples, and constraints as a multiline comment at the top of the file.
2.  **`Solution` Class**: Created a class `Solution` with the method `networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int`.
3.  **Graph Construction**: The `times` list is converted into an adjacency list (`graph`) where keys are source nodes and values are lists of `(target_node, travel_time)` tuples. I used `collections.defaultdict(list)`.
4.  **Dijkstra's Algorithm Adaptation**:
    *   `signal_received_time`: A dictionary to store the shortest time from `k` to every other node. Initialized with `float('inf')` for all nodes, and `0` for the start node `k`. Nodes are 1-indexed, which is handled by initializing the dictionary from `1` to `n`.
    *   **Priority Queue**: A min-heap (`priority_queue`) stores `(time, node)` tuples, prioritized by time.
    *   **Iteration**: The algorithm iterates, popping the node with the smallest travel time.
    *   **Path Relaxation**: For each neighbor of the current node, if a shorter path is found by going through the current node, `signal_received_time` is updated, and the neighbor is pushed onto the priority queue with the new, shorter time.
    *   **Optimization**: If a node is popped from the priority queue but its `time_to_current_node` is already greater than the stored `signal_received_time[current_node]`, it means a shorter path to this node was already processed, so it's skipped.
5.  **Result Calculation**:
    *   After Dijkstra's algorithm completes, the `signal_received_time` dictionary contains the shortest times from `k` to all reachable nodes.
    *   The function then iterates from node `1` to `n` to find the maximum time recorded in `signal_received_time`.
    *   If any node's time is still `float('inf')`, it means that node is unreachable from `k`, and the function returns `-1`.
    *   Otherwise, it returns the `max_time`.
6.  **Comments**: Added comments to explain different parts of the code.
7.  **Example Usage**: Included an `if __name__ == '__main__':` block with the examples from LeetCode and a few custom ones to test different scenarios (e.g., cycles, unreachable nodes, single node graph).

The solution should correctly solve the problem using Dijkstra's algorithm.
