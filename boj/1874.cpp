#include <iostream>
#include <stack>

using namespace std;


void stack_sequence() {
    stack<int> s;
    stack<int> tmp;
    stack<char> res;
    int n;
    int k;

    cin >> n;
    k = n;
    for (int i = 0; i < n; i++) {
        int num;

        cin >> num;
        s.push(num);    
    }
    while (!s.empty()) {
        int num = 0;
        while (!s.empty() && num < s.top()) {
            num = s.top();
            s.pop();
            tmp.push(num);
            res.push('-');
        }
        if (tmp.top() == k) {
            while (tmp.top() == k) {
                tmp.pop();
                k--;
                res.push('+');
                if (tmp.empty()) {
                    break ;
                }
            }
        } else {
            cout << "NO";
            return ;
        }
    }

    while (!res.empty()) {
        cout << res.top() << "\n";
        res.pop();
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    stack_sequence();
}