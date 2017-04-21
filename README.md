# Graph Coloring Project

**The following would work on Linux and Mac.** <br/>
*I don't know about Windows; give it a shot!*

To get started, clone this repo:
```
git clone https://github.com/arjunkrishnababu96/graph-coloring.git
```

#### Makefile Usage
A `Makefile` is included. To compile `greedy.c` for instance, run:
```
$ make greedy
```
This would create an executable with the name `greedy`. To run this executable, type:
```
$ ./greedy
```

(`greedy` expects command-line arguments, which I have not shown above)

To compile and create executables for all `.c` source files, run:
```
$ make
```

To remove all object files and executables, run:
```
$ make clean
```

#### Python Script to Create Graphs
**Requires [Python 3.6](https://www.python.org/downloads/release/python-360/)**

A python script `creategraph.py` has been provided to automatically generate graphs using the `randomgraph` C program.

To see documentation for `creategraph.py`, type:
```
$ python creategraph.py --help
```

The documentation for `creategraph.py` is self-explanatory.

All the graph files created would be saved to `outputs/` directory.
