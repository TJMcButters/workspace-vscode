#include <stdio.h>
#include <vector>
#include <iostream>
#include <typeinfo>

using namespace std;

bool stopRun = true;
int height, total, count;
double average;
vector <int> heights;

int findAverage(int tot, int size)
{
    int returnMe = tot / size;
    return returnMe;
}

int main ()
{
    while (stopRun)
    {
        cout << "Enter a height, or -1 to quit: ";
        if (!(cin >> height))
        {
            cout << "Please enter an integer: ";
            cin.clear();
            cin.ignore(10000, '\n');
        }

        // TODO: How to catch for values == 0 or < -1?

        else if (height != -1)
        {
            heights.push_back(height);
        }
        else if (height == -1)
        {
            stopRun = false;
        }
    }
    cout << "Total: ";
    for (int i = 0; i < heights.size(); i++)
    {
        if (i == 0)
        {
            cout << heights[i];
        }
        else if (i != 0)
        {
            cout << " + " << heights[i];
        }
        total += heights[i];
    }
    cout << " = " << total;
    average = findAverage(total, heights.size());
    cout << "\nAverage height: " << average;
    return 0;
}
