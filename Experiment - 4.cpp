#include<bits/stdc++.h>
using namespace std;

int main() {
  int n, m, start;
  cout << "Enter number of vertices: ";
  cin >> n;
  cout << "Enter number of edges: ";
  cin >> m;
  cout << "Enter start node: ";
  cin >> start;
  vector < vector < int >> adjList(n + 1, vector < int > {});
  for (int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    adjList[u].push_back(v);
    adjList[v].push_back(u);
  }
  vector < int > traversal(n + 1, 0);
  queue < int > q;
  q.push(start);
  traversal[start] = 1;
  cout << "BFS: " << endl;
  while (!q.empty()) {
    int count = q.size();
    for (int i = 0; i < count; i++) {
      int top = q.front();
      cout << top << ' ';
      q.pop();
      for (int val: adjList[top]) {
        if (!traversal[val]) {
          traversal[val] = 1;
          q.push(val);
        }
      }
    }
    cout << endl;
  }
  return 0;
}