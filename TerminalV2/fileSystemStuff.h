#ifndef FILESYSTEMSTUFF_H
#define FILESYSTEMSTUFF_H

#include <iostream>
#include <filesystem>
#include <string>


void ls() {
	std::filesystem::path targetPath = std::filesystem::current_path();

	try {
		if (std::filesystem::exists(targetPath)) {
			for (auto& stuff : std::filesystem::directory_iterator(targetPath)) {
				std::string fileType = stuff.is_directory() ? " [DIR] " : " [FILE] ";
				std::cout << fileType << stuff.path().filename().string() << "\n";
			}
		}
	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}

void cd() {
	std::string pathInput;
	std::cin.ignore();
	getline(std::cin, pathInput);

	try {
		if (pathInput.empty()) {
			std::filesystem::path currentPath = std::filesystem::current_path();
			filesystem:current_path(currentPath.parent_path());
		}
		else {
			std::filesystem::current_path(pathInput);
		}
	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}

}

void PWD() {
	std::filesystem::path currentPath = std::filesystem::current_path();
	std::cout << "Current path: " << currentPath << "\n";
}

void mkDir() {
	std::string dirName;
	getline(std::cin, dirName);
	remove(dirName.begin(), dirName.end(), ' ');

	try {
		if (!(dirName.empty())) {
			std::filesystem::create_directory(dirName);
			std::cout << "Created successfully...\n";

		}
	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}

void rmDir() {
	std::string dirName;
	getline(std::cin, dirName);
	try {
		if (!(dirName.empty()) && std::filesystem::exists(dirName)){
			if (std::filesystem::is_directory(dirName)) {
				std::filesystem::remove(dirName);
				std::cout << "Removed successfully...\n";

			}
			else {
				std::cout << "Not a directory...\n";
			}
		}
		else {
			std::cout << "Doesent exist...\n";

		}
	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}

void moveFile() {
	std::string fileToMove;
	std::string destination;

	std::cin >> fileToMove;
	std::cin >> destination;

	try {
		if (!std::filesystem::exists(fileToMove)) {
			std::cout << "File doesnt exist...\n";
			return;
		}

		std::filesystem::path source(fileToMove);
		std::filesystem::path dest(destination);


		if (std::filesystem::is_directory(dest)){
			dest /= source.filename(); // uses the /= operator from std::filesystem::path to add the filename onto the destination path.
		}

		std::filesystem::rename(source, dest);
		std::cout << "Moved successfully.\n";

	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}


void copyFile() {
	std::string fileToCopy;
	std::string destination;

	std::cin >> fileToCopy;
	std::cin >> destination;

	try {
		if (std::filesystem::exists(fileToCopy)) {

			std::filesystem::path source(fileToCopy);
			std::filesystem::path dest(destination);
			
			if (std::filesystem::is_directory(dest)) {
				dest /= source.filename();
			}

			std::filesystem::copy_file(source, dest);
			std::cout << "Copy successful...\n";
		}
		else {
			std::cout << "Unsuccessful...\n";
		}
	
	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}

}

void renameFile() {
	std::string oldFile;								
	std::string newFile;

	std::cin >> oldFile;
	std::cin >> newFile;

	try {
		if (std::filesystem::exists(oldFile)) {
			std::filesystem::rename(oldFile, newFile);
			std::cout << "Renamed successfully";
		}
		else {
			std::cout << "File doesnt exist...\n";
		}

	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}

void removeFileThing() {
	std::string fileToRemove;
	std::cin >> fileToRemove;

	try {
		if (std::filesystem::exists(fileToRemove) && !(std::filesystem::is_directory(fileToRemove))){
			std::filesystem::remove(fileToRemove);
			std::cout << "Removed successfully...\n";
		}
		else {
			std::cout << "Remove unsuccessful...\n";
		}
	}
	catch (const std::filesystem::filesystem_error& e) {
		std::cout << "Error: " << e.what() << "\n";
	}
}

#endif // !FILESYSTEMSTUFF_H
