#include "funciones.hpp"
#include <cstdlib>
#include <fstream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int foo(int a) { return a * 2; }

int calibration_number(std::string palabra) {

	int n = 0;
	int first = 0;

	if (palabra.find_first_of("0123456789") != string::npos) {
		first = palabra.find_first_of("0123456789");
		n = (palabra.at(first) - '0') * 10;
	}
	if (palabra.find_last_of("0123456789") != string::npos) {
		int last = 0;
		last = palabra.find_last_of("0123456789");
		n += palabra.at(last) - '0';
	}
	return n;
}

int suma_calibraciones(char *fichero) {
	ifstream is(fichero);

	string palabra;
	int suma = 0;
	if (is.is_open()) {
		while (is >> palabra) {
			suma += calibration_number(palabra);
		}
		is.close();
	} else {
		cout << "No se ha podido abrir el archivo";
		exit(1);
	}

	return suma;
}

int calibration_number2(std::string palabra) {
	map<string, int> map_num = {
	    {"one", 1}, {"two", 2},   {"three", 3}, {"four", 4}, {"five", 5},
	    {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}, {"1", 1},
	    {"2", 2},   {"3", 3},     {"4", 4},     {"5", 5},    {"6", 6},
	    {"7", 7},   {"8", 8},     {"9", 9}};

	string digitos = "0123456789";

	int n = 0;
	int first = 0;
	int min_first = 10000000;
	int primer_numero = 0;
	int last = 0;
	int max_last = -1;
	int ultimo_numero = 0;

	for (auto x : map_num) {
		if (palabra.find(x.first) != string::npos) {
			first = palabra.find(x.first);
			if (first < min_first) {
				min_first = first;
				primer_numero = x.second;
			}
		}
	}

	n = primer_numero * 10;

	for (auto x : map_num) {
		if (palabra.rfind(x.first) != string::npos) {
			last = palabra.rfind(x.first);
			if (last > max_last) {
				max_last = last;
				ultimo_numero = x.second;
			}
		}
	}
	n += ultimo_numero;
	return n;

	for (auto x : map_num)

		return n;
}

int suma_calibraciones2(char *fichero) {
	ifstream is(fichero);

	string palabra;
	int suma = 0;
	if (is.is_open()) {
		while (is >> palabra) {
			int sumando = calibration_number2(palabra);
			suma += sumando;
		}
		is.close();
	} else {
		cout << "No se ha podido abrir el archivo";
		exit(1);
	}

	return suma;
}
