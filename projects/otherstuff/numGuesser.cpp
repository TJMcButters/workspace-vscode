#include <iostream>
#include <stdio.h>
#include <string>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    int num, guess, tries = 0;
    srand(time(0));
    num = rand() % 100 + 1;
    cout << "Guess my number game\n\n";

    while (guess != num)
    {
        cout << "Enter a guess between 1 and 100: ";
        cin >> guess;
        tries++;

        if (guess > num)
            cout << "too high\n";
        else if (guess < num)
            cout << "too low\n";
        else
            cout << "\nCorrect! You got it in " << tries << " guesses!\n";
    }
    return 0;
}