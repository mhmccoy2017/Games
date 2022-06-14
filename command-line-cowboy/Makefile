CC = g++


command-line-cowboy: clc.o
	$(CC) clc.o -o command-line-cowboy 

clc.o: clc.cpp
	$(CC) -c clc.cpp

clean: 
	rm *.o command-line-cowboy