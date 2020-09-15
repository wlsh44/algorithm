#include <iostream>
#include <stack>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    stack<int> s;
    s.push(4);
    s.push(3);
    s.push(6);
    s.push(8);
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    s.push(7);
    s.push(5);
    cout << s.top() << endl;
    s.pop();
    s.push(2);
    s.push(1);
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();
    cout << s.top() << endl;
    s.pop();

}