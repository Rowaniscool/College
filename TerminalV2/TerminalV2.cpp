#include <iostream>
#include <filesystem>
#include "cmds.h"
#include "utilities.h"
#include "fileSystemStuff.h"
#include "fileStuff.h"



int main()
{
	std::cout << "---- Rowans Awesome Terminal ----\n" << "Type 'Help' For Cmds\n";

	while (true) {
		std::string userInput;
		std::filesystem::path currentPath = std::filesystem::current_path();

		std::cout << "\n" << currentPath << ": ";
		std::cin >> userInput;

		for (auto& userInputFinal : userInput) {
			userInputFinal = tolower(userInputFinal);
		}

		if (userInput == "calc" || userInput == "calulator") {
			calculator();
		}
		else if (userInput == "help" || userInput == "cmd" || userInput == "cmds") {
			helpCmd();
		}
		else if (userInput == "clear" || userInput == "cls") {
			system("cls");
		}
		else if (userInput == "ls") {
			ls();
		}
		else if (userInput == "cd") {
			cd();
		}
		else if (userInput == "pwd") {
			PWD();
		}
		else if (userInput == "mkdir" || userInput == "md") {
			mkDir();
		}
		else if (userInput == "remove" || userInput == "rmdir") {
			rmDir();
		}
		else if (userInput == "cat") {
			catFile();
		}
		else if (userInput == "touch" || userInput == "tu") {
			touchFile();
		}
		else if (userInput == "move") {
			moveFile();
		}
		else if (userInput == "copy") {
			copyFile();
		}
		else if (userInput == "rename") {
			renameFile();
		}
		else if (userInput == "delete") {
			removeFileThing();
		}
		else if (userInput == "edit");
		editFile();
	}
}
