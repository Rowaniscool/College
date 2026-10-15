#include <iostream>
#include <vector>
#include <random>
#include <string>
#include <Windows.h>
#include <chrono>
#include <thread>

using namespace std;

class Player {
public:
    int loot;
    int lootGenAmount;
    int x = 10;
    int y = 10;
    char playerCharacter = 84;
};

class Enemy {
public:
    char enemyChar = 33;
    int enemyAmount;
    int speed;
    int x;
    int y;

};

HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
COORD position = { 0, 0 };

// Declaring Variables
Player player;
Enemy enemy;

int rows = 20;
int cols = 50;

vector<Enemy> enemies;
vector<vector<char>> grid(rows, vector<char>(cols, ' '));

void wallGeneration() {
    // Left and right walls
    for (int i = 0; i < rows; i++) {
        grid[i][0] = '#';
        grid[i][cols - 1] = '#';
    }

    // Top and bottom walls
    for (int i = 0; i < cols; i++) {
        grid[0][i] = '#';
        grid[rows - 1][i] = '#';
    }

}

void lootGeneration() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> distribY(1, rows - 5);
    uniform_int_distribution<int> distribX(1, cols - 6);

    int roomsCreated = 0;
    while (roomsCreated < player.lootGenAmount) {

        // Pick a random starting position
        int startX = distribX(gen);
        int startY = distribY(gen);

        // --------------------------------
        // CHECK IF THE ROOM CAN BE PLACED
        // --------------------------------
        bool canGenerate = true;
        for (int y = 0; y < 3; y++) {
            for (int x = 0; x < 5; x++) {

                // If ANY square already contains a wall,
                // we cannot place the room here.
                if (grid[startY + y][startX + x] == '#' or grid[startY + y + 1][startX + x + 1] == '#') {
                    canGenerate = false;
                }
            }
        }


        // Only generate the room if every square was empty.
        if (canGenerate) {

            // TOP WALL
            for (int x = 0; x < 5; x++) {
                grid[startY][startX + x] = '#';
            }
            // LEFT WALL
            for (int y = 0; y < 3; y++) {
                grid[startY + y][startX] = '#';
            }
            // RIGHT WALL
            for (int y = 0; y < 3; y++) {
                grid[startY + y][startX + 4] = '#';
            }

            // Put the loot in the center of the room
            grid[startY + 1][startX + 2] = '$';
            roomsCreated++;

        }

    }
}

void mapGeneration() {
    grid[player.y][player.x] = player.playerCharacter;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cout << grid[i][j];
        }
        cout << "\n";
    }
    wallGeneration();
}





// ---- Movement ---- //
void moveUp() {
    if (player.y > 0 && !(grid[player.y - 1][player.x] == '#')) {
        grid[player.y][player.x] = ' ';
        player.y--;
        if (grid[player.y][player.x] == '$') {
            player.loot += 1;
        }
        grid[player.y][player.x] = player.playerCharacter;
    }
    else {
        SetConsoleCursorPosition(hConsole, position);
    }

}
void moveDown() {
    if (player.y < rows - 1 && !(grid[player.y + 1][player.x] == '#')) {
        grid[player.y][player.x] = ' ';
        player.y++;

        grid[player.y][player.x] = player.playerCharacter;
    }
    else {
        SetConsoleCursorPosition(hConsole, position);
    }
}
void moveLeft() {
    if (player.x > 0 && !(grid[player.y][player.x - 1] == '#')) {
        grid[player.y][player.x] = ' ';
        player.x--;
        if (grid[player.y][player.x] == '$') {
            player.loot += 1;
        }
        grid[player.y][player.x] = player.playerCharacter;
    }
    else {
        SetConsoleCursorPosition(hConsole, position);
    }
}
void moveRight() {
    if (player.x < cols - 1 && !(grid[player.y][player.x + 1] == '#')) {
        grid[player.y][player.x] = ' ';
        player.x++;
        if (grid[player.y][player.x] == '$') {
            player.loot += 1;
        }
        grid[player.y][player.x] = player.playerCharacter;
        
    }
    else {
        SetConsoleCursorPosition(hConsole, position);
    }
}

int main()
{
    int UserChoice;
    cout << "\n--------- Dungeon Game ---------\n1. Easy\n2.Normal\n3.Hard\n------------------\nChose: ";
    cin >> UserChoice;

    switch (UserChoice)
    {
    case 1:
        player.Health = 200;
        enemy.speed = 50;
        enemy.enemyAmount = 1;
        player.lootGenAmount = 1;
        break;


    case 2:
        player.Health = 100;
        enemy.speed = 100;
        enemy.enemyAmount = 3;
        player.lootGenAmount = 3;
        break;


    case 3:
        player.Health = 50;
        enemy.speed = 200;
        enemy.enemyAmount = 3;
        player.lootGenAmount = 5;
        break;


    default:
        break;
    }
    mapGeneration();
    lootGeneration();



    while (true) {
        if (GetAsyncKeyState('W') & 0x8000) {
            moveUp();

        }
        if (GetAsyncKeyState('S') & 0x8000) {
            moveDown();

        }
        if (GetAsyncKeyState('D') & 0x8000) {
            moveRight();

        }
        if (GetAsyncKeyState('A') & 0x8000) {
            moveLeft();

        }

        SetConsoleCursorPosition(hConsole, position); // Clears console more effectively in long run
        mapGeneration();

        cout << "Gold: " << player.loot;
        if (player.loot == player.lootGenAmount) {
            cout << "You win!\n";
            break;
        }
        this_thread::sleep_for(chrono::milliseconds(10));


    }
}

