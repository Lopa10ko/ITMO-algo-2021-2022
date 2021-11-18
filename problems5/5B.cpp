#include <fstream>
#include <iostream>
#include <vector>
using namespace std;
 
struct bst {
    int key;
    int left;
    int right;
};
vector <bst> bin_tree;
bool condition = true;
 
void check_binary(int parent, int left, int right) {
    if (bin_tree[parent].key <= left || right <= bin_tree[parent].key) {
        condition = false;
        return;
    }
    if (bin_tree[parent].left != 0) {
        check_binary(bin_tree[parent].left, left, bin_tree[parent].key);
    }
    if (bin_tree[parent].right != 0) {
        check_binary(bin_tree[parent].right, bin_tree[parent].key, right);
    }
}
 
int main() {
    ifstream fin("check.in");
    ofstream fout("check.out");
    int n;
    fin >> n;
 
    if (n == 0 || n == 1) {
        fout << "YES\n";
        return 0;
    }
    bin_tree.resize(n + 1);
    for (int i = 1; i <= n; i++) {
        fin >> bin_tree[i].key >> bin_tree[i].left >> bin_tree[i].right;
    }
    check_binary(1, -1000000001, 1000000001);
    fout << ((condition == false) ? "NO\n" : "YES\n");
    return 0;
}