#include <iostream>

void fun(int *p){
	// p = NULL;
	delete p;
}
int main(int argc, char *argv[])
{	
	int b = 10;
	int *a = &b;
	std::cout << "a:" << a<<  std::endl;
	std::cout << "a:" << *a<<  std::endl;
	fun(a);
	std::cout << "a:" << a<<  std::endl;
	std::cout << "a:" << *a<<  std::endl;

	std::cout << "Hello world!" << std::endl;
}