#include <fstream>
#include <iostream>


int main () {
  std::ifstream file;
  file.open("input.txt");

  file.close();
  return 0;
}
