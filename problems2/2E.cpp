#include <fstream>
#include <iostream>
using namespace std;

void get_k(int * arr, int left, int right, int k){
    int key = arr[(left + right) / 2], i = left, j = right;
    while(i <= j){
        while(arr[i] < key) {i++;}
        while(arr[j] > key) {j--;}
        if(i <= j) {swap(arr[i], arr[j]); i++; j--;}
    }
//    if left < j then QSort (left,j)
//    if i < right then QSort (i,right)
    if (k > j && k < i) {return;}
    if (left < j && k <= j) {get_k(arr, left, j, k);}
    if (i < right && k >= i) {get_k(arr, i, right, k);}
}

int main()
{
    ifstream fin("kth.in");
    ofstream fout("kth.out");
    int n, k;
    fin >> n >> k;
    int A, B, C;
    int * arr = new int[n];
    fin >> A >> B >> C >> arr[0] >> arr[1];
    for(int i = 2 ; i < n ; i++) {arr[i] = arr[i - 2] * A + arr[i - 1] * B + C;}
    get_k(arr, 0, n - 1, k - 1);
    fout << arr[k - 1];
    return 0;
}
