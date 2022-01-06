"""
Contained are classes for modelling and solving pathfinding problems in 2D grids, where 1s represent
traversable nodes and 0s represent untraversable nodes.
"""

class Node():
    """
    A class representing a node.

    Params:
    -------
    pos : list
        [x, y] co-ordinates of the node.
    parent : Node
        The previous node on a shortest path to this node.

    Properties:
    -----------
    pos : list
        [x, y] co-ordinates of the node.
    parent : Node
        The previous node on the shortest path to this node.
    G : int
        The distance from the source node.
    H : int
        The manhattan distance to the target node, ignoring obstacles.
    F : int
        The sum of G and H.

    """
    def __init__(self, pos=None, parent=None):
        
        self.pos = pos
        self.parent = parent
        self.G = 0
        self.H = 0
        self.F = 0

    def __eq__(self, other):
        """
        Define equality between Node objects as based on position.
        """

        return self.pos == other.pos


class GridMap():
    """
    A class representing a "map" as a 2D grid.
    
    Params:
    -------
    A : list
        A 2D array representing a grid. 1 = traversable, 0 = untraversable

    Properties:
    -----------
    A : list
        A 2D array representing a grid. 1 = traversable, 0 = untraversable

    """
    def __init__(self, A):
        
        self.A = A


    def is_valid_node(self, node):
        """
        Returns True if node co-ordinates are valid, False if they are out of range or they are on 
        a blocked grid square.

        Params:
        -------
        node : Node
            The node object to be checked for validity.

        Returns:
        --------
        is_valid : bool
            Whether the node is valid.
        
        """
        # Checks if either co-ordinate of the node is smaller than 0 or larger than the max index
        # of its respective grid dimension
        if (node.pos[0] < 0 or node.pos[1] < 0 or node.pos[0] > len(self.A[0])-1 or node.pos[1] > 
            len([row[0]for row in self.A])-1):
            
            return False

        # Checks node is not untraversable
        elif not self.A[node.pos[1]][node.pos[0]]: 
            
            return False

        else:
            return True


    def get_neighbours(self, node):
        """
        Returns the neighbours of the current node.

        Params:
        -------
        node : Node
            The node to query for its neighbours.

        Returns:
        --------
        neighbours : list
            List of neighbours of the queried node.

        """
        
        # Initialize list of neighbours
        neighbours = []
        
        # For each direction up, down, left, right
        for neighbour_pos in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            
            # Create Node object for neighbour
            neighbour = Node([neighbour_pos[0] + node.pos[0], neighbour_pos[1] + node.pos[1]], parent=node)
            
            # Check validity of node
            if not self.is_valid_node(neighbour):
                continue
            
            # Add to list of neighbours
            neighbours.append(neighbour)

        return neighbours


class PathFind():
    """
    A class to hold pathfinding methods.

    """
    def find_shortest_path(A, P, Q):
        """
        Implements the A* pathfinding algorithm for finding shortest paths 
        between a source node P and a target node Q.

        Params:
        -------
        
        A: list
            A 2D array where 1 represents available squares and 0 represents
            blocked squares.

        P: tuple
            The [x, y] co-ordinates of the source node.

        Q: tuple
            The [x, y] co-ordinates of the target node.

        Returns:
        --------

        shortest_distance: int
            The shortest distance from P to Q.

        """
        # Check source and target are valid
        assert A.is_valid_node(Node(P)), "Source is not valid."
        assert A.is_valid_node(Node(Q)), "Target is not valid."

        #### ALGORITHM STARTS ####

        # Initialize open and closed lists
        open_nodes = []
        closed_nodes = []

        # Add the start node to open_nodes
        start_node = Node(P)
        open_nodes.append(start_node)

        # Loop until target node is reached
        while open_nodes:

            # Set current node to the node with the lowest F-cost in open_nodes
            current = Node()
            
            best_f = float("inf")
            for node in open_nodes:
                if node.F < best_f:
                    best_f = node.F
                    current = node

            # Move current from open_nodes to closed_nodes
            open_nodes.remove(current)
            closed_nodes.append(current)

            # If current is target, return distance
            if current.pos == Q:
                shortest_distance = current.G
                return shortest_distance

            # Generate neighbours of current
            neighbours = [node for node in A.get_neighbours(current) if node not in closed_nodes]

            # For each neighbour
            for neighbour in neighbours:
                
                # If neighbour is in closed skip to next neighbour
                if neighbour in closed_nodes:
                    continue

                # Set G, H, and F for new path
                neighbour.G = current.G + 1
                neighbour.H = abs(neighbour.pos[0] - current.pos[0]) + abs(neighbour.pos[1] - current.pos[1]) # Manhattan distance
                neighbour.F = neighbour.G + neighbour.H

                # If neighbour is not in open, add it to open               
                node = [node for node in open_nodes if node.pos == neighbour.pos]
                if not node:
                    open_nodes.append(neighbour)

                # If new path to neighbour is shorter than stored path, update node in open
                elif neighbour.G < node[0].G:

                    # Set new F-cost of neighbour in open list
                    node.F = neighbour.F
                    node.G = neighbour.G
                    node.H = neighbour.H
                    
                    # Set parent of neighbour to current
                    node.parent = current

        # If loop exits, target is unreachable
        return "<node unreachable>"
