# PathFindPy

Submission for technical test.

Implementation ccompleted with my best understanding of:

* OOP 
* SOLID principles 
* Unit testing (using the built-in `unittest` Python module).

The code implementing classes for objects of type `Node`, `GridMap`, and `PathFind` are contained in `pathfind/pathfind.py`. 

The pathfinding algorithm `find_shortest_path` contained in the `PathFind` class is based on the A* pathfinding algorithm.

There are many, many test cases I would realistically test for, but writing all of them out is probably not what is expected for the technical test, so I've included some examples of test cases ***below*** which I would also implement in reality.

## Running tests

Run `python -m unittest discover ./test -v` from inside the parent directory to execute all tests.

## Note on invalid inputs

I wasn't sure whether to handle the cases in which users input invalid input for the grid- in a proper scenario I obviously would, but I didn't want to overdo it for the purpose of the assignment. Just wanted to make it clear that I would when designing a system in an industry setting.

## Additional test cases

using 5x5 grid:
* both points on same node
* points next to each other
* no wall
* wall exists between points
* wall exists, but not between points
* 2 walls between points
* 2 walls between points - with ends of walls touching end of grid and overlapping with a line between
* vertical wall
* horizontal wall
* 2 walls: vertical and horizontal wall and overlapping with 2 lines between 
also vice versa for following:
* Q above P
* Q below P
* Q left of P
* Q right of P

using non 5x5 grid
* P above wall, Q above wall
* 3 walls between points
* 0x0 grid??
* empty point arrays??
* 1x4 grid with and without walls
* 2x2 grid with and without walls
* 6x2 grid with 2 walls
* wall all across grid - no passage - both vertical and horizontal
* all nodes as a wall, except outer edges:
P0000
XXXX0
Q0000
* all nodes as wall, except points:
PXX
XXX
QXX
* enclosed wall:
00P00
0XXX0
0XQX0
XX0X0
00000
* mazes, e.g. (11x8):
POOOOOOOOOO
OXXXXXXXXXO
OOOOXXOOOOO
OXXXXXXXXXO
OXXXXXXOOOO
OOOXQXXXXXO
XXXXOXXXXXO
OOOOOOOOOOO

Also testing for various incorrect user inputs, other conditions which break the program, *etc. etc.*
