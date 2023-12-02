#include "funciones.hpp"
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <limits.h>
#include <map>
#include <sstream>
#include <string>

using namespace std;

int foo(int a) { return a * 2; }

void removeChar(std::string &str, char c) {
	auto b = std::remove(str.begin(), str.end(), c);
	str.erase(b, str.end());
}

bool partida_posible(string linea, int max_red, int max_green, int max_blue) {
	removeChar(linea, ':');
	removeChar(linea, ',');

	istringstream iss(linea);
	string prueba;

	iss >> prueba;
	linea.erase(0, prueba.length() + 1);
	string id_str;
	iss >> id_str;
	linea.erase(0, id_str.length() + 1);

	map<string, int> max_colores;
	max_colores["blue"] = 0;
	max_colores["green"] = 0;
	max_colores["red"] = 0;

	while (linea.find(";") != string::npos) {
		auto separador = linea.find(";");
		string ronda = linea.substr(0, separador);
		linea.erase(0, ronda.length() + 2);
		istringstream ironda(ronda);
		string color;
		int numero;
		while (!ironda.eof()) {
			ironda >> numero;
			ironda >> color;
			if (max_colores[color] < numero) {
				max_colores[color] = numero;
			}
		}
	}
	string ronda = linea;
	istringstream ironda(ronda);
	string color;
	int numero;
	while (!ironda.eof()) {
		ironda >> numero;
		ironda >> color;
		if (max_colores[color] < numero) {
			max_colores[color] = numero;
		}
	}

	if (max_colores["red"] > max_red)
		return false;
	else if (max_colores["green"] > max_green)
		return false;
	else if (max_colores["blue"] > max_blue)
		return false;

	return true;
}

int suma_posibles_partidas(string archivo) {
	ifstream is(archivo);
	if (is.is_open()) {
		string linea;
		int suma = 0;
		int contador = 0;
		while (getline(is, linea)) {
			contador++;
			if (partida_posible(linea, 12, 13, 14) && !linea.empty()) {
				suma += contador;
			}
		}
		return suma;
	} else {
		cout << "No se pudo abrir el archivo" << endl;
		exit(1);
	}
}

int powerOfSetOfCubes(std::string linea) {
	removeChar(linea, ':');
	removeChar(linea, ',');

	istringstream iss(linea);
	string prueba;

	int min_red = 0;
	int min_green = 0;
	int min_blue = 0;

	iss >> prueba;
	linea.erase(0, prueba.length() + 1);
	string id_str;
	iss >> id_str;
	linea.erase(0, id_str.length() + 1);

	map<string, int> min_colores;
	min_colores["blue"] = 0;
	min_colores["green"] = 0;
	min_colores["red"] = 0;

	while (linea.find(";") != string::npos) {
		auto separador = linea.find(";");
		string ronda = linea.substr(0, separador);
		linea.erase(0, ronda.length() + 2);
		istringstream ironda(ronda);
		string color;
		int numero;
		while (!ironda.eof()) {
			ironda >> numero;
			ironda >> color;
			if (min_colores[color] < numero) {
				min_colores[color] = numero;
			}
		}
	}
	string ronda = linea;
	istringstream ironda(ronda);
	string color;
	int numero;
	while (!ironda.eof()) {
		ironda >> numero;
		ironda >> color;
		if (min_colores[color] < numero) {
			min_colores[color] = numero;
		}
	}

	return min_colores["red"] * min_colores["green"] * min_colores["blue"];
}
