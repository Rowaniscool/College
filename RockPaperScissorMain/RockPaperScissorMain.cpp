#include <iostream>
#include <random>
#include <vector>
using namespace std;

int UserScore = 0, ComputerScore = 0;


void MainFunction() {
	// The computers choice
	vector<string> PotentialOptions = { "Rock", "Paper", "Scissor" };
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> distr(0, PotentialOptions.size() - 1);

	string ConfirmedOption = PotentialOptions[distr(gen)];


	// The Players Choice
	string UserInput;
	cout << "<--Options-->\nRock\nPaper\nScissor\n: ";
	cin >> UserInput;


	cout << "You chose: " << UserInput << "\n";
	cout << "The computer chose: " << ConfirmedOption << "\n";

	if (UserInput == ConfirmedOption) {
		cout << "Its a tie";
	}
	else if ((UserInput == "Rock" && ConfirmedOption == "Scissor") ||
		(UserInput == "Paper" && ConfirmedOption == "Rock") ||
		(UserInput == "Scissor" && ConfirmedOption == "Paper")) {

		UserScore++;
		cout << "You win!\n\n";

	}
	else {
		ComputerScore++;
		cout << "You lose!\n";
	}
	cout << "Your score :" << UserScore << "\n" << "Computers score: " << ComputerScore << "\n\n\n\n";
}

int main() {

	while (1 > 0) {
		MainFunction();
	}
}


