#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <limits>
#include <fstream>

//ofstream   write to a file
//ifstream   read from a file
//fstream    read AND write

using namespace std;
vector<string> taskList;

void saveTasks() {
    ofstream file("tasks.txt");

    for (string task : taskList) {
        file << task << "\n";
    }

    file.close();
}


void makeTask() {
    string taskToDo;

    cout << "Enter task to do: \n";
    cin.ignore();

    getline(cin, taskToDo);
    taskToDo = "[X] " + taskToDo;

    taskList.push_back(taskToDo);
    saveTasks();

    cout << "-----Added " << taskToDo << " to list-----\n";
}

void loadTasks() {
    ifstream file("tasks.txt");

    if (!file.is_open()) {
        cout << "Could not open tasks.txt\n";
        return;
    }

    string task;

    while (getline(file, task)) {
        taskList.push_back(task);
    }

    file.close();
}


void displayTask() {
    int tasklistIndex = 0;

    cout << "-------Tasks-------\n";

    for (string task : taskList) {
        tasklistIndex++;
        cout << tasklistIndex << ": " << task << "\n";
    }
}

void deleteTask() {
    int tasktoRemove;
    int tasklistIndex = 0;

    for (string tasks : taskList) {
        tasklistIndex++;
        cout << "Number: " << tasklistIndex << "| Task: " << tasks << "\n";
    }
    cout << "Delete task number: \n";
    cin >> tasktoRemove;

    if (tasktoRemove <= tasklistIndex) { // Checks to make sure they arent erasing nothing which would crash the program
        taskList.erase(taskList.begin() + tasktoRemove - 1); // Removes the task
        cout << "---Removed successfully!---\n";
    }
    else {
        cout << "Error out of range\n";
    }
    saveTasks();
    
}

void wipeList() {
    if (taskList.empty()) {
        cout << "Tasklist already empty\n";
    }
    else {
        taskList.clear();
        cout << "Tasklist cleared!\n";

    }
    saveTasks();
}



void completeTask() {
    int tasklistIndex = 0;
    int tasktoComplete;

    cout << "--- Tasks ---\n";

    for (string tasks : taskList) {
        tasklistIndex++;
        cout << tasklistIndex << ". " << tasks << "\n";
    }

    cout << "Enter task number to complete: ";
    cin >> tasktoComplete;

    if (tasktoComplete >= 1 && tasktoComplete <= taskList.size()) {

        string fullText = taskList[tasktoComplete - 1];
        string extractedText = fullText.substr(4);

        taskList[tasktoComplete - 1] = "[V] " + extractedText;

        saveTasks();

        cout << "---Task completed!---\n";
    }
    else {
        cout << "Out of range\n";
    }
}

int main()
{
    loadTasks();
    while (true) {

        int UserChoice;
        cout << "\n\n=============== TO DO LIST ===============\n";
        cout << "1. Enter Task\n2. View Task List\n3. Delete Task\n4. Wipe List\n5. Complete Task\n6. Exit program\n";
        cout << "==========================================\nChoice: ";
        while (!(cin >> UserChoice)) {
            cout << "Enter a valid input: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard the text
        }

        string yesNo;

        switch (UserChoice) {
        case 1:
            makeTask();
            break;

        case 2:
            displayTask();
            break;

        case 3:
            deleteTask();
            break;

        case 4:

            cout << "Are you sure y/n: ";
            cin >> yesNo;

            if (yesNo == "y" || yesNo == "Y") { // this --> || <-- stands for 'or' and is more standard
                wipeList();
            }
            else {
                cout << "Continuing...\n";
            }
            break;

        case 5:
            completeTask();
            break;

        case 6:
            cout << "Closing...";
            return(0);

        default:
            cout << "Enter a valid input\n";
            
        }
    }
}