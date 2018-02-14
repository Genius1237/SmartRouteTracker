# SmartRouteTracker

### Problem 1 : Missionaries and Cannibals

To run the program
`Python3 Problem1.py`

The number of Missionaries and Cannibals initially can be fixed to any number, and the boat is assumed to be able to carry a maximum of two passengers for a trip.

<br>

The class MissionRescue is used for finding the sequence of trips to reach our problem goal: **Transfer all passengers from West Bank to East Bank**

**State Space Representation**
*A state can be identified by the following attributes*
- Number of Missionaries in the West Bank (between 0 to self.numMissionaries)
- Number of Cannibals in the East Bank (between 0 to self.numCannibals)
- Position of Boat (flag can be 0 or 1, 0 implies boat present in West bank, 1 -> East Bank)
<br>

#### Key functions used to accomplish this task :-

- **possiblePaths()** gives the set of all possible next states for the current state
- **searchSolution()** Function that start searching from state: self.state till state 0,0 via Depth First Backtracking, and returns the path (may not be the shortest path) from start state to 0,0.
- **showResults()** Method to present the solution as a Sequence of Boat rides from west to east bank and vice versa.