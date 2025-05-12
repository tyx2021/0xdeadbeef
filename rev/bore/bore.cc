#include <bits/stdc++.h>
using namespace std;

string flag = "deadbeef{REDACTED}";

int main() {
  cout << ">>> ";
  int inp;
  cin >> inp;
  for (int i = 0; i < 29; ++i) {
    cout << ((int)flag[i] ^ inp) << " ";
  }
}
