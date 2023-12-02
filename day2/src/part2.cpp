#include "funciones.hpp"
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {

	ifstream is("input.txt");
	int n = 0;

	if (!is) {
		cout << "Error al abrir el archivo" << endl;
		return 1;
	}

	while (!is.eof()) {
		string linea;
		getline(is, linea);

		n += powerOfSetOfCubes(linea);
	}

	is.close();

	cout << n << endl;

	return 0;
}
