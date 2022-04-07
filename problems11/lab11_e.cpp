#include <iostream>
#include <fstream>
#include <vector>
const long long inf = 1e9;
struct Edge {
    long long vertex_first, vertex_second, weight;
};

int main() {
    std::ifstream fin("negcycle.in");
    std::ofstream fout("negcycle.out");
    long long n;
    fin >> n;
    std::vector<Edge> matrix(n);
    std::vector<long long> negcycle(n, -1);
    std::vector<long long> weight_map(n, inf);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int weight;
            fin >> weight;
            matrix.push_back({i, j, weight});
        }
    }
    long long flag;
    for (int _ = 0; _ < n; _++) {
        flag = -1;
        for (Edge j : matrix) {
            if (weight_map[j.vertex_second] > weight_map[j.vertex_first] + j.weight) {
                weight_map[j.vertex_second] = weight_map[j.vertex_first] + j.weight;
                negcycle[j.vertex_second] = j.vertex_first;
                flag = j.vertex_second;
            }
        }
    }
    if (flag == -1) {fout << "NO";}
    else {
        std::vector<long long> all_negcycle;
        long long all_flag = flag;
        for (long long i = 0; i < n; i++) {all_flag = negcycle[all_flag];}
        for (long long i = all_flag; i != all_flag || all_negcycle.empty(); i = negcycle[i]) {all_negcycle.push_back(i);}
        all_negcycle.push_back(all_flag);
        fout << "YES\n" << all_negcycle.size() << "\n";
        for (long long i = all_negcycle.size() - 1; i >= 0; i--) {fout << all_negcycle[i] + 1 << " ";}
    }
    return 0;
}