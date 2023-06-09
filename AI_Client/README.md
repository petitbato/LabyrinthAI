# Labyrinth AI

The program contains the scripts of an AI made for playing Ravensburger's Labyrinth game.

## Strategy

The strategy used in this program is the Breadth First Search algorithm. It seeks first for every displacement possible with every tile insertion possible, and choose the best, based on the distance between the objective and the final position, if it cannot reach the objective first. This program does not support tile rotation.

## Libraries

The libraries used in this project are basic Python libraries, such as :
- the socket library for the connection to the server
- the json library for sending json data to the server
- the sys library for stopping the loop when necessary
- the math library for the sqrt function
- the copy library for the deepcopy function
