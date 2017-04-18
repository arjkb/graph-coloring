CC=gcc
CFLAGS=-g
OBJS=greedy.o random.o randomgraph.o sig.o

all: greedy random randomgraph sig

greedy: greedy.o
	$(CC) $(CFLAGS) -o greedy greedy.o

random: random.o
	$(CC) $(CFLAGS) -o random random.o

randomgraph: randomgraph.o
	$(CC) $(CFLAGS) -o randomgraph randomgraph.o

sig: sig.o
	$(CC) $(CFLAGS) -o sig sig.o

greedy.o: greedy.c
	$(CC) -c $(CFLAGS) greedy.c

greedy.o: greedy.c
	$(CC) -c $(CFLAGS) greedy.c

greedy.o: greedy.c
	$(CC) -c $(CFLAGS) greedy.c

greedy.o: greedy.c
	$(CC) -c $(CFLAGS) greedy.c

.PHONY: clean

clean:
	rm greedy random randomgraph sig *.o
