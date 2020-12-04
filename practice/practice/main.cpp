#include <stdio.h>
#include <iostream>

int main() {

	int nums[20];
	int nums_length = sizeof(nums) / sizeof(*nums);

	for (int i = 0; i < nums_length; i++) {
		nums[i] = i;
	}

	for (int y = 0; y < nums_length; y++) {
		std::cout << nums[y] + 1 << std::endl;
	}



	return 0;

}