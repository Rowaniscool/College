#ifndef UTILITIES_H
#define UTILITIES_H

#include <iostream>
#include <cmath>
#include "fileStuff.h"

void calculator() {
	double num1;
	double num2;
	double sum;
	std::string operatorChoice;

	std::cout << "--- Calculator ---\n+, -, *, /, ^\nEnter first num: ";
	std::cin >> num1;
	std::cout << "Enter second num: ";
	std::cin >> num2;
	std::cout << "Enter operator: ";
	std::cin >> operatorChoice;

	if (operatorChoice == "+") {
		sum = num1 + num2;
		std::cout << "Sum: " << sum;
	}
	if (operatorChoice == "-") {
		sum = num1 - num2;
		std::cout << "Sum: " << sum;
	}
	else if (operatorChoice == "*") {
		sum = num1 * num2;
		std::cout << "Sum: " << sum;
	}
	else if (operatorChoice == "/") {
		sum = num1 / num2;
		std::cout << "Sum: " << sum;
	}
	else if (operatorChoice == "^") {
		sum = pow(num1, num2);
		std::cout << "Sum: " << sum;

	}

}


void calender() {

}

#endif // !UTILITIES_H
