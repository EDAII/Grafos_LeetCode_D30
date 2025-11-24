# 847. Shortest Path Visiting All Nodes

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

## Example 1:

![alt text](assets/image-1.png)

**Input**: graph = `[[1,2,3],[0],[0],[0]]`
**Output**: 4
**Explanation**: One possible path is `[1,0,2,0,3]`