#include <iostream>
#include <fstream>
#include <cmath>
#define HASH_SPACE 1000010
using namespace std;

int get_hash(int value) {
    return abs(value % HASH_SPACE);
}


struct hashset {
    int value;
    struct hashset *next;
} **Hashtable;

bool exists_value(int value) {
    hashset *current = Hashtable[get_hash(value)];
    //iterative -- alternative binsearch on hashtable
    while (current != NULL && current -> value != value) {
        current = current -> next;
    }
    return ((current == NULL) ? false : true);
}

void insert_value(int value) {
    //parenting 
    hashset *current, *current_next;
    int index = get_hash(value);
    current = new hashset;
    if (exists_value(value)) return;
    current_next = Hashtable[index];
    Hashtable[index] = current;
    current -> next = current_next;
    current -> value = value;
    return;
}

void delete_value(int value) {
    hashset *current = Hashtable[get_hash(value)], *current_next = 0;
    while (current != NULL && current -> value != value) {
        current_next = current;
        current = current -> next;
    }
    if (current == NULL) return;
    if (current_next != NULL) {
        current_next -> next = current -> next;
    }
    else {
        Hashtable[get_hash(value)] = current -> next;
    }
    current = NULL;
}

int main() {
    ifstream fin("set.in");
    ofstream fout("set.out");
    Hashtable = new hashset * [HASH_SPACE];
    //g++ nullptr
    for (int i = 0; i < HASH_SPACE; i++) Hashtable[i] = NULL;
    int value = 0;
    string action;
    while (fin >> action) {
        fin >> value;
        if (action == "insert") {
            insert_value(value);
        }
        else if (action == "delete") {
            delete_value(value);
        }
        else if (action == "exists") {
            fout << ((exists_value(value)) ? "true" : "false") << "\n";
        }
    }
    return 0;
}