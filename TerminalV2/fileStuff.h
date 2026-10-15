#ifndef FILESTUFF_H
#define FILESTUFF_H
#define WIN32_LEAN_AND_MEAN

#include <iostream>
#include <filesystem>
#include <fstream>
#include <string>
#include <windows.h>
#include <conio.h>

void touchFile() {
    std::string fileName;
    std::string text;
    std::cin >> fileName;

    std::cout << "Press Ctrl+Q to quit...\n";
    std::cout << "Start writing:\n";

    while (true) {
        char c = _getch();

        // Ctrl + Q
        if (c == 17) {
            std::cout << "\nQuitting...\n";
            break;
        }
        // Enter
        if (c == '\r') {
            std::cout << '\n';
            text += '\n';
        }
        else {
            std::cout << c;
            text += c;
        }
    }
    std::ofstream file(fileName);
    if (!file) {
        std::cout << "Could not create file...\n";
        return;
    }

    file << text;
    file.close();
    std::cout << "File saved...\n";
}

void catFile() {
    std::string userInput;
    std::string text;
    std::cin >> userInput;

    std::ifstream fileToOpen(userInput);

	while (std::getline(fileToOpen, text)) {
        std::cout << text;
	}
    std::cout << "\n"; {
        
    }

}

void editFile() {
    std::string file;
    std::string textFromFile;
    std::string userInputText;

    std::cin >> file;

    std::ifstream fileToOpen(file);

    if (!fileToOpen) {
        std::cout << "Could not open file...\n";
        return;
    }

    while (std::getline(fileToOpen, textFromFile)) {
        std::cout << textFromFile << '\n';
        userInputText += textFromFile;
        userInputText += '\n';
    }

    fileToOpen.close();

    while (true) {
        char c = _getch();

        if (c == 17) { // Ctrl + Q
            std::cout << "\nQuitting...\n";
            break;
        }

        if (c == '\r') {
            std::cout << "\n";
            userInputText += '\n';
        }
        else {
            std::cout << c;
            userInputText += c;
        }
    }

    std::ofstream outputFile(file);

    if (!outputFile) {
        std::cout << "Could not create file...\n";
        return;
    }

    outputFile << userInputText;
    outputFile.close();

    std::cout << "File saved...\n";
}

#endif 
