#include <iostream>
#include <algorithm>
using namespace std;

class Jug {
  int capacity;
  int value;
  public:
    Jug(int n) {
      capacity = n;
      value = 0;
    }

  void Fill() {
    value = capacity;
  }

  void Empty() {
    value = 0;
  }

  bool isFull() {
    return value >= capacity;
  }

  bool isEmpty() {
    return value == 0;
  }

  //A.transfer(B) -> Transfer contents of B to A until A is full
  void transfer(Jug & B) {
    int old_value = value;
    value = value + B.value;
    value = value > capacity ? capacity : value;
    B.value = B.value - (value - old_value);
  }

  int getValue() {
    return value;
  }
};

bool check(int a, int b, int c) {
  if (c > a) {
    cout << "A can't hold more water than it's capacity!\n";
    return false;
  }
  if (c % __gcd(a, b) == 0) return true;
  cout << "Can't reach this state with the given jugs\n";
  return false;
}

void solve(Jug A, Jug B, int result) {
  while (A.getValue() != result) {
    if (!A.isFull() && B.isEmpty()) {
      cout << "Fill B\n";
      B.Fill();
      cout << "(A, B) = (" << A.getValue() << ", " << B.getValue() << ")\n";
    }
    if (A.isFull()) {
      cout << "Empty A\n";
      A.Empty();
      cout << "(A, B) = (" << A.getValue() << ", " << B.getValue() << ")\n";
    }
    cout << "Pour from B into A\n";
    A.transfer(B);
    cout << "(A, B) = (" << A.getValue() << ", " << B.getValue() << ")\n";
  }
}

int main() {
  int a, b, result;
  cout << "Enter capacity of A: ";
  cin >> a;
  cout << "Enter capacity of B: ";
  cin >> b;
  do {
    cout << "Enter required water in A: ";
    cin >> result;
  } while (!check(a, b, result));
  Jug A(a), B(b);
  cout << "\n(A, B) = (" << A.getValue() << ", " << B.getValue() << ")\n";
  solve(A, B, result);
  cout << "Done!" << endl;
  return 0;
}