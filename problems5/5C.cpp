#include <fstream>
#include <string>
using namespace std;


struct Node {
    int key;
    Node *left, *right;
};

//searching for element with key = value
bool exists(Node* subtree, int value) {
    if (subtree == NULL) {
        return false;
    } 
    if (value == subtree -> key) {
        return true;
    }
    if (value < subtree -> key) {
        return exists(subtree -> left, value);
    }  
    else{
        return exists(subtree -> right, value);
    }
}

// //standart left - parent - right travelling
// void inorder_traversal(Node* subtree) {
//     ofstream fout("out.txt");
//     if (subtree != NULL) {
//         inorder_traversal(subtree -> left);
//         fout << subtree -> key << " ";
//         inorder_traversal(subtree -> right);
//     } else {
//         return;
//     }
// }

//insertion (recursive)
Node* insertion(Node* &subtree, int value) {
    if (subtree == NULL) {
        subtree = new Node;
        subtree -> key = value;
        subtree -> left = NULL;
        subtree -> right = NULL;
    }
    else if (subtree -> key > value) {
        insertion(subtree -> left, value);
    }
    else if (subtree -> key < value) {
        insertion(subtree -> right, value);
    }
    return subtree;
}

//searching for min element
Node* find_min(Node* &current) {
    if (current -> left == NULL) {
        return current;
    }
    return find_min(current -> left);
}

//searching for max element
Node* find_max(Node* &current) {
    if (current -> right == NULL) {
        return current;
    }
    return find_max(current -> right);
}

//deletion (recursive)
Node* deletion(Node* &subtree, int value) {
    if (subtree == NULL) {
        return subtree;
    }
    if (value < subtree -> key) {
        subtree -> left = deletion(subtree -> left, value);
    }
    else if (value > subtree -> key) {
        subtree -> right = deletion(subtree -> right, value);
    }
    else if (subtree -> left != NULL && subtree -> right != NULL) {
        subtree -> key = find_min(subtree -> right) -> key;
        subtree -> right = deletion(subtree -> right, subtree -> key);
    } 
    else {
        if (subtree -> left != NULL) {
            subtree = subtree -> left;
        }
        else {
            subtree = subtree -> right;
        }
    }
    return subtree;
}

//searching for min element greater than subtree.key (recursive)
Node* get_next(Node* &subtree, int key) {
    Node *current = subtree, *successor = NULL;
    while (current != NULL) {
        if (current -> key > key) {
            successor = current;
            current = current -> left;
        } 
        else {
            current = current -> right;
        }
    }
    return successor;
}

//searching for max element less than subtree.key (recursive)
Node* get_prev(Node* &subtree, int key) {
    Node *current = subtree, *successor = NULL;
    while (current != NULL) {
        if (current -> key < key) {
            successor = current;
            current = current -> right;
        } 
        else {
            current = current -> left;
        }
    }
    return successor;
}

int main() {
    ifstream fin("bstsimple.in");
    ofstream fout("bstsimple.out");
    Node* bst_tree = NULL;
    string action;
    int x;
    while (fin >> action) {
        fin >> x;
        
        //inorder_traversal(bst_tree);

        if (action == "insert"){
            insertion(bst_tree, x);
        }

        if (action == "delete") {
            deletion(bst_tree, x);
        }

        if (action == "exists") {
            if (exists(bst_tree, x)) {
                fout << "true\n";
            }
            else {
                fout << "false\n";
            }
        }

        if (action == "next") {
            Node* current = get_next(bst_tree, x);
            if (current == NULL) {
                fout << "none\n";
            }
            else {
                fout << current -> key << "\n";
            }
        }

        if (action == "prev") {
            Node* current = get_prev(bst_tree, x);
            if (current == NULL) {
                fout << "none\n";
            }
            else {
                fout << current -> key << "\n";
            }
        }
        //inorder_traversal(bst_tree);
    }
    return 0;
}

