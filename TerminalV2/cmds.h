#ifndef CMDS_H
#define CMDS_H

#include <iostream>

void helpCmd() {
	std::cout << R"(
FILE SYSTEM
ls                 List directory
cd <path>          Change directory
pwd                Show current directory
mkdir <name>       Create directory
rmdir <name>       Remove directory
del <file>         Delete file
copy <src> <dest>  Copy file
move <src> <dest>  Move file
rename <old> <new> Rename file

FILES
cat <file>         Display file
touch <file>       Create file
edit <file>        Open editor

UTILITIES
calc               Calculator
clear              Clear screen
help               Show commands
exit               Exit terminal
)";
}



#endif