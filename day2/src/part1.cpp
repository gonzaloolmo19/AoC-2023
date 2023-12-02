#include "funciones.hpp"
#include <algorithm>
#include <iostream>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {

	int n = 0;

	n = suma_posibles_partidas("input.txt");
	cout << n;
	return 0;
}
