#include "funciones.hpp"
#include <iostream>

// If parameter is not true, test fails
// This check function would be provided by the test framework
#define TEST_CASE(x)                                                           \
	{                                                                          \
		std::cout << "Testing " << #x << std::endl;                            \
		if (!(x))                                                              \
			std::cout << __FUNCTION__ << " failed on line " << __LINE__        \
			          << std::endl;                                            \
		else                                                                   \
			std::cout << "Test Passed" << std::endl;                           \
	}

// Test for function1()
// You would need to write these even when using a framework
void test_foo() { TEST_CASE(foo(2) == 4) }

int main(void) {
	// Call all tests. Using a test framework would simplify this.
	test_foo();
	TEST_CASE(suma_calibraciones("test.txt") == 142);
	TEST_CASE(suma_calibraciones2("test2.txt") == 281)
}
