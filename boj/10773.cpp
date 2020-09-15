#include <iostream>
#include <stack>

using namespace std;

int k;

long long zero() {
    stack<int> s;
    long long res = 0;
    int size;

    for (int i = 0; i < k; i++) {
        int num;

        cin >> num;
        if (num == 0) {
            s.pop();
        } else {
            s.push(num);
        }
    }

    size = s.size();
    for (int i = 0; i < size; i++) {
        res += s.top();
        s.pop();
    }
    return res;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> k;
    cout << zero();
}