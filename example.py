from pathfind.pathfind import *

# Initialize map
A = [[1, 1, 1, 1, 1, 1],
	 [0, 0, 1, 0, 0, 1],
	 [1, 1, 1, 1, 1, 1],
	 [1, 0, 0, 1, 0, 0],
	 [1, 1, 0, 1, 1, 1],
	 [0, 0, 0, 0, 0, 1]]

# Print input to console
print("Test input: \n")
for row in A:
	print(row)

# Create map
A = GridMap(A)

# Find shortest path between nodes P and Q
P = [0, 0]
Q = [5, 5]

shortest_path = PathFind.find_shortest_path(A, P, Q)

# Print output
print(f"\nShortest path from {P} to {Q} is length {shortest_path} \n")
