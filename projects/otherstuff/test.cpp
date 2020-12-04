#include <typeinfo>
#include <stdio.h>
#include <iostream>

using namespace std;

string x = "Hello";

int main ()
{
    for (char ch : x) {
        cout << "[" << ch << "]";
    }
}