#include <stdio.h>
#include <iostream>

using namespace std;

int main() {

    int x = 0;

    do {
        
        cout << "The value of x is: " + x << endl;
        x = x + 1;
        
    } while ( x < 20 );

    return 0;
}