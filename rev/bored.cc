// i lost the source file LMAO heres a recoded version hopefully correct

#include <bits/stdc++.h>
using namespace std;

string flag = "deadbeef{th1s_x0r_1s_s0_b0r3}";

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  cout << ">>> ";
  int inp;
  cin >> inp;
  for (int i = 0; i < 29; ++i) {
    cout << ((int)flag[i] ^ inp) << " ";
  }
}
