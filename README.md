# Graph Coloring Project

[![Python Version](https://img.shields.io/badge/python-v3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

**The following would work on Linux and Mac.** <br/>
*I don't know about Windows; give it a shot!*

For instructions about the project, see [Lab1.pdf](https://github.com/arjunkrishnababu96/graph-coloring/blob/master/Lab1.pdf).

In addition to the original `.c` files, this repository contains a [`Makefile`](#makefile-usage), and a couple of python scripts. See below.

To get started, clone this repo:
```
git clone https://github.com/arjunkrishnababu96/graph-coloring.git
```


#### Branches
[`greedy_summary`](https://github.com/arjunkrishnababu96/graph-coloring/tree/greedy_summary) <br/>
Contains script to generate graphs between `n = 40` and `n = 60`, and 30% to 60% of max-edges for each of those `n`. <br/>
To clone:
```
git clone -b greedy_summary https://github.com/arjunkrishnababu96/graph-coloring.git
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
**Requires [Python 3.6](https://www.python.org/downloads/)**

1. `creategraph.py` generates graphs. <br/>Saves the graphs to `outputs/` with `.graph` extension.
2. `run_greedy.py` to run the `greedy` algorithm on all graphs in `outputs/`.<br/>Saves the result to `outputs/` with `.greedy` extension.

To know about about the usage of the scripts, run:
```
python3 creategraph.py --help
python3 run_greedy.py --help

```

You may have to modify `creategraph.py` to generate the exact type of graphs you want. <br/> E-Mail me for help with this.
