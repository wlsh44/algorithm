#include <iostream>

using namespace std;

int main() {
    int arr[26] = {0};
    string s;

    cin >> s;
    for (auto c : s) {
        arr[c - 'a']++;
    }
    for (int i = 0; i < 26; i++) {
        cout << arr[i] << " ";
    }
}