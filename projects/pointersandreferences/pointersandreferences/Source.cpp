#include <iostream>

using namespace std;

// Creates a pointer 'ptr' with memory location of 00000000 (Null)
int* ptr;

// Creates an integer variable set to the value 7
int var = 7;

// Creates another integer variable set to the value 21
int foo = 21;

// *ptr will tell us the value of the address that it is pointing to
/*
For example:
If ptr is pointing to the same memory location as var, then *ptr will provide us with '7', instead of whatever memory location that var is at. 
*/

// ptr = &var will assign ptr to the same address as the address that var lives at
// An asterisk before the variable is known as a 'de-referenced value'. 

int main()
{
	ptr = &var;
	cout << &var << endl;
	cout << *ptr << endl;

	ptr = &foo;
	cout << &foo << endl;
	cout << *ptr << endl;
}