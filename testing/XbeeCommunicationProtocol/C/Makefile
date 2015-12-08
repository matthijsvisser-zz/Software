# "all" is name of the default target, running "make" without params would use it
all: executable1

# for C++, replace CC (c compiler) with CXX (c++ compiler) which is used as default linker
CC=$(CXX)
CXX = g++
CXXFLAGS = -Wall -g

# tell which files should be used, .cpp -> .o make would do automatically
executable1: XbeeCom.o test.o
	$(CXX) $(CXXFLAGS) -o main test.o XbeeCom.o
