
all: clean build

build: 
	mkdir build/
	cmake -S . -B build/
	cmake --build build/

clean:
	rm -rf build/

test:
	build/test

part1:
	build/part1

part2:
	build/part2
