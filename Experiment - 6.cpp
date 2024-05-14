#include <bits/stdc++.h>
using namespace std;

string removePunctuation(string s) {
  string removed;
  for (auto i: s) {
    if (ispunct(i)) continue;
    else removed += i;
  }
  return removed;
}

int main() {
  string input = "Hello! I am Sahil Aggarwal.";
  cout << removePunctuation(input);
  return 0;
}