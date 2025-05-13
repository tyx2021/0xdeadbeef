#include <bits/stdc++.h>
using namespace std;

string flag = "deadbeef{th3_x0r+1s_b0r3}";

int main() {
  cout << ">>> ";
  int inp;
  cin >> inp;
  for (int i = 0; i < 29; ++i) {
    cout << ((int)flag[i] ^ inp) << " ";
  }
}
