#include <iostream>
#include <stdio.h>
#include <string>
#include "Log.h"
#include <vector>

using namespace std;

float findAverage(int tot, int times)
{
	return (float)(tot / times);
}

class Player
{

};

int main()
{
	int height, total = 0, iter = 0;
	float average;
	vector <int> y;
	bool keepGoing = true;

	while (keepGoing)
	{
		cout << "Enter a height in inches, or '-1' to quit: ";
		if (!(cin >> height))
		{
			cout << "Please enter an integer";
			cin.clear();
			cin.ignore(100000, '\n');
		}
		else if (height == -1)
		{
			keepGoing = false;
		}
		else 
		{
			y.push_back(height);
			iter++;
		}
	}
	for (int i = 0; i < sizeof(y); i++)
	{
		total += y[i];
	}
	average = findAverage(total, iter);
	cout << "The average height is: " << average << endl;
}