#include <iostream>
using namespace std;

void printGetal(int* getalPtr) {
    cout << *getalPtr << endl;
}
void printLetter(char* letterPtr) {
    cout << *letterPtr << endl;
}
void print(void* ptr, char type) {
    switch (type) {
    case 'i':cout << *((int*)ptr) << endl; break;
    case 'c':cout << *((char*)ptr) << endl; break;
    }
}

int main()
{
    int getal = 5;
    char letter = 'b';
    // printGetal(&getal);
    // printLetter(&letter);
    print(&getal,'i');
    print(&letter,'c');


    system("pause>0");
    return 0;

}