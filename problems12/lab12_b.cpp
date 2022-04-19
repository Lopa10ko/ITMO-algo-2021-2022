#include <vector>
#include <iostream>
int main() {
    long long n;
    std::cin >> n;
    std::vector<long long> seq, lis;
    for (long long i = 0; i < n; ++i) {
        long long temp;
        std::cin >> temp;
        seq.push_back(temp);
    }
    std::vector<int> parent(seq.size());
    lis.push_back(0);
    long long aim, index;
    for (long long i = 1; i < seq.size(); i++) {
        if (seq[lis.back()] < seq[i]) {
            parent[i] = lis.back();
            lis.push_back(i);
            continue;
        }
        for (aim = 0, index = lis.size() - 1; aim < index;) {
            int c = (aim + index) / 2;
            if (seq[lis[c]] < seq[i]) {aim = c + 1;}
            else {index = c;}
        }
        if (seq[i] < seq[lis[aim]]) {
            if (aim > 0) {parent[i] = lis[aim - 1];}
            lis[aim] = i;
        }
    }
    for (aim = lis.size(), index = lis.back(); aim--; index = parent[index]) {lis[aim] = index;}
    std::cout << lis.size() << std::endl;
    for (long long li : lis) {std::cout << seq[li] << " ";}
    return 0;
}