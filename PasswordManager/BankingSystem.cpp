#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <fstream>


using namespace std;
class PasswordEntry {
public:
    string website;
    string username;
    string password;
};

vector<PasswordEntry> informationStore;


void saveData() {
    ofstream userData("Data.txt");
    for (PasswordEntry data : informationStore) {
        userData << data.website << "\n";
        userData << data.username << "\n";
        userData << data.password << "\n";
    }
    cout << "Saved\n";
}

void loadData() {
    ifstream data("Data.txt");

    while (data) {
        PasswordEntry infoEntry;

        getline(data, infoEntry.website);
        getline(data, infoEntry.username);
        getline(data, infoEntry.password);

        if (data) {
            informationStore.push_back(infoEntry);
        }
    }
}


void enterData() {
    PasswordEntry infoEntry;

    string websiteInput;
    string usernameInput;
    string passwordInput;

    cout << "Enter the website name: ";
    cin >> websiteInput;
    cout << "Enter the username: ";
    cin >> usernameInput;
    cout << "Enter the password: ";
    cin >> passwordInput;

    infoEntry.website = websiteInput;
    infoEntry.username = usernameInput;
    infoEntry.password = passwordInput;

    informationStore.push_back(infoEntry);
    saveData();
}

void viewPassword() {
    if (informationStore.empty()) {
        cout << "\nCurrently no passwords\n";
    }
    else {
        for (PasswordEntry stuff : informationStore) {
            cout << "\n\n--------- Data ----------" << endl;
            cout << "Website: " << stuff.website << endl;
            cout << "Username: " << stuff.username << endl;
            cout << "Password: " << stuff.password << endl;
            cout << "---------------------------\n" << endl;
        }
    }
}

void deletePassword() {
    int numberDisplay = 0;
    int passwordChoice;

    for (PasswordEntry stuff : informationStore) {
        numberDisplay++;
        cout << "\n--------------\n";
        cout << numberDisplay << ". " << "Website: " << stuff.website << "\n" << "Password: " << stuff.password << "\n";
        cout << "--------------\n";
    }

    cout << "Enter number to delete: ";
    cin >> passwordChoice;

    if (passwordChoice >= 1 && passwordChoice <= passwordChoice ) {
        informationStore.erase(informationStore.begin() + passwordChoice - 1);

    }
    else {
        cout << "Out of range\n";
    }
    saveData();
    
}

void searchPassword() {
    string searchInput;
    bool found = false;

    cout << "Search for password: ";
    cin >> searchInput;

    for (PasswordEntry stuff : informationStore) {
        if (stuff.website == searchInput) {
            cout << "Found\n";
            cout << "Website: " + stuff.website + "\n" << "Password: " + stuff.password + "\n" << "Username: " + stuff.username + "\n";
            found = true;
        }
    }
    if (!found) {
        cout << "password not found...\n";
    }
}

void editPassword() {
    int passwordEdit;
    int options = 0;
    PasswordEntry newPassword;

    for (PasswordEntry stuff : informationStore) {
        options++;

        cout << "\n-----Select password to edit -----\n";
        cout << options << ".\n";
        cout << "Website: " + stuff.website + "\n";
        cout << "Username: " + stuff.username + "\n";
        cout << "Password: " + stuff.password + "\n";

    }
    cout << "Chose password to edit: ";
    cin >> passwordEdit;

    if (passwordEdit >= 1 && passwordEdit <= options) {
        cout << "New password: ";
        cin >> newPassword.password;


        informationStore[passwordEdit - 1].password = newPassword.password;

    }
    else {
        cout << "Error out of range\n";
    }
    saveData();
}

int main() {
    loadData();

    while (true) {
        int userChoice;
        cout << " ----------\n1.Enter data\n2.View data\n3.Delete Password\n4.Search for password\n5.Edit password\n6.Exit\n----------\n";

        while (!(cin >> userChoice)) {
            cout << "Invalid input\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid text like if they entered 'g', it essentially ignores it
        }

        switch (userChoice)
        {
        case 1:
            enterData();
            break;
        case 2:
            viewPassword();
            break;
        case 3:
            deletePassword();
            break;
        case 4:
            searchPassword();
            break;
        case 5:
            editPassword();
            break;
        case 6:
            return 0;
            break;



        default:
            break;
        }
    }

    return 0;
}