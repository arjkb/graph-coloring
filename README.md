# Graph Coloring Project

**The following would work on Linux and Mac.** <br/>
*I don't know about Windows; give it a shot!*

For instructions about the project, see [Lab1.pdf](https://github.com/arjunkrishnababu96/graph-coloring/blob/master/Lab1.pdf).

In addition to the original `.c` files, this repository contains a [`Makefile`](#makefile-usage), and a [`creategraph.py` python script.](#python-script-to-create-graphs) See below.

To get started, clone this repo:
```
git clone https://github.com/arjunkrishnababu96/graph-coloring.git
```
---
### Makefile Usage
A `Makefile` is included to compile the `.c` files. To compile `greedy.c` for instance, run:
```
make greedy
```
This would create an executable with the name `greedy`. To run this executable, type:
```
./greedy
```

(`greedy` expects command-line arguments, which have been omitted above).

To compile and create executables for all `.c` source files, run:
```
make
```

To remove all object files and executables, run:
```
make clean
```
---
### Python Script to Create Graphs
**Requires [Python 3.6](https://www.python.org/downloads/release/python-360/)**

`creategraph.py` automatically generates graphs based on parameters passed as input to it. It internally runs `randomgraph.c`.

To know more about its usage, see the documentation:
```
python creategraph.py --help
```

The documentation for `creategraph.py` is self-explanatory.

All the graph files created using this script would be saved to `outputs/` directory.
